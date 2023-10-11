# what is markers?
#
# In Pytest markers are used to add metadata to test. making it easier to
# categorize and control test executions. Markers Can be used for various purpose, condtion
# test case, running or skiping, grouping tests.

'''
1.skip
2.skipif
3.xfail
4.parametrize
5.timeout
6.Custom Marker

'''
import pytest

#skip

#
# def test_implemented():
#     assert True
#
# @pytest.mark.skip(reason='Due smoke not use it')
# def test_not_implemented():
#     assert True

#----------------------------------------------------------------------------------------
#skipif

# @pytest.mark.skipif(condition=False,reason='mera maan')
# def test_skip_if_condition_true():
#     assert True

# import pytest
# import platform
#
# def test_os_dependent_function():
#     assert True
#
# @pytest.mark.skipif(platform.system()== 'Linux',reason='In same os not working')
# def test_os_dependent_function_linux_only():
#     assert True
#
#
# @pytest.mark.skipif(platform.system()== 'Windows',reason='In same os not working')
# def test_os_dependent_function_windows_only():
#     assert True

#------------------------------------------------------------------------------------------------

#xfail

# import pytest
#
# # @pytest.mark.xfail
# # def test_excepted_to_fail():
# #     assert False
#
# def divide(a,b):
#     if b == 0:
#         raise ValueError('Cannot divied by Zero')
#     return a/b
#
# @pytest.mark.xfail
# def test_divided_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         result = divide(10,0)
#         assert result == 10

#parameterize

# import pytest
# from TREENETRA_AT_5.PytTestProject.BasicTestCase.decore_cal import add
#
# @pytest.mark.parametrize("input_a,input_b,expected",
#                          [(1,2,(2,3)),
#                           (10,20,(200,30)),
#                           (-1,-2,(2,-3)),
#                           (-10,-20,(200,-30)),
#                           (0,0,(1,1))])
# def test_decore(input_a,input_b,expected):
#     result = add(input_a,input_b)
#     assert result == expected


# import pytest
# import time
#
# def perform_compex_calculation():
#     time.sleep(3)
#     return 'Result'
#
# @pytest.mark.timeout(2)
# def test_complex_calculation_timeout():
#     result = perform_compex_calculation()
#     assert result =='Result'

#Custome Markers

# import pytest
#
# @pytest.mark.smoke
# def test_1():
#     assert True
#
# @pytest.mark.regression
# def test_2():
#     assert True
#
# @pytest.mark.regression
# def test_3():
#     assert True
#
# @pytest.mark.smoke
# def test_4():
#     assert True
#
# def test_5():
#     assert True
#
# def test_6():
#     assert True

