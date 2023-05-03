import random
import unittest
from unittest.mock import MagicMock

from gladiator.models.reply import Reply
from gladiator.services.gladiator_interface import GladiatorInterface


class TestGladiatorService(unittest.TestCase):

    def test_run(self):
        # Arrange
        mock_gladiator = MagicMock(spec=GladiatorInterface)

        replies = [Reply(i + 1, f"Sample answer {i + 1}", random.randint(0, 100)) for i in range(5)]
        mock_gladiator.run.return_value = (True, None, replies)

        gladiator = mock_gladiator

        # Act
        data = {"prompt": "Who is the father of AI?"}
        success, _, replies = gladiator.run(data['prompt'])

        # Assert
        self.assertTrue(success)
        self.assertCountEqual(replies, replies)
        mock_gladiator.run.assert_called_with(data["prompt"])


if __name__ == '__main__':
    unittest.main()
