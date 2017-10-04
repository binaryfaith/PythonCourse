def draw_stars(arr):
    newarr = []
    x = 0
    for count in range(len(arr)):
        x = arr[count] * "*"
        print x
draw_stars([4, 6, 1, 3, 5, 7, 25])

def draw_stars_mixed(x):
    for count in x:
        if isinstance(count, int)==True:
            print  count * "*"
        if isinstance(count, str)==True:
            print count[0].lower() * len(count)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_mixed(x)
