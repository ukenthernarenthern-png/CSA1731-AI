% A small state-space model of the Monkey and Banana problem.
% State is state(MonkeyPosition, BoxPosition, MonkeySupport, HasBanana).
action(state(door, corner, floor, no), walk_to_box,
       state(corner, corner, floor, no)).
action(state(corner, corner, floor, no), push_box_to_middle,
       state(middle, middle, floor, no)).
action(state(middle, middle, floor, no), climb_box,
       state(middle, middle, on_box, no)).
action(state(middle, middle, on_box, no), grasp_banana,
       state(middle, middle, on_box, yes)).

solve(State, Goal, Plan) :- plan(State, Goal, [State], Plan).
plan(Goal, Goal, _, []) :- !.
plan(State, Goal, Visited, [Action|Rest]) :-
    action(State, Action, Next),
    \+ member(Next, Visited),
    plan(Next, Goal, [Next|Visited], Rest).

% Query:
% ?- solve(state(door, corner, floor, no),
%          state(middle, middle, on_box, yes), Plan).
