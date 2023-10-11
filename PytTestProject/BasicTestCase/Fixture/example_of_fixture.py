import pytest
import tempfile
import os
import shutil

@pytest.fixture
def temp_directory(request):
    #before the function exceute :- setup -- precondition
    temp_dir = tempfile.mkdtemp()
    print(f'Setting Up temporary directory:{temp_dir}')

    yield temp_dir # yiled it's a generator the temporary dir path to the test

    #teardown :- Remove the temp dir after the test
    print(f'Tearning down temp directory:{temp_dir}')
    # os.rmdir(temp_dir)
    shutil.rmtree(temp_dir)
