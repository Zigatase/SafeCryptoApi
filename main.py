# SafeCryptoApi -> PyWallet (BugHix)
from safecryptoapi.pywallet import wallet

# generate 12 word mnemonic seed
seed = wallet.generate_mnemonic()

# create bitcoin wallet
w = wallet.create_wallet(network="BTC", seed=seed, children=1)

print(w)

# SafeCryptoApi -> Bitcoinlib
