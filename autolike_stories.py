from instabot import Bot 

bot = Bot()
bot.login(username="your_username", password="your_password")

stories = bot.get_user_stories(user_id)

bot.like_stories(stories)
bot.logout()
