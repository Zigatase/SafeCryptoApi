from safecryptoapi.pywallet import wallet

# Generate 12 word mnemonic seed
seed = wallet.generate_mnemonic()

# Create bitcoin wallet
walletBTC = wallet.create_wallet(network="BTC", seed=seed, children=1)

# Create bitcoin wallet
walletETH = wallet.create_wallet(network="ETH", seed=seed, children=1)

# Print Generation Wallet
print(walletBTC)
print(walletETH)