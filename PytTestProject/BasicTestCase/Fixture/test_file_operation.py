import os
from TREENETRA_AT_5.PytTestProject.BasicTestCase.Fixture.example_of_fixture import temp_directory


def test_write_and_read_file(temp_directory):

    test_file = os.path.join(temp_directory,'test_file.txt')

    with open(test_file,'w') as var:
        var.write('Python TREENETRA')

    with open(test_file,'r') as var:
        content = var.read()
    assert content == 'PythonTREENETRA'
