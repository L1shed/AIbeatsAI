import unittest
from unittest.mock import MagicMock, patch
import sys
import os
# sys.path.append('../bot.py')    
# from ..bot
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bot

class TestBot(unittest.TestCase):

    @patch('bot.driver')
    @patch('bot.what_beats')
    def test_play_function(self, mock_what_beats, mock_driver):
        # Mock elements for the Selenium driver
        mock_driver.find_elements.return_value = [MagicMock(), MagicMock(text="rock")]
        mock_driver.find_element.return_value = MagicMock()

        # Simulate response from what_beats function
        mock_what_beats.return_value = "paper"

        bot.play()
        

        # Check if the correct interactions were made with the web elements
        mock_driver.find_element.assert_called()
        mock_driver.find_elements.assert_called()
        self.assertEqual(mock_what_beats.call_count, 1)
        mock_driver.find_element().send_keys.assert_called_with("paper" + bot.Keys.RETURN)
        class TestBot(unittest.TestCase):

            @patch('bot.driver')
            @patch('bot.what_beats')
            def test_play_function(self, mock_what_beats, mock_driver):
                # Mock elements for the Selenium driver
                mock_driver.find_elements.return_value = [MagicMock(), MagicMock(text="rock")]
                mock_driver.find_element.return_value = MagicMock()

                # Simulate response from what_beats function
                mock_what_beats.return_value = "paper"

                bot.play()
                
                # Check if the correct interactions were made with the web elements
                mock_driver.find_element.assert_called()
                mock_driver.find_elements.assert_called()
                self.assertEqual(mock_what_beats.call_count, 1)
                mock_driver.find_element().send_keys.assert_called_with("paper" + bot.Keys.RETURN)

            @patch('bot.driver')
            @patch('bot.what_beats')
            def test_play_function_recursive(self, mock_what_beats, mock_driver):
                # Mock elements for the Selenium driver
                mock_driver.find_elements.return_value = [MagicMock(), MagicMock(text="rock")]
                mock_driver.find_element.return_value = MagicMock()
                mock_driver.find_element().send_keys.side_effect = [None, Exception("Stop recursion")]

                # Simulate response from what_beats function
                mock_what_beats.return_value = "paper"

                with self.assertRaises(Exception) as context:
                    bot.play()

                self.assertTrue("Stop recursion" in str(context.exception))
                self.assertEqual(mock_what_beats.call_count, 1)
                mock_driver.find_element().send_keys.assert_called_with("paper" + bot.Keys.RETURN)

            @patch('bot.driver')
            @patch('bot.what_beats')
            def test_play_function_no_next_button(self, mock_what_beats, mock_driver):
                # Mock elements for the Selenium driver
                mock_driver.find_elements.return_value = [MagicMock(), MagicMock(text="rock")]
                mock_driver.find_element.return_value = MagicMock()

                # Simulate response from what_beats function
                mock_what_beats.return_value = "paper"

                # Simulate no next button found
                mock_driver.find_element.side_effect = [MagicMock(), Exception("No next button")]

                with self.assertRaises(Exception) as context:
                    bot.play()

                self.assertTrue("No next button" in str(context.exception))
                self.assertEqual(mock_what_beats.call_count, 1)
                mock_driver.find_element().send_keys.assert_called_with("paper" + bot.Keys.RETURN)

if __name__ == '__main__':
    unittest.main()
