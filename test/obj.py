def processObj(file):
    vertices = []
    faces = []
    normals = []
    textures = []

    cont = 0
    for line in file:
        lineArr = line.rstrip().split(' ')

        if lineArr[0] == 'v':
            vertices.append(list(map(float, lineArr[1:])))
        elif lineArr[0] == 'f':
            faces.append([list(map(int, f.split('/'))) for f in lineArr[1:]])
        # elif lineArr[0] == 'vn':
        #     normals.append(list(map(float, lineArr[1:])))
        elif lineArr[0] == 'vt':
            textures.append(list(map(float, lineArr[1:])))

    return faces, vertices, textures
