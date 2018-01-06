import praw

reddit = praw.Reddit(client_id = 'zZIMQvXKnrm-aw',client_secret = '4n0iJRdyx_y0X_NH0biminhzM50', username= 'duperdays', password= 'KingDuper', user_agent= 'PRAW')

subreddit = reddit.subreddit('Politics')

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, Ups: {}, Downs: {}, Have I visited: {}'.format
        (submission.title,submission.ups,submission.downs, submission.visited))

        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            print(20* '-')
            print('Parent ID:', comment.parent())
            print('Comment ID:', comment.id)
            print(comment.body)
           

