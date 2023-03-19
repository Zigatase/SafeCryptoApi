from safecryptoapi.bitcoinlib.wallets import Wallet, wallet_delete
from safecryptoapi.bitcoinlib.mnemonic import Mnemonic

# Generate 12 word mnemonic seed
passphrase = Mnemonic().generate()
print(passphrase)

# Creat Wallet
w = Wallet.create("Wallet123122", keys=passphrase, network='bitcoin')

# Creat New Account
account_btc2 = w.new_account('Account BTC 2')
account_ltc1 = w.new_account('Account LTC', network='litecoin')

# Get key
w.get_key()

w.get_key(account_btc2.account_id)
w.get_key(account_ltc1.account_id)

# Print info Wallet
w.info()