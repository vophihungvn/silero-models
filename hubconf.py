import sys
sys.path.append("src/silero")
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

