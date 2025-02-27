from fastapi import APIRouter, UploadFile, File, HTTPException
from app.whisper_service import transcribe_audio
import shutil
import uuid
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/")
def health_check():
    return {"health_check": "server is running"}


@router.post("/transcribe")
async def transcribe_audio_file(file: UploadFile = File(...)):
    """
    Recieved an audio file to transcribe and returns it afterwards
    """
    try:
        file_ext = file.filename.split(".")[-1]
        file_path = f"{UPLOAD_DIR}/{uuid.uuid4()}.{file_ext}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcription = transcribe_audio(file_path)

        os.remove(file_path)

        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
