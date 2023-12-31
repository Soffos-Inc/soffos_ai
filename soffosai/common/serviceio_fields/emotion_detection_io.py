from .service_io import ServiceIO
from ..constants import ServiceString


class EmotionDetectionIO(ServiceIO):
    service = ServiceString.EMOTION_DETECTION
    required_input_fields = ["text"]
    optional_input_fields = ["sentence_split", "sentence_overlap", "emotion_choices"]
    input_structure = {
        "sentence_split": int,
        "sentence_overlap": bool,
        "text": str,
        "emotion_choices": list
    }
    output_structure = {
        "spans": [
            {
                "detected_emotions": list,
                "text": str,
                "span_start": int,
                "span_end": int
            },
        ]
    }
