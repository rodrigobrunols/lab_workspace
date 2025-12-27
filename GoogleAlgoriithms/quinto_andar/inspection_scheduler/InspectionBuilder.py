from collections import defaultdict


def build_schedule(schedule):
    sources = set()
    destinations = set()
    source_to_dest = defaultdict()

    for s, d in schedule:
        sources.add(s)
        destinations.add(d)
        source_to_dest[s] = d

    start = None
    for s in sources:
        if s not in destinations:
            start = s
            break

    if start is None:
        return ""

    path = []
    curr = start
    while curr in source_to_dest:
        path.append(str(curr))
        curr = source_to_dest[curr]
    path.append(curr)
    # print(path)

    return "->".join(path)


def main():
    schedule_1 = [['1', '2'], ['2', '3'], ['3', '4'], ['4', '5']]
    result = build_schedule(schedule_1)
    print(result)



if __name__ == "__main__":
    main()

