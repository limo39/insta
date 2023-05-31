from time import sleep
from instapy import InstaPy
from instapy.util import smart_run

# Function to send auto-reply message
def send_auto_reply(message, reply_text):
    reply = f"Auto-Reply: {reply_text}"
    message.reply(reply)
    print(f"Auto-reply sent to {message.user.username}")

session = InstaPy(username='your_username', password='your_password')
with smart_run(session):
    session.get_unread_inbox()

    for message in session.inbox:

        msg_text = message.text.lower()

        if 'hello' in msg_text:
            send_auto_reply(message, 'Hi! How can I assist you?')
        elif 'help' in msg_text:
            send_auto_reply(message, 'Sure, what do you need help with?')
        elif 'thank you' in msg_text:
            send_auto_reply(message, 'You\'re welcome!')
        else:
            send_auto_reply(message, 'Sorry, I couldn\'t understand.')
            
        message.mark_seen()

        sleep(3)
