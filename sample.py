from collections import Counter


def top_occurrences(lst):
    # Comptage des occurrences de chaque élément dans la liste
    counts = Counter(lst)
    # Convertir le Counter en une liste de tuples (élément, compteur)
    most_common_three = counts.most_common(3)
    # Créer une liste des éléments les plus fréquents sans les compteurs
    most_common_elements = [item[0] for item in most_common_three]
    # Réordonner les éléments en conservant leur ordre d'apparition original dans la liste
    top_three = []
    # top_three = [item for item in lst if item in most_common_elements and item not in top_three]
    for item in lst:
        if item in most_common_elements and item not in top_three:
            top_three.append(item)
    return [item for item in top_three]


print(top_occurrences([3, 1, 2, 5, 3, 3, 2, 2, 1, 5, 1, 1, 1, 1]))