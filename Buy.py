# Configurable options
PRIVATE_KEY = "Your Private Key"
RPC_URL = "Your RPC URL"
PUBLIC_KEY = "Your PUBLIC Key (wallet adress)"
MINT = "Contract Adress of the pump.fun token you want to buy"
AMOUNT = 0.0001
SLIPPAGE = 2
PRIORITY_FEE = 0.005

import requests
from solders.transaction import VersionedTransaction
from solders.keypair import Keypair
from solders.commitment_config import CommitmentLevel
from solders.rpc.requests import SendVersionedTransaction
from solders.rpc.config import RpcSendTransactionConfig

response = requests.post(url="https://pumpportal.fun/api/trade-local", data={
    "publicKey": PUBLIC_KEY,
    "action": "buy",             
    "mint": MINT,     
    "amount": AMOUNT,            
    "denominatedInSol": "true", 
    "slippage": SLIPPAGE,              
    "priorityFee": PRIORITY_FEE,        
    "pool": "pump"               
})

if response.status_code == 200 and response.content:
    keypair = Keypair.from_base58_string(PRIVATE_KEY)
    try:
        tx = VersionedTransaction(VersionedTransaction.from_bytes(response.content).message, [keypair])
        
        commitment = CommitmentLevel.Confirmed
        config = RpcSendTransactionConfig(preflight_commitment=commitment)
        txPayload = SendVersionedTransaction(tx, config)

        rpc_response = requests.post(
            url=RPC_URL,
            headers={"Content-Type": "application/json"},
            data=SendVersionedTransaction(tx, config).to_json()
        )

        rpc_json = rpc_response.json()

        if 'result' in rpc_json:
            txSignature = rpc_json['result']
            print(f'Transaction: https://solscan.io/tx/{txSignature}')
        else:
            print("Buy transaction failed")
    except Exception:
        print("Buy transaction failed")
else:
    print("Buy transaction failed")
