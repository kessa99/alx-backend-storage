#!/usr/bin/env python3
"""
insert document in collection in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a new document in collection based on kwargs.
    :param mongo_collection: pymongo collection object
    :param kwargs: keyword arguments representing document
    :return: new _id of the insert document
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
