import sys, os
sys.path.append(os.path.dirname(__file__))

from src.silero import (
    silero_stt,
    silero_tts,
    silero_te,
)
dependencies = ["torch"]


__all__ = [
    "silero_stt",
    "silero_tts",
    "silero_te",
]

