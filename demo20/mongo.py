import  pymongo


mo = pymongo.MongoClient(host='127.0.0.1',port=27017).waiwei

def waiwei_list():
    data = mo.meinv.find()
    count = mo.meinv.count()
    return  data,count

def get_detail(name):
    # pipeline = [
    #     {
    #         '$group': {
    #             '_id': name,
    #             '_img_url':'$img_url'
    #         }
    #     }
    # ]
    # results = list(mo.meinv.aggregate(pipeline=pipeline))
    data = mo.meinv.find_one({'title':name})
    return  data