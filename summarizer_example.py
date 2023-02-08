import chatterbox
import os

def get_key():
  if (not os.path.exists(".key")):
    raise Exception(".key file not found")
  
  with open(".key", "r") as f:
    key = f.read()
  return key

chatterbox.initialize_api(get_key())

bot_name = "SummarizerBot"
bot_description = "A bot that summarizes your input."
bot_example_exchange = "Human: Hello, how are you?\SummarizerBot: I don't have feelings, I only summarize input."

friend_bot = chatterbox.ChatterBox(name=bot_name,
                                    description=bot_description,
                                    example_exchange=bot_example_exchange)

while True:
    human_input = input("Human: ")
    response = friend_bot.get_next_message(human_input)
    print(f"{bot_name}: {response}")

