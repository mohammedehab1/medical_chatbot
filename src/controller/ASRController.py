import os
import uuid
from stores.whisper import WhisperService
from .AudioPreprocessor import AudioPreprocessor

class ASRController:

    def __init__(self):
        self.whisper = WhisperService()

    def transcribe(self, audio_path: str) -> str:

        temp_file = f"temp_{uuid.uuid4().hex}.wav"

        try:

            processed_file = AudioPreprocessor.process(
                audio_path=audio_path,
                output_path=temp_file
            )

            text = self.whisper.transcribe(processed_file)
            return text

        finally:

            if os.path.exists(temp_file):
                os.remove(temp_file)