import collections

#might need to create func to add edges or don need cos we have set map

def bfs(start_node, adj_list):

    #need to go learn how to explain this line lmao
    visited, queue = set(), collections.deque([start_node])
    visited.add(start_node)

    while queue:
        cur_node = queue.popleft()
        print(str(cur_node), end = " ")

        for neighbor in adj_list[cur_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



def main():
    
    #This part we change later and add the map
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(0, graph)

if __name__ == "__main__":
    main()

