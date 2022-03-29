import Calculation
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(6,3,9),(1,2,3)])
def test_add2no(a,b,c):

    result=Calculation.add2no(a,b)
    assert result == c

@pytest.mark.parametrize("a,b,c",[(2,5,6,),(20,10,30),(7,8,6)])
def test_sub2no(a,b,c):

    result= Calculation.sub2no(a,b)
    assert result == c

@pytest.mark.parametrize("a,b,c",[(2,5,6,),(20,10,30),(7,8,6)])
def test_mul2no(a,b,c):

    result= Calculation.mul2no(a,b)
    assert result == c

@pytest.mark.parametrize("a,b,c",[(2,5,6,),(20,10,30),(7,8,6)])
def test_div2no(a,b,c):

    result= Calculation.div2no(a,b)
    assert result == c