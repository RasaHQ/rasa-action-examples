from .client import Client
from actions.actions import ActionCustomFallback

message = {
    'entities': [],
    'intent': {'confidence': 0.4, 'name': 'inform'},
    'intent_ranking': [
        {'confidence': 0.3, 'name': 'new_order'},
        {'confidence': 0.3, 'name': 'what_happened'},
        {'confidence': 0.4, 'name': 'inform'}],
    'text': 'stroop stroop stroopwafels!!!!'
}


def test_base_usecase():
    action = ActionCustomFallback()

    client = Client(action=action)
    msg_back, slots = client.invoke_message(message=message)
    print(msg_back)

    assert "Could you speficy/rephrase?" in msg_back["text"]
    assert len(msg_back['buttons']) == 3
