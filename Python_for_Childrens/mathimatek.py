for x in range(90):
    for y in range(90):
        for z in range(90):
            if x + y + z == 100 and x*100+y*40+z*2 == 2000:
                print(x,y,z)