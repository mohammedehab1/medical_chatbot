from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from controller.ChatController import ChatController
import os

chat_controller = ChatController()

chat_router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

class TextRequest(BaseModel):
    text: str

@chat_router.post("/text")
async def chat_text(data: TextRequest):

    response = await chat_controller.handle_text_input(
        data.text
    )

    return response

@chat_router.post("/voice")
async def chat_voice(file: UploadFile = File(...)):

    input_audio_path = f"temp_{file.filename}"

    with open(input_audio_path, "wb") as f:
        f.write(await file.read())

    try:

        output_audio_path = await chat_controller.handle_audio_file(
            input_audio_path
        )

        if not os.path.exists(output_audio_path):
            return {
                "error": "Output audio file not found"
            }

        return FileResponse(
            path=output_audio_path,
            media_type="audio/mpeg",
            filename="response.mp3"
        )

    except Exception as e:

        return {
            "error": str(e)
        }

    finally:

        if os.path.exists(input_audio_path):
            os.remove(input_audio_path)