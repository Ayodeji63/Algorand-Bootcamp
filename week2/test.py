import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))


# My address: OVCI6WVFYIKZWWHTOWJ746SHE5LLB7PTBVW3LALHMCBKFXC3FJIY5DJTWE
# My passphrase: initial capital air basket box bounce april during tackle coil have stumble help wine shuffle cruel moon brush whip heart spin save syrup absent agree
generate_algorand_keypair()


def first_transaction_example(my_mnemonic, my_address):
    algod_address = "https://testnet-api.algonode.cloud"
    algod_client = algod.AlgodClient("", algod_address)

    print("My address: {}".format(my_address))
    private_key = mnemonic.to_private_key(my_mnemonic)
    print(private_key)
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = constants.MIN_TXN_FEE
    params.fee = 1000
    receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    amount = 100000
    note = "Hello World".encode()

    unsigned_txn = transaction.PaymentTxn(
        my_address, params, receiver, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Signed transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(
            algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(
        account_info.get('amount')))
    print("Amount transfered: {} microAlgos".format(amount))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")


# private_key = "8A0NJgSU7+9HyzmK/TY0vzWrYrRQSjEaQT5+P+i919LncWd6cbFiNNs6m/0cTAj2ZqiEXgTDT8thhGj4fsGkNQ=="
# my_mnemonic = "initial capital air basket box bounce april during tackle coil have stumble help wine shuffle cruel moon brush whip heart spin save syrup absent agree"
# my_address = "OVCI6WVFYIKZWWHTOWJ746SHE5LLB7PTBVW3LALHMCBKFXC3FJIY5DJTWE"
# first_transaction_example(my_mnemonic, my_address)

private_key = "LcKFv+JkPOqRlm8daiXHOa6wBvhMYVAQnN63BhKX9L0hqROY6r61RiRYyhbtyjRn2dd7O0GhOnciT4rFavBLtQ=="
my_mnemonic = "east blade garlic evolve juice kind region hurdle dry noble toe toe genuine accuse guitar genuine anxiety icon urban hidden catch chair use absent lava"
my_address = "EGURHGHKX22UMJCYZILO3SRUM7M5O6Z3IGQTU5ZCJ6FMK2XQJO25ZIQROI"
first_transaction_example(my_mnemonic, my_address)
# account 2 Address = QHREXSB574H2JZV75S5OIN2JKKUEAWDPMXRD2SGFKCWSIE3JLYKPXVITTI
# My private key = sjpZptMP/y2NXEVvUkDdBqjSzOyBnnc6K1ARKeBlPy+B4kvIPf8PpOa/7LrkN0lSqEBYb2XiPUjFUK0kE2leFA==
# My passphrase = film gossip spring wood wrap enter tongue earn evil access huge lesson pipe creek author ozone exclude provide pool much scare sunny ketchup ability master

# Account 3
# My address = EGURHGHKX22UMJCYZILO3SRUM7M5O6Z3IGQTU5ZCJ6FMK2XQJO25ZIQROI
# My private key = LcKFv+JkPOqRlm8daiXHOa6wBvhMYVAQnN63BhKX9L0hqROY6r61RiRYyhbtyjRn2dd7O0GhOnciT4rFavBLtQ==
# My passphrase = east blade garlic evolve juice kind region hurdle dry noble toe toe genuine accuse guitar genuine anxiety icon urban hidden catch chair use absent lava
