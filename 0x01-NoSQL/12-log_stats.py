#!/usr/bin/env python3
"""
write scrip that provides some stats
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats():
    """
    1-connexion to database
    2-Calcul coleection number in the database
    3-calculs for the number of method used
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    num_logs = collection.count_documents({})
    print("{} logs".format(num_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = collection.count_documents({"method": method})
        print("\t{} {}".format(method, num_method))

    num_get_status = collection.count_documents(
                        {"method": "GET", "path": "/status"})
    print("{} method = GET path=/status".format(num_get_status))


if __name__ == "__main__":
    log_stats()
