% Backward chaining: prove a goal from known facts and rules.
rule(mortal(X), [human(X)]).
rule(grandparent(X, Z), [parent(X, Y), parent(Y, Z)]).

prove(Goal, Facts) :-
    member(Goal, Facts).
prove(Goal, Facts) :-
    rule(Goal, Conditions),
    prove_all(Conditions, Facts).

prove_all([], _).
prove_all([Goal|Rest], Facts) :-
    prove(Goal, Facts),
    prove_all(Rest, Facts).

% Queries:
% ?- prove(mortal(socrates), [human(socrates)]).
% ?- prove(grandparent(ann, cara),
%          [parent(ann, bob), parent(bob, cara)]).
