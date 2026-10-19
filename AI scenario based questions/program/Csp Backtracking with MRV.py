slots = ["Morning", "Afternoon", "Evening"]
conflicts = {
    "W1": {"W2", "W3"},
    "W2": {"W1", "W3", "W4"},
    "W3": {"W1", "W2", "W5"},
    "W4": {"W2", "W5"},
    "W5": {"W3", "W4"}
}
domains = {
    "W1": slots[:], "W2": slots[:],
    "W3": ["Afternoon", "Evening"],
    "W4": ["Morning", "Afternoon"],
    "W5": slots[:]
}
assignment = {}

def backtrack():
    if len(assignment) == len(domains):
        return True
    unassigned = [w for w in domains if w not in assignment]
    # MRV, then highest degree among unassigned neighbours, then workshop number
    def key(w):
        legal = [s for s in domains[w]
                 if all(assignment.get(n) != s for n in conflicts[w])]
        degree = sum(n not in assignment for n in conflicts[w])
        return (len(legal), -degree, int(w[1:]))
    w = min(unassigned, key=key)
    for s in slots:
        if s not in domains[w]:
            continue
        if all(assignment.get(n) != s for n in conflicts[w]):
            assignment[w] = s
            if backtrack():
                return True
            del assignment[w]
    return False

if backtrack():
    for w in sorted(assignment, key=lambda x: int(x[1:])):
        print(w, "=", assignment[w])
else:
    print("No valid timetable exists.")
