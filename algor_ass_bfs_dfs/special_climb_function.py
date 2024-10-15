# dfs 사용
# 올라가는 횟수와 내려가는 횟수는 각각 최대 높이 N번만 가능
# N = climb_heigh
# 최종 결과에서는 up = N , down = N 이어야 함.
# up은 항상 down보다 크거나 같음.

def dfs_climb(climb_height : int, teacher_loc, up : int, down : int, biggest_climb : int) -> int:
    if up == climb_height and down == climb_height: 
        return biggest_climb
    temp1, temp2 = -1, -1
    if up - down < climb_height and up < climb_height and teacher_loc[up + down + 1][up - down + 1] == False: # 위로 올라갈 때 선생이 없다면 dfs 정상 진행
        
        if(biggest_climb < up - down + 1):
            temp1 = dfs_climb(climb_height, teacher_loc, up + 1, down, up - down + 1)

        else:
            temp1 = dfs_climb(climb_height, teacher_loc, up + 1, down, biggest_climb)
    
    if up - down > 0 and down < climb_height and teacher_loc[up + down + 1][up - down - 1] == False:
         temp2 = dfs_climb(climb_height, teacher_loc, up, down + 1, biggest_climb)
    if up - down == 0 and teacher_loc[up + down + 1][up - down + 1] == True:
        return -1
    if (up - down < climb_height and teacher_loc[up + down + 1][up - down + 1] == True) and (up - down > 0 and teacher_loc[up + down + 1][up - down - 1] == True):
        return -1
    if temp1 > temp2: return temp1
    else: return temp2

# 올라가는 횟수와 내려가는 횟수는 각각 최대 높이 N번만 가능
# N = climb_heigh
# 최종 결과에서는 up = N , down = N 이어야 함.
# up은 항상 down보다 크거나 같음.
from collections import deque

# up - down == 현재 높이
# up == climb_height and down climb_height 일 경우 더 이상 이동 불가
# up <= climb_height, down <= climb_height 
# up - down == 0일 때, down 불가능
# up - down == climb_height 일 때, up 불가능

# curUpDown[0] == up
# curUpDown[1] == down

# x좌표 == up + down
# y좌표 == up - down
# 항상 up은 down보다 큼. 

# 올라갈 수 있는 상황이면 무조건 올라감
# 올라갈 수 없는 경우일 경우만 내려감
# 현재 상태에서 최대 가능한 높이 = climb_height - down
def bfs_climb(climb_height : int, teacher_loc) -> int:

    curUpDown = deque([[0,0]])
    biggestHeight = -1

    while curUpDown:
        temp_updown = curUpDown.popleft()
        #print(temp_updown)
        if temp_updown[0] < climb_height:
            # 올라가는 경우
            if temp_updown[0] - temp_updown[1] < climb_height:
                if teacher_loc[temp_updown[0] + temp_updown[1] + 1][temp_updown[0] - temp_updown[1] + 1] == False:
                    curUpDown.append([temp_updown[0] + 1, temp_updown[1]])
                    if biggestHeight < temp_updown[0] - temp_updown[1] + 1:
                        biggestHeight = temp_updown[0] - temp_updown[1] + 1

        if temp_updown[1] < climb_height:
            # 내려가는 경우
            if temp_updown[0] - temp_updown[1] > 0:
                if teacher_loc[temp_updown[0] + temp_updown[1] + 1][temp_updown[0] - temp_updown[1] - 1] == False:
                    curUpDown.append([temp_updown[0], temp_updown[1] + 1])
                    if biggestHeight < temp_updown[0] - temp_updown[1] - 1:
                        biggestHeight = temp_updown[0] - temp_updown[1] - 1
                
        
    return biggestHeight

biggestHeight = -1
temp_big = -1
def dfs_climb_2(climb_height : int, teacher_loc, up : int, down : int) -> int:
    global biggestHeight
    global temp_big
    if temp_big < up - down:
        temp_big = up - down
    
    #print(biggestHeight)
    
    
    if climb_height - down <= biggestHeight:
        return biggestHeight
    
    #print(temp_updown)
    if up < climb_height:
        # 올라가는 경우
        if up - down < climb_height: # 현재 높이가 최대(climb_height)가 아닐 경우
            if teacher_loc[up + down + 1][up - down + 1] == False:
                
                    biggestHeight = dfs_climb_2(climb_height, teacher_loc, up + 1, down) 

    if down < climb_height:
        # 내려가는 경우
        if up - down > 0:
            if teacher_loc[up + down + 1][up - down - 1] == False:
                
                    biggestHeight = dfs_climb_2(climb_height, teacher_loc, up, down + 1)
            
    if up == climb_height and down == climb_height:
        biggestHeight = temp_big 
        return biggestHeight
    else:
        temp_big = -1
        return biggestHeight
    