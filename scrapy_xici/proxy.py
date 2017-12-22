import traceback
import pymongo

class GetIp():
    def __init__(self):
        MONGO_URL = 'localhost'
        MONGO_DB = 'xici'
        MONGO_TABLE = 'xici_get_ip'
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        self.result = db[MONGO_TABLE].find({'IP': {'$exists': True}})

    def get_ips(self):
        http = []
        https = []
        for h in self.result:
            if h['属性'] == 'HTTP':
                http.append(h['IP'] + ':' + h['端口'])
            elif h['属性'] == 'HTTPS':
                https.append(h['IP'] + ':' + h['端口'])
        print('HTTP:',len(http),"HTTPS:",len(https))
        return {'http':http,'https':https}

