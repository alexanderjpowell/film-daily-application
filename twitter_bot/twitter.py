
import tweepy
import time
import requests
import json
import datetime

consumer_key = "<consumer_key>"
consumer_secret = "<consumer_secret>"
access_token = "<access_token>"
access_token_secret = "<access_token_secret>"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

url = "https://api.apixu.com/v1/current.json?"
params = {
	"key" : "<api_key>",
	"q" : "Richmond"
}

if __name__ == "__main__":

	while True:
		response = requests.get(url, params=params)
		json_string = response.json()
		weather_description = json_string['current']['condition']['text']
		timestamp = str(datetime.datetime.now())
		status = "The current weather conditions are: " + weather_description + " (" + timestamp + ")"
		api.update_status(status)

		time.sleep(60*60) # Sleep for 1 hour