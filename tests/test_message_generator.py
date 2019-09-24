from message_generator import MessageGenerator
from datetime import datetime, timezone
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

        # Ensures that the timestamp is UTC
        msg_date = dateutil.parser.parse(msg['time'])
        assert msg_date.tzname() == 'UTC'

        # Ensure that the timestamp is up to date (not older than 10 seconds)
        delta = (datetime.now(timezone.utc) - msg_date)
        assert  delta.total_seconds() < 10

        # Ensure that the data field contains the right value types
        assert 'timestamp' in msg['data']
        assert 'rand_int' in msg['data']
