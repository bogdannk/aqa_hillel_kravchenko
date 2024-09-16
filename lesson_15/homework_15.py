
"""First solution only with checking the angle a,
so that the angle b is not recalculated when the side a changes."""
# class Rhomb:
#     def __init__(self, side_a: int | float, angle_a: int | float):
#         setattr(self, "side_a", side_a)
#         setattr(self, "angle_a", angle_a)
#
#     def __setattr__(self, name: str, value: int | float):
#         if name == "angle_a":
#             super().__setattr__(name, value)
#             super().__setattr__("angle_b", 180 - value)
#         else:
#             super().__setattr__(name, value)
#
#     def __str__(self):
#         return f"Rhomb: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"
#
#
# """Example usage"""
# rhomb = Rhomb(10, 100)
# print(rhomb)

"""Second solution with name and angle checks"""
class Rhomb:
    def __init__(self, side_a: int, angle_a: int | float):
        setattr(self, "side_a", side_a)
        setattr(self, "angle_a", angle_a)

    def __setattr__(self, name: str, value: int | float):
        if name == "side_a":
            if value <= 0:
                raise ValueError("The length of the side must be greater than 0")
            else:
                super().__setattr__(name, value)
        elif name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("The angle should be between 0 and 180 degrees")
            else:
                super().__setattr__(name, value)
                super().__setattr__("angle_b", 180 - value)
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Romb: side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}"

"""Example usage"""
rhomb = Rhomb(20, 150)
print(rhomb)

