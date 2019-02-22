
import tweepy
import time
import requests
import json
import datetime

consumer_key = "V5FNhKq8oenfINn8KiKBdjYbQ"
consumer_secret = "P2PINUIxMUjCwZ2jrMeKzoitkhfizNqFHcDBf5M5L9IjgAgknQ"
access_token = "1010519805101830144-XPPv6brzyJTQ4AG80q50atj0JlLba7"
access_token_secret = "T7V0QtLrQ5DId2TxiqBq0iMOuyykeWpBS4KG0IXaMHMMa"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

url = "https://api.apixu.com/v1/current.json?"
params = {
	"key" : "f73a65f9b9b94f009de144318192202",
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