from fastapi import FastAPI
from routes.chat import chat_router
from routes.check import check_router

app = FastAPI()

app.include_router(check_router)
app.include_router(chat_router)