import pytest


@pytest.mark.order(1)
@pytest.mark.usefixtures('setup')
def test_setup():
    pass
