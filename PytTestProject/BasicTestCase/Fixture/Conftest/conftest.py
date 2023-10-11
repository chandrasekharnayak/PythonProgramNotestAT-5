'''pytest serves as a way to organize fixtures and othe configuration option
for your test. This file is automatically discovered by help of pytest and
allows you to share fixture and configuration across multiple tset modules '''

import pytest

@pytest.fixture
def common_pallindrom_fixture():
    def is_pallindrom(str):
        return str == str[::-1]
    return is_pallindrom

