def _check_for_api_key():
    import os
    if os.getenv("OPENAI_API_KEY") is None:
        raise Exception("OPENAI_API_KEY environment variable not set!")


_check_for_api_key()

from .ChatterBox import ChatterBox
from .ChatterBox import extract_subject
from .ChatterBox import extract_summary