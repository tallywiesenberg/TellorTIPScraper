import requests

from decouple import config
import web3
from web3 import Web3


WEB3_INFURA_PROJECT_ID = config('WEB3_INFURA_PROJECT_ID')

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{WEB3_INFURA_PROJECT_ID}'))

address = "0x0ba45a8b5d5575935b8158a88c631e9f9c95a2e5"

r = requests.get(f'https://api.etherscan.io/api?module=contract&action=getabi&address={address}')
abi = r.json()
#need to access abi from abi json
tellor_core = web3.eth.contract(address=address, abi=???)