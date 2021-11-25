from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import deploy_mocks, get_account


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
        deploy_mocks
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
