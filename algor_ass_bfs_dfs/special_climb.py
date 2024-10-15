#dfs 사용
# 올라가는 횟수와 내려가는 횟수는 각각 최대 높이 N번만 가능
from special_climb_function import dfs_climb, bfs_climb, dfs_climb_2
import sys
if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    climb_height, teacher_number = map(int, input().split())
    
    
    teacher_loc = [[False for i in range(climb_height + 1)] for j in range(climb_height * 2 + 1)]
    for i in range(teacher_number):
        temp_x, temp_y = map(int, input().split())
        teacher_loc[temp_x][temp_y] = True
    
    #print(teacher_loc[10][0])
    #print(dfs_climb(climb_height, teacher_loc, 0, 0, 0))
    #print(bfs_climb(climb_height, teacher_loc))
    print(dfs_climb_2(climb_height, teacher_loc, 0, 0))
    # 입력