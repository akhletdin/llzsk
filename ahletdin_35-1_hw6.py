def bubble_sort(lst):
    sort_lst = []
    while len(lst) != 0:
        m = lst.index(min(lst))
        sort_lst.append(lst.pop(m))
    return f"отсортированный список - {sort_lst}"

data = []
def binary_search(lst, number):
    l = lst[0]
    r = lst[-1]
    m = len(lst) // 2
    while True:
        if m < number:
            data.append(m)
            l = m
            m = (l + r) // 2
        elif m > number:
            data.append(m)
            r = m
            m = (l + m) // 2
        elif m == number:
            data.append(m)
            return "всё!"


print(bubble_sort([22, 65, 56, 42, 34, 12, 41]))
print(binary_search(range(1, 51), 12), f"{data} количество попыток - {data}")
