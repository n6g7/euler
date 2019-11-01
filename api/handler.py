import json
from datetime import datetime, timedelta

from cli.run import get_problem


def response(status, data):
    return {
            "statusCode": status,
            "body": json.dumps(data),
            "headers": {
                'Access-Control-Allow-Origin': '*',
            },
        }


def solve(event, context):
    raw_number = event["pathParameters"]["number"]

    try:
        number = int(raw_number)
    except ValueError:
        return response(400, {
            "error": f'Invalid problem number: "{raw_number}"'
        })

    try:
        problem = get_problem(number)
    except ModuleNotFoundError:
        return response(404, {
            "error": f'No solution for problem {number:d} (yet!)'
        })

    start = datetime.now()
    solution = problem.run()
    end = datetime.now()
    duration = end - start

    return response(200, {
        "problem": number,
        "solution": solution,
        "duration": duration / timedelta(milliseconds=1)
    })
