

graph={};
n=int(input("Enter the no of keys u want to enter"));
for i in range(0,n):
    d=[];
    key=int(input("Enter the key"));
    for j in range(0,n):
        choice=input("Do u want to continue?(y/n)");
        if(choice=='y'):
            n1=int(input("Enter the vlues for the list"));
            d.append(n1);
        else:
            break;
    graph[key]=d;
print(graph);
        
def bfs(graph,node):
    visited=[];
    queue=[];

    visited.append(node);
    queue.append(node);

    while(queue):
        m=queue.pop(0);
        print(m, end=" ");

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour);
                queue.append(neighbour);

start=int(input("Enter the node u want to start with:"));
bfs(graph,start);
