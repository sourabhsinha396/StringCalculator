from main import StringCalculator

def test_empty_string_should_return_zero():
    string_calculator = StringCalculator("")
    assert string_calculator.get_sum() == 0