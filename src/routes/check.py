from fastapi import APIRouter

check_router = APIRouter(
    prefix="/check",
    tags=["check"]
)

@check_router.get("/")
def check():
    return {
        "status": "ok",
        "service": "medical_chatbot"
    }