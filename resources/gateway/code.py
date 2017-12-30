import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "basdasdaasd"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()