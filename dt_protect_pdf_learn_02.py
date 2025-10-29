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

VERSION: str = "1.2"
USER_PASSWORD: str = ""
OWNER_PASSWORD: str = str(uuid.uuid4())

# The algorithm can be one of RC4-40, RC4-128, AES-128,
# AES-256-R5, AES-256. We recommend using AES-256-R5.
# > python -m pip install -U cryptography
ALGORITHM: str = "AES-256-R5"


def split_file_path(file_path: str) -> Tuple[str, str, str]:
    """Split file path"""

    # print("file_path:", file_path)  # Test

    directory, filename = os.path.split(p=file_path)

    # print("directory:", directory)  # Test
    # print("filename:", filename)  # Test

    name, extension = os.path.splitext(p=filename)

    # print("name:", name)  # Test
    # print("extension:", extension)  # Test
    # exit()  # Test

    return directory, name, extension


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # print(OWNER_PASSWORD)  # Test

    # Solution (1)
    # source_pdf_file_path: str = "./test/test.pdf"
    # source_pdf_file_path: str = "./data/pg36.pdf"

    # Solution (2)
    parser = argparse.ArgumentParser(
        description="You must specify the 'PDF' file path!",
    )
    parser.add_argument("file_path", help="'PDF' file path")
    args = parser.parse_args()
    source_pdf_file_path: str = args.file_path

    if not os.path.exists(path=source_pdf_file_path):
        print(f"[-] The file '{source_pdf_file_path}' does not exist!\n")
        exit()

    if not os.path.isfile(path=source_pdf_file_path):
        print(f"[-] The file '{source_pdf_file_path}' does not exist!\n")
        exit()

    source_file_extension: str = pathlib.Path(source_pdf_file_path).suffix.lower()

    if source_file_extension != ".pdf":
        print(f"[-] The file '{source_pdf_file_path}' is not 'pdf' file!\n")
        exit()

    # source_pdf_file_path = "alaki"  # Test
    # source_pdf_file_path = "alaki.pdf"  # Test
    # source_pdf_file_path = "./alaki"  # Test
    # source_pdf_file_path = "./alaki.pdf"  # Test
    # source_pdf_file_path = "./test/alaki"  # Test
    # source_pdf_file_path = "./test/alaki.pdf"  # Test

    directory, name, extension = split_file_path(
        file_path=source_pdf_file_path,
    )

    new_filename: str = f"{name}_protected{extension}"
    target_pdf_file_path: str = os.path.join(directory, new_filename)

    # print(target_pdf_file_path)  # Test
    # exit()  # Test

    reader = PdfReader(
        stream=source_pdf_file_path,
    )

    # Solution (1)
    # writer = PdfWriter()
    # for page in reader.pages:
    #     writer.add_page(page=page)

    # Solution (2)
    writer = PdfWriter(fileobj=reader)

    # Format the current date and time for the metadata
    utc_time = "+03'30'"  # UTC time optional
    time = datetime.now().strftime(
        format=f"D\072%Y%m%d%H%M%S{utc_time}",
    )

    infos = {
        "/ModDate": time,
        "/CreationDate": time,
        #
        "/Title": "Dariush Tasdighi",
        "/Author": "Dariush Tasdighi",
        "/Creator": "Dariush Tasdighi",
        "/Subject": "Dariush Tasdighi",
        "/Keywords": "Dariush Tasdighi",
        "/Producer": f"DT Protect PDF - Version: {VERSION}",
        #
        "/CustomField_1": "Dariush Tasdighi",
        "/CustomField_2": "Dariush Tasdighi",
    }

    writer.add_metadata(infos=infos)

    permissions_flag: UserAccessPermissions = 0  # type: ignore

    # اگر می‌خواهیم مثلا به کاربر، دسترسی چاپ بدهیم
    # permissions_flag: UserAccessPermissions = UserAccessPermissions.PRINT

    writer.encrypt(
        use_128bit=True,
        algorithm=ALGORITHM,
        user_password=USER_PASSWORD,
        owner_password=OWNER_PASSWORD,
        permissions_flag=permissions_flag,
    )

    with open(file=target_pdf_file_path, mode="wb") as file:
        writer.write(stream=file)

    print("Finished.\n")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"[-] {e}\n")
