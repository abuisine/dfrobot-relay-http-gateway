import web, os
from Relay import *

urls = (
	'/',		'version',
	'/relays',	'relays'
)

Relay = Relay(os.environ['RELAY_HOSTNAME'], os.environ['RELAY_PORT'])

class version:
	def GET(self):
		return "Version: %s"%Relay.getVersion()['version']

	def POST(self):
		return "Version: %s"%Relay.getVersion()['version']

class relays:
	def filterRequest(self, input):
		return {k:v for k,v in input.iteritems() if k[:5] == 'relay'}

	def render(self, relays):
		html = "<html>"
		for relay in relays:
			html += "%s: %s<br>"%(relay, relays[relay])
		html += "</html>"
		return html

	def GET(self):
		if ( len(web.input()) ):
			return Relay.setRelayStatus(self.filterRequest(web.input()))
		else:
			return self.render(Relay.getRelayStatus())

	def POST(self):
		if ( len(web.input()) ):
			return Relay.setRelayStatus(self.filterRequest(web.input()))
		else:
			return self.render(Relay.getRelayStatus())

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()