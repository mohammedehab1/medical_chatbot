from groq import Groq
from helpers.config import settings

class WhisperService:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.WHISPER_MODEL  

    def transcribe(self, audio_file) :

        if isinstance(audio_file, str):
            file = open(audio_file, "rb")
            close_file = True
        else:
            file = audio_file
            close_file = False

        try:
            response = self.client.audio.transcriptions.create(
                file=file,
                model=self.model
            )

            return response.text

        except Exception as e:
            raise RuntimeError(f"Transcription failed: {e}")

        finally:
            if close_file:
                file.close()