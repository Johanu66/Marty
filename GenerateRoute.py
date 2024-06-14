from GridManager import GridManager

class GenerateRoute:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.route = []

    # Initialisation des variables globales
    route_codes = {
        "light_blue": "begin",
        "dark_blue": "right",
        "pink": "left",
        "green": "forward",
        "yellow": "backward",
        "red": "end"
    }

    distance = 7

    routes = [
        {"origin": "light_blue", "distance": distance}
    ]

    # Fonction pour obtenir la direction suivante
    @staticmethod
    def get_next_position(x, y, direction):
        if direction == "forward":
            return x - 1, y
        elif direction == "backward":
            return x + 1, y
        elif direction == "left":
            return x, y - 1
        elif direction == "right":
            return x, y + 1
        else:
            print(f"Unknown direction: {direction}")

    # Fonction pour vérifier si une position est valide dans la grille
    @staticmethod
    def is_valid_position(x, y):
        return 0 <= x < GridManager.grille_size and 0 <= y < GridManager.grille_size

    # Fonction pour produire la liste de la route complète
    @staticmethod
    def produce_route():
        route = []
        for start in GenerateRoute.routes:
            origin_color = start["origin"]
            distance = start["distance"]
            
            # Trouver la position de départ dans la grille
            start_pos = None
            for i in range(GridManager.grille_size):
                for j in range(GridManager.grille_size):
                    if GridManager.grille[i][j] == origin_color:
                        start_pos = (i, j)
                        break
                if start_pos:
                    break

            if not start_pos:
                raise ValueError(f"Origin color {origin_color} not found in the grid")

            # Parcourir la grille en suivant les directions jusqu'à la couleur rouge (end)
            x, y = start_pos
            while True:
                current_color = GridManager.grille[x][y]
                route.append((current_color, (x, y)))

                if current_color == "red":
                    break

                direction = GenerateRoute.route_codes.get(current_color)
                if direction is None:
                    raise ValueError(f"No direction found for color {current_color}")

                x, y = GenerateRoute.get_next_position(x, y, direction)
                if not GenerateRoute.is_valid_position(x, y):
                    raise ValueError(f"Invalid move from ({x}, {y}) in direction {direction}")

        GenerateRoute.routes = route