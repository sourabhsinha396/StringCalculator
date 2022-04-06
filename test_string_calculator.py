from main import StringCalculator

def test_empty_string_should_return_zero():
    string_calculator = StringCalculator("")
    assert string_calculator.get_sum() == 0


def test_one_value_should_return_itself():
    string_calculator = StringCalculator("3")
    assert string_calculator.get_sum() == 3