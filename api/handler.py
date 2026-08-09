import json

from cli.run import problem_exists, run_problem


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

    if not problem_exists(number):
        return response(404, {
            "error": f'No solution for problem {number:d} (yet!)'
        })

    solution, elapsed = run_problem(number)

    return response(200, {
        "problem": number,
        "solution": solution,
        "duration": elapsed * 1000
    })
