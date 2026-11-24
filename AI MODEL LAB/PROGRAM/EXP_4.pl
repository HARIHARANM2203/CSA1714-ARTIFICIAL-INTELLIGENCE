
% Connected City Facts
connected(chennai, bangalore).
connected(chennai, coimbatore).
connected(bangalore, hyderabad).
connected(bangalore, mysore).
connected(coimbatore, madurai).
connected(mysore, hyderabad).
connected(madurai, hyderabad).

% Bidirectional road connection
road(X, Y) :-
    connected(X, Y).

road(X, Y) :-
    connected(Y, X).

% Main DFS predicate
dfs(Start, Goal, Path) :-
    travel(Start, Goal, [Start], ReversePath),
    reverse(ReversePath, Path).

% Base case
travel(Goal, Goal, Visited, Visited).

% Recursive case
travel(Current, Goal, Visited, Path) :-
    road(Current, Next),
    \+ member(Next, Visited),
    travel(Next, Goal, [Next|Visited], Path).
