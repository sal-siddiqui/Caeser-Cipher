from typing import List, Dict
from string import (
    ascii_lowercase as ASCII_LOWERCASE,
    ascii_uppercase as ASCII_UPPERCASE,
)
import argparse


def _read_file(file_name: str) -> List[str]:
    """
    Reads the contents of a file and returns a list of lines.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        List[str]: A list containing the lines of the file.
    """
    with open(file_name, "r") as reader:
        return reader.readlines()


def _write_file(file_name: str, lines: List[str]) -> None:
    """
    Writes a list of lines to a file.

    Args:
        file_name (str): The name of the file to write to.
        lines (List[str]): A list of lines to be written to the file.
    """
    with open(file_name, "w") as writer:
        writer.writelines(lines)


def _shift_char(char: str, key: int) -> str:
    """
    Shifts a character by the given key in the alphabet while preserving the case.

    Args:
        char (str): The character to shift.
        key (int): The number of positions to shift.

    Returns:
        str: The shifted character or the original character if it's not alphabetical.
    """
    if char.islower():
        # Shift lowercase letters
        return ASCII_LOWERCASE[(ASCII_LOWERCASE.index(char) + key) % 26]
    elif char.isupper():
        # Shift uppercase letters
        return ASCII_UPPERCASE[(ASCII_UPPERCASE.index(char) + key) % 26]
    return char  # Return non-alphabetical characters unchanged


def _encrypt(lines: List[str], key: int = 3) -> List[str]:
    """
    Encrypts a list of strings using a Caesar cipher with a specified key.

    Args:
        lines (List[str]): The list of strings to encrypt.
        key (int, optional): The shift value for the cipher. Default is 3.

    Returns:
        List[str]: A list of encrypted strings.
    """
    return ["".join(_shift_char(char, key) for char in line) for line in lines]


def _decrypt(lines: List[str], key: int = 3) -> List[str]:
    """
     Decrypts a list of strings using a Caesar cipher with a specified key.

    Args:
        file_name (str): The name of the file to write to.
        key (int, optional): The shift value for the cipher. Defaults to -3.

    Returns:
        List[str]: A list of decrypted strings.
    """
    return ["".join(_shift_char(char, -key) for char in line) for line in lines]


def parse_arguments() -> Dict[str:str]:
    global_parser = argparse.ArgumentParser(prog="ccipher")

    subparsers = global_parser.add_subparsers(
        title="subcommands", help="Ceaser Cipher Operations"
    )

    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    encrypt_parser.add_argument(
        dest="file_name", type=str, help="The name of the file to encrypt."
    )
    encrypt_parser.add_argument(
        dest="key", default=3, help="The shift value for the cipher. Defaults to 3."
    )
    encrypt_parser.add_argument(
        dest="output_file",
        type=str,
        default=None,
        help="The name of the file to write the output to. Defaults to `file_name`",
    )
    encrypt_parser.set_defaults(func=encrypt)

    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    decrypt_parser.add_argument(
        dest="file_name", type=str, help="The name of the file to encrypt."
    )
    decrypt_parser.add_argument(
        dest="key", default=3, help="The shift value for the cipher. Defaults to 3."
    )
    decrypt_parser.add_argument(
        dest="output_file",
        type=str,
        default=None,
        help="The name of the file to write the output to. Defaults to `file_name`",
    )
    decrypt_parser.set_defaults(func=decrypt)

    args = global_parser.parse_args()

    print(args.__dict__)


def encrypt(file_name: str, key: int = 3, output_file: str = None) -> None:
    """
    Encrypt a file using a Caesar cipher with a specified key and write to the specified file.

    Args:
        file_name (str): The name of the file to encrypt.
        key (int, optional): The shift value for the cipher. Defaults to 3.
        output_file (str, optional): The name of the file to write the output to. Defaults to `file_name`
    """
    if output_file is None:
        output_file = file_name

    lines = _read_file(file_name)
    lines_encrypted = _encrypt(lines, key)

    _write_file(output_file, lines_encrypted)


def decrypt(file_name: str, key: int = 3, output_file: str = None) -> None:
    """
    Decrypt a file using a Caesar cipher with a specified key and write to the specified file.

    Args:
        file_name (str): The name of the file to decrypt.
        key (int, optional): The shift value for the cipher. Defaults to 3.
        output_file (str, optional): The name of the file to write the output to. Defaults to `file_name`
    """
    if output_file is None:
        output_file = file_name

    lines = _read_file(file_name)
    lines_decrypted = _decrypt(lines, key)

    _write_file(output_file, lines_decrypted)


if __name__ == "__main__":
    pass
