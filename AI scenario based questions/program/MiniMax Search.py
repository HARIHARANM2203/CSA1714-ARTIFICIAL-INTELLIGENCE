# Two X moves; each has two O replies; each reply has two X outcomes.
tree = [
    [[4, 7], [8, 2]],  # X first move 1
    [[3, 5], [6, 9]]   # X first move 2
]
root_values = []
for x_move in tree:
    o_values = [max(final_scores) for final_scores in x_move]
    root_values.append(min(o_values))
    print("O reply values:", o_values, "=> X move value:", min(o_values))
best_move = root_values.index(max(root_values)) + 1
print("Best first move:", best_move)
print("Guaranteed score:", max(root_values))
