from dotenv import load_dotenv
import os
import requests

load_dotenv()

twitter_endpoint = os.getenv("TWITTER_API_ENDPOINT")
path = "/2/users/me" #"/tweets/search/recent"
#query="?query=bitcoin&tweet.fields=author_id"

twitter_api_token = "Bearer " + os.getenv("TWITTER_API_KEY")

twitter_url = twitter_endpoint + path #+ query

#headers = {"Authorization": twitter_api_token}
#, headers=headers
response = requests.get("https://api.coinlore.net/api/ticker/?id=90,80")
print(response.content)

# connection = http.client.HTTPSConnection(twitter_endpoint)
# connection.request("GET", "/")
# response = connection.getresponse()
# print("Status: {} and reason: {}".format(response.status, response.reason))

# connection.close()

