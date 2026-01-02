Now that we have a [Block](http://www.codewars.com/kata/55b75fcf67e558d3750000a3) let's move on to something slightly more complex: a `Sphere`.

## Arguments for the constructor 
```python
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
```
```csharp
radius -> integer
mass -> integer
```
    
## Methods to be defined
```python
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
```
```csharp
GetRadius()       =>  radius of the Sphere
GetMass()         =>  mass of the Sphere
GetVolume()       =>  volume of the Sphere (a double rounded to 5 place after the decimal)
GetSurfaceArea()  =>  surface area of the Sphere (a double rounded to 5 place after the decimal)
GetDensity()      =>  density of the Sphere (a double rounded to 5 place after the decimal)
```

## Example
```python
ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208
```
```csharp
Sphere ball = new Sphere(2,50)
ball.GetRadius() ->       2
ball.GetMass() ->         50
ball.GetVolume() ->       33.51032
ball.GetSurfaceArea() ->  50.26548
ball.GetDensity() ->      1.49208
```

Any feedback would be much appreciated