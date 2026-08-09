import math
import os
import subprocess
import sys
from abc import ABC, abstractmethod
from time import perf_counter

PROBLEMS_PER_LEVEL = 25
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(PROJECT_ROOT, 'build')


def _exec(cmd, env=None):
    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=PROJECT_ROOT, env=env
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout.strip()


class Language(ABC):
    extensions: tuple

    def prepare(self, source: str) -> None: ...

    @abstractmethod
    def run(self, source: str) -> str: ...


class CompiledLanguage(Language, ABC):
    @abstractmethod
    def compile_cmd(self, source: str, binary: str) -> list: ...

    def _binary(self, source: str) -> str:
        name = os.path.splitext(os.path.basename(source))[0]
        return os.path.join(BUILD_DIR, name)

    def prepare(self, source: str) -> None:
        binary = self._binary(source)
        stale = not os.path.exists(binary) or \
            os.path.getmtime(binary) <= os.path.getmtime(source)
        if stale:
            os.makedirs(BUILD_DIR, exist_ok=True)
            result = subprocess.run(
                self.compile_cmd(source, binary),
                capture_output=True, text=True
            )
            if result.returncode != 0:
                raise RuntimeError(f'Compilation failed:\n{result.stderr}')

    def run(self, source: str) -> str:
        return _exec([self._binary(source)])


class Python(Language):
    extensions = ('.py',)

    def run(self, source: str) -> str:
        env = {**os.environ, 'PYTHONPATH': PROJECT_ROOT}
        return _exec([sys.executable, source], env=env)


class Go(CompiledLanguage):
    extensions = ('.go',)

    def compile_cmd(self, source: str, binary: str) -> list:
        return ['go', 'build', '-o', binary, source]


class Rust(CompiledLanguage):
    extensions = ('.rs',)

    def compile_cmd(self, source: str, binary: str) -> list:
        return ['rustc', source, '-o', binary]


_BY_EXT = {
    ext: lang()
    for lang in [Python, Go, Rust]
    for ext in lang.extensions
}


def _level(n):
    return math.ceil(n / PROBLEMS_PER_LEVEL)


def _find_source(n):
    level_dir = os.path.join(PROJECT_ROOT, 'solutions', f'level{_level(n)}')
    if not os.path.isdir(level_dir):
        return None, None
    for entry in os.listdir(level_dir):
        name, ext = os.path.splitext(entry)
        if name == f'problem{n}' and ext in _BY_EXT:
            return os.path.join(level_dir, entry), ext
    return None, None


def list_problems():
    levels_dir = os.path.join(PROJECT_ROOT, 'solutions')
    numbers = []
    for level_dir in sorted(os.listdir(levels_dir)):
        full = os.path.join(levels_dir, level_dir)
        if not os.path.isdir(full):
            continue
        for entry in os.listdir(full):
            name, ext = os.path.splitext(entry)
            if name.startswith('problem') and ext in _BY_EXT:
                try:
                    numbers.append(int(name[len('problem'):]))
                except ValueError:
                    pass
    return sorted(numbers)


def problem_exists(n):
    source, _ = _find_source(n)
    return source is not None


def run_problem(n):
    source, ext = _find_source(n)
    if source is None:
        raise FileNotFoundError(f'No solution for problem {n}')
    lang = _BY_EXT[ext]
    lang.prepare(source)
    start = perf_counter()
    answer = lang.run(source)
    return answer, perf_counter() - start
