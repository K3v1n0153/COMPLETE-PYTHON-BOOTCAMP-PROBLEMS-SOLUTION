"""
Get the volume and surface_area of a cylinder

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume() --> 56.52
c.surface_area() --> 94.2
"""

#######################
## SOLUTION BY KEVIN ##
#######################

class Cylinder:

	def __init__(self, height=1, radius=1):

		self.height = height
		self.radius = radius

	def volume(self):
		return self.height*3.14*self.radius**2

	def surface_area(self):
		return (2*3.14*self.radius**2) + (2*3.14*self.radius*2)

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())