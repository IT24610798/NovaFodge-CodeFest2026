import os
import time
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# Try these models in order - if the first is overloaded, fall back to the next
FALLBACK_MODELS = [
    "google/gemma-4-31b-it:free",
    "openrouter/free",
]


def call_llm(prompt: str, max_retries: int = 2) -> str:
    for model in FALLBACK_MODELS:
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                )
                print(f"(Answered by: {model})")
                return response.choices[0].message.content
            except RateLimitError:
                wait_time = (attempt + 1) * 5
                print(f"{model} rate limited, waiting {wait_time}s...")
                time.sleep(wait_time)
            except Exception as e:
                print(f"{model} failed with error: {e}")
                break  # try the next model instead of retrying this one

    raise Exception("All fallback models failed.")


if __name__ == "__main__":
    answer = call_llm("Say hello in one sentence.")
    print(answer)