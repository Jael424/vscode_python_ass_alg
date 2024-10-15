#오른쪽이나 아래쪽으로만 이동할 수 있다.
#왼쪽, 위쪽, 대각선 이동은 할 수 없다.

if __name__ == "__main__":
    row, column = map(int, input().split())
    
    
    matrix = [[0 for i in range(column + 1)] for j in range(row + 1)]
    for i in range(row):
        temp_list =  map(list, input().split())
        for j in range(column):
            matrix[i + 1][j + 1] = temp_list[j]

    print(matrix)
    
    # 입력