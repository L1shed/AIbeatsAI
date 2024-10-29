import unittest
from unittest.mock import MagicMock, patch
from chat_api import what_beats

class TestChatAPI(unittest.TestCase):

    def test_hardcoded_response(self):
        # Test if the hardcoded response for 'rock' works
        result = what_beats("rock")
        self.assertEqual(result, "paper")

    def test_valid_response_format(self):
        # Here, you would mock the API call to return a controlled response
        with patch('chat_api.client') as mock_client:
            mock_response = MagicMock()
            mock_response.choices[0].message.content = "scissors."
            mock_client.chat.completions.create.return_value = mock_response
            
            result = what_beats("paper")
            self.assertEqual(result, "scissors")

    def test_word_already_used(self):
        # Mock for recursive call and duplicate word handling
        with patch('chat_api.words', ["scissors"]):
            with patch('chat_api.client') as mock_client:
                mock_response = MagicMock()
                mock_response.choices[0].message.content = "scissors."
                mock_client.chat.completions.create.return_value = mock_response

                result = what_beats("paper")
                self.assertNotEqual(result, "scissors")

if __name__ == '__main__':
    unittest.main()
