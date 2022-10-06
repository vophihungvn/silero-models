import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
print(sys.path)

from silero import (
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

