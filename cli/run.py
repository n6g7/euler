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

    def prepare(self, source: str) -> None:
        _sync_cargo_toml(source)
        super().prepare(source)


_BY_EXT = {
    ext: lang()
    for lang in [Python, Go, Rust]
    for ext in lang.extensions
}


def _level(n):
    return math.ceil(n / PROBLEMS_PER_LEVEL)


def _sync_cargo_toml(source):
    cargo_path = os.path.join(PROJECT_ROOT, 'Cargo.toml')
    name = os.path.splitext(os.path.basename(source))[0]
    try:
        with open(cargo_path) as f:
            if name in f.read():
                return
    except FileNotFoundError:
        pass
    import glob
    rs_files = sorted(glob.glob(
        os.path.join(PROJECT_ROOT, 'solutions', 'level*', 'problem*.rs')
    ))
    lines = [
        '# Auto-generated — do not edit\n',
        '[package]\nname = "euler"\nversion = "0.1.0"\nedition = "2021"\n',
    ]
    for path in rs_files:
        n = os.path.splitext(os.path.basename(path))[0]
        rel = os.path.relpath(path, PROJECT_ROOT)
        lines.append(f'\n[[bin]]\nname = "{n}"\npath = "{rel}"\n')
    with open(cargo_path, 'w') as f:
        f.writelines(lines)


def _find_source(n):
    level_dir = os.path.join(PROJECT_ROOT, 'solutions', f'level{_level(n)}')
    if not os.path.isdir(level_dir):
        return None, None
    for entry in os.listdir(level_dir):
        name, ext = os.path.splitext(entry)
        if name == f'problem{n}' and ext in _BY_EXT:
            return os.path.join(level_dir, entry), _BY_EXT[ext]
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
    source, lang = _find_source(n)
    if source is None:
        raise FileNotFoundError(f'No solution for problem {n}')
    lang.prepare(source)
    start = perf_counter()
    answer = lang.run(source)
    return answer, perf_counter() - start
