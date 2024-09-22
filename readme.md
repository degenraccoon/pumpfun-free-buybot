# Pump.fun Buy Bot by @degenraccoon

This is a simple, free to use bot that will buy a specified token on pump.fun.

!!If you need a custom volume bot, auto sniper, bump bot for pump.fun/solana, contact @degenraccoon on TG
!!We have a ready to use auto sniper for sale, contact @degenraccoon on TG

## What will you need for this script?

- Python 3.6 or higher
- `requests` library
- `solders` library

You can install the required libraries using pip:

```
pip install requests solders
```

## Configuration

Before running the script, you need to configure the following parameters at the top of the `Buy.py` file:

```python
PRIVATE_KEY = "Your_Private_Key_Here"
RPC_URL = "Your_RPC_URL_Here"
PUBLIC_KEY = "Your_Public_Key_Here"
MINT = "Token_Mint_Address_Here"
AMOUNT = 0.0001  # Amount to buy
SLIPPAGE = 50    # Slippage tolerance
PRIORITY_FEE = 0.005  # Priority fee
```

- `PRIVATE_KEY`: Your Solana wallet's private key
- `RPC_URL`: The RPC endpoint URL you want to use
- `PUBLIC_KEY`: Your Solana wallet's public key
- `MINT`: The mint address of the token you want to buy
- `AMOUNT`: The amount of tokens to buy (denominated in SOL)
- `SLIPPAGE`: The slippage tolerance for the transaction
- `PRIORITY_FEE`: The priority fee for the transaction

## Usage

1. Clone this repository or download the `Buy.py` file.
2. Configure the script by editing the parameters at the top of the file.
3. Run the script using Python:

```
python Buy.py
```

The script will attempt to execute the buy transaction and print the transaction URL if successful, or an error message if it fails.

## Security Warning

This script contains sensitive information (private key). Make sure to keep it secure and never share it publicly. Consider using environment variables or a secure configuration management system for production use.

## Disclaimer

This script is provided as-is, without any warranties. Use it at your own risk. Make sure you understand the implications of executing transactions on the Solana blockchain before using this script.

## License

[MIT License](LICENSE)
