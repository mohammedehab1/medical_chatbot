import asyncio
import os
from .ASRController import ASRController
from .LLMController import LLMController
from .TTSController import TTSController
from utils.AudioRecorder import AudioRecorder

class ChatController:

    def __init__(self):
        self.asr = ASRController()
        self.llm = LLMController()
        self.tts = TTSController()
        self.recorder = AudioRecorder()

    def start_recording(self):
        self.recorder.start()

    def stop_recording(self):
        return self.recorder.stop()

    def handle_text(self, text: str) -> str:
        return self.llm.chat(text)

    async def handle_text_input(self, text: str) -> str:
        return await asyncio.to_thread(self.handle_text, text)

    async def handle_voice(self, audio_path: str):

        if not audio_path or not os.path.exists(audio_path):
            return "Audio file not found"

        try:

            text = await asyncio.to_thread(
                self.asr.transcribe,
                audio_path
            )

            response_text = await asyncio.to_thread(
                self.llm.chat,
                text
            )

            audio_output_path = await self.tts.synthesize(response_text)

            return audio_output_path

        except Exception as e:
            return f"Error in voice pipeline: {str(e)}"

    async def handle_audio_file(self, audio_path: str):
        return await self.handle_voice(audio_path)