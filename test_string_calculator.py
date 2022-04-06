from main import StringCalculator

def test_empty_string_should_return_zero():
    string_calculator = StringCalculator("")
    assert string_calculator.get_sum() == 0


def test_one_value_should_return_itself():
    string_calculator = StringCalculator("3")
    assert string_calculator.get_sum() == 3

    string_calculator = StringCalculator("4,")
    assert string_calculator.get_sum() == 4


def test_two_integers_should_add_correctly():
    string_calculator = StringCalculator("3,5")
    assert string_calculator.get_sum() == 8

    string_calculator = StringCalculator("0,0")
    assert string_calculator.get_sum() == 0

    string_calculator = StringCalculator("-2,-3")
    assert string_calculator.get_sum() == -5



