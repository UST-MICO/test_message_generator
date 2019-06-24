from message_generator import MessageGenerator
from datetime import datetime
import dateutil.parser


class TestMessageGenerator:

    def test_get_random_message(self):
        source = 'testing_message_generator'
        msg_gen = MessageGenerator(source=source)
        msg = msg_gen.get_random_message()

        # Ensures that the message is of type dict (hence can be converted to json)
        assert isinstance(msg, dict)

        # Ensure that all required context attributes CloudEvent are set
        for key in ['specversion', 'type', 'source', 'id', 'time', 'contenttype', 'data']:
            assert key in msg.keys()

        # Ensure that the source was set appropriately
        assert msg['source'] == source

        # Ensure that the timestamp is up to date (not older than 10 seconds)
        msg_date = dateutil.parser.parse(msg['time'])
        delta = (datetime.now() - msg_date)
        assert  delta.total_seconds() < 10
