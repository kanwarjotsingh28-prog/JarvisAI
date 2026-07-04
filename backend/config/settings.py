from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    Settings.RECORD_DURATION
    Settings.SAMPLE_RATE
    Settings.VOICE_RATE