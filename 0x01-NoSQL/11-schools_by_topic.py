#!/usr/bin/env python3
"""
search specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    :param mongo_collection: pymongo collection object
    :param topic: topic search(string)
    :return: list of schools macthing the topic
    """
    schools =mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)
