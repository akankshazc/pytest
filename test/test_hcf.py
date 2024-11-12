from source.hcf import hcf
from source.hcf import hcf_euclidean
import pytest


def test_hcf():
    assert hcf(4, 6) == 2
    assert hcf(8, 12) == 4
    assert hcf(9, 27) == 9
    assert hcf(10, 15) == 5
    assert hcf(12, 15) == 3
    with pytest.raises(UnboundLocalError):
        hcf(12, 0)


def test_hcf_euclidean():
    assert hcf_euclidean(4, 6) == 2
    assert hcf_euclidean(8, 12) == 4
    assert hcf_euclidean(9, 27) == 9
    assert hcf_euclidean(10, 15) == 5
    assert hcf_euclidean(12, 15) == 3
    with pytest.raises(UnboundLocalError):
        hcf(12, 0)
