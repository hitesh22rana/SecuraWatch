import os
import shutil
from datetime import datetime
from uuid import uuid4


class StorageService:
    directory: str = "storage"

    @classmethod
    def __init__(cls) -> None:
        cls.make_directory(directory=StorageService.directory, scratch=True)

    @classmethod
    def make_directory(cls, directory: str, scratch: bool = False) -> None:
        path: str = directory if scratch else StorageService.directory + "/" + directory
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
        return f"{StorageService.directory}/{file_id}{file_extension}"

    @classmethod
    def get_folder_path(cls, file_id: str) -> str:
        return f"{StorageService.directory}/{file_id}"

    @classmethod
    def get_files(cls, path: str, type: str) -> list[str]:
        files: list[str] = []
        for file in os.listdir(path):
            if file.endswith(type):
                files.append(f"{path}/{file}")

        return files

    @classmethod
    def validate_file_id(cls, file_id: str) -> bool:
        return os.path.exists(
            StorageService.get_file_path(
                file_id, StorageService.get_file_extension(file_id)
            )
        )

    @classmethod
    def delete_directory(cls, directory: str) -> None:
        path: str = StorageService.directory + "/" + directory
        if not os.path.exists(path):
            return None

        shutil.rmtree(path)


storage_service = StorageService()
