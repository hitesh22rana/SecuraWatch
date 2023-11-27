import os
from datetime import datetime
from uuid import uuid4


class Storage:
    directory: str = "storage"

    @classmethod
    def __init__(self) -> None:
        if not os.path.exists(Storage.directory):
            os.makedirs(Storage.directory)

    @classmethod
    def get_file_extension(cls, file_name: str) -> str:
        indx: int = file_name.rfind(".")
        return file_name[indx:] if indx != -1 else ""

    @classmethod
    def generate_file_id(self) -> str:
        return str(datetime.now().strftime("%Y%m-%d%H-%M%S-") + str(uuid4()))

    @classmethod
    def get_file_path(self, file_id: str, file_extension: str) -> str:
        return f"{Storage.directory}/{file_id}.{file_extension}"

    @classmethod
    def validate_file_id(self, file_id: str) -> bool:
        return os.path.exists(
            Storage._get_file_path(file_id, Storage._get_file_extension(file_id))
        )


storage = Storage()
