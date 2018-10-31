import matplotlib.pyplot as plt 
n = int(input("Enter number of Processes"))
bt=[]
ct=[]
wt=[]
for i in range(n):
    print("Enter Burst Time of process",i+1)
    bt.append(int(input()))
ct.append(bt[0])
for i in range(1,n):
    ct.append(bt[i]+ct[i-1])
tat = ct
for i in range(n):
    wt.append(tat[i]-bt[i])
print(bt)
plot=[]
for i in range(len(bt)):
    plot.append([x for x in range(bt[i]+1)])
for i in range(1,len(bt)):
    plot[i]=[x+plot[i-1][-1]-1 for x in range(1,bt[i]+2)]
for i in plot:
    plt.hist(i,1,label='Process'+str(plot.index(i)))
print(tat)
print("Average TurnAround Time is",sum(tat)/len(tat))
print("Average Waiting Time is",sum(wt)/len(wt))
plt.title("FCFS")
plt.legend()
plt.ylim(0,1)
plt.show()

