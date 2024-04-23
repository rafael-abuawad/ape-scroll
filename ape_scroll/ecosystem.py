from typing import cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (534352, 534352),
    "sepolia": (534351, 534351),
}


class ScrollConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    goerli: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class Scroll(Ethereum):
    @property
    def config(self) -> ScrollConfig:  # type: ignore
        return cast(ScrollConfig, self.config_manager.get_config("scroll"))