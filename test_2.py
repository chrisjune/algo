import sys
import os
# Complete the function below.

def electionWinner(votes):
    max=-1
    name = ''
    votes.sort()
    for i in range(len(votes)):
        cnt=votes.count(votes[i])
        if cnt>=max:
            name=votes[i]
            max = cnt
    return name

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    votes_cnt = 0
    votes_cnt = int(input())
    votes_i = 0
    votes = []
    while votes_i < votes_cnt:
        try:
            votes_item = str(input())
        except:
            votes_item = None
        votes.append(votes_item)
        votes_i += 1


    res = electionWinner(votes);
    f.write(res + "\n")


    f.close()