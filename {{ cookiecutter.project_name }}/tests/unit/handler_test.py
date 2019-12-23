import handler


def test_handle():
    event = {"word": "word"}
    assert handler.handle(event, None) == "WORD"
