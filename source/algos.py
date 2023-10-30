import pygame
from maze import SearchSpace, Node
from const import *
from heapq import heappush, heappop
from collections import deque

def DFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement DFS algorithm')

    # Using deque for stack
    open_set = deque([g.start])
    closed_set = set()
    father = [-1]*g.get_length()
    
    while open_set:
        u = open_set.popleft()
        closed_set.add(u)
        u.set_color(BLUE, sc)
        
        if g.is_goal(u):
            nxt = u.id
            
            while father[nxt] != -1:
                prev = father[nxt]
                pygame.draw.line(sc, WHITE, g.grid_cells[nxt].rect.center, g.grid_cells[prev].rect.center)
                pygame.time.delay(10)
                pygame.display.update()
                nxt = prev
            return
        for v in g.get_neighbors(u):
            # not in closed_set: have not visited yet
            # not in open_set: avoid going to a cycle
            if v not in closed_set and v not in open_set:
                open_set.appendleft(v)
                father[v.id] = u.id
                v.set_color(RED, sc)
    
    raise NotImplementedError('not implemented')

def BFS(g: SearchSpace, sc: pygame.Surface):
    print('Implement BFS algorithm')

    # Using deque for a queue
    open_set = deque([g.start])
    closed_set = set()
    father = [-1]*g.get_length()
    
    while open_set:
        u = open_set.popleft()
        closed_set.add(u)
        u.set_color(BLUE, sc)

        if g.is_goal(u):
            nxt = u.id
            
            while father[nxt] != -1:
                prev = father[nxt]
                pygame.draw.line(sc, WHITE, g.grid_cells[nxt].rect.center, g.grid_cells[prev].rect.center)
                pygame.time.delay(10)
                pygame.display.update()
                nxt = prev
            return

        for v in g.get_neighbors(u):
            # not in closed_set: have not visited yet
            # not in open_set: avoid going to a cycle
            if v not in closed_set and v not in open_set:
                open_set.append(v)
                father[v.id] = u.id
                v.set_color(RED, sc)
                
    raise NotImplementedError('not implemented')

def UCS(g: SearchSpace, sc: pygame.Surface):
    print('Implement UCS algorithm')
    
    # Using heapq for a priority queue
    open_set = [(0, g.start.id)]
    father = [-1]*g.get_length()
    cost = [100_000]*g.get_length()
    cost[g.start.id] = 0
    
    while open_set:
        # take the lowest cost cell
        tmp, uId = heappop(open_set)
        u = g.grid_cells[uId]
        
        if tmp != cost[uId]:
            continue
        u.set_color(BLUE, sc)
        
        if g.is_goal(u):
            nxt = u.id
            
            while father[nxt] != -1:
                prev = father[nxt]
                pygame.draw.line(sc, WHITE, g.grid_cells[nxt].rect.center, g.grid_cells[prev].rect.center)
                pygame.time.delay(10)
                pygame.display.update()
                nxt = prev
            return
        
        for v in g.get_neighbors(u):
            if cost[v.id] > cost[uId] + 1:
                cost[v.id] = cost[uId] + 1
                father[v.id] = uId
                heappush(open_set, (cost[v.id], v.id))
                v.set_color(RED, sc)
    
    raise NotImplementedError('not implemented')

def AStar(g: SearchSpace, sc: pygame.Surface):
    print('Implement AStar algorithm')

    # Using heapq for a priority queue
    open_set = [(g.get_length() - 1, g.start.id)]
    father = [-1]*g.get_length()
    cost = [100_000]*g.get_length()
    cost[g.start.id] = 0
    # h function 
    h = [0] * g.get_length()
    
    for i in range (g.get_length()):
        if g.grid_cells[i].is_brick:  
            h[i] = float('inf')
        else: 
            h[i] = g.get_length() - i - 1
    
    while open_set:
        # take the lowest f() value cell
        tmp, uId = heappop(open_set)
        u = g.grid_cells[uId]
        
        if tmp != cost[uId] + h[uId]:
            continue
        
        u.set_color(BLUE, sc)
        
        if g.is_goal(u):
            nxt = u.id
            
            while father[nxt] != -1:
                prev = father[nxt]
                pygame.draw.line(sc, WHITE, g.grid_cells[nxt].rect.center, g.grid_cells[prev].rect.center)
                pygame.time.delay(10)
                pygame.display.update()
                nxt = prev
            return
        
        for v in g.get_neighbors(u):
            if cost[v.id] + h[v.id] > h[v.id] + cost[uId] + 1:
                cost[v.id] = cost[uId] + 1
                father[v.id] = uId
                heappush(open_set, (cost[v.id] + h[v.id], v.id))
                v.set_color(RED, sc)
    
    raise NotImplementedError('not implemented')
