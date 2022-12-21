import pymongo
client = pymongo.MongoClient("mongodb+srv://TanujaDhope1:admin78@cluster0.aojtki0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
db1 = client['mongotest1'] ## create data base
coll = db1['test']  ## name of collection
# retrieving  all the documents in the collection
# find code goes here

cursor = coll.find()
print(cursor)
# iterate code goes here
for doc in cursor:
    print(doc)

# Retrieve specific documents in the collection
# find code goes here
db1 = client['mongotest1'] ## create data base
coll = db1['test']  ## name of collection
cursor = coll.find({"isbn": True})
# iterate code goes here
print(cursor)
print('Single query ')
for i in cursor:
    print(i)
# Retrieving using multiple criteria
# find code goes here
print('Query using multiple criteria')
cursor = coll.find({"William Shakespeare": False, "category": "Fiction"})
print(cursor)
# iterate code goes here
for doc in cursor:
    print(doc)

# insert code goes here
docs = [
	{"name": "Halley's Comet", "officialName": "1P/Halley", "orbitalPeriod": 85, "radius": 3.4175, "mass": 2.2e14},
	{"name": "Wild2", "officialName": "81P/Wild", "orbitalPeriod": 6.41, "radius": 1.5534, "mass": 2.3e13},
	{"name": "Comet Hyakutake", "officialName": "C/1996 B2", "orbitalPeriod": 17000, "radius": 0.77671, "mass": 8.8e12},
    ]
result = coll.insert_many(docs)
# display the results of your operation
print(result.inserted_ids)
cursor=coll.find()
for j in cursor:
    print(j)

# find code goes here
#Select documents using the less-than operator
print('Select documents using the less-than operator')
cursor = coll.find({"orbitalPeriod": {"$lt": 75}})
for j in cursor:
    print(j)
#Read Data with Compound Queries
print('Select documents with compound Queries')
##Select documents using the less-than operator,greater than and and
cursor = coll.find({"orbitalPeriod": {"$lt": 75},"radius":{"$gt": 1.4}})
for j in cursor:
    print(j)

# find code goes here
cursor = coll.find({ "$or": [ {"orbitalPeriod": {"$lt": 17000}}, {"radius":{"$gt": 3.4}},] } )
print("Compound QUERY USING OR")
for j in cursor:
    print(j)


#Delete specific documents in the comets collection.


# delete code goes here
doc ={
        "orbitalPeriod": {
              "$gt": 5,
              "$lt": 85
        }
    }
result = coll.delete_many(doc)
# amount deleted code goes here
print("Number of documents deleted: ", result.deleted_count)

#Update all documents in collection
#1 mile = 1.60934 kilometers
a = {
    '$mul':{'radius':1.60934}

}
ans1 = coll.update_many({},a)
# display the results of your operation
print("Number of documents updated: ", ans1.modified_count)