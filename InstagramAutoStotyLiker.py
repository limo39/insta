import instaloader
import time

def auto_like_stories(username, password):
    L = instaloader.Instaloader()

    try:
        L.login(username, password)
        
        profile = instaloader.Profile.from_username(L.context, username)
        
        stories = profile.get_stories()

        for story in stories:
            L.seen_story(story)
            
            L.like_story(story)

            time.sleep(2)

    except instaloader.exceptions.LoginRequiredException:
        print("Login failed. Please check your credentials.")

    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Two-factor authentication required. Please provide the verification code.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("The specified profile does not exist.")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        L.logout()

# Provide your Instagram username and password
username = "your_username"
password = "your_password"

# Call the function to auto-like stories
auto_like_stories(username, password)
