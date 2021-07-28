import praw

reddit = praw.Reddit(
    client_id="aCsxA497160GjRop_8DDXA",
    client_secret="rAuMc2mxJPwLMsX4xYqNrpg5ifa7ig",
    user_agent="reddit bot for udemy course",
    username="DistinctCap2574",
    password="this is the password",
    check_for_async=False
)

import random
import time
def karma():
  try:
    messages = ["Upvoted, upvote in return?", "Great post, care to share the upvotes!"]
    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
  except:
    time.sleep(300)
    karma()
karma()
