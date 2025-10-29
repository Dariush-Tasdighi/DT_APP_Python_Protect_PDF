# **************************************************
# Simple Installation:
# - Download and Install Python:
#   - https://www.python.org/downloads
#
# - In Windows Command Prompt [OR] Windows PowerShell:
# > python -m pip install -U pip
# > python -m pip install -U rich
# > python -m pip install -U pypdf
# > python -m pip install -U cryptography
#
# - For Testing:
# > python .\dt_protect_pdf.py .\test\test.pdf
#
# - For Running:
# > python dt_protect_pdf c:\googooli\magooli.pdf
# **************************************************

import os
import uuid
import pathlib
import argparse
from rich import print
from typing import Tuple
from datetime import datetime

from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf.constants import UserAccessPermissions

VERSION: str = "1.5"
USER_PASSWORD: str = ""
ALGORITHM: str = "AES-256-R5"
OWNER_PASSWORD: str = str(uuid.uuid4())


def split_file_path(file_path: str) -> Tuple[str, str, str]:
    """Split file path"""

    directory, filename = os.path.split(p=file_path)
    name, extension = os.path.splitext(p=filename)

    return directory, name, extension


def validate_pdf_file_path(file_path: str) -> None:
    """Validate PDF file path"""

    if not os.path.exists(path=file_path):
        print(f"[-] The file '{file_path}' does not exist!\n")
        exit()

    if not os.path.isfile(path=file_path):
        print(f"[-] The file '{file_path}' does not exist!\n")
        exit()

    source_file_extension: str = pathlib.Path(file_path).suffix.lower()

    if source_file_extension != ".pdf":
        print(f"[-] The file '{file_path}' is not 'pdf' file!\n")
        exit()


def create_target_pdf_file_path(source_pdf_file_path: str) -> str:
    """Create target PDF file path"""

    directory, name, extension = split_file_path(
        file_path=source_pdf_file_path,
    )

    target_filename: str = f"{name}_protected{extension}"
    result: str = os.path.join(directory, target_filename)

    return result


def protect_pdf_file(file_path: str):
    """Protect PDF file"""

    validate_pdf_file_path(
        file_path=file_path,
    )

    target_pdf_file_path: str = create_target_pdf_file_path(
        source_pdf_file_path=file_path,
    )

    reader = PdfReader(stream=file_path)
    writer = PdfWriter(fileobj=reader)

    utc_time = "+03'30'"
    time = datetime.now().strftime(
        format=f"D\072%Y%m%d%H%M%S{utc_time}",
    )

    infos = {
        "/ModDate": time,
        "/CreationDate": time,
        "/Title": "Dariush Tasdighi",
        "/Author": "Dariush Tasdighi",
        "/Creator": "Dariush Tasdighi",
        "/Subject": "Dariush Tasdighi",
        "/Keywords": "Dariush Tasdighi",
        "/Producer": f"DT Protect PDF - Version: {VERSION}",
        "/CustomField_1": "Dariush Tasdighi",
        "/CustomField_2": "Dariush Tasdighi",
    }

    writer.add_metadata(infos=infos)

    permissions_flag: UserAccessPermissions = 0  # type: ignore

    writer.encrypt(
        use_128bit=True,
        algorithm=ALGORITHM,
        user_password=USER_PASSWORD,
        owner_password=OWNER_PASSWORD,
        permissions_flag=permissions_flag,
    )

    with open(file=target_pdf_file_path, mode="wb") as file:
        writer.write(stream=file)


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    description: str = "You must specify the 'PDF' file path!"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file_path", help="'PDF' file path")
    args = parser.parse_args()
    source_pdf_file_path: str = args.file_path

    protect_pdf_file(file_path=source_pdf_file_path)

    print("Finished.\n")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"[-] {e}\n")
