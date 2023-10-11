
def test_file1_specific():
    assert 1+1 ==2

def test_using_common_fixture(common_pallindrom_fixture):
    assert common_pallindrom_fixture('mam') is True