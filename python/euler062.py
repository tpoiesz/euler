import euler as e

cubes = []

nn = 1002
while True:
    i = str(nn**3)
    cubes.append(i)
    count = 0
    cubePerms = [cube for cube in cubes if e.isPerm(cube, i)]
    if len(cubePerms) > 4:
        print cubePerms
        break
    nn += 1
