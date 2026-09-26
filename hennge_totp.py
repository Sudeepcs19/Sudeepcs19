import time
import hmac
import hashlib
import struct

USER_ID = "ninjasamuraisumotorishogun@example.com"
SECRET = USER_ID + "HENNGECHALLENGE004"

TIME_STEP = 30
DIGITS = 10


def generate_totp():
    counter = int(time.time()) // TIME_STEP
    counter_bytes = struct.pack(">Q", counter)

    digest = hmac.new(
        SECRET.encode("ascii"),
        counter_bytes,
        hashlib.sha512
    ).digest()

    offset = digest[-1] & 0x0F

    binary_code = (
        ((digest[offset] & 0x7F) << 24)
        | (digest[offset + 1] << 16)
        | (digest[offset + 2] << 8)
        | digest[offset + 3]
    )

    return f"{binary_code % 10**DIGITS:010d}"


print("Current TOTP:", generate_totp())