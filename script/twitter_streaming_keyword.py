# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "971754780749172736-N7fMVHEJsi7fsBZITGt4Qv5TLp6n2eS"
ACCESS_SECRET = "LuHZoRFZeHlRuHyrdxMZiMWLWItpwroZjNtNAkOyeve87"
CONSUMER_KEY = "Qvv4f5bG3QsZOEluHOp27cXwN"
CONSUMER_SECRET = "No5y6jzLEKD1ZQuopvOj6FrAzhPUPggYHJY4ugRCA2J7rWGm4j"

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)
# twitter = Twitter(auth=oauth)


# Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()
iterator = twitter_stream.statuses.filter(track=["renault", "clio", "megane",
                                                 "captur", "kadjar", "talisman",
                                                 "twingo", "kangoo", "espace",
                                                 "zoe", "scenic"], language="fr")
# iterator = twitter.search.tweets(q="Renault", result_type='recent', lang='en', count=1000)
# iterator = twitter.statuses.user_timeline(screen_name="caradisiac")


# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 100000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print(json.dumps(tweet))

    # The command below will do pretty printing for JSON data, try it out
    # print(json.dumps(tweet, indent=4))

    if tweet_count <= 0:
        break
