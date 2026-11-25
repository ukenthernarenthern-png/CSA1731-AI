% Best-first search using a heuristic score for each node.
edge(s, a). edge(s, b).
edge(a, c). edge(b, d).
edge(c, goal). edge(d, goal).
heuristic(s, 5). heuristic(a, 3). heuristic(b, 4).
heuristic(c, 1). heuristic(d, 2). heuristic(goal, 0).

best_first(Start, Goal, Path) :-
    heuristic(Start, H),
    search([H-[Start]], Goal, [], ReversePath),
    reverse(ReversePath, Path).

search([_-[Goal|Rest]|_], Goal, _, [Goal|Rest]) :- !.
search([_- [Node|Rest]|Frontier], Goal, Visited, Path) :-
    ( member(Node, Visited) ->
        search(Frontier, Goal, Visited, Path)
    ; findall(H-[Next,Node|Rest],
              (edge(Node, Next), \+ member(Next, Visited), heuristic(Next, H)),
              Children),
      append(Frontier, Children, Combined),
      keysort(Combined, Ordered),
      search(Ordered, Goal, [Node|Visited], Path)
    ).

% Query:
% ?- best_first(s, goal, Path).
