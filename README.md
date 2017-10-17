# Sign up and Create an App

Go to [foursquare](https://developer.foursquare.com/), sign up and create an app.

I used my localhost for the Application Url and Redirect Url: `https://127.0.0.1:8000`.

Store the `CLIENT_ID`, `CLIENT_SECRET` and `REDIRECT_URL`.

# Installation

Use the [foursquare python library](https://github.com/mLewisLogic/foursquare) to get access and query the API.

```shell
pip install foursquare
```

# Authorization

Building a python module that allows access and interacts with foursquare.

More info [here](https://developer.foursquare.com/docs/api/configuration/authentication)

### Step 1

Direct users to Foursquare with your registered redirect uri.

```python

# Using built-in python requests:

import re
import requests
import urllib
from app_info import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

redirect_uri = urllib.quote(REDIRECT_URI)

auth_uri = 'https://foursquare.com/oauth2/authenticate?client_id=%s&response_type=code&redirect_uri=%s' % (CLIENT_ID, redirect_uri)

r = requests.get(auth_uri)

# Using the foursquare library

import foursquare

client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
auth_uri = client.oauth.auth_url()

```
### Step 2

If the user accepts, they will be redirected back to your URI with a code.


```python
# Manually go to the auth_uri, allow access and save the code from the redirect url.
# The following expression extracts the code from the redirect url.

CODE = re.findall('\/\?code=([A-Z0-9]+)',response_url)[0]

```

### Step 3

Your server should exchange the code it got in step 2 for an access token.

```python

# With this CODE it is now possible to get the access_token.

# Using built-in python requests:

token_url = 'https://foursquare.com/oauth2/access_token?client_id=%s&client_secret=%s&grant_type=authorization_code&redirect_uri=%s&code=%s' % (CLIENT_ID, CLIENT_SECRET, redirect_uri, CODE)

# Using the foursquare library

# Interrogate foursquare's servers to get the user's access_token
access_token = client.oauth.get_token(CODE)

# Apply the returned access token to the client
client.set_access_token(access_token)
```

# Querying

Visit the [foursquare python library](https://github.com/mLewisLogic/foursquare) for more info and examples.