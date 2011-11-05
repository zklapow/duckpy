#!/usr/bin/env python

from api import *
from widget import *

# Insert a key here for this to work
key = "2li9ezar1c6eydg75r18tvjmfsyvmyrirl1mn0ft0jx6a0clqq"

# URL for a counter used for testing
url = "https://push.ducksboard.com/values/11910/"

if __name__ == "__main__":
	api = API(key)
	counter = Counter(url, api)
	counter.update(30)
	
