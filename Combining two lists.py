def combine_lists(list1, list2):
    merged = sorted(list1 + list2, key=lambda x: x["positions"][0])
    result = []

    for item in merged:
        if not result:
            result.append(item)
            continue

        last = result[-1]
        l1, r1 = last["positions"]
        l2, r2 = item["positions"]

        overlap = min(r1, r2) - max(l1, l2)
        len1 = r1 - l1
        len2 = r2 - l2

        # Fixed: use >= instead of >
        if overlap >= len1 / 2 or overlap >= len2 / 2:
            combined_values = last["values"] + item["values"]
            result[-1] = {
                "positions": [l1, r1],
                "values": combined_values
            }
        else:
            result.append(item)

    return result


if __name__ == "__main__":
    import ast

    print("Enter list1 (e.g. [{'positions': [0, 10], 'values': [1, 2]}]):")
    list1 = ast.literal_eval(input())

    print("Enter list2 (e.g. [{'positions': [5, 15], 'values': [3, 4]}]):")
    list2 = ast.literal_eval(input())

    result = combine_lists(list1, list2)
    print("\n Combined Output:")
    for item in result:
        print(item)
