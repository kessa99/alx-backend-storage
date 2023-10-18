#!/usr/bin/env python3

"""
listt all documents Mongo in python
"""


def list_all(mongo_collection):
    """
    list document
    """
    documents = []
    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)
    return documents
