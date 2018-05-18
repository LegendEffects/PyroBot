import tweepy, os, random

auth = tweepy.OAuthHandler('<Consumer Token>', '<Consumer Secret>')
auth.set_access_token('<key>', '<secret>')

api = tweepy.API(auth)

responsefile = open('responses.txt', 'r')
responsemsg = responsefile.read()
responses = responsemsg.replace("'", "").split(";")

print(responses)

# '970615160346894336' - Pyros twitter ID

user = ['970615160346894336']
imgDir = "images"
print("Starting..")


def process_tweet(status):
    image = imgDir+'/'+random.choice(os.listdir(imgDir))
    response = random.choice(responses)
    api.update_with_media(image, "@{} {}".format(status.user.screen_name, response), in_reply_to_status_id=status.id)
    print("Replied with {} and image {}.").format(response, image)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.author.id_str in user:
            process_tweet(status)


print("Starting the stream listener")
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(follow=user)

print("Goodbye ;(")
