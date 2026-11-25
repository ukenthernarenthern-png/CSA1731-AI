% Forward chaining over a small set of initial facts and rules.
initial_facts([human(socrates), parent(ann, bob), parent(bob, cara)]).

rule([human(X)], mortal(X)).
rule([parent(X, Y), parent(Y, Z)], grandparent(X, Z)).

satisfy([], _).
satisfy([Condition|Rest], Facts) :-
    member(Condition, Facts),
    satisfy(Rest, Facts).

derive(Facts, Conclusion) :-
    rule(Conditions, Conclusion),
    satisfy(Conditions, Facts),
    \+ member(Conclusion, Facts).

forward_chain(Facts, Closure) :-
    ( derive(Facts, NewFact) ->
        forward_chain([NewFact|Facts], Closure)
    ; Closure = Facts
    ).

% Query:
% ?- initial_facts(Facts), forward_chain(Facts, Closure).
