import re
from random import sample, randrange
import os
from twitter import Twitter, OAuth
import json

def generate_tweet():
  max_tweet_length = 280
  directory = os.fsencode("/home/erviewre/h3podcastbot/punctuated_scripts")

  sentences = []
  episodes = {}
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    with open('/home/erviewre/h3podcastbot/punctuated_scripts/' + filename, 'r') as f:
      episode_text = f.read()
      episodes.update({ episode_text: filename })
      sentences += re.findall(r".*?[\.\!\?]+", episode_text)

  rand_index = randrange(len(sentences))
  while (len(sentences[rand_index]) > max_tweet_length):
    rand_index = randrange(len(sentences))

  tweet = ""
  episode = None

  for i in range(5):
    if (len(tweet + sentences[rand_index + i]) > max_tweet_length):
      break
    tweet = tweet + sentences[rand_index + i]

  for key in episodes.keys():
    if (tweet in key):
      episode = episodes[key]

  return tweet, episode[:-4]

def post(tweet, episode):
  with open('/home/erviewre/h3podcastbot/config.json') as f:
    config = json.load(f)

  t = Twitter(auth=OAuth(config["accessToken"], config["accessTokenSecret"], config["clientKey"], config["clientSecret"]))
  response = json.loads(json.dumps(t.statuses.update(status=tweet)))

  if (episode is not None):
    t.statuses.update(status="@H3PodcastBot This quote is from " + episode, in_reply_to_status_id=response["id"])

def main():
  tweet, episode = generate_tweet()
  post(tweet, episode)

if __name__ == "__main__":
  main()
