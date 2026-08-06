from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")

db = client["BankingRiskAnalytics"]

collection = db["customers"]

print("="*70)
print("MONGODB ANALYTICS")
print("="*70)

print("\n1. Total Customers")
print(collection.count_documents({}))

print("\n2. Housing Loan Customers")
print(collection.count_documents({"housing":"yes"}))

print("\n3. Personal Loan Customers")
print(collection.count_documents({"loan":"yes"}))

print("\n4. Customers Above Age 60")
print(collection.count_documents({"age":{"$gt":60}}))

print("\n5. Married Customers")
print(collection.count_documents({"marital":"married"}))

print("\n6. Customers With Tertiary Education")
print(collection.count_documents({"education":"tertiary"}))

print("\n7. Successful Marketing Campaign")
print(collection.count_documents({"y":"yes"}))

print("\n8. Top 10 Oldest Customers")

cursor = collection.find(
    {},
    {
        "_id":0,
        "age":1,
        "job":1,
        "education":1,
        "marital":1
    }
).sort("age",-1).limit(10)

df = pd.DataFrame(list(cursor))

print(df)

print("\nMongoDB Analytics Completed Successfully.")