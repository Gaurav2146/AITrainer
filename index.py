import pymongo

# Replace with your MongoDB connection string
# For local MongoDB instance, use something like:
# client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Accessing a database
db = client["AITrainer"]

# Accessing a collection
collection = db["Cources"]

# Example document to be inserted
document = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "New York"
}

# Inserting a document into the collection
insert_result = collection.insert_one(document)
print(f"Inserted document ID: {insert_result.inserted_id}")

# Querying the collection
query_result = collection.find_one({"name": "John Doe"})
if query_result:
    print("Found document:", query_result)
else:
    print("Document not found.")

# Closing the connection
client.close()
