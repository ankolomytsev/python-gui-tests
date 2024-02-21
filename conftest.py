import pytest
from fixture.application import Application
from comtypes.client import CreateObject
import os


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\akolomytsev\\addressbook\\Addressbook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xl_"):
            testdata = load_from_xl(fixture[3:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_xl(file):
    xl = CreateObject('Excel.Application')
    xl.Workbooks.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.xlsx"))
    testdata = []
    for i in range(10):
        group = xl.Range[f'A{i+1}'].Value[()]
        testdata.append(group)
    xl.Quit()
    return testdata