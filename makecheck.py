# Contributors: obewyn
# Donate link: https://github.com/Obewyn/
# stable tag : 0.1



```python
import requests
from bs4 import BeautifulSoup
import time

# Function to check for new posts
def check_new_posts():
    # Replace 'website_url' with the actual URL of the website you want to scrape
    website_url = 'https://www.example.com'
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Replace 'post_element' with the HTML element that contains the post information
    post_element = soup.find('div', class_='post')
    
    # Check if the post element exists
    if post_element:
        # Replace 'last_post' with the variable or storage you use to keep track of the last post
        if post_element.text != last_post:
            # Replace 'alert_function' with the function or code that triggers the alert
            alert_function()
            # Update the last post variable with the new post
            last_post = post_element.text
    
    # Adjust the time interval (in seconds) based on how often you want to check for new posts
    time.sleep(60)  # Check every 60 seconds

# Replace 'alert_function' with the actual function or code that triggers the alert
def alert_function():
    print("New post published!")

# Replace 'last_post' with the variable or storage you use to keep track of the last post
last_post = ""

# Call the function to start checking for new posts
check_new_posts()
```

Make sure to customize the script by replacing 'website_url', 'post_element', 'last_post', and 'alert_function' with the appropriate values for the website you want to scrape and the alert mechanism you want to use.
