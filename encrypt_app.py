#!/usr/bin/env python3
"""Encrypt source-app.html into app.enc for the public GitHub Pages repo.

The access code is read interactively and is never written to disk.
Requires: pip install cryptography
"""
from pathlib import Path
from base64 import b64encode
from getpass import getpass
import json, os, sys

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ITERATIONS = 310000

here = Path(__file__).resolve().parent
source = here / "source-app.html"
output = here / "app.enc"

if not source.exists():
    sys.exit("Missing source-app.html. Copy the latest Sanskrit app here first.")

code = getpass("New access code: ")
confirm = getpass("Confirm access code: ")
if not code:
    sys.exit("Access code cannot be empty.")
if code != confirm:
    sys.exit("Access codes do not match.")

salt = os.urandom(16)
iv = os.urandom(12)
key = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=ITERATIONS,
).derive(code.encode("utf-8"))

ciphertext = AESGCM(key).encrypt(iv, source.read_bytes(), None)
payload = {
    "version": 1,
    "kdf": "PBKDF2-SHA256",
    "iterations": ITERATIONS,
    "cipher": "AES-256-GCM",
    "salt": b64encode(salt).decode(),
    "iv": b64encode(iv).decode(),
    "ciphertext": b64encode(ciphertext).decode(),
}
output.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
print(f"Wrote {output}")
print("The access code was not saved.")
