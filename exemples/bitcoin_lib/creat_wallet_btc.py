from safecryptoapi.bitcoinlib.wallets import Wallet

# --- Creat BTC Address ---
# Creat Legacy (P2PKH) Address
wallet_P2PKH = Wallet.create('WalletLegacy1', network='bitcoin', witness_type='legacy')
key_P2PKH = wallet_P2PKH.get_key()

# Creat Segwit (P2WPKH) Address
wallet_P2WPKH = Wallet.create('WalletSegwit1', network='bitcoin', witness_type='segwit')
key_P2WPKH = wallet_P2WPKH.get_key()

# Creat Script (P2SH)
wallet_P2SH = Wallet.create('WalletScript1', network='bitcoin', witness_type='p2sh-segwit')
key_P2SH = wallet_P2SH.get_key()

# Print For All Address
print(f"Legacy: {key_P2PKH.address}"
      f"\nSegwit: {key_P2WPKH.address}"
      f"\nScryptL {key_P2SH.address}")
