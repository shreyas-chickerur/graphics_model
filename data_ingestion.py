from itertools import permutations

def ingest_data(filename):
    data = list()
    f = open(filename, 'r')
    file_lines = f.readlines()
    num_vertices = int(file_lines[0].strip().split(',')[0])
    num_lines = int(file_lines[0].strip().split(',')[1])
    vertices_dict = dict()
    lines_list = list()
    for i in range(1, num_vertices + 1):
        line = file_lines[i].strip().split(',')
        v_id = int(line[0])
        vertex = [float(x) for x in line[1:]]
        vertices_dict[v_id] = vertex
    for i in range(num_vertices + 1, num_vertices + 1 + num_lines):
        line = file_lines[i].strip().split(',')
        line = [int(x) for x in line]
        all_combinations = permutations(line, 3)
        for val in all_combinations:
            lines_list.append(val)
    return vertices_dict, lines_list