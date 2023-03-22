#Quick Sort
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left_arr=[i for i in arr[1:] if i<=pivot]
    right_arr=[i for i in arr[1:] if i>=pivot]
    #print(left_arr)
    #print(right_arr)
    return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)
arr=[30,20,50,40,10,20]
print(arr)
res=quick_sort(arr)
print(res)
#Breadth First Search in Graphs
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []    

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue:          
        m = queue.pop(0) 
        print (m, end = " ") 

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
        queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, '5')
