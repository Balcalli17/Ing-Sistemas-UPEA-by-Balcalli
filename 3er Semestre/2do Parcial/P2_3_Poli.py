class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector2D(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar):  # escalar * vector
        return self.__mul__(escalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

# ── Programa principal ──
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")       # (4, 6)
print(f"v1 - v2 = {v1 - v2}")       # (-2, -2)

v3 = Vector2D(2, 3)
print(f"v3 = {v3}")
print(f"v3 * 3  = {v3 * 3}")        # (6, 9)
print(f"2 * v3  = {2 * v3}")        # (4, 6)

v4 = Vector2D(5, 5)
v5 = Vector2D(1, 2)
print(f"v4 - v5 = {v4 - v5}")       # (4, 3)
