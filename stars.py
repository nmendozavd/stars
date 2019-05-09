def draw_stars(list):
    for x in list:
        print "*" * x
x = [4,6,1,3,5,7,25]

draw_stars(x)

def stars2(list):
    for x in list:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length
x = [4, "Tom", 1, "Michael", 5,7, "Jimmy Smith"]
stars2(x)