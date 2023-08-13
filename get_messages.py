import sqlite3
import subprocess
import datetime

def get_recent_imessage_texts(time=None, sender=None):
  """Fetches the most recent iMessage texts from the chat.db database file.

  Returns:
    A list of dictionaries, where each dictionary contains the following information:
      * sender: The sender's phone number or email address.
      * message: The message text.
      * date: The message date and time.
      * service: The message service (iMessage or SMS).
  """
  conn = sqlite3.connect("chat.db")
  cur = conn.cursor()
  first_query = """SELECT * FROM (
                SELECT
                m.rowid,
                coalesce(m.cache_roomnames, h.id) ThreadId,
                m.is_from_me IsFromMe,
                case when m.is_from_me = 1 then m.account
                else h.id end as FromPhoneNumber,
                case when m.is_from_me = 0 then m.account
                else coalesce(h2.id, h.id) end as ToPhoneNumber,
                datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as TextDate,
                m.service Service,
                m.text MessageText

                FROM
                message as m
                left join handle as h on m.handle_id = h.rowid
                left join chat as c on m.cache_roomnames = c.room_name /* note: chat.room_name is not unique, this may cause one-to-many join */
                left join chat_handle_join as ch on c.rowid = ch.chat_id
                left join handle as h2 on ch.handle_id = h2.rowid

                WHERE
                -- try to eliminate duplicates due to non-unique message.cache_roomnames/chat.room_name
                (h2.service is null or m.service = h2.service)
                ORDER BY m.date ASC
              ) 
              WHERE Service = 'iMessage' 
              """ 
  first_fragment = ("AND (FromPhoneNumber = '{}' OR ToPhoneNumber = '{}')\n".format(sender, sender) if sender else "")
  second_fragment = ("AND TextDate > '{}'".format(time) if time else "")
  # second_query = """
  #             LIMIT 40
  #             """
  full_query = first_query + first_fragment + second_fragment
  cur.execute(full_query)
  results = cur.fetchall()
  return [convert(result) for result in results]

def convert(record):
  return {
    "id": record[0],
    "from_me": record[2] == 1,
    "sender": record[3],
    "recipient": record[4],
    "time_sent": record[5],
    "text": record[7]
  }