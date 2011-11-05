duckpy is a dead simple python package, based on urllib2, which allows you to interface with the ducksboard API.

Usage
-----
### Numeric Widgets
Using the numeric widgets is simple. First we need to create an api object with our credentials

	>>> import duckpy
	>>> api = duckpy.api("YOUR API KEY")
Next we create the widget, in this case I'm going to use a Counter but you may use any numeric widget.

	>>> from duckpy.widget import Counter
	>>> count = Counter("YOUR WIDGET URL")
Now that we have a wiget set up we can simply update its value like so:

	>>> count.update(42)
