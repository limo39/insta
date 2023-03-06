from instabot import Bot

# Create a new instance of the bot
bot = Bot()

# Login to your account
bot.login(username='your_username', password='your_password')

# Get the list of people you follow
following = bot.get_user_following('your_username')

# Unfollow each user in the list
for user_id in following:
    bot.unfollow(user_id)

# Logout from your account
bot.logout()