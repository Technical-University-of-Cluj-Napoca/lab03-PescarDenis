from utils import *
from collections import deque
from queue import PriorityQueue
from grid import Grid
from spot import Spot
import math
def bfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    if(start == None or end == None) : 
        return False

    Q = deque() #queue for bfs
    Q.append(start)

    visited =[]
    visited.append(start) #visited nodes
    came_from = {} #empty dictionary for reconstructing the path

    while (len(Q)!=0) :
        if(quit) : 
            pygame.quit
        curr = Q.popleft() #remove the element from the left
    #reconstruct the path
        if curr == end :# if we reached the end
            while curr in came_from : #check if the curr is in the constructing vector
                curr = came_from[curr] # go to the parent
                curr.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True
        for neighbor in curr.neighbors :
            if neighbor not in visited and not neighbor.is_barrier() :
                visited.append(neighbor)
                came_from[neighbor] = curr
                Q.append(neighbor)
                neighbor.make_open()
        draw()
        if(curr != start) :
            curr.make_closed()
    return False

def dfs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    if(start == None or end == None) : 
            return False

    stack =[]
    stack.append(start)

    visited =[]
    visited.append(start) #visited nodes
    came_from = {} #empty dictionary for reconstructing the path

    while (len(stack)!=0) :
            if(quit) : 
                pygame.quit
            curr = stack.pop()#remove the element from the left
        #reconstruct the path
            if curr == end :# if we reached the end
                while curr in came_from : #check if the curr is in the constructing vector
                    curr = came_from[curr] # go to the parent
                    curr.make_path()
                    draw()
                end.make_end()
                start.make_start()
                return True
            for neighbor in curr.neighbors :
                if neighbor not in visited and not neighbor.is_barrier() :
                    visited.append(neighbor)
                    came_from[neighbor] = curr
                    stack.append(neighbor)
                    neighbor.make_open()
            draw()
            if(curr != start) :
                curr.make_closed()
    return False

def h_manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:

    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def h_euclidian_distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
 
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))


def astar(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    count = 0
    open_heap = PriorityQueue()
    open_heap.put((0,count,start))
    came_from = {}
    g_score = {}
    for row in grid.grid:
        for spot in row :
            g_score[spot] = float('inf')
    g_score[start]= 0
    f_score = {}
    for row in grid.grid:
        for spot in row :
            f_score[spot] = float('inf')
    f_score[start] = h_euclidian_distance(start.get_position(),end.get_position())
    lookup_set = {start}

    while not open_heap.empty():
        # Allow quitting while running visualization
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_heap.get()[2]  # extract the Spot
        lookup_set.remove(current)

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            tentative_g = g_score[current] + 1  # cost between nodes = 1
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h_euclidian_distance(neighbor.get_position(), end.get_position())

                if neighbor not in lookup_set:
                    count += 1
                    open_heap.put((f_score[neighbor], count, neighbor))
                    lookup_set.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    # No path found
    return False




def dls(draw: callable, grid: Grid, start: Spot, end: Spot, limit: int) -> bool:
    if start is None or end is None:
        return False

    stack = [(start, 0)]
    visited = {start}
    came_from = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current, depth = stack.pop()

        if current == end:
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            end.make_end()
            start.make_start()
            return True

        if depth < limit:
            for neighbor in current.neighbors:
                if neighbor not in visited and not neighbor.is_barrier():
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    stack.append((neighbor, depth + 1))
                    neighbor.make_open()

            draw()

        if current != start:
            current.make_closed()

    return False

def ucs(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
   
    count = 0  
    open_heap = PriorityQueue()
    open_heap.put((0, count, start))
    came_from = {}
    g_score = {spot: float('inf') for row in grid.grid for spot in row}
    g_score[start] = 0
    lookup_set = {start}

    while not open_heap.empty():
        # Allow quitting while running visualization
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_heap.get()[2]
        lookup_set.remove(current)

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            start.make_start()
            end.make_end()
            return True


        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                if neighbor not in lookup_set:
                    count += 1
                    open_heap.put((g_score[neighbor], count, neighbor))
                    lookup_set.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False

def greedy_search(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
   
    
    count = 0  
    open_heap = PriorityQueue()
    h_start = h_euclidian_distance(start.get_position(), end.get_position())
    open_heap.put((h_start, count, start))
    
    came_from = {}
    
    visited = {start} 
    
    while not open_heap.empty():
        current = open_heap.get()[2]

        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                current.make_path()
                draw()
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor.is_barrier():
                continue
            
            if neighbor not in visited: 
                came_from[neighbor] = current
                h_neighbor = h_euclidian_distance(neighbor.get_position(), end.get_position())

                count += 1
                open_heap.put((h_neighbor, count, neighbor))
                visited.add(neighbor) 
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed() 

    return False

def ids(draw: callable, grid: Grid, start: Spot, end: Spot, max_depth: int) -> bool:
    if start is None or end is None:
        return False

    for depth in range(max_depth + 1):
        for row in grid.grid:
            for spot in row:
                if not spot.is_barrier() and spot != start and spot != end:
                    spot.reset()

        draw()

        found = dls(draw, grid, start, end, limit=depth)
        if found:
            return True

    return False


def ida_star(draw: callable, grid: Grid, start: Spot, end: Spot) -> bool:
    if start is None or end is None:
        return False

    threshold = h_manhattan_distance((start.row, start.col), (end.row, end.col))

    while threshold < float('inf'):
        for row in grid.grid:
            for spot in row:
                if not spot.is_barrier() and spot != start and spot != end:
                    spot.reset()

        stack = [(start, 0, [start])]
        min_exceeded = float('inf')

        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current, g_cost, path = stack.pop()

            f_cost = g_cost + h_manhattan_distance((current.row, current.col), (end.row, end.col))

            if f_cost > threshold:
                min_exceeded = min(min_exceeded, f_cost)
                continue

            if current == end:
                for node in path[1:-1]:
                    node.make_path()
                    draw()
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                if neighbor.is_barrier() or neighbor in path:
                    continue

                neighbor.make_open()
                stack.append((neighbor, g_cost + 1, path + [neighbor]))

            draw()

            if current != start:
                current.make_closed()

        threshold = min_exceeded

    return False


