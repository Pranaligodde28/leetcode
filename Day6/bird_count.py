class Birds:
    bird_count={}
    def __init__(self,name=None, b_type=None, color=None):
        self.name = name
        self.b_type = b_type
        self.color = color

        if color in Birds.bird_count:
            Birds.bird_count[color] += 1 
        else:
            Birds.bird_count[color] = 1

    def get_count(color):
        return Birds.bird_count.get(color,0)

B1 = Birds("Parrot", "Domestic", "Green")
B2 = Birds("Sparrow", "Domestic", "Black")
B3 = Birds("Sparrow", "Domestic" , "Black")
B4 = Birds("Bat", "Wild", "Grey")
B5 = Birds("Parrot", "Domestic", "Green")
B6 = Birds("Bat", "Wild", "Grey")
B7 = Birds("Bat", "Wild ", "Grey")
B8 = Birds("Parrot", "Domestic", "Green")

print("Birds color: green: ", Birds.get_count("Green"))
