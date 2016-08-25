import math

PROBLEMS_PER_LEVEL = 25

def get_problem(n):
    level = math.ceil(n / PROBLEMS_PER_LEVEL)
    level_package = 'solutions.level%s' % level

    return __import__(
        '%s.problem%s' % (level_package, n),
        fromlist=(level_package)
    )

def problem_exists(n):
    try:
        return get_problem(n) != None
    except:
        return False

def run_problem(n):
    return get_problem(n).run()
