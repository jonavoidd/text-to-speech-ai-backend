import whisper
import tempfile
import os


def transcribe_audio(file_path: str):
    """
    Transcribes an in-meory audio file using OpenAI's whisper model
    """

    model = whisper.load_model("tiny")

    try:
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"
