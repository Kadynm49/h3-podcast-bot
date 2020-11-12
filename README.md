# h3-podcast-bot

This is a twitter bot made for fun that posts quotes from https://www.youtube.com/c/h3podcast

You can find the bot's twitter page here: https://twitter.com/h3podcastbot

The script of each podcast is retrieved using this tool: https://www.dvdvideosoft.com/?app=dlstyt which grabs youtube's auto-generated captions for given video

Then I use [punctuator](https://pypi.org/project/punctuator/) to add punctuation to the scripts

I have the bot running on an ubuntu VM set with the following crontab file:

```0 */7 * * * python3 /home/erviewre/h3podcastbot/tweet.py >> /dev/null 2>&1```

😁
