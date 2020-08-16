# -*- coding: utf-8 -*-

import pytest
from python_template.skeleton import fib

__author__ = "Patrick Evans"
__copyright__ = "Patrick Evans"
__license__ = "MIT"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
