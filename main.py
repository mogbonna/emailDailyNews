import requests

api_key = '2af417cc6b9043ffb0cd889e32831a8d'
url = ('https://newsapi.org/v2/top-headlines?country=us&'
       'category=business&apiKey=2af417cc6b9043ffb0cd889e32831a8d')

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
