import util
import parser


def encrypt_file(file_name: str, key: int = 3, output_file: str = None) -> None:
    """
    Encrypt a file using a Caesar cipher with a specified key and write to the specified file.

    Args:
        file_name (str): The name of the file to encrypt.
        key (int, optional): The shift value for the cipher. Defaults to 3.
        output_file (str, optional): The name of the file to write the output to. Defaults to `file_name`
    """
    if output_file is None:
        output_file = file_name

    lines = util.read_file(file_name)
    lines_encrypted = util.encrypt_lines(lines, key)

    util.write_file(output_file, lines_encrypted)


def decrypt_file(file_name: str, key: int = 3, output_file: str = None) -> None:
    """
    Decrypt a file using a Caesar cipher with a specified key and write to the specified file.

    Args:
        file_name (str): The name of the file to decrypt.
        key (int, optional): The shift value for the cipher. Defaults to 3.
        output_file (str, optional): The name of the file to write the output to. Defaults to `file_name`
    """
    if output_file is None:
        output_file = file_name

    lines = util.read_file(file_name)
    lines_decrypted = util.decrypt_lines(lines, key)

    util.write_file(output_file, lines_decrypted)


def brute_force(file_name: str, output_file: str = None) -> None:
    pass


if __name__ == "__main__":
    args = parser.parse_arguments()
    if args["encrypt"] is True:
        encrypt_file(args["file"], args["key"], args["output"])
    else:
        decrypt_file(args["file"], args["key"], args["output"])
