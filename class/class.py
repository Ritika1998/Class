class Polygon:
    number_of_sides=0
    length_of_sides=[]

    def __init__(self,n):
        self.number_of_sides = n
        for i in range(n):
            self.length_of_sides.append(0)

    def input_sides(self):
        for i in range(self.number_of_sides):
            self.length_of_sides[i] = input("sides %d" %(i+1))



    def print_sides(self):
        for i in range(self.number_of_sides):
            print("side %d= %d" % (i+1, self.length_of_sides[i]))


p1 = Polygon(4)
p2 = Polygon(3)

p1.input_sides()
p1.print_sides()




class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

t1=Triangle()

print t1.number_of_sides

t1.input_sides()
t1.print_sides()

