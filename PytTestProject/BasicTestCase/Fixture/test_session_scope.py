import pytest

@pytest.fixture(scope='session',autouse=True)
def my_own_session_run_at_beginning(request): # seesion --- regression
    print('\n my_own_session_run_at_beginning')

    def my_own_session_run_at_end():

        print('\n my_own_session_run_at_end')
    request.addfinalizer(my_own_session_run_at_end)



def test_alpha_1(my_own_session_run_at_beginning):
    print('\n in test_alpha_1()')


# setup and teardown
# function ---- 1 test_case ----- multiple_senario
# module   ---- function ------ multiple test case for multple senario
# class ---- function ----- class --- multiple test case
# session --- function --- nested --- outer function-- depend --- inner
#
# t
# Para - parameterization ---
# Jenkins -- connect with Pytest
# Create env in docker



