import time
from instabot import Bot

bot = Bot()

bot.login(username='your_username', password='your_password')

following = bot.get_user_following('_limo.39')

timeout = 1

for user_id in following:
    bot.unfollow(user_id)
    print(f"Unfollowed user {user_id}. Waiting {timeout} seconds...")
    time.sleep(timeout)

bot.logout()
