from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from loguru import logger
from app.whisper_service import transcribe_audio
import tempfile
import asyncio
import os

websocket_router = APIRouter()
connections = []


@websocket_router.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    """
    Websocket for real-time transcription
    """

    try:
        while True:

            audio_bytes = await websocket.accept()
            connections.append(websocket)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_bytes)
                temp_audio_path = temp_audio.name

            transcription = transcribe_audio(temp_audio_path)
            await websocket.send_json({"transcription": transcription})

            os.remove(temp_audio_path)
    except WebSocketDisconnect:
        connections.remove(websocket)
