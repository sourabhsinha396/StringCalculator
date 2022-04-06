import pytest

from main import StringCalculator


class TestStringCalculator:
    def test_empty_string_should_return_zero(self):
        string_calculator = StringCalculator("")
        assert string_calculator.get_sum() == 0


    def test_one_value_should_return_itself(self):
        string_calculator = StringCalculator("3")
        assert string_calculator.get_sum() == 3

        string_calculator = StringCalculator("4,")
        assert string_calculator.get_sum() == 4


    def test_two_integers_should_add_correctly(self):
        string_calculator = StringCalculator("3,5")
        assert string_calculator.get_sum() == 8

        string_calculator = StringCalculator("0,0")
        assert string_calculator.get_sum() == 0

        string_calculator = StringCalculator("-2,-3")
        assert string_calculator.get_sum() == -5

    def test_should_fail_on_non_string_input(self):
        with pytest.raises(ValueError):
            string_calculator = StringCalculator("3.4")
            assert string_calculator.get_sum()

    def test_should_accept_unknown_number_of_arguments(self):
        string_calculator = StringCalculator("1,2,3,4")
        assert string_calculator.get_sum() == 10
        string_calculator = StringCalculator("0,0,0,0")
        assert string_calculator.get_sum() == 0



