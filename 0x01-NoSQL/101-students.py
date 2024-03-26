#!/usr/bin/env python3
"""
write a function returns all students sorted by average
"""


def top_students(mongo_collection):
    """
    1-utilisation de l'operation d'agregation dans
    MongoDB pour traiter les donnees
    2- inclut le champ name tel quel
    3-calcul de la moyenne des cores dans le champs 'topics'
    4-trie les resultats par la moyenne des scores
      dans l'ordre decroissant
    5-renvoie le resultat e l'operation d'agregation
    """

    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top_students
