from preloaded import Vector

def cross_product(a: Vector, b: Vector) -> Vector:
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return Vector(x=x, y=y, z=z)
