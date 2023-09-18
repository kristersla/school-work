class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi*radius**2
    
    def __init__(self, diametre):
        
        print(f"New circle with diametre: {diametre}")
        

circle = Circle(100)

pizza_area = circle.area(12/2)
print(pizza_area)
teaching_table_area = circle.area(36/2)
print(teaching_table_area)
round_room_area = circle.area(11460/2)
print(round_room_area)

circle1 = Circle(100)