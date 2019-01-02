import twitter

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api(consumer_key, consumer_secret,
                  access_token_key, access_token_secret)

statuses = api.GetUserTimeline(count=200)
for status in statuses:
    api.DestroyStatus(status._id)
