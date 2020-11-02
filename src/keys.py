import argparse
import json
import os

from decouple import config
import requests
import web3
from web3 import Web3


WEB3_INFURA_PROJECT_ID = config('WEB3_INFURA_PROJECT_ID')

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{WEB3_INFURA_PROJECT_ID}'))

ETHERSCAN_KEY = config("ETHERSCAN_KEY")

address = Web3.toChecksumAddress("0x0ba45a8b5d5575935b8158a88c631e9f9c95a2e5")

r = requests.get(f'https://api.etherscan.io/api?module=contract&action=getabi&address={address}&apikey={ETHERSCAN_KEY}').json()

with open('./abi.json') as f:
    abi = f.read()
# abi = json.loads(r["result"])

# if not os.path.isfile('abi.json'):
#     with open('abi.json', 'w', encoding='utf-8') as f:
#         json.dump(abi, f, ensure_ascii=False, indent=4)

tellor_core = w3.eth.contract(address=address, abi=abi)