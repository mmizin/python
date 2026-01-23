@pytest.fixture(scope="class")
def _setup():
    ...


@pytest.fixture(scope="function")
def _setup_test_user(
    request
):
    fixture_data = request.getfixturevalue("_setup")
