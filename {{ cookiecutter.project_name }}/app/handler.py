import boto3

import util

SESSION = boto3.session.Session()


def handle(event, _context):
    word = event.get("word", "")
    return util.upcase_string(word, SESSION)
