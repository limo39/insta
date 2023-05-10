import time
from instabot import Bot

bot = Bot()

bot.login(username='_limo.39', password='1379@Insta')

following = bot.get_user_following('_limo.39')

timeout = 1

for user_id in following:
    bot.unfollow(user_id)
    print(f"Unfollowed user {user_id}. Waiting {timeout} seconds...")
    time.sleep(timeout)

bot.logout()
