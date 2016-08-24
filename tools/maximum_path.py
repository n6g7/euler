def maximum_path_pyramid(pyramid):
    path = [[pyramid[0][0]]]

    for i in range(1, len(pyramid)):
        path.append([pyramid[i][0] + path[i-1][0]])

        for j in range(1, i):
            m = max(path[i-1][j-1], path[i-1][j])
            path[i].append(pyramid[i][j] + m)

        path[i].append(pyramid[i][i] + path[i-1][i-1])

    return max(path[-1])
