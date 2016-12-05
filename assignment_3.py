# Python script to work with companies house api  
# Companies House API --> (https://developer.companieshouse.gov.uk/api/docs/)

# https://github.com/JamesGardiner/chwrapper 
# http://chwrapper.readthedocs.io/en/latest/user/install.html#install

#import the wrapper
from chwrapper import (Search)
#import os so can get api key securely
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
#import json
import json

# Set access token
# access_token = os.environ.get('ACCESS_TOKEN')
#create search object
# s = Search(access_token=access_token)
# uses python requests http://docs.python-requests.org/en/latest/
# s. makes sure the token is passed in the request.


# Search a company by company number
def company_by_number(number):
	access_token = os.environ.get('ACCESS_TOKEN')
	#create search object
	s = Search(access_token=access_token)
	# set r as the request
	r = s.search_companies(number)
	# return results as an array
	return (r.json()['items'])


# # Search for a company name by keyword
# def company_by_name(keyword):
# 	# set r as the request
# 	r = s.search_companies(keyword)
# 	# Loop to show we can print out as a list. Could also create a list and append to list.
# 	for details in (r.json()['items']):
# 		print("{} Company Number is: {} and was incorporated on {}".format(details['title'], details['company_number'], details['date_of_creation'] ))
	

# # Search for a company directors names by keyword
# def director_by_name(keyword):
# 	# set r as the request
# 	r = s.search_officers(keyword)
# 	# return results as an array
# 	return (r.json()['items'])

def company_profile(number):
	access_token = os.environ.get('ACCESS_TOKEN')
	#create search object
	s = Search(access_token=access_token)
	# set r as the request
	r = s.profile(number)
	# return results as an array
	return r.json()


#########
# Print as define returns the result
# print(company_by_number("08313497"))
# No print as the define prints the result
# company_by_name("mobile media advertising")
# Print as define returns the result
# print(director_by_name("Mark Jones"))

