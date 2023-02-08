import openai

_MAX_MAX_TOKENS = 4096
_LETTERS_PER_TOKEN = 4
_AVERAGE_WORD_LENGTH = 6
_TOKENS_PER_WORD = _LETTERS_PER_TOKEN * _AVERAGE_WORD_LENGTH

CHAT_PREFIX = """This is a conversation with an AI assistant """ + \
                """proficient in science and engineering.""" + \
                """The assistant is very knowledgeable, but when""" + \
                """too uncertain of its response it asks for more information.\n"""
CLEAN_CONVERSATION_HISTORY = CONVERSATION_HISTORY = """Human: Hello, how are you?""" + \
                                                    """AI assistant: Hi, I am fine. How can I help you today?"""
CHAT_SUFFIX = "AI assistant: "

def initialize_api(key: str):
    openai.api_key = key


def _send_api_request(prompt, max_tokens=1024, 
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


def _calc_max_tokens(desired_length_in_words: int, prompt: str):
    num_tokens_from_words = int(desired_length_in_words * _TOKENS_PER_WORD) + 1
    max_num_tokens_after_prompt = _MAX_MAX_TOKENS - len(prompt)
    return min(num_tokens_from_words, max_num_tokens_after_prompt)


SUMMARY_PREFIX = SUBJECT_PREFIX = "This is the original paragraph:\n"
SUBJECT_SUFFIX = "The above paragraph's subject is: "
SUMMARY_SUFFIX = "and its summary is:"

def extract_subject(text, desired_length_in_words=10):
    subject_prompt = f"{SUBJECT_PREFIX}{text}\n{SUBJECT_SUFFIX}"

    max_tokens = _calc_max_tokens(desired_length_in_words, subject_prompt)

    subject_response = _send_api_request(subject_prompt, max_tokens=max_tokens, 
                                            stop=['.', '.\n'], temperature=0.3, presence_penalty=2)
    subject = subject_response['choices'][0]['text'].strip()
    return subject


def extract_summary(text, desired_length_in_words=50):
    subject = extract_subject(text, desired_length_in_words=10)
    summary_prompt = f"{SUMMARY_PREFIX}{text}\n{SUBJECT_SUFFIX}{subject}, {SUMMARY_SUFFIX}\n"

    max_tokens = _calc_max_tokens(desired_length_in_words, summary_prompt)

    summary_response = _send_api_request(summary_prompt, max_tokens=max_tokens, stop=['.\n'], temperature=0.3)
    summary = summary_response['choices'][0]['text'].strip()
    return summary


class ChatterBox:
    def __init__(self, name: str, description: str, example_exchange: str):
        self.__initial_history = self.__conversation_history = example_exchange
        self.__prefix = description
        self.__name = name
    
    def clear_conversation(self):
        self.__conversation_history = self.__initial_history

    def get_next_message(self, text, desired_length_in_words=350):
        chat_prompt = f"{self.__prefix}{self.__conversation_history}\nHuman: {text}\n{self.__name}:"

        max_tokens = _calc_max_tokens(desired_length_in_words, chat_prompt)

        chat_response = _send_api_request(chat_prompt, max_tokens=max_tokens, stop=['.\n\n'], temperature=0.9)
        message = chat_response['choices'][0]['text'].strip()

        conversation_so_far = f"{self.__conversation_history}\nHuman: {text}\n{self.__name}: {message}\n"
        converstion_summary = extract_summary(conversation_so_far, desired_length_in_words=0.5*len(conversation_so_far.split()))
        converstion_summary = converstion_summary.strip()

        self.__conversation_history = f"previously in the conversation: {converstion_summary}\n\n"

        return message

