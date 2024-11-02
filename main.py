import requests
from send_email import send_email

topic = "tesla"
api_key = '2af417cc6b9043ffb0cd889e32831a8d'
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'sortBy=publishedAt&'
       'apiKey=2af417cc6b9043ffb0cd889e32831a8d&'
       'language=en')

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Define the subject and create the body content
subject = "Top Today's News Headlines"
body = f"Subject: {subject}\n\n"

# Access the article titles and descriptions
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += (f"{article['title']}\n{str(article['description'])}\n"
                 f"{article['url']}\n\n")

# Encode the body and send the email
body = body.encode("utf-8")
send_email(message=body)
