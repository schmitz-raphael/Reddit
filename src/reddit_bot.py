import praw
from dotenv import load_dotenv
import os

#create a wrapper class for the reddit client
class Bot:
    def __init__(self):
        print("Reddit bot ready")
        load_dotenv()
        password = os.getenv("PASSWORD")
        username = os.getenv("USERNAME")
        self.reddit = praw.Reddit(
            client_id = "zzuPHnlAjZiDTS4yygD4Mw",
            client_secret = "a8llxIjL5ympSseOom2Y6GFBFAUNRQ",
            password = password,
            user_agent="Script to scrap posts of subreddit",
            username = username,
        )



    #function to get recent posts off a subreddit
    def getMostRecentPosts(self,subreddit):
        subreddit = self.reddit.subreddit(subreddit)
        return subreddit.hot(limit = 5)
    