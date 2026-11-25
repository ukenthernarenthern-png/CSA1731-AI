% Towers of Hanoi: move N disks from Source to Destination using Auxiliary.
hanoi(0, _, _, _) :- !.
hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    Previous is N - 1,
    hanoi(Previous, Source, Auxiliary, Destination),
    format('Move disk from ~w to ~w~n', [Source, Destination]),
    hanoi(Previous, Auxiliary, Destination, Source).

% Query: ?- hanoi(3, left, right, center).
