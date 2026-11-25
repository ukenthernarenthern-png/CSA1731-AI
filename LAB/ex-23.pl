% Bird facts and a simple rule for birds that can fly.
bird(sparrow).
bird(eagle).
bird(penguin).
bird(ostrich).
flies(sparrow).
flies(eagle).
flightless(penguin).
flightless(ostrich).

can_fly(Bird) :-
    bird(Bird),
    flies(Bird),
    \+ flightless(Bird).

% Queries:
% ?- can_fly(sparrow).       % true
% ?- can_fly(penguin).       % false
% ?- can_fly(Bird).          % backtracks over birds that can fly
