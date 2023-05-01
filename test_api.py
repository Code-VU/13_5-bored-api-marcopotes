from unittest.mock import patch
import bored

def test_averages(capsys):
    with patch('builtins.input', side_effect=['key', 5585829]):
        bored.assignment_13_5()
        captured = capsys.readouterr()
        statements = captured.out.split("\n")
        final_result = statements[-2]
        assert final_result == "Recommended Activity: Go to an escape room"
        
