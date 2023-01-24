import pytest

@pytest.fixture()
def SetUp():
    print("start")

def test_methodA(SetUp):
    print("running method A")

def test_methodB(SetUp):
    print("running method B")