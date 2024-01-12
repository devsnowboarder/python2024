import pytest
from pyTestExample.BaseClass import BaseClass


# @pytest.mark.parametrize("x,y,z", [(10, 20, 200), (20, 40, 200)])
# def test_method( x, y, z, ):
#     print("this is for logging")
#     assert x * y == z


class TestExample3(BaseClass):

    # def test_method(self, x, y, z,):
    #     print("this is for logging")
    #     assert x * y == z

    def test_method2(self, BaseClass):
        self.getLogger()
