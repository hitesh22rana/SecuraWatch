import subprocess


class VideoService:
    @classmethod
    def __init__(cls):
        pass

    @classmethod
    async def video_to_image(
        cls,
        input_path: str,
        fps: int,
        scale_x: int,
        scale_y: int,
        output_folder: str,
        output_format: str,
    ) -> None | subprocess.CalledProcessError:
        ffmpeg_command = [
            "ffmpeg",
            "-i",
            input_path,
            "-vf",
            f"fps={fps},scale={scale_x}:{scale_y}",
            f"{output_folder}/%d.{output_format}",
        ]

        try:
            subprocess.run(
                ffmpeg_command,
                check=True,
                stderr=subprocess.DEVNULL,
            )

        except subprocess.CalledProcessError as e:
            raise e


video_service = VideoService()
