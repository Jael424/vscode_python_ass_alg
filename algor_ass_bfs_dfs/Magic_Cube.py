
#A: 윗줄과 아랫줄에 있는 4개의 숫자를 서로 바꿉니다.
def A_fuc(cube_table_const) -> str:
    cube_table = list(cube_table_const)
    for i in range(4):
        temp = cube_table[i]
        cube_table[i] = cube_table[i + 4]
        cube_table[i + 4] = temp 
    return ''.join(cube_table)

#B: 각 줄의 숫자를 오른쪽으로 한 칸씩 이동시키고, 맨 오른쪽 숫자를 맨 왼쪽으로 이동시킵니다.
#0123 -> 3012
#4567 -> 7456
def B_fuc(cube_table_const) -> str:
    cube_table = list(cube_table_const)
    cube_table.insert(0,cube_table.pop(3))
    cube_table.insert(4,cube_table.pop(7))
    return ''.join(cube_table)

#C: 가운데 4개 정사각형의 숫자를 반시계 방향으로 한 번 회전시킵니다.
# 1 2 5 6 -> 1 2 5 6
#          =
# 0 1 2 3 -> 1 3 0 2 -> 원래 값의 위치가 왼쪽으로 이동하므로
def C_fuc(cube_table_const) -> str:
    cube_table = list(cube_table_const) 
    temp = [cube_table[1], cube_table[2]
            ,cube_table[5], cube_table[6]]
    
    cube_table[1] = temp[1]
    cube_table[2] = temp[3]
    cube_table[5] = temp[0]
    cube_table[6] = temp[2]

    return ''.join(cube_table)

#D: 1번 위치와 5번 위치의 숫자를 서로 바꿉니다. (1번과 5번은 위 표의 좌측 상단과 우측 하단의 위치를 의미합니다)
def D_fuc(cube_table_const) -> str:
    cube_table = list(cube_table_const)
    temp = cube_table[0]
    cube_table[0] = cube_table[7]
    cube_table[7] = temp
    
    return ''.join(cube_table)
    
""" magic_cube = "12348765"
def dfs_cube(cube_table, searchNum : int, before_cmd = None) -> int:
    if before_cmd != 'A' :
        temp = A_fuc(cube_table)
        if temp == magic_cube:
            return searchNum
        else:
            return dfs_cube(temp, searchNum + 1, 'A')
    
    temp = B_fuc(cube_table)
    if temp == magic_cube:
        return searchNum
    else:
        dfs_cube(temp, searchNum + 1, 'B')

    temp = C_fuc(cube_table)
    if temp == magic_cube:
        return searchNum
    else:
        dfs_cube(temp, searchNum + 1, 'C')
    
    if before_cmd != 'D' :
        temp = D_fuc(cube_table)
        if temp == magic_cube:
            return searchNum
        else:
            dfs_cube(temp, searchNum + 1, 'D')
     """

from collections import deque

def bfs_cube(cube_table_answer) -> int:
    magic_cube = "12348765"
    cube_que = deque([magic_cube,])
    searchNum_que = deque([0,])
    beforeCmd_que = deque('0')
    while cube_que:
        temp_cube = cube_que.popleft()
        temp_searchNum = searchNum_que.popleft()
        temp_beforeCmd = beforeCmd_que.popleft()
        
        if temp_beforeCmd != 'A':
            temp_str = A_fuc(temp_cube)
            if temp_str == cube_table_answer:
                return temp_searchNum + 1
            else:
                cube_que.append(temp_str)
                searchNum_que.append(temp_searchNum + 1)
                beforeCmd_que.append('A')
        
        temp_str = B_fuc(temp_cube)
        if temp_str == cube_table_answer:
            return temp_searchNum + 1
        else:
            cube_que.append(temp_str)
            searchNum_que.append(temp_searchNum + 1)
            beforeCmd_que.append('B')
        
        temp_str = C_fuc(temp_cube)
        if temp_str == cube_table_answer:
            return temp_searchNum + 1
        else:
            cube_que.append(temp_str)
            searchNum_que.append(temp_searchNum + 1)
            beforeCmd_que.append('C')
        
        if temp_beforeCmd != 'D':
            temp_str = D_fuc(temp_cube)
            if temp_str == cube_table_answer:
                return temp_searchNum + 1
            else:
                cube_que.append(temp_str)
                searchNum_que.append(temp_searchNum + 1)
                beforeCmd_que.append('D')

                



if __name__ == "__main__":
    magic_cube_inp = "12348765"
    magic_cube_inp = list(magic_cube_inp)

    """     
    for i in range(4):
        magic_cube_inp[i] = input()
    
    for i in range(4):
        magic_cube_inp[-1 - i] = input() 
    """

    magic_cube_inp = input().split()
    temp = magic_cube_inp[4]
    magic_cube_inp[4] = magic_cube_inp[7]
    magic_cube_inp[7] = temp
    temp = magic_cube_inp[5]
    magic_cube_inp[5] = magic_cube_inp[6]
    magic_cube_inp[6] = temp 
    print(bfs_cube(''.join(magic_cube_inp)))


