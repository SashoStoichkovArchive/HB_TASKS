import copy
import pprint

def drop_bomb(m, x, y):
    bomb = m[x][y]

    if x-1 >= 0:
        if m[x-1][y] >= bomb:
            m[x-1][y] -= bomb
        else:
            m[x-1][y] = 0

    if y+1 <= len(m[x]) - 1:
        if m[x][y+1] >= bomb:
            m[x][y+1] -= bomb
        else:
            m[x][y+1] = 0

    if x+1 <= len(m) - 1:
        if m[x+1][y] >= bomb:
            m[x+1][y] -= bomb
        else:
            m[x+1][y] = 0

    if y-1 >= 0:
        if m[x][y-1] >= bomb:
            m[x][y-1] -= bomb
        else:
            m[x][y-1] = 0

    if x-1 >= 0 and y-1 >= 0:
        if m[x-1][y-1] >= bomb:
            m[x-1][y-1] -= bomb
        else:
            m[x-1][y-1] = 0

    if x-1 >= 0 and y+1 <= len(m[x]) - 1:
        if m[x-1][y+1] >= bomb:
            m[x-1][y+1] -= bomb
        else:
            m[x-1][y+1] = 0

    if x+1 <= len(m) - 1 and y+1 <= len(m[x]) - 1:
        if m[x+1][y+1] >= bomb:
            m[x+1][y+1] -= bomb
        else:
            m[x+1][y+1] = 0

    if x+1 <= len(m) - 1 and y-1 >= 0:
        if m[x+1][y-1] >= bomb:
            m[x+1][y-1] -= bomb
        else:
            m[x+1][y-1] = 0

    return m

def sum_of_el_in_matrix(m):
    result = 0

    for x in range(len(m)):
        result += sum(m[x])
    
    return result

def matrix_bombing_plan(m):
    result = dict()

    for x in range(len(m)):
        for y in range(len(m[x])):
            add_m = copy.deepcopy(m)
            
            drop_bomb(add_m, x, y)
            result.update({(x, y): sum_of_el_in_matrix(add_m)})
            
    return result

if __name__ == "__main__":
    pprint.pprint(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))