#!/bin/bash
cp /Users/stevewang/Library/Messages/chat.db . # Replace this path with wherever your `chat.db` file is located.
sleep $((RANDOM % 1800))

output=$(/opt/homebrew/bin/python3 ~/Documents/imessage/chatter.py --name=+15555555555) # Replace the number here with the contact.
echo "$output"
osascript ~/Documents/imessage/send.applescript "Rrr" "$output" # Replace Rrr with name of contact in your Contacts app. 
