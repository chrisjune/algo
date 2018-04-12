def findpair(list,paired):
    cnt = 0
    tot = 0
    fin=True
    for i in range(0,4):
        if paired[i] == 0:
            fin = False
    if fin == True:
        return 1

    for x in range(0,4):
        for y in range(x+1,4):
            if list[x][y]==1 and paired[x]==0 and paired[y]==0:
                paired[x]=1
                paired[y]=1
                ret=findpair(list,paired)
                if ret != 0:
                    cnt+=ret
                    if tot<cnt:
                        tot=cnt
                        print(x,y,"/",ret,cnt)

                list[x][y]=0
                paired[x]=0
                paired[y]=0
    return cnt

arr=[
    [0,1,1,1],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,0]]
print(findpair(arr,[0,0,0,0]))