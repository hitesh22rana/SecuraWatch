from typing import Any

from ultralytics import YOLO


class ModelService:
    # Segmeneted model
    _prediction_model = YOLO("models/yolov8s-seg.pt")

    @classmethod
    def __init__(cls) -> None | Exception:
        if not cls._prediction_model:
            raise Exception("error: failed to load prediction model")

    @classmethod
    def predict(cls, images: list[str]) -> list[Any] | Exception:
        try:
            results = cls._prediction_model.predict(images)
            return results
        except Exception as e:
            return e


model_service = ModelService()
