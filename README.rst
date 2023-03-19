
SafeCryptoApi
===========

**Simple BIP32 (HD) wallet creation for: BTC, BTX, RVN, MXT, BTG, BCH, ETH, LTC, DASH, DOGE**

BIP32 (or HD for "hierarchical deterministic") wallets allow you to create
child wallets which can only generate public keys and don't expose a
private key to an insecure server.

This library simplify the process of creating new wallets for the
BTC, BTX, RVN, MXT, BTG, BCH, ETH, LTC, DASH and DOGE cryptocurrencies.

Enjoy!

--------------

Installation
-------------

Install via PiP:

.. code:: bash

   $ sudo pip install safecryptoapi


Example code:
=============

Create HD Wallet
----------------

The following code creates a new Bitcoin HD wallet:

.. code:: python

    # create_btc_wallet.py

    from safecryptoapi import wallet

    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()

    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)

    print(w)

Output looks like this:

.. code:: bash

    $ python create_btc_wallet.py

    {
      "coin": "BTC",
      "seed": "price scare winner wrap describe slender toy wedding type become book beach",
      "private_key": 'd4a605fb4196f7f872b2c4b60a30a2f04ea050b457df30eee40b04ccf84df624',
      "public_key": '047f6a8a7c5786a149ee5d2996b0f1a0b08cfd3f019f117566a7c6f7e9dbc05a6ce36c4c0fd84a9e56f6748ddcd7d0c63d734c645a446b547ff314a09e5a29c46e',
      "xprivate_key": "xprv9s21ZrQH143K2Dizn667UCo9oYPdTPSMWq7D5t929aXf1kfnmW79CryavzBxqbWfrYzw8jbyTKvsiuFNwr1JL2qfrUy2Kbwq4WbBPfxYGbg",
      "xpublic_key": "xpub661MyMwAqRbcEhoTt7d7qLjtMaE7rrACt42otGYdhv4dtYzwK3RPkfJ4nEjpFQDdT8JjT3VwQ3ZKjJaeuEdpWmyw16sY9SsoY68PoXaJvfU",
      "address": '1Hsn2cRy1B3Bvk72bFa6xpVHf9F92vx1D8'
      "wif": "L4M57uEdXVz13uLUfvoK7dsMPjqaEsVVFTHAUjNxYZFMCvMSvorC",
      "children": [{
         "xpublic_key": 'xpub69FQtJwZTFLtC7ruWDkJsojMeQMvgHxxtLJi1QLDZhSPTyeUitXG5vs95qWL2h4wKbYtEjoqjEWkBo7T4doNNwrC5arxKMBj4ejnVe2eEPe',
         "address": '1FWYdwjLuzFJN1yRciV6rErRcujZh3niA4',
         "path": 'm/0',
         "bip32_path": "m/44'/0'/0'/0",
         "wif": ''
     }]
    }

Similarly, you can do the same for an Ethereum wallet:

.. code:: python

    # create_eth_wallet.py

    from safecryptoapi import wallet

    seed = wallet.generate_mnemonic()
    w = wallet.create_wallet(network="ETH", seed=seed, children=1)

    print(w)

Output looks like this (no WIF for Ethereum):

.. code:: bash

    $ python create_eth_wallet.py

    {
      "coin": "ETH",
      "seed": "traffic happy world clog clump cattle great toy game absurd alarm auction",
      "address": "0x3b777f60eb04fcb13e6b27e468532e491409722e",
      "xprivate_key": "xprv9yTuSjwb95QZznV6epMWpb4Kpc2S8ZRaQuAf5B697YXtQD2tDmmJ5KvwJWVjtbVrdJ1WBKNnuodrpTKGfHfiPSEgrAxUjL5RP1gQwwT3fFx",
      "xpublic_key": "xpub6GhhMtkVjoPi5DKtqapKzMzrzdGjo1EPc7Ka6KdeoXYdCrTBH1Hu1wKysm8boWSy8VeTKVJi6gQJ2qJ4YG2ZhvFDcUUgMJrFCJWN1PGtBry",
      "wif": "",
      "children": [{
        "address": "0x87eb82d43fa7316df0a989c0d951a9037ed02f9b",
        "path": "m/0",
        "xpublic_key": "xpub6LnpVXD73jNuAYXxzQCnEY6wXQspwkiAEkZWoX4BW9Tzx6KbUrMUYAU1Yvw4kebPHSPiEJPo8irHWHSwQR6WuVwUj85xURsugPWeJVH6sau",
        "wif": ""
      }]
    }

\* Valid options for `network` are: BTC, BTG, BCH, LTC, DASH, DOGE

Create Child Wallet
-------------------

You can create child-wallets (BIP32 wallets) from the HD wallet's
**Extended Public Key** to generate new public addresses without
revealing your private key.

Example:

.. code-block:: python

    # create_child_wallet.py

    from safecryptoapi import wallet

    WALLET_PUBKEY = 'YOUR WALLET XPUB'

    # generate address for specific user (id = 10)
    user_addr = wallet.create_address(network="BTC", xpub=WALLET_PUBKEY, child=10)

    # or generate a random address, based on timestamp
    rand_addr = wallet.create_address(network="BTC", xpub=WALLET_PUBKEY)

    print("User Address\n", user_addr)
    print("Random Address\n", rand_addr)

Output looks like this:

.. code:: bash

    $ python create_child_wallet.py

    User Address
    {
      "address": "13myudz3WhpBezoZue6cwRUoHrzWs4vCrb",
      "path": "m/0/395371597"
    }
    Random Address
    {
      "address": "1KpS2wC5J8bDsGShXDHD7qdGvnic1h27Db",
      "path": "m/0/394997119"
    }

-----

IMPORTANT
=========

Enjoy!