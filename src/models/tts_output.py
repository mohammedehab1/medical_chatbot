from pydantic import BaseModel

class TTSOutput(BaseModel):
    audio_path: str