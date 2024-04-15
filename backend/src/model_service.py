from typing import Any, Dict, Union

from ultralytics import YOLO


class Predicition:
    def __init__(self, class_label: str, confidence: float) -> None:
        self.class_label = class_label
        self.confidence = confidence

    def to_dict(self) -> Dict[str, Union[str, float]]:
        return {
            "class_label": self.class_label,
            "confidence": self.confidence,
        }

    def __repr__(self) -> str:
        return f"<Prediction: class_label={self.class_label}, confidence={self.confidence}>"


class ModelService:
    # Segmeneted model
    _prediction_model = YOLO("models/yolov8m-seg.pt")

    @classmethod
    def __init__(cls) -> None | Exception:
        if not cls._prediction_model:
            raise Exception("error: failed to load prediction model")

    @classmethod
    def _parse_predictions(cls, results: Any) -> list[Predicition] | Exception:
        try:
            parsed_predictions: list[Predicition] = []

            for result in results:
                for box in result.boxes:
                    class_label = result.names[box.cls[0].item()]
                    confidence = box.conf[0].item()

                    parsed_predictions.append(Predicition(class_label, confidence))

            return parsed_predictions
        except Exception as e:
            return e

    @classmethod
    def predict(cls, images: list[str]) -> list[Predicition] | Exception:
        try:
            predictions = cls._prediction_model.predict(images)
            return cls._parse_predictions(predictions)
        except Exception as e:
            return e


model_service = ModelService()
