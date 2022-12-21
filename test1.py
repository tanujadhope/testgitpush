import pymongo
client = pymongo.MongoClient

client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.aojtki0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = [{"isbn": 9780198321668,"title": "Romeo and Juliet","author": "William Shakespeare","category": "Tragedy","year": 2008},
{"isbn": 9781505297409,"title": "Treasure Island","author": "Robert Louis Stevenson","category": "Fiction","year":2014}]

db1 = client['mongotest1']
coll = db1['test']
coll.insert_many(d)

d1={"isbn": 9780060859749, "title": "After Alice: A Novel", "author": "Gregory Maguire", "category": "Fiction", "year":2016}
coll.insert_one(d1)
cursor = coll.find()
print(cursor)
# iterate code goes here
for doc in cursor:
    print(doc)

