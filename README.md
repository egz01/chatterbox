# chatterbox
This packge is a GPT-3 based chatbot abstraction that allows the user to easily configure an instance to behave in vraious ways.

Usage of chatterbox requires an OpenAI API Key, [which can be obtained here](https://platform.openai.com/account/api-keys).
Note that usage of this API isn't free, however there's usually more than enough free credit for new users :)

Below is a sample bot and some exchanges with it:

![image](https://user-images.githubusercontent.com/12452166/218300625-28fd88ca-e02a-41e7-a74e-4e26d0335e13.png)

## Installation
* using make (intended to work on linux, and only ever tested on linux):
    1. clone this repository
    2. place your API key in a .env: echo "export OPENAI_API_KEY=sk-..." > .env
    3. run "source .env" to add this variable to your environment
    4. run make install
    
The result of a successful installation should look something like this:

<img width="505" alt="image" src="https://user-images.githubusercontent.com/12452166/218300543-b8ed8403-2d07-4472-acb9-bc0e13a322af.png">


## Other usage
I haven't gotten around to document the library yet, however sample usage can be found in the examples module.
