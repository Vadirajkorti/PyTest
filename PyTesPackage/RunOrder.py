import pytest

@pytest.fixture(scope='module')
def SetUp():
    print("start")
    yield
    print("end")

@pytest.mark.run(order=2)
def test_methodA(SetUp):
    print("running method A")

@pytest.mark.run(order=1)
def test_methodB(SetUp):
    print("running method B")

def test_methodC(SetUp):
    print("running method C")

def test_methodD(SetUp):
    print("running method D")

def test_methodE(SetUp):
    print("running method E")