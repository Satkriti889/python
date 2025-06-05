# `__sub__(self, other)` for `-`

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __sub__(self, other):
       
        if isinstance(other, Vector2D):
            
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector2D(new_x, new_y)
        else:
           
            return NotImplemented 
   
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = Vector2D(4, 6)
v4 = Vector2D(1, 2)

print(v1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")


v_diff = v1 - v2
print(f"v1 - v2 = {v_diff}")
print(f"Is v_difference a Vector2D? {isinstance(v_diff, Vector2D)}")


print(f"Does v1 == v2? {v1 == v2}")
print(f"Does v1 == v4? {v1 == v4}") 
print(f"Does v_difference == v3? {v_diff == v3}") 