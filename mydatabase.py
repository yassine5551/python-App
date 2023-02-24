from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

mydb = client["Stages"]

mycol = mydb["DBStage"]
def addToDb(id,price,domain,name,duree):
    data = {
    "id":id,
    "price":price,
    "domain":domain,
    "nameStage":name,
    "durre":duree
    }
    mycol.insert_one(data)

def update(id,price,domain,name,duree):
        data = {"$set":{
            "id":id,
    "price":price,
    "domain":domain,
    "nameStage":name,
    "durre":duree
        }}
        mycol.update_one({"id":id},data)


def deletedata(id):
        mycol.delete_one({"id":id})




