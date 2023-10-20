#!/usr/bin/env python3

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    1-connexion to database
    2-Calcul coleection number in the database
    3-calculs for the number of method used
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_logs = nginx_collection.count_documents({})
    print("{} logs".format(num_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = nginx_collection.count_documents({"method": method})
        print("\t{} {}".format(num_method, method))

    num_get_status = nginx_collection.count_document({"method": "GET", "path": "/status"})
    print("{} method = GET path=/status".format(num_get_status))
