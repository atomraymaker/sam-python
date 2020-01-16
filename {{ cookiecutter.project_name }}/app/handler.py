import boto3
import util
from logger import LOG

SESSION = boto3.session.Session()


def handle(event, _context):
    LOG.info("Loaded event", lambda_input=event)
    word = event.get("word", "")
    return util.upcase_string(word, SESSION)
