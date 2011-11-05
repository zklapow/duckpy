#!/usr/bin/env python

from api import *
from widget import *

# Insert a key here for this to work
key = ""

# URL for a counter used for testing
url = ""

if __name__ == "__main__":
	api = API(key)
	counter = Counter(url, api)
	counter.update(30)
	
