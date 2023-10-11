import pytest

@pytest.fixture(scope='class')
def class_level_fixture():
    print('\n Settings up class-level fixtues')

    data = {'Keys':'Values','Keys_2':['A','B','C']}
    yield data
    print('\n Teardown up class-level fixtues')


#Test class using the class-level

class TestClassLevelFixture:

    def test_case_1(self,class_level_fixture):
        assert 'Keys' in class_level_fixture
        assert class_level_fixture['Keys']=='Values'
        # print(class_level_fixture['Keys'])
        # print(type(class_level_fixture))

    def test_case_2(self,class_level_fixture):
        assert 'C' in class_level_fixture['Keys_2']

    
    def test_case_3(self,class_level_fixture):
        assert 'D' in class_level_fixture['Keys_2']



