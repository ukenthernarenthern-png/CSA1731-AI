% Family tree facts: parent(Parent, Child).
parent(john, mary).
parent(john, peter).
parent(mary, alice).
parent(mary, james).
parent(peter, sophia).
parent(alice, emma).

father(john, mary).
father(john, peter).
father(peter, sophia).
mother(mary, alice).
mother(mary, james).
mother(alice, emma).

sibling(X, Y) :- parent(P, X), parent(P, Y), dif(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Queries:
% ?- grandparent(john, Grandchild).
% ?- sibling(mary, Sibling).
% ?- ancestor(john, emma).
