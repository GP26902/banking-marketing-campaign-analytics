import pytest

import data_prep


@pytest.fixture(scope="session")
def raw():
    """The raw file, untouched."""
    return data_prep.load_raw()


@pytest.fixture(scope="session")
def df():
    """The prepared table the dashboard uses."""
    return data_prep.prepare()
