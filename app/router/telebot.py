"""router for managing telegram bot interactions."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
async def get_status():
    return {"status": "ok"}


@router.post("/send-message")
async def send_message(message: str):
    # Logic to send message via Telegram Bot API
    return {"status": "message sent", "message": message}
