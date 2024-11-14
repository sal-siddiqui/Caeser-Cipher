from argparse import ArgumentParser
from typing import Dict


def parse_arguments() -> Dict:
    parser = ArgumentParser()

    parser.description = "Encrypt or decrypt a file using a specified key."
    parser.usage = "ccipher.py [-h] {-e | -d} file key [-o OUTPUT]"
    parser.epilog = "Note: You must choose either the -e (encrypt) or -d (decrypt) option, but not both."

    parser.add_argument(
        "file",
        help="Name of the file to encrypt or decrypt",
        type=str,
    )
    parser.add_argument(
        "key", help="The key used for encryption or decryption", type=int
    )

    parser.add_argument(
        "-e", "--encrypt", help="encrypts the specified file", action="store_true"
    )
    parser.add_argument(
        "-d", "--decrypt", help="decrypts the specified file", action="store_true"
    )
    parser.add_argument(
        "-o", "--output", help="saves the result in another file", type=str
    )

    args = parser.parse_args()

    if not (args.encrypt ^ args.decrypt):
        parser.error(
            "The options -e/--encrypt and -d/--decrypt are mutually exclusive. Please choose one."
        )

    return args.__dict__
