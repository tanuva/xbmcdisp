class Settings:
	"""
	This is the actual configuration file. It is interpreted like ordinary Python code,
	so you can do any kind of magic here that comes to your mind.
	"""

	# URL of your XBMC instance's web interface.
	#xbmcHost = "http://raspberry.pi:80"
	xbmcHost = "http://localhost:80"

	# Display device as Serdisplib expects it
	# See http://serdisplib.sourceforge.net/docs/index.html#serdisp_connect__SDCONN_open
	#dispDevice = "USB:7c0/1501"
	dispDevice = "USB:7c0/1501"

	# Display model as Serdisplib expects it
	# Look for your display on http://serdisplib.sourceforge.net/#displays, where
	# "Name in serdisplib" is the value that goes here.
	#dispModel = "CTINCLUD"
	dispModel = "CTINCLUD"
