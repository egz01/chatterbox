import sys
import chatterbox

def main():
  bot_name = "HelperBot"
  bot_description = "This is a conversation with an accomplished academic\n" + \
                    "bot that uses its immense knowledge to assist in research in any field."

  bot_example_exchange = "Human: Hello, how are you today?\nHelperBot: Great. How can I help?"

  helper_bot = chatterbox.ChatterBox(name=bot_name,
                                      description=bot_description,
                                      example_exchange=bot_example_exchange)

  if len(sys.argv) > 1:
    human_input = sys.argv[1]
    response = helper_bot.get_next_message(human_input)
    print(f"Human: {human_input}\n{bot_name}: {response}")
  else:
    while True:
        human_input = input("Human: ")
        response = helper_bot.get_next_message(human_input)
        print(f"{bot_name}: {response}")


if __name__ == "__main__":
  main()