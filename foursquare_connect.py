
import re
import requests
import foursquare # pip install foursquare

from six.moves.urllib import parse
from app_info import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


# Connection to foursquare API endpoint using the foursquare python library


# -----------------------------------------------------------------------------------------
#  Authorization
# -----------------------------------------------------------------------------------------

# Initializing the Foursquare class (from the foursquare library) with the parameters provided by foursquare
client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

# Building the step 1 url to request the code
auth_uri = client.oauth.auth_url()

# The user (in this case us) is required to manually open the auth_uri in the browser to get the code
print 'Go to: ', auth_uri

# Copy and paste the redirect url here so the code can be extracted and stored
response_url = raw_input('Enter code in redirect url: ')

CODE = re.findall('\/\?code=([A-Z0-9]+)',response_url)[0]

# Interrogate foursquare's servers to get the user's access_token
access_token = client.oauth.get_token(CODE)

# Apply the returned access token to the client
client.set_access_token(access_token)

# Access granted!


# -----------------------------------------------------------------------------------------
#  Interact with the API
# -----------------------------------------------------------------------------------------

# Get the user's data
user = client.users()




'''

# -----------------------------------------------------------------------------------------
#  Example
# -----------------------------------------------------------------------------------------

	Querying japanese restaurants in Barcelona and storing them in a mongoDB database

	import foursquare as fq
	import pandas as pd
	import pprint
	import pymongo

	pp = pprint.PrettyPrinter(indent=2)


	# Connection to mongoDB
	# -------------------------------------------------------------------------------------

		Connect to mongo before running this script:

			- Open a terminal and run 'mongod'
			- Open another terminal and run 'python FourSquareAPI.py'

	try:
	    conn=pymongo.MongoClient()
	    print "Connected successfully!!!"
	except pymongo.errors.ConnectionFailure, e:
	   print "Could not connect to MongoDB: %s" % e 
	conn

	# Database (already created)
	db = conn['restaurants_bcn']

	# Collection
	venues=db.foursquare

	# Document (check if existing)
	venues.create_index('id',unique=True)


	# Interaction with foursquare API using foursquare python library
	# -------------------------------------------------------------------------------------

	restaurants_bcn = client.venues.explore(params={'near': 'Barcelona', 'query': 'sushi', 'offset': 50})

	# Parsing response and saving in db

	for groups in restaurants_bcn['groups']:
		 for group in groups['items']:

			venue = group['venue']

			venue_row = {'id':None, 'name': None}

			venue_row['id'] = venue['id']
			venue_row['name'] = venue['name']

			print venue['name']

			if 'rating' in venue:
				venue_row['rating'] = venue['rating']
			if 'price' in venue:
				#1 is < $10 an entree, 2 is $10-$20 an entree, 3 is $20-$30 an entree, 4 is > $30
				venue_row['price_range'] = venue['price']['tier']
				venue_row['price_currency'] = venue['price']['currency']
				venue_row['price_message'] = venue['price']['message']
			if 'phone' in venue['contact']:
				venue_row['phone']= venue['contact']['phone']
			if 'city' in venue['location']:
				venue_row['city'] = venue['location']['city']
			if 'postalCode' in venue['location']:
				venue_row['merchant_zipcode'] = venue['location']['postalCode']
			if 'address' in venue['location']:
				venue_row['address'] = venue['location']['address']
			if 'lat' in venue['location']:
				venue_row['latitude'] = venue['location']['lat']
			if 'lng' in venue['location']:
				venue_row['longitude'] = venue['location']['lng']
			for categories in venue['categories']:
				category_list = []
				if 'name' in categories:
					category_list.append(categories['name'])
				venue_row['category'] = ",".join(category_list)

			try:
				likes = client.venues.likes(venue['id'])
				venue_row['likes'] = likes['likes']['count']
			except:
				continue

			try:
				hours = client.venues.hours(venue['id'])
				venue_row['hours'] = hours
			except:
				continue

			try:
				similar = client.venues.similar(venue['id'])
				venue_row['similar'] = similar
			except:
				continue

			try:
				links = client.venues.links(venue['id'])
				venue_row['links'] = links
			except:
				continue

			# try:
			# 	stats = client.venues.stats(venue['id'])
			# 	venue_row['stats'] = stats
			# except:
			# 	continue

			# try:
			# 	events = client.venues.events(venue['id'])
			# 	venue_row['events'] = events
			# except:
			# 	continue

			# try:
			# 	menu = client.venues.menu(venue['id'])
			# 	venue_row['menu'] = menu
			# except:
			# 	continue			

			try:
				venues.insert(venue_row)
			except:
				continue

'''





'''

# Deprecated 

# Establishing connection to foursquare API without foursquare 

AUTH_ENDPOINT = 'https://foursquare.com/oauth2/authenticate'
TOKEN_ENDPOINT = 'https://foursquare.com/oauth2/access_token'
API_ENDPOINT = 'https://api.foursquare.com/v2'

# Authorization

class FoursquareAPI(object):

	def __init__(self):

		"""Sets up the api object"""
		self.CLIENT_ID = CLIENT_ID
		self.CLIENT_SECRET = CLIENT_SECRET
		self.REDIRECT_URI = REDIRECT_URI

	def auth_url(self):
		"""Gets the url a user needs to access to give up a user token"""
		params = {
			'client_id': self.CLIENT_ID,
			'response_type': u'code',
			'redirect_uri': self.REDIRECT_URI,
		}
		return '{AUTH_ENDPOINT}?{params}'.format(
			AUTH_ENDPOINT=AUTH_ENDPOINT,
			params=parse.urlencode(params))


logObj = FoursquareAPI()

print logObj.auth_url()




Deprecated

import re
import requests
import foursquare # pip install foursquare

from six.moves.urllib import parse
from app_info import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

AUTH_ENDPOINT = 'https://foursquare.com/oauth2/authenticate'

params = {
'client_id': CLIENT_ID,
'response_type': u'code',
'redirect_uri': REDIRECT_URI,
}

r = requests.request("GET", url=AUTH_ENDPOINT, headers={}, params=parse.urlencode(params))

'''


