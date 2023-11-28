import os
from datetime import datetime
from uuid import uuid4


class StorageManager:
    directory: str = "storage"

    @classmethod
    def __init__(cls) -> None:
        cls.make_directory(directory=StorageManager.directory, scratch=True)

    @classmethod
    def make_directory(cls, directory: str, scratch: bool = False) -> None:
        path: str = directory if scratch else StorageManager.directory + "/" + directory
        if not os.path.exists(path):
            os.makedirs(path)

    @classmethod
    def get_file_extension(cls, file_name: str) -> str:
        indx: int = file_name.rfind(".")
        return file_name[indx:] if indx != -1 else ""

    @classmethod
    def generate_file_id(cls) -> str:
        return str(datetime.now().strftime("%Y%m-%d%H-%M%S-") + str(uuid4()))

    @classmethod
    def get_file_path(cls, file_id: str, file_extension: str) -> str:
        return f"{StorageManager.directory}/{file_id}{file_extension}"

    @classmethod
    def get_folder_path(cls, file_id: str) -> str:
        return f"{StorageManager.directory}/{file_id}"

    @classmethod
    def validate_file_id(cls, file_id: str) -> bool:
        return os.path.exists(
            StorageManager._get_file_path(
                file_id, StorageManager._get_file_extension(file_id)
            )
        )


storage_manager = StorageManager()
