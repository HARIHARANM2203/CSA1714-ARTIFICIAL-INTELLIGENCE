
def alphabeta(values, alpha=float("-inf")):
    best_move = None
    best_value = float("-inf")
    scored = 0
    skipped = []

    for move_name, leaves in values:
        node_value = float("inf")
        beta = float("inf")

        for i, score in enumerate(leaves):
            scored += 1
            node_value = min(node_value, score)
            beta = min(beta, node_value)

            if beta <= alpha:
                skipped.extend(leaves[i + 1:])
                break

        if node_value > best_value:
            best_value = node_value
            best_move = move_name

        alpha = max(alpha, best_value)

    return best_move, best_value, scored, skipped


# Input values from Question 5
moves = [
    ("M1", [6, 9, 7]),
    ("M2", [4, 8, 10]),
    ("M3", [7, 5, 12])
]

# Call the function
move, value, scored, skipped = alphabeta(moves)

# Display the output
print("Chosen move:", move)
print("Value:", value)
print("Positions scored:", scored)
print("Skipped positions:", skipped)
