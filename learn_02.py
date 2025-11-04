import os
from rich import print
import argparse  # Solution (3)


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # Solution (1)
    source_pdf_file_path = r"c:\alaki\dolaki\temp.pdf"

    print(f"source_pdf_file_path = {source_pdf_file_path}")
    print("\nFinished.\n")
    # /Solution (1)

    # Solution (2)
    # source_pdf_file_path = input("Sourcd PDF File Path: ")

    # print(f"source_pdf_file_path = {source_pdf_file_path}")
    # print("\nFinished.\n")
    # /Solution (2)

    # Solution (3)
    # description: str = "You must specify the 'PDF' file path!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("file_path", help="'PDF' file path")
    # args = parser.parse_args()

    # source_pdf_file_path: str = args.file_path

    # print(f"source_pdf_file_path = {source_pdf_file_path}")
    # print("\nFinished.\n")
    # /Solution (3)

    # Test
    # description: str = "You must specify the full name!"
    # parser = argparse.ArgumentParser(description=description)
    # parser.add_argument("first_name", help="First Name")
    # parser.add_argument("last_name", help="Last Name")
    # args = parser.parse_args()

    # first_name: str = args.first_name
    # last_name: str = args.last_name

    # full_name: str = f"Full Name: {first_name} {last_name}"

    # print(full_name)
    # /Test


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"[-] {e}\n")
