from typing import List
from string import (
    ascii_lowercase as ASCII_LOWERCASE,
    ascii_uppercase as ASCII_UPPERCASE,
)


def read_file(file_name: str) -> List[str]:
    """
    Reads the contents of a file and returns a list of lines.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        List[str]: A list containing the lines of the file.
    """
    with open(file_name, "r") as reader:
        return reader.readlines()


def write_file(file_name: str, lines: List[str]) -> None:
    """
    Writes a list of lines to a file.

    Args:
        file_name (str): The name of the file to write to.
        lines (List[str]): A list of lines to be written to the file.
    """
    with open(file_name, "w") as writer:
        writer.writelines(lines)


def shift_char(char: str, key: int) -> str:
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


def encrypt_lines(lines: List[str], key: int = 3) -> List[str]:
    """
    Encrypts a list of strings using a Caesar cipher with a specified key.

    Args:
        lines (List[str]): The list of strings to encrypt.
        key (int, optional): The shift value for the cipher. Default is 3.

    Returns:
        List[str]: A list of encrypted strings.
    """
    return ["".join(shift_char(char, key) for char in line) for line in lines]


def decrypt_lines(lines: List[str], key: int = 3) -> List[str]:
    """
     Decrypts a list of strings using a Caesar cipher with a specified key.

    Args:
        file_name (str): The name of the file to write to.
        key (int, optional): The shift value for the cipher. Defaults to -3.

    Returns:
        List[str]: A list of decrypted strings.
    """
    return ["".join(shift_char(char, -key) for char in line) for line in lines]
