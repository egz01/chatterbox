# chatterbox
This packge is a GPT-3 based chatbot abstraction that allows the user to easily configure an instance to behave in vraious ways.

For example, here is a ChatterBox instance configured to be a supporting friend (friend_example.py):

<img width="611" alt="image" src="https://user-images.githubusercontent.com/12452166/217963426-85c8d630-512e-46e8-8326-f9d6f0fbccef.png">

The conversation that this configuration yields is clearly very friendly and heartwarming:
<img width="779" alt="image" src="https://user-images.githubusercontent.com/12452166/217961005-ecfffe58-a304-4eee-b795-df766c86245d.png">

And here is an example of a Chatterbox configured to be an annoying little brat (brat_example.py):
<img width="784" alt="image" src="https://user-images.githubusercontent.com/12452166/217962356-22d35bf2-775d-4c5b-a6a9-c75b52627e62.png">

And lastly, here's an example of usage of the package to implement a sort of research assistant:
<img width="790" alt="image" src="https://user-images.githubusercontent.com/12452166/218153409-97d62644-962a-4952-a162-848e6d9a4b5b.png">

Usage of chatterbox requires an OpenAI API Key, [which can be obtained here](https://platform.openai.com/account/api-keys).
Note that usage of this API isn't free, however there's usually more than enough free credit for new users :)

## Installation
* using make (intended to work on linux, and only ever tested on linux):
    1. clone this repository
    2. place your API key in a .env: echo "export OPENAI_API_KEY=sk-..." > .env
    3. run "source .env" to add this variable to your environment
    4. run make install 

## Othe rusage
I haven't gotten around to document the library yet, however sample usage can be found in the examples module.
