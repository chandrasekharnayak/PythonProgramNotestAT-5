import pytest

@pytest.fixture(scope='module')
def module_level_fixture():
    print('\n Settings up class-level fixtues')

    data = {'Keys':'Values','Keys_2':['A','B','C']}
    yield data
    print('\n Teardown up class-level fixtues')


def test_case_1(module_level_fixture):
    assert 'Keys' in module_level_fixture
    assert module_level_fixture['Keys'] == 'Values'



def test_case_2(module_level_fixture):
    assert 'C' in module_level_fixture['Keys_2']


def test_case_3(module_level_fixture):
    assert 'D' in module_level_fixture['Keys_2']

# pytest test_module_scope.py::test_case_2 -v -s