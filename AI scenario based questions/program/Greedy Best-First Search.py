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

frontier = [(h["Gate"], "Gate", ["Gate"], 0)]
visited = set()
while frontier:
    _, node, path, distance = heappop(frontier)
    if node in visited:
        continue
    visited.add(node)
    if node == "Auditorium":
        print("Route:", " -> ".join(path))
        print("Distance:", distance, "m")
        break
    for nxt, cost in graph[node].items():
        if nxt not in visited:
            heappush(frontier, (h[nxt], nxt, path + [nxt], distance + cost))
