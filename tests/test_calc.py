import pytest


class TestCalc:
    @pytest.mark.parametrize(
        "expression,expected",
        [
            ("90 + 21", 111),
            ("90 - 10", 80),
            ("5 * 5", 25),
            ("5 / 5", 1),
        ],
    )
    def test_calc(self, calc, expression, expected):
        assert calc(expression) == expected
