class PrimitiveRotator:

    def __init__(self, direction):
        self.direction = direction
        self.map = {
            1: {     # anti-clockwise
                (1, 1): (-1, 1),
                (-1, 1): (-1, -1),
                (-1, -1): (1, -1),
                (1, -1): (1, 1),
            },
            -1: {   # clockwise
                (1, 1): (1, -1),
                (1, -1): (-1, -1),
                (-1, -1): (-1, 1),
                (-1, 1): (1, 1)
            }
        }

    def next_vector(self, input_vector):
        return self.map[self.direction][input_vector]
