blockSize =list(map(int,input('Enter Block Sizes: ').split()))
processes = list(map(int,input('Enter Proccesses: ').split()))
sort = sorted(blockSize)
Result = []
for i in range(len(processes)):
    for j in range(len(blockSize)):
        if sort[j] >= processes[i]:
            Result.append([i,blockSize.index(sort[j])])
            sort[j]-=processes[i]
            break
print('Process No\t\tProcess Size\t\t Block No.\t')
for x,y in Result:
    print(' ',x+1,'\t\t\t',processes[x],'\t\t\t',y+1)
print('\nRemaining Processes if any Are not Allocated to any block') 

