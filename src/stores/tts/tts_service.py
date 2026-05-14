import edge_tts
import os
from helpers.config import settings

class TTsService:
    def __init__(self):
        self.voices_ar = settings.TTS_VOICES_AR.split(",")
        self.voices_en = settings.TTS_VOICES_EN.split(",")
        self.output_path = settings.AUDIO_OUTPUT_PATH

    def _is_arabic(self, text: str):
        return any('\u0600' <= c <= '\u06FF' for c in text)

    async def tts(self, text: str) -> str:
        voices = self.voices_ar if self._is_arabic(text) else self.voices_en

        for v in voices:
            try:
                communicate = edge_tts.Communicate(text, v)
                await communicate.save(self.output_path)
                return self.output_path

            except Exception as e:
                print(f" Failed with {v}: {e}")

        raise RuntimeError("All TTS voices failed")