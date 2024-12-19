def get_matrix (n, m, value) : # oбъявили функцию с параметрами
    matrix = [] # создали пустой список внутри функции
    for i in range(n): # написали первый цикл для n
        matrix.append([]) # добавили пустой список в список matrix


        for j in range(m): # внутренний цикл для m
            matrix[i].append(value) #пополнили ранее пустой список значениями value
    print(matrix)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)