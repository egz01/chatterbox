import chatterbox

def main():
  bot_name = "FriendBot"
  bot_description = "A friendly bot that can talk about anything, and uses a lot of emoticons"
  bot_example_exchange = "Human: Hello, how are you?\nFriendBot: Great! Happy to hear from you today :)"
  
  friend_bot = chatterbox.ChatterBox(name=bot_name,
                                      description=bot_description,
                                      example_exchange=bot_example_exchange)
  
  while True:
      human_input = input("Human: ")
      response = friend_bot.get_next_message(human_input)
      print(f"{bot_name}: {response}")
  
  if __name__ == "__main__":
    main()