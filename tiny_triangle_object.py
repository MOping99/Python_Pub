import matplotlib.pyplot as plt

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "{},{},{}".format(str(self.a), str(self.b), str(self.c))

    def graph(self):
        x = [self.a[0],self.b[0],self.c[0],self.a[0]]
        y = [self.a[1],self.b[1],self.c[1],self.a[1]]
        plt.plot(x,y)
        plt.show()

def main():
    Tri1 = Triangle((0,0), (0,3), (4,0))
    print(Tri1)
    Tri1.graph()


main()
