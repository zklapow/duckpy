#!/usr/bin/env python

import widget
import urllib2
import json
import base64

ducksboard = "http://www.push.ducksboard.com/"

class API():
	def __init__(self, key, widgets=None):
		self.key = key
		if widgets is None:
			self.widgets = []
		else:
			self.widgets = widgets
		
		# Create the authorization header
		self.auth = base64.encodestring("%s:x" % key)
		self.auth = self.auth.replace('\n', '')
		
	def _open(self, url, data):
		req = urllib2.Request(url, data, {'Authorization': 'Basic %s' % self.auth})
		return urllib2.urlopen(req)
		
	def _add_widget(self, widget):
		self.widgets.append(widget)
