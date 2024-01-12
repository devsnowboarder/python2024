
import pytest

# pytest_plugins = [
#     "fixtures.conftest"
# ]
@pytest.fixture(scope ="class")
def setup():
    print(" I will be executing first")
    yield
    print(" I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Jimmy","Wowng","test@aol.com"]


@pytest.fixture(params=[("chrome","mike"),("Firefox","shetty"),("IE","jimmy")])
def crossBrowser(request):
    return request.param
