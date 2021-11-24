from brownie import SimpleStorage, accounts, config


def read_contract():
    # `SimpleStorage[-1]` gives most recent deployment
    simple_storage = SimpleStorage[-1]
    # ABI
    # Adress
    print(simple_storage.retrieve())


def main():
    read_contract()
