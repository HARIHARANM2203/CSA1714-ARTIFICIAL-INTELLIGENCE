from heapq import heappush, heappop

graph = {
    "Gate": {"Library": 120, "Canteen": 200},
    "Library": {"Gate": 120, "Lab": 150, "Hostel": 300},
    "Canteen": {"Gate": 200, "Hostel": 100, "Admin": 260},
    "Lab": {"Library": 150, "Auditorium": 350},
    "Hostel": {"Library": 300, "Canteen": 100, "Auditorium": 180},
    "Admin": {"Canteen": 260, "Auditorium": 120},
    "Auditorium": {"Lab": 350, "Hostel": 180, "Admin": 120}
}
h = {"Gate": 400, "Library": 330, "Canteen": 240, "Lab": 280,
     "Hostel": 160, "Admin": 110, "Auditorium": 0}

pq = [(h["Gate"], 0, "Gate")]
parent = {"Gate": None}
g = {"Gate": 0}
closed = set()

while pq:
    f, cost, node = heappop(pq)
    if node in closed:
        continue
    if node == "Auditorium":
        path = []
        cur = node
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print("Route:", " -> ".join(path))
        print("Distance:", g[node], "m")
        break
    closed.add(node)
    for nxt, road in graph[node].items():
        new_g = g[node] + road
        if new_g < g.get(nxt, float("inf")):
            g[nxt] = new_g
            parent[nxt] = node
            heappush(pq, (new_g + h[nxt], new_g, nxt))
