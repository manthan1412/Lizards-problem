import numpy as np
import copy

filename = "input.txt"
file = open(filename, "r")

method = file.readline()
n = int(file.readline())
p = int(file.readline())
first_row = list(file.readline().strip())
first_row = list(map(int, first_row))
nursery = [first_row]

max_depth = p
# lizards = np.array([], dtype=int)
tree_pos_x = {}
tree_pos_y = {}
nos_trees = 0

l = len(first_row)
for j in range(0, l):
    if first_row[j] == 2:
        nos_trees += 1
        if str(0) in tree_pos_x:
            tree_pos_x[str(0)].append(j)
        else:
            tree_pos_x[str(0)] = [j]
        if str(j) in tree_pos_y:
            tree_pos_y[str(j)].append(0)
        else:
            tree_pos_y[str(j)] = [0]

i = 1
for line in file:
    line = list(line.strip())
    line = list(map(int, line))
    l = len(line)
    for j in range(0, l):
        if line[j] == 2:
            nos_trees += 1
            if str(i) in tree_pos_x:
                tree_pos_x[str(i)].append(j)
            else:
                tree_pos_x[str(i)] = [j]
            if str(j) in tree_pos_y:
                tree_pos_y[str(j)].append(i)
            else:
                tree_pos_y[str(j)] = [i]

    nursery.append(line)  # = np.vstack((nursery, np.array(line, dtype=int)))
    i += 1

# print(tree_pos_x)
# print(tree_pos_y)
file.close()


def write_to_file(result, data):
    out_filename = "output.txt"
    f = open(out_filename, "w+")
    if not result:
        f.write("FAIL\n")
    else:
        if result == 1:
            final_nursery = [[0 for i in range(0, n)] for j in range(0, n)]
            for ele in tree_pos_x:
                for item in tree_pos_x[ele]:
                    final_nursery[int(ele)][item] = 2
            for ele in data:
                for item in data[ele]:
                    final_nursery[item][int(ele)] = 1
        else:
            final_nursery = data
        f.write("OK\n")
        for i in range(0, n):
            for j in range(0, n):
                f.write(str(final_nursery[i][j]))
            f.write("\n")
            # f.write("\n")
    f.close()


def DFS():
    row = 0
    start = 0
    lizards = {}
    lizards_x = {}
    lizard_placed = 0

    while True:
        if row == n or start == n:
            # solution not found
            if row == 0:
                last_empty = -1
                for i in range(n - 1, -1, -1):
                    if nursery[row][i] == 0:
                        last_empty = i
                last_l = -1
                for i in range(n - 1, -1, -1):
                    if nursery[row][i] == 1:
                        last_l = i
                if last_empty == -1 or last_l == -1:
                    write_to_file(0, "FAIL")
                    # print("FAILED")
                    return
                if last_l != -1:
                    if last_l == last_empty:
                        return

            # solution found
            if row == n:
                if lizard_placed == max_depth:
                    write_to_file(2, nursery)
                    # print("Solution found")
                else:
                    write_to_file(0, "FAIL")
                    # print("FAILED")
                return

            # backtrack
            while str(row) not in lizards_x:
                row -= 1
                if row < 0:
                    row = 0
                    break

                    # if row == 0:
                    # print("lizards", lizards)
                    # print("lizards_x", lizards_x)
                    # print("nursery", nursery)
                    # print("start", start)
            if str(row) in lizards_x:
                last_lizard = lizards_x[str(row)].pop()
                index = lizards[str(last_lizard)].index(row)
                del lizards[str(last_lizard)][index]
                if not lizards[str(last_lizard)]:
                    del lizards[str(last_lizard)]

                nursery[row][last_lizard] = 0
                start = last_lizard + 1
                lizard_placed -= 1

                if not lizards_x[str(row)]:
                    del lizards_x[str(row)]

            else:
                start = n

        else:

            while nursery[row][start] == 2:
                start += 1
                if start == n:
                    row += 1
                    start = 0
                if row == n:
                    break

            if row < n and start < n:

                while not is_valid(lizards, row, start):
                    start += 1
                    if start == n:
                        row += 1
                        start = 0
                    if row == n:
                        break

                # Update
                if row < n and start < n:
                    str_start = str(start)
                    if str_start in lizards:
                        lizards[str_start].append(row)
                    else:
                        lizards[str_start] = [row]

                    if str(row) in lizards_x:
                        lizards_x[str(row)].append(start)
                    else:
                        lizards_x[str(row)] = [start]
                    nursery[row][start] = 1
                    lizard_placed += 1
                    if lizard_placed == max_depth:
                        write_to_file(2, nursery)
                        # print("Solution found")
                        return

                    if str(row) in tree_pos_x:
                        temp_list = tree_pos_x[str(row)]
                        l = len(temp_list)
                        start_updated = False
                        if temp_list[0] > start:
                            start = temp_list[0] + 1
                            start_updated = True
                            if start == n:
                                start = 0
                                row += 1
                        for i in range(1, l - 1):
                            if temp_list[i] < start and start < temp_list[i + 1]:
                                start = temp_list[i + 1]
                                start_updated = True
                        if not start_updated:
                            if start < temp_list[-1]:
                                start = temp_list[-1] + 1
                                if start == n:
                                    start = 0
                                    row += 1
                            else:
                                start = 0
                                row += 1
                    else:
                        start = 0
                        row += 1

                    if start == 0 and row == n:
                        row -= 1
                        start = n
                elif row == n and start == 0:
                    row -= 1
                    start = n
            elif row == n and start == 0:
                row -= 1
                start = n

                # else:
                # start += 1


def search(array, start, end, key):
    mid = int((start + end) / 2)

    if array[mid] < key < array[mid + 1]:
        return array[mid]
    if start == end:
        return -1
    elif array[mid] > key:
        return search(array, start, mid, key)
    else:
        return search(array, mid + 1, end, key)


def is_valid(placed_lizards, lizard_i, lizard_j):
    if nursery[lizard_i][lizard_j] == 2:
        return 0
    # check vertical
    str_j = str(lizard_j)
    if str_j in placed_lizards:
        last_lizard = placed_lizards[str_j][-1]
        if str_j in tree_pos_y:
            l = len(tree_pos_y[str_j])
            # last_tree = tree_pos_y[str_j][-1]
            try:
                last_tree = search(tree_pos_y[str_j], 0, l - 1, lizard_i)
            except:
                last_tree = tree_pos_y[str_j][-1]
            if lizard_i < last_tree or last_tree < last_lizard:
                return 0
        else:
            return 0

    # check diagonal
    # can change this using the function of line
    x = lizard_i
    y = lizard_j
    while x >= 0 and y >= 0:
        if nursery[x][y] == 2:
            break
        elif str(y) in placed_lizards:
            temp_l = placed_lizards[str(y)]
            if x in temp_l:
                return 0
        x -= 1
        y -= 1

    x = lizard_i - 1
    y = lizard_j + 1
    while x >= 0 and y < n:
        if nursery[x][y] == 2:
            break
        elif str(y) in placed_lizards:
            temp_l = placed_lizards[str(y)]
            if x in temp_l:
                return 0
        x -= 1
        y += 1

    return 1


def place_lizard(zoo, x, y):
    row = []
    for j in range(0, n):
        row.append(zoo[0][j])
    new_nursery = np.array(row, dtype=int)
    for i in range(1, n):
        row = []
        for j in range(0, n):
            row.append(zoo[i][j])
        new_nursery = np.vstack((new_nursery, np.array(row)))
    new_nursery[x][y] = 1

    # vertical
    for i in range(x + 1, n):
        if new_nursery[i][y] == 2:
            break
        new_nursery[i][y] = -1

    # diagonal
    i = x + 1
    j = y - 1
    while i < n and j > -1:
        if new_nursery[i][j] == 2:
            break
        new_nursery[i][j] = -1
        i += 1
        j -= 1

    i = x + 1
    j = y + 1
    while i < n and j < n:
        if new_nursery[i][j] == 2:
            break
        new_nursery[i][j] = -1
        i += 1
        j += 1

    return new_nursery


def get_valid_positions(nursery_data):
    valid_positions = []
    row = nursery_data["row"]
    # if row == 8:
    # print ("here it is")
    start = nursery_data["start_value"]
    for i in range(start, n):
        if nursery[row][i] == 2:
            return valid_positions, i
        else:
            if is_valid(nursery_data["lizards"], row, i):
                valid_positions.append(i)

    return valid_positions, n - 1


def generate_bfs_cases(nursery_data, valid_positions, last_value):
    new_generated = []
    l = len(valid_positions)
    depth = nursery_data["depth"] + 1
    row = nursery_data["row"]
    last_value += 1
    max_raw = False
    if last_value == n:
        new_raw = row + 1
        last_value = 0
    else:
        new_raw = row
    if new_raw == n:
        max_raw = True
        # print("here too")
    for i in range(0, l):

        new_lizards = copy.deepcopy(nursery_data["lizards"])
        if str(valid_positions[i]) in new_lizards:
            new_lizards[str(valid_positions[i])].append(row)
        else:
            new_lizards[str(valid_positions[i])] = [row]
        new_nursery = {
            "lizards": new_lizards,
            "depth": depth,
            "start_value": last_value,
            "row": new_raw
        }
        new_generated.append(new_nursery)

    return new_generated, depth, max_raw


def BFS():
    availability = []
    for i in range(0, n):
        availability.append([0, 0, 0])
    bfs_queue = [{
        "lizards": {},
        "depth": 0,
        "row": 0,
        "start_value": 0
    }]
    printed = False
    while bfs_queue:
        valid_positions, last_value = get_valid_positions(bfs_queue[0])
        if valid_positions:
            generated_cases, depth, max_raw = generate_bfs_cases(bfs_queue[0], valid_positions, last_value)
            if depth == max_depth and generated_cases:
                write_to_file(1, generated_cases[0]["lizards"])
                # print(generated_cases[0])
                printed = True
                break
            if not max_raw:
                bfs_queue += generated_cases
            bfs_queue.pop(0)
        else:
            last_value += 1
            if last_value == n:
                if bfs_queue[0]["row"] < n - 1:
                    bfs_queue[0]["row"] += 1
                    bfs_queue[0]["start_value"] = 0
                else:
                    bfs_queue.pop(0)
            else:
                bfs_queue[0]["start_value"] = last_value

    if not printed:
        write_to_file(0, "FAIL")
        # print("Failed")

    return


def SA():
    return


write_to_file(0, "FAIL")
if n == 1:
    if p == 1:
        if nursery[0] == 0:
            write_to_file(1, {"0": [0]})
        else:
            write_to_file(0, "FAIL")
    else:
        write_to_file(0, "FAIL")

else:
    if p > n + nos_trees:
        write_to_file(0, "FAIL")
        # print("FAILED")
    elif method == "DFS\n":
        # TODO: improve DFS
        DFS()
    else:
        BFS()

