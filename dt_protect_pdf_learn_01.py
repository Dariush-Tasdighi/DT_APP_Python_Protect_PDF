import os
import uuid
import pathlib
from rich import print
from datetime import datetime

from pypdf import PdfReader
from pypdf import PdfWriter
from pypdf.constants import UserAccessPermissions

VERSION: str = "1.1"
USER_PASSWORD: str = ""
OWNER_PASSWORD: str = str(uuid.uuid4())

# The algorithm can be one of RC4-40, RC4-128, AES-128,
# AES-256-R5, AES-256. We recommend using AES-256-R5.
# > python -m pip install -U cryptography
ALGORITHM: str = "AES-256-R5"


def main() -> None:
    """Main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # print(OWNER_PASSWORD)  # Test

    # source_pdf_file_path: str = "./data/pg36.pdf"
    # target_pdf_file_path: str = "./data/pg36_protected.pdf"

    source_pdf_file_path: str = "./test/test.pdf"
    target_pdf_file_path: str = "./test/test_protected.pdf"

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
