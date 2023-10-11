
def test_file_2_specific():
    assert 2*2 ==4

def test_using_common_fixture(common_pallindrom_fixture):
    assert common_pallindrom_fixture('123') is True