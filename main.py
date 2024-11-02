import requests
from send_email import send_email

api_key = '2af417cc6b9043ffb0cd889e32831a8d'
url = ('https://newsapi.org/v2/top-headlines?country=us&'
       'category=business&apiKey=2af417cc6b9043ffb0cd889e32831a8d')

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Define the subject and create the body content
subject = "Top Business News Headlines"
body = f"Subject: {subject}\n\n"

# Access the article titles and descriptions
for article in content["articles"]:
    if article["title"] is not None:
        body += f"{article['title']}\n{str(article['description'])}\n\n"

# Encode the body and send the email
body = body.encode("utf-8")
send_email(message=body)
