def k_cross_validation(lst: list):
    for i in range(len(lst)):
        test = lst[i]
        train = []

        for j in range(len(lst)):
            if i == j:
                continue
            else:
                train.append(lst[j])

        print(train, test)

k_cross_validation([1, 2, 3, 4, 5, 6, 7, 8, 9])


