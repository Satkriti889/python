# `__gt__(self, other)` for `>`
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __gt__(self, other):
    
        if isinstance(other,Vector2D):
            return(self.x,self.y)>(other.x,other.y)
        else:
            print("error")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector2D(3, 4)
v2 = Vector2D(3, 3)
v3 = Vector2D(4, 2)
v4 = Vector2D(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
print(f"v4 = {v4}")

print(f"v1 > v2? {v1 > v2}")
print(f"v2 > v3? {v2 > v3}")
print(f"v1 > v4? {v1 > v4}")
