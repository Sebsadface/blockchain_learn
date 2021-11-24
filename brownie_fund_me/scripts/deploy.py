from brownie import FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # Pass the price feed address to the FundMe contract
    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
