from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # Pass the price feed address to the FundMe contract

    # if on a persistent network(eg: rinkeby), use the associate address
    # otherwise, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mocks Deployed!")

    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
