import itertools

n = 5
taken = [[False] * n * n for _ in range(n * n)]


def add_solution(solution):
    for li in solution:
        for el1, el2 in itertools.product(li, li):
            taken[el1][el2] = True
            taken[el2][el1] = True


found = False


def nn(rest_elements, current_list, current_res):
    global found
    if found:
        return current_res
    # print(rest_elements, current_list, current_res)
    if len(current_res) == n:
        found = True
        return current_res
    if len(current_list) == n:
        current_res.append(current_list)
        # print(current_res)
        nn(rest_elements, [], current_res)
    for el in rest_elements:
        if found:
            break
        if not any([taken[taken_el][el] for taken_el in current_list]):
            current_list.append(el)
            copied_elements = rest_elements.copy()
            copied_elements.remove(el)
            nn(copied_elements, current_list, current_res)
            if found:
                break
            rest_elements.append(el)
            current_list.remove(el)

    return current_res


res = nn(list(range(n * n)), [], [])
add_solution(res)
print("NEW")
found = False
res = nn(list(range(n * n)), [], [])
add_solution(res)
print(res)
found = False
res = nn(list(range(n * n)), [], [])
add_solution(res)
print(res)
# found = False
# res = nn(list(range(n * n)), [], [])
# add_solution(res)
# print(res)
