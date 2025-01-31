# unbreakable_encryption.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Edited: Brendon A. Kay for exercise 4

import base64

from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


def encrypt_image(original_bytes: bytes) -> Tuple[int, int]:
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> bytes:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    IKE_IMAGE = "Fighters-of-zaron-pirate-king-ike.png"
    NEW_IKE_IMAGE = "Fighters-of-zaron-pirate-king-ike_2.png"

    with open(IKE_IMAGE, "rb") as image:
        b64encoded_file = base64.b64encode(image.read())

    key1, key2 = encrypt_image(b64encoded_file)
    result: bytes = decrypt(key1, key2)

    with open(NEW_IKE_IMAGE, "wb") as new_image:
        new_image.write(base64.b64decode(result))

    print("Success!")
