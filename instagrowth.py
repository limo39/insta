from instapy import InstaPy

session = InstaPy(username="your_username", password="your_password")

session.login()

session.set_do_follow(True, percentage=50)
session.set_do_like(True, percentage=100)

session.set_user_interact(amount=3, randomize=True, percentage=50)
session.set_relationship_bounds(enabled=True, max_followers=10000)

session.set_quota_supervisor(enabled=True, sleep_after=["likes", "follows"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                             peak_likes_hourly=57,
                             peak_likes_daily=585,
                             peak_follows_hourly=48,
                             peak_follows_daily=380,
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=402,
                             peak_comments_hourly=21,
                             peak_comments_daily=182,
                             peak_server_calls_hourly=None,
                             peak_server_calls_daily=4700)

session.start()
