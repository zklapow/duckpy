#!/usr/bin/env python

import urllib2
import json
import time
import base64
import cStringIO

class Timeline():
	orange = "https://dashboard.ducksboard.com/static/img/timeline/orange.gif"
	red = "https://dashboard.ducksboard.com/static/img/timeline/red.gif"
	green = "https://dashboard.ducksboard.com/static/img/timeline/green.gif"
	created = "https://dashboard.ducksboard.com/static/img/timeline/created.gif"
	edited = "https://dashboard.ducksboard.com/static/img/timeline/edited.gif"
	deleted = "https://dashboard.ducksboard.com/static/img/timeline/deleted.gif"
	
	def __init__(self, url, api=None):
		self.url = url
		self.api = api
		self.api._add_widget(self)
	
	def update(self, title, image, content, link=None, key=None):
		if type(image) is file:
			image = base64.b64encode(image.read())
			image = 'data:image/png;base64,%s'%image
		
		if link is not None:
			value = {'title': title, 'image':image, 'content': content, 'link':link}
		else:
			value = {'title': title, 'image':image, 'content': content}
			
		timestamp = time.time()
		
		return self.api._open(self.url, json.dumps({'timestamp': timestamp, 'value':value}))
	

class Image():
	def __init__(self, url, api=None):
		self.url = url
		self.api = api
		self.api._add_widget(self)
		
	def update(self, image, caption, key = None):
		if type(image) is file:
			image = base64.b64encode(image.read())
			image = 'data:image/png;base64,%s'%image
		
		timestamp = time.time()
		
		return self.api._open(self.url, json.dumps({'timestamp': timestamp, 'value': {'source': image, 'caption':caption}}))


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
		timestamp = time.time()
		
		if element is None and self.multi is True:
			# Update all urls
			for x in self.url:
				return self.api._open(x, json.dumps({"value": value, "timestamp": timestamp}))
		elif element:
			return self.api._open(self.url[element], json.dumps({"value": value, "timestamp": timestamp}))
		else:
			return self.api._open(self.url, json.dumps({"value": value, "timestamp": timestamp}))
		

class Counter(Numeric):
	pass

class Graph(Numeric):
	pass

class Bar(Numeric):
	pass

class Box(Numeric):
	pass

class Pin(Numeric):
	pass

class Gauge(Numeric):
	def update(self, value, element = None, key = None):
		if value < 0 or value > 1:
			print "Values for Gauges should be between 0 and 1, the value given is not."
		else:
			return Numeric.update(self, value, element, key)