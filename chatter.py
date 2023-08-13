from get_messages import get_recent_imessage_texts
from chatgpt import query
import datetime
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--name", type=str, help="The name of the person.")
  args = parser.parse_args()
  if args.name:
    now = datetime.datetime.now()
    time = (now - datetime.timedelta(hours=96)).strftime("%Y-%m-%d")
    messages = get_recent_imessage_texts(time, args.name)
    if messages:
      convo = ""
      curr = []
      curr_me_status = None
      for message in messages:
        if not message["text"]:
          curr_me_status = message["from_me"]
          continue
        if message["from_me"] != curr_me_status and curr:
          start = "Me: " if not message["from_me"] else "Friend: " 
          convo += (start + ". ".join(curr) + "\n")
          curr = []
        curr_me_status = message["from_me"]
        curr.append(message["text"])
      if curr_me_status == False:
        if curr:
          start = "Me: " if message["from_me"] else "Friend: " 
          convo += (start + ". ".join(curr) + "\n")
          convo += "Me: "
        output = query(convo).replace("Me: ", "")
        print(output)
