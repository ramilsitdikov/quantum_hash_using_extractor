def vector_on_matrix_mod_n(matrix_2_2, vector_2, modulo):
    '''
    :param matrix_2_2: 2-d array 2 on 2 numbers
    :param vector_2: array of 2 numbers
    :param modulo: number
    :return matrix on vector multiplication by modulo
    '''
    first = (matrix_2_2[0][0] * vector_2[0] + matrix_2_2[0][1] * vector_2[1]) % modulo
    second = (matrix_2_2[1][0] * vector_2[0] + matrix_2_2[1][1] * vector_2[1]) % modulo
    return [first, second]


def sum_of_two_vectors(vector1, vector2, modulo):
    '''
    :param vector1: array of 2 numbers
    :param vector2: array of 2 numbers
    :param modulo: number
    :return sum of 2 vectors by modulo
    '''
    first = (vector1[0] + vector2[0]) % modulo
    second = (vector1[0] + vector2[0]) % modulo
    return [first, second]


def make_expander_graph(ring_size):
    T1 = [[1, 2], [0, 1]]
    T2 = [[1, 0], [2, 1]]
    e1 = [1, 0]
    e2 = [0, 1]
    '''
    :param ring_size: number of vertices
    :return expander graph
    '''

    # generate vertices
    vertices = []
    for i in range(ring_size):
        for j in range(ring_size):
            vertices.append([i, j])

    print("vertices =", vertices)

    # generate edges
    edges = []
    for vertix in vertices:
        first = vector_on_matrix_mod_n(T1, vertix, ring_size)
        second = vector_on_matrix_mod_n(T2, vertix, ring_size)
        third = sum_of_two_vectors(first, e1, ring_size)
        fourth = sum_of_two_vectors(second, e2, ring_size)
        edges.extend([[vertix,first], [vertix,second], [vertix,third], [vertix,fourth]])

    for edge in edges:
        print(edge)



if __name__ == "__main__":
    n = 3
    make_expander_graph(n)

