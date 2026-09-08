"""
Retry wrapper for Voyage AI embedding calls.

WHY THIS EXISTS:
Query-time embeddings (one per user question/reflect-loop iteration)
can't be batched the way bulk document ingestion can — they happen
one at a time, as the loop runs. If a rate limit is hit mid-demo, this
retries with exponential backoff instead of crashing the whole search.
"""

import time
import functools
from typing import Callable, Any


def retry_on_rate_limit(max_retries: int = 5, base_delay: float = 2.0):
    """
    Decorator that retries a function call if it raises a rate-limit
    error, waiting longer between each attempt (exponential backoff).

    WHY EXPONENTIAL (not fixed) delay: if you retry instantly, you'll
    likely hit the same limit again immediately. Waiting 2s, then 4s,
    then 8s... gives the per-minute window time to actually reset.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    # Voyage/most APIs signal rate limits via a 429 status
                    # or an error message containing "rate limit"
                    error_text = str(e).lower()
                    if "rate limit" in error_text or "429" in error_text:
                        last_error = e
                        delay = base_delay * (2 ** attempt)
                        print(f"Rate limit hit, retrying in {delay:.1f}s (attempt {attempt + 1}/{max_retries})...")
                        time.sleep(delay)
                    else:
                        raise  # not a rate-limit error, don't swallow it
            raise last_error  # exhausted retries, surface the real error

        return wrapper
    return decorator


# Example usage in your semantic_search.py:
#
# from src.utils.retry import retry_on_rate_limit
#
# @retry_on_rate_limit(max_retries=5, base_delay=2.0)
# def embed_query(text: str):
#     return voyage_client.embed([text], model="voyage-4-lite").embeddings[0]