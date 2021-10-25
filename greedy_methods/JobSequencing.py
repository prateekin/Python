class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
    

# job sequencing function
def jobSequencing(jobs):
    jobs = sorted(jobs, key= lambda x: x.profit, reverse=True)
    totalProfit = 0
    result = [0 for x in range(0, len(jobs))]
    slot  = [False for x in range(0, len(jobs))]
    for i in range(len(jobs)):
        for j in range(min(len(jobs),jobs[i].deadline) -1 , -1, -1):
            if slot[j] == False:
                result[j] = i
                slot[j] = True
                totalProfit += jobs[i].profit
                break
            
    print(f"The total profit obtained : Rs {totalProfit}")
    print("The Order of jobs is : ", end=" ")
    for k in range(len(jobs)):
        if slot[k] == True:
            print(jobs[result[k]].id, end=" ")

# main function
jobs = [Job('a', 2, 100), Job('b', 1 , 19), Job('c', 2, 27), Job('d', 1, 25), Job('e', 3, 15)]
jobSequencing(jobs)