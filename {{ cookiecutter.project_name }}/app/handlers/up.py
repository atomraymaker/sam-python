from lib import formatter


def handle(event, context):
    word = event.get("word", "")
    return formatter.up(word)
