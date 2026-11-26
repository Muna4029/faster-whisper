from faster_whisper.audio import decode_audio
from faster_whisper.transcribe import (
    AsyncBatchedInferencePipeline,
    BatchedInferencePipeline,
    WhisperModel,
)


# Lazily import utils functions to avoid importing optional dependencies (e.g. requests)
# during package import / test collection.
def available_models(*args, **kwargs):
    from faster_whisper.utils import available_models as _available_models

    return _available_models(*args, **kwargs)


def download_model(*args, **kwargs):
    from faster_whisper.utils import download_model as _download_model

    return _download_model(*args, **kwargs)


def format_timestamp(*args, **kwargs):
    from faster_whisper.utils import format_timestamp as _format_timestamp

    return _format_timestamp(*args, **kwargs)


from faster_whisper.version import __version__

__all__ = [
    "available_models",
    "decode_audio",
    "WhisperModel",
    "BatchedInferencePipeline",
    "AsyncBatchedInferencePipeline",
    "download_model",
    "format_timestamp",
    "__version__",
]
