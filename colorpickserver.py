import web
import json
import os
import lifx

urls = (
    "172.27.99.15:80/color", "colorme",
)


class dbread:
    def GET(self):
        data = db.select('SensorData', order='Time DESC', limit=40)

        #TODO: read the sensor data and render the corresponding website with the input data table
        data = [[(d['Time'] - datetime(1970,1,1)).total_seconds(),d['Temperature'],d['Humidity']] for d in list(data)]
        # data = [[str(d['Time']),d['Temperature'],d['Humidity']] for d in list(data)]
        data.sort()
        return render.wg(data)
class colorme:
    def GET(self):
        data=web.input();
        setBulbColor(data.h, data.s, data.b, data.k)




import threading
def run():

    app = web.application(urls, globals())
    app.run()
