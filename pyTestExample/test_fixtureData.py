import pytest
from pyTestExample.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        print("\n",dataLoad)

    def test_editProfile2(self, dataLoad):
        print("\n",dataLoad[1])

    def test_chrome(self,crossBrowser):
        print(crossBrowser)
