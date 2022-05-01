import queue as Q
def search(graph,start,end):
    if start not in graph:
        print('Invalid starting index')
        return
    if end not in graph:
        print('Invalid ending index')
        return
    queue=Q.PriorityQueue()
    queue.put((0,[start]))
    
    while(queue):
        node=queue.get()
        current=node[1][len(node[1]-1)]
        
        if end in node[1]:
            print("Path is found in"+str(node[1])+",Cost="+str(node[0]))
            break
        cost=node[0]
        for i in graph[current]:
            temp=node[1][:]
            temp.append(i)
            queue.append((cost+graph[current][i],temp))
            
graph={}
n=int(input('Enter the no of keys'));
for i in range(0,n):
    d={}    
    key=input('Enter the key')
    n1=int(input('Enter the no of keys for inner dict'))
    for j in range(0,n1):
        key2=input('Enter the inner key')
        cost=int(input('Enter the cost of the inner dict'))
        d[key2]=cost
    graph[key]=d
print(graph)
start=input('Enter the starting node')
end=input('Enter the final node')
search(graph,start,end)
