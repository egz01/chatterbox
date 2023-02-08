import chatterbox
import os

def get_key():
  if (not os.path.exists(".key")):
    raise Exception(".key file not found")
  
  with open(".key", "r") as f:
    key = f.read()
  return key

chatterbox.initialize_api(get_key())

bot_name = "BratBot"
bot_description = "A bratty little bot that likes to talk about itself." +\
                  "It usually replies very rudely, and doesn't care about what you say."

bot_example_exchange = "Human: Hello, how are you?\BratBot: wouldn't you like to know?"

brat_bot = chatterbox.ChatterBox(name=bot_name,
                                    description=bot_description,
                                    example_exchange=bot_example_exchange)

while True:
    human_input = input("Human: ")
    response = brat_bot.get_next_message(human_input)
    print(f"{bot_name}: {response}")

