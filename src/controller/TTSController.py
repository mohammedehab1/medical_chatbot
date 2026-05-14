from stores.tts import TTsService

class TTSController:
    def __init__(self):
        self.tts_service = TTsService()

    async def synthesize(self, text: str) -> str:
        audio_path = await self.tts_service.tts(text)
        return audio_path