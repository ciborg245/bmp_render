def processObj(file):
    vertices = []
    faces = []
    normals = []
    textures = []

    cont = 0
    for line in file:
        try:
            lineArr = line.rstrip().split()

            if lineArr[0] == 'v':
                vertices.append(list(map(float, lineArr[1:])))
            elif lineArr[0] == 'f':
                faces.append([list(map(int, f.replace('-','').split('/'))) for f in lineArr[1:]])
            elif lineArr[0] == 'vn':
                normals.append(list(map(float, lineArr[1:])))
            elif lineArr[0] == 'vt':
                textures.append(list(map(float, lineArr[1:])))
        except Exception as e:
            pass
            # print(e)
            # print(line)
            # print(lineArr)

    return faces, vertices, textures
