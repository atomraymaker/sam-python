import formatter

import boto3

SESSION = boto3.session.Session()


def handle(event, _context):
    word = event.get("word", "")
    return formatter.upcase_string(word, SESSION)
