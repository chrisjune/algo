list=[[1,0,0,0,0,0,1],
      [1,0,0,0,0,0,1],
      [1,1,0,0,1,1,1]]
    
coverType=[[[0,0],[0,1],[1,0]],
           [[0,0],[0,1],[1,1]],
           [[0,0],[1,0],[1,1]],
           [[0,0],[1,0],[1,-1]]]

def set(board,x,y,type,delta):
    ret = True
    for i in range(0,3):
        ny=coverType[type][i][0] + y
        nx=coverType[type][i][1] + x

        if nx >= len(board[0]) or ny >= len(board) or ny<0 or nx <0 :
            ret = False
            break
        if board[ny][nx] >= 1 :
            ret = False
        board[ny][nx] += delta
    return ret



def cover(board):
    x = -1
    y = -1
    cnt=0
    ret=0
    for j in range(0,len(board)):
        for i in range(0,len(board[0])):
            if board[j][i] ==0:
                cnt+=1
    if cnt==0:
        return 1

    for j in range(0,len(board)):
        for i in range(0,len(board[0])):
            if board[j][i]==0 :
                x = i
                y = j

                for k in range(0,4):
                    if set(board,x,y,k,1):
                        ret= ret + cover(board)
                    set(board,x,y,k,-1) 
    return ret

print(cover(list))