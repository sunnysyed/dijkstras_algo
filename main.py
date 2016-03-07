from collections import defaultdict
from heapq import *
import collections


def readfile(fname):
	global edges
	with open(fname) as f:
		next(f)
		for line in f:
			l = line.split()
			edges.append((l[0], l[1], int(l[2])))
	
def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el

def findShortestPath(f, t):
    g = defaultdict(list)
    for node,to,dis in edges:
        g[node].append((dis,to))

    nodes, seen = [(0,f,())], set()
    while nodes:
        (dis,cur,path) = heappop(nodes)
        if cur not in seen:
            seen.add(cur)
            path = (cur, path)
            if cur == t: return (dis, path)

            for c, to in g.get(cur, ()):
                if to not in seen:
                    heappush(nodes, (dis+c, to, path))

    return "Graph is not connected"

if __name__ == "__main__":
	global edges
	edges = []
	print 'Case1.txt'
	readfile('Case1.txt')
	solution = list(flatten(findShortestPath("A", "B")))
	
	print solution[0]
	for i in reversed(solution[1:]):
		print i,
	edges = []
	print '\nCase2.txt'
	readfile('Case2.txt')
	solution = list(flatten(findShortestPath("A", "B")))
	
	print solution[0]
	for i in reversed(solution[1:]):
		print i,
	edges = []
	print '\nCase3.txt'
	readfile('Case3.txt')
	solution = list(flatten(findShortestPath("A", "B")))
	
	print solution[0]
	for i in reversed(solution[1:]):
		print i,
	