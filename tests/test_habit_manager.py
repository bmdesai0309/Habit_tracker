import unittest
from unittest.mock import patch, mock_open
import habit_manager
import json
from datetime import datetime, timedelta

class TestHabitManager(unittest.TestCase):

    @patch("habit_manager.os.path.exists")
    @patch("habit_manager.open", new_callable=mock_open, read_data="{}")
    def test_add_new_habit(self, mock_file, mock_exists):
        mock_exists.return_value = True
        habit_manager.add_habit("Exercise")

        written_chunks = [call.args[0] for call in mock_file().write.call_args_list]
        written_output = ''.join(written_chunks)
        expected_data = {
            "Exercise": {
                "dates_completed": []
            }
        }

        self.assertEqual(json.loads(written_output), expected_data)

    @patch("habit_manager.os.path.exists")
    @patch("habit_manager.open", new_callable=mock_open, read_data=json.dumps({
        "Exercise": {"dates_completed": []}
    }))
    def test_mark_habit_completed(self, mock_file, mock_exists):
        mock_exists.return_value = True
        today = datetime.today().strftime("%Y-%m-%d")

        habit_manager.mark_habit_completed("Exercise")

        written_chunks = [call.args[0] for call in mock_file().write.call_args_list]
        written_output = ''.join(written_chunks)
        expected_data = {
            "Exercise": {
                "dates_completed": [today]
            }
        }

        self.assertEqual(json.loads(written_output), expected_data)
    
    @patch("habit_manager.print")
    @patch("habit_manager.load_data")
    def test_generate_weekly_report(self, mock_load_data, mock_print):
        today = datetime.today().strftime("%Y-%m-%d")
        five_days_ago = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")
        old_date = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")

        # Mock data: "Reading" has 2 recent completions, "Exercise" has none
        mock_load_data.return_value = {
            "Reading": {
                "dates_completed": [today, five_days_ago, old_date]
            },
            "Exercise": {
                "dates_completed": []
            }
        }


        # Run the report
        habit_manager.generate_weekly_report()

        # Capture all print outputs
        printed_lines = [str(call.args[0]) for call in mock_print.call_args_list]

        # Debug: print lines if test fails
        print("DEBUG OUTPUT:")
        for line in printed_lines:
            print(line)

        # Flexible matching (lowercase to avoid emoji or spacing mismatch)
        has_reading = any("habit: reading" in line.lower() for line in printed_lines)
        has_two_days = any("2" in line and "7" in line for line in printed_lines)
        has_exercise = any("habit: exercise" in line.lower() for line in printed_lines)
        has_no_completion = any("no completions" in line.lower() for line in printed_lines)

        self.assertTrue(has_reading, "Expected 'Habit: Reading' in output.")
        self.assertTrue(has_two_days, "Expected '2 / 7 days' match in output.")
        self.assertTrue(has_exercise, "Expected 'Habit: Exercise' in output.")
        self.assertTrue(has_no_completion, "Expected 'No completions this week.' in output.")
    
    @patch("habit_manager.print")
    @patch("habit_manager.load_data")
    @patch("habit_manager.save_data")
    def test_delete_habit(self, mock_save_data, mock_load_data, mock_print):
        mock_load_data.return_value = {
            "Reading": {"dates_completed": ["2025-05-29"]},
            "Exercise": {"dates_completed": []}
        }

        habit_manager.delete_habit("Reading")

        # Expect 'Reading' to be removed, only 'Exercise' remains
        expected_data = {
            "Exercise": {"dates_completed": []}
        }

        mock_save_data.assert_called_with(expected_data)
        mock_print.assert_any_call("Habit 'Reading' has been deleted.")
    
    @patch("habit_manager.print")
    @patch("habit_manager.load_data")
    def test_list_habits(self, mock_load_data, mock_print):
        mock_load_data.return_value = {
            "Reading": {"dates_completed": []},
            "Exercise": {"dates_completed": []}
        }

        habit_manager.list_habits()

        # Check that both habit names are printed
        printed_lines = [str(call.args[0]) for call in mock_print.call_args_list]
        self.assertTrue(any("1. Reading" in line for line in printed_lines))
        self.assertTrue(any("2. Exercise" in line for line in printed_lines))





if __name__ == '__main__':
    unittest.main()
