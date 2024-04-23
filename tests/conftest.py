import ape
import pytest


@pytest.fixture
def networks():
    return ape.networks


@pytest.fixture
def accounts():
    return ape.accounts


@pytest.fixture
def scroll(networks):
    return networks.get_ecosystem("scroll")


@pytest.fixture(autouse=True)
def eth_tester_provider():
    if not ape.networks.active_provider or ape.networks.provider.name != "test":
        with ape.networks.get_ecosystem("scroll").local.use_provider("test") as provider:
            yield provider
    else:
        yield ape.networks.provider