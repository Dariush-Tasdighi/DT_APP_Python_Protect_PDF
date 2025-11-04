import os
from rich import print
from typing import Tuple


def split_file_path(file_path: str) -> Tuple[str, str, str]:
    """Split file path"""

    print(f"file_path = {file_path}\n")  # Test

    directory, filename = os.path.split(p=file_path)

    print(f"directory = {directory}")  # Test
    print(f"filename = {filename}")  # Test

    name, extension = os.path.splitext(p=filename)

    print(f"name = {name}")  # Test
    print(f"extension = {extension}")  # Test

    return directory, name, extension


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # source_pdf_file_path: str = "c:\alaki\dolaki\temp.pdf"
    # target_pdf_file_path: str = "c:\alaki\dolaki\temp_protected.pdf"

    source_pdf_file_path: str = "alaki"  # Test
    # source_pdf_file_path: str = "alaki.pdf"  # Test
    # source_pdf_file_path: str = "./alaki"  # Test
    # source_pdf_file_path: str = "./alaki.pdf"  # Test
    # source_pdf_file_path: str = "./test/alaki"  # Test
    # source_pdf_file_path: str = "./test/alaki.pdf"  # Test
    # source_pdf_file_path: str = "c:\\test\\alaki"  # Test
    # source_pdf_file_path: str = "c:\\test\\alaki.pdf"  # Test
    # source_pdf_file_path: str = r"c:\test\alaki"  # Test
    # source_pdf_file_path: str = r"c:\test\alaki.pdf"  # Test

    directory, name, extension = split_file_path(
        file_path=source_pdf_file_path,
    )

    new_filename: str = f"{name}_protected{extension}"
    target_pdf_file_path: str = os.path.join(directory, new_filename)

    print(f"\ntarget_pdf_file_path = {target_pdf_file_path}")  # Test
    print("\nFinished.\n")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"[-] {e}\n")
