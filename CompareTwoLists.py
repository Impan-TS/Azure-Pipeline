def compare_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common_elements = list(set1.intersection(set2))

    only_in_list1 = list(set1.difference(set2))

    only_in_list2 = list(set2.difference(set1))

    print("Common elements:", common_elements)
    print("Only in list1:", only_in_list1)
    print("Only in list2:", only_in_list2)

    return {
        "common_elements": common_elements,
        "only_in_list1": only_in_list1,
        "only_in_list2": only_in_list2
    }


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    compare_lists(list1, list2)
