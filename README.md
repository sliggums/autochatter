# autochatter
Chatbot that sends messages in iMessage.

## How it works
Assumes you are running this script on a Mac and an account that has iMessage capabilities.

First, need to store your ChatGPT API key either in the `chatgpt.py` file or store is in your local environment variable (modifiable in your `~/.bash_profile` folder in Macs).

Then, need to update the `message.sh` file in several places:
- The `chat.db` file path.
- The phone number of the person whose message you want to see in L5.
- The contact name of the person above person in L7.
  
Future functionalities will allow for this to be a more streamlined process, but for now will have this hacky implementation.

Then, run this file with 
```
./message.sh
```

You can choose to run it as a cronjob as well.
