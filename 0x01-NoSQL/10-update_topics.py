#!/usr/bin/env python3
"""
update document
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    :param mongo_collection: pymongo collection object
    :param name: school name to update (string)
    :param topics: list of strings representing the new topics
    :return: number of update documents
    """

    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )

    return result.modified_count
