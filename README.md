# README

## Overview

This Python script fetches the latest news articles related to a specified topic (in this case, "Tesla") using the News API, then formats the top 20 article headlines and descriptions into an email body. The script finally sends this formatted content as an email. The code is customizable for other topics by adjusting the `topic` variable.

## Requirements

- **Python 3.x**
- **News API Key**: A valid API key from [NewsAPI](https://newsapi.org/) to access their news articles.
- **Email Sending Module**: This script uses an external module `send_email` to send emails. Ensure that `send_email` is implemented in your environment to handle the email-sending functionality.

## Setup Instructions

1. **Install Required Libraries**: Ensure you have the `requests` library installed. You can install it via:
   ```bash
   pip install requests
   ```

2. **API Key**: Replace the placeholder `api_key` in the code with your actual API key from [NewsAPI](https://newsapi.org/).

3. **Configure Email Sending**:
   - Ensure you have implemented a function `send_email` in a separate file `send_email.py`.
   - The function should accept the parameter `message` to send the formatted news content.

## Usage

### Code Explanation

1. **Import Libraries**:
   - `requests`: Used to make HTTP requests to the News API.
   - `send_email`: Custom module for sending emails.

2. **Define Topic and API URL**:
   - Set the `topic` variable to specify the search query for news articles.
   - Construct the URL for the News API request, setting parameters like `q` (query), `sortBy` (sorting by the latest), `language`, and `apiKey`.

3. **Make API Request**:
   - Send a GET request to the News API and parse the JSON response.

4. **Format Email Content**:
   - Define a subject (`"Top Today's News Headlines"`).
   - Extract and format the top 20 articles’ titles, descriptions, and URLs into a message body.

5. **Send Email**:
   - Encode the `body` in UTF-8 and pass it to the `send_email` function to send the email.

### Example Run

```python
# Run the script by executing:
python script_name.py
```

## Customization

To modify the search topic, change the value of the `topic` variable. For example, setting `topic = "technology"` will fetch articles about technology.

## Troubleshooting

- **Invalid API Key**: Ensure the API key is correct. Check [NewsAPI](https://newsapi.org/) for API key issues.
- **Email Not Sending**: Verify the `send_email` function in `send_email.py` is properly configured with your email credentials and settings.

## License

This script is open for personal and educational use.