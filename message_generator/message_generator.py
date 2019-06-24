from datetime import datetime
import uuid
from logging import info


class MessageGenerator:

    def __init__(self, source):
        self.default_fields = {
            'specversion': '0.2',
            'type': 'io.github.ust.mico.test_message',
            'source': source,
            'contenttype': 'application/json',
        }
        info('MessageGenerator was created')

    def get_random_message(self) -> dict:
        msg = {
                'id': uuid.uuid4().hex,
                'time': datetime.now().isoformat(),
                'data': {
                    'timestamp': datetime.timestamp(datetime.now())
                }}
        return {**msg, **self.default_fields}
