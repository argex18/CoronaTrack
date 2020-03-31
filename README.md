# CoronaTrack

# Implemented 31/03/2020, 00:27
__Warning: I'm still implementing the function for email sending.

# Implementing function for data zipping

# The Covid-19 outbreak is one of most serious emergencies against which the world is actually fighting. 
# This data scraper takes all data about the pandemic by reliable sources and send them by email in a JSON file.
# It can be set to be periodically run every hour, day or any range of time you want.
# You won't need to worry of the outbreak going thanks to it.
# Thought to be secure and based on OAuth2 standard authentication and authorization protocol.

# Dependencies required:
  1) BeautifulSoup4 (for web data scraping)
  2) Requests (for getting the page in which data are contained)
  3) google-api-python-client (for OAuth2 authentication and authorization)

# You MUST have pip installed to follow this guide (it's usually provided by default in any Python distribution)
# WARNING: in this guide, the third-part-packages are going to be installed globally.
# To reduce the risk of conflicts with your system libraries, it would be better to use a virtual environment.
# Follow these links to know more about them:
    ENG: https://docs.python.org/3/tutorial/venv.html, https://realpython.com/python-virtual-environments-a-primer/
    IT: https://riptutorial.com/it/python/example/2934/creazione-e-utilizzo-di-un-ambiente-virtuale
# I HIGHLY recommend to read at least one of those links...

# BeautifulSoup4
# To install it you can simply open a terminal and digit: 
    pip install bs4

# Requests
# To install it you can simply open a terminal and digit:
    pip install requests

# google-api-python-client
# To install them you can simply open a terminal and digit:
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 
# More about Google Gmail APIs for Python on: https://developers.google.com/gmail/api/quickstart/python

# Once completed these tasks, you now have to create your credentials which then will need you to get your access token.
# To do this, go to https://developers.google.com/ , sign in your Google account and add our application to yours.
# You can create it and give it the name you want. You won't need any sort of verification.
# Once done that, click on Credentials panel and generate the OAuth secrets for your application.
# You just need to specify the name of your client (whatever you want) and kind of your application.
# "Other" option works fine.
# Once created, the credentials should appear on the OAuth table of Credentials page.
# Download the json file. Save it in CoronaTrack project folder.
# WARNING: Don't save it in other locations otherwise you will have to modify the script to take the file path by input.

# Once completed this last passage, you got it! Simply run the script by digiting on your terminal:
    cd path_to_CoronaTrack_folder
    python .\main.py
# First time you run the script, it will be asked you to sign in your Google account and give to the app you
# created before the permission to send emails as you. Accept to gain the access token.

# The access token should last for 100 days by default. Then it will be necessary refreshing it.
# Obviously, if you refuse, the script will generate an error. Please, trust me and don't refuse;)
