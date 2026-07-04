from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    WHISPER_MODEL = "base"

    SAMPLE_RATE = 16000

    VOICE_RATE = 180

    RECORD_DURATION = 3