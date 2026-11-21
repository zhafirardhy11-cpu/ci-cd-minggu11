import pytest
from kalkulator import tambah, kurang, bagi
 
def test_tambah():
    assert tambah(2, 3) == 5
 
def test_kurang():
    assert kurang(5, 2) == 3
 
def test_bagi_nol():
    with pytest.raises(ValueError):
        bagi(1, 0)
