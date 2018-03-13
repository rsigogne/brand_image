# Variables that contains the user credentials to access Twitter API
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

access_token = "971754780749172736-N7fMVHEJsi7fsBZITGt4Qv5TLp6n2eS"
access_secret = "LuHZoRFZeHlRuHyrdxMZiMWLWItpwroZjNtNAkOyeve87"
consumer_key = "Qvv4f5bG3QsZOEluHOp27cXwN"
consumer_secret = "No5y6jzLEKD1ZQuopvOj6FrAzhPUPggYHJY4ugRCA2J7rWGm4j"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('test.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=["#renault", "#clio", "#megane",
                             "#captur", "#kadjar", "#talisman",
                             "#twingo", "#kangoo", "#espace",
                             "#zoe", "#scenic", "#Renault", "#Clio", "#Megane",
                             "#Captur", "#Kadjar", "#Talisman",
                             "#Twingo", "#Kangoo", "#Espace",
                             "#Zoe", "#Scenic"])