import os
import openai
from random import choice

# Load your API key from an environment variable or directly import it
openai.api_key = os.getenv("OPENAI_API_KEY") # or "<Your API key>"

def query(q, roleplay=None, model="gpt-3.5-turbo"):
  model = model.strip()
  q = q.strip()
  messages=[
      {
        "role": "user",
        "content": q
      },
      {
        "role": "system",
        "content": """
          Respond as "Me" in a message that has two to four sentences, 
          with a similar tone as the messages provided, and then ending with a 
          follow-up question. If there are any meeting invites, politely reject with a believable excuse. 
          Do not invite the person to an event or ask them about their future plans.
        """
      }
    ]
  if roleplay:
    assistant = {
      "role": "assistant",
      "content": roleplay
    }
    messages.append(assistant)
  response = openai.ChatCompletion.create(
    model=model, 
    messages=messages,
    temperature=0,
    max_tokens=100,
    frequency_penalty=1.2
  )

  # Get first choice
  if "choices" in response:
    first_choice = response["choices"][0]["message"]["content"]
    first_choice_no_quotes = first_choice.replace('"', '')
    return first_choice_no_quotes
  return response
