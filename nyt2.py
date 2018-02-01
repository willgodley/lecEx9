import requests
import secrets
import json

# gets stories from a particular section of NY times
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl, params).json()

section = 'science'
stories = get_stories(section)
print(stories) # large json object
