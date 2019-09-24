from datetime import datetime, timezone
import uuid
from logging import info
from random import randint as randint
from json import load
from config import PROJECT_PATH


class MessageGenerator:
    """
    The MessageGenerator creates random according to the CloudEvent convention.
    """

    def __init__(self, source):
        """
        Initializes the default fields, that are sent with every message and loads the blind texts.
        :param source: str, representing the 'source' field, which is supposed to be defined by the user defined
        """

        self.default_fields = {
            'specversion': '0.2',
            'type': 'io.github.ust.mico.test_message',
            'source': source,
            'contenttype': 'application/json',
        }
        info('MessageGenerator was created')
        with open(PROJECT_PATH / 'blind_texts.json', 'r') as f:
            self.blind_texts = load(f)
        info('Blind texts were loaded')

    def get_random_message(self) -> dict:
        """
        Creates a CloudEvent message with the following properties:
        * id: a uuid for this message
        * data: dict with timestamp
        :return: dict, representing the CloudEvent message
        """
        blind_txt = self.blind_texts[randint(0, len(self.blind_texts) - 1)]
        msg = {
                'id': uuid.uuid4().hex,
                'time': datetime.now(timezone.utc).isoformat(),
                'data': {
                    'timestamp': datetime.now().timestamp(),
                    'rand_int': randint(1, 100),
                    'text': blind_txt
                }}
        return {**msg, **self.default_fields}
