import openai
import os

# constants
_MAX_MAX_TOKENS = 4096
_LETTERS_PER_TOKEN = 4
_AVERAGE_WORD_LENGTH = 6
_TOKENS_PER_WORD = _LETTERS_PER_TOKEN * _AVERAGE_WORD_LENGTH

def initialize_api():
    openai.api_key = os.getenv("OPENAI_API_KEY")

def calc_max_tokens(desired_length_in_words: int, prompt: str):
    num_tokens_from_words = int(desired_length_in_words * _TOKENS_PER_WORD) + 1
    max_num_tokens_after_prompt = _MAX_MAX_TOKENS - len(prompt)
    return min(num_tokens_from_words, max_num_tokens_after_prompt)

def send_api_request(prompt, max_tokens=1024, 
                        temperature=0.6, stop='.\n', 
                        retries=0, tokens_step=100, 
                        model='text-davinci-003', choices=1,
                        presence_penalty=0,
                        frequency_penalty=0):
    
    if openai.api_key is None:
        raise ValueError("API key not set! call initialize_api(key) first.")
    
    if type(stop) is not list:
        stop = [stop]

    while True:
        try:
            response = openai.Completion.create(model=model,
                                                prompt=prompt,
                                                temperature=temperature,
                                                max_tokens=max_tokens,
                                                stop=stop,
                                                n=choices,
                                                presence_penalty=presence_penalty,
                                                frequency_penalty=frequency_penalty)
            break
        except openai.error.RateLimitError as e:
            max_tokens += tokens_step
            if max_tokens >= _MAX_MAX_TOKENS:
                raise e
    
    return response
