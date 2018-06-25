"""Test the `geology` module."""

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import pytest

from hugs.calc import snell_angle


def test_snell():
    """Test the basic wind component calculation."""
    res = snell_angle(12, 2500, 4000)
    assert_almost_equal(res, 19.43022, 4)
