#!/usr/bin/env python

import urllib2
import json

class Numeric():
	def __init__(self, url, api=None):
		if type(url) == list and len(url) > 1:
			self.multi = True
		else:
			self.multi = False
		
		self.url = url
		self.api = api
		self.api._add_widget(self)
		
	def update(self, value, element = None, key = None):
		"""
		Update the value of the widget.
		Params:
			value : The value to set the widget to
			element : The element in a multi-part widget to be updated. If none all are updated
			key : An API key if not using the API class
		"""
		if element is None and self.multi is True:
			# Update all urls
			pass
		else:
			self.api._open(self.url, json.dumps({"value": value}))
		
class Counter(Numeric):
	pass
		
