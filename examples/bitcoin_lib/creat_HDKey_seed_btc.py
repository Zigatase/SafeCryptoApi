from safecryptoapi.bitcoinlib import *

# Generation 12 word mnemonic seed
seed = mnemonic.Mnemonic(language='english').generate()

# Creating master key wizard using seed
master_key = keys.HDKey.from_seed(seed)
print(master_key)

# X Key
xprivate_key = master_key.wif_private()
xpublic_key = master_key.wif_public()

# Hex Key
hex_private_key = master_key.private_hex
hex_public_key = master_key.public_hex

# Wif Key
wif_private_key = master_key.wif_key()

# Print Wif and Hex key
print(f"Wif Private: {wif_private_key}")
print(f"Hex Public: {hex_public_key}")

# Legacy
print(f"\nLegacy Address: {master_key.address(encoding='base58')}")

# Segwit
print(f"Segwit Address: {master_key.address(encoding='bech32')}")

# Script
print(f"Script Address: {master_key.address(script_type='p2sh')}")

'''
Electrum check address generation:
    p2pkh:
    p2wpkh:
'''