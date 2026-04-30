from src.app.calc import Calculator
import pytest


@pytest.fixture
def calc():
    return Calculator()
