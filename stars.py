
def stars(list):
    for x in list:
        print "*" * x


nums = [6,2,5,7,9]
stars(nums)


def stars2(list):
    for x in list:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(x)
