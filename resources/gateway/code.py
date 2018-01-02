import web, os
from Relay import *

urls = (
    '/', 'index'
)

Relay = Relay(os.environ['RELAY_HOSTNAME'], os.environ['RELAY_PORT'])

class index:
    def GET(self):
    	return Relay.getVersion()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()