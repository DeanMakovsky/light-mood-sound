import web
import json
import os
import lifx

urls = (
    "/color", "colorme",
)


class colorme:
    def GET(self):
        data=web.input();
        setBulbColor(data.h, data.s, data.b, data.k)




import threading
def run():

    app = web.application(urls, globals())
    app.run()

if __name__=="__main__":
    run()