# Task 1
def count_sum(l: list) -> int:
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + count_sum(l[1:])


count_sum([1, 2, 3, 4])


# Task 2
def count_emb_list_sum(l: list) -> int:
    total = 0
    for el in l:
        if type(el) == type([]):
            total = total + count_emb_list_sum(el)
        else:
            total = total + el

    return total

if __name__ == '__main__':
    # Task 2
    print(count_emb_list_sum([1, 2, [3, 4, [5, 6], 7], 8]))
