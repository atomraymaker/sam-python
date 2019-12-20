from handlers import up


def test_handle():
    event = {"word": "word"}
    assert up.handle(event, None) == "WORD"
