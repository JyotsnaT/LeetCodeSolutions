class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        

        def is_exit(x,y):
            print(x, y)
            if maze[x][y] == '.':
                if x == 0 or x == n-1 or y == 0 or y == m-1:
                    return True
            return False

        
        def bfs(a,b, dist_till_here):
            visited = [[False for i in range(m)] for j in range(n)]
            min_dist_to_exit = n*m
            exit_found = False
             
            maze_queue = deque()
            maze_queue.append([a,b,0])
            visited[a][b] = True
            
            while(len(maze_queue) > 0):

                popped_cell = maze_queue.popleft()
                x = popped_cell[0]
                y = popped_cell[1]
                dist_till_here = popped_cell[2]
                if is_exit(x,y):
                    if x == a and y == b:
                        print("point is same as entrance")
                    else:
                        exit_found = True
                        min_dist_to_exit = min(min_dist_to_exit, dist_till_here)
                        break
                if x>0 and not visited[x-1][y] and maze[x-1][y] == '.':
                    maze_queue.append([x-1,y,dist_till_here+1])
                    visited[x-1][y] = True
                if x<n-1 and not visited[x+1][y] and maze[x+1][y] == '.':
                    maze_queue.append([x+1,y,dist_till_here+1])
                    visited[x+1][y] = True
                if y>0 and not visited[x][y-1] and maze[x][y-1] == '.':
                    maze_queue.append([x,y-1,dist_till_here+1])
                    visited[x][y-1] = True
                if y<m-1 and not visited[x][y+1] and maze[x][y+1] == '.':
                    maze_queue.append([x,y+1,dist_till_here+1])
                    visited[x][y+1] = True
            return exit_found, min_dist_to_exit
 
        exit_found, min_dist_to_exit = bfs(entrance[0], entrance[1], 0)

        return min_dist_to_exit if exit_found else -1