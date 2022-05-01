graph={}
n=int(input('Enter the no of keys u want to enter'))
for i in range(0,n):
    d=[]
    key=(input('Enter the key'))
    for j in range(0,2):
        choice=input('do u want to continue?');
        if(choice=='y'):
            n1=(input('Enter the values'))
            d.append(n1)
        else:
            break;  
    graph[key]=d
    print(graph)
visited=[]
def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph);
start=input("Enter the node with which u want to start:")
print("The dfs path is:")
dfs(start,visited,graph)