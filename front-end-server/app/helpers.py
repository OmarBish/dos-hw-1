from flask import jsonify
import requests



from app import cache
from app import catalog_servers,order_servers


def buildResponse(status = 'Success',message='',code=200,data=None):
    res = {'status':status,'message':message}
    if data is not None:
        res['data'] = data
    return jsonify(res) ,code

@cache.memoize(60) #sec
def getCachedResponse(base , route , body):
    return getResponse(base , route , body)

def getResponse(base , route , body):
    url = None

    if base == "order":
        url = order_servers[randint(0,len(order_servers))
    else:
        url = catalog_servers[randint(0,len(catalog_servers))

    return requests.post(url + route ,json=body)
