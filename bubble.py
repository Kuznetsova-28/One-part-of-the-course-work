def bubble(arr, dim):
    alg_count = [0, 0]  # список из 2-ч элементов для хранения показателей эффективности

    for i in range(0, dim - 1):  # внешний цикл кол-во итераций

        for j in range(len(arr) - 1, i, -1):  # обход массива с обратной стороны
            alg_count[0] += 1
            if arr[j] < arr[j - 1]:  # если элемент с меньшим индексом больше, то нужно сделать обмен
                alg_count[1] += 1
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # обмен

    return alg_count