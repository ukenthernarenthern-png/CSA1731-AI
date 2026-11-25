% Sum the integers from 1 to N.
% sum_to(+N, -Sum) accepts a non-negative integer N.
sum_to(0, 0).
sum_to(N, Sum) :-
    N > 0,
    Previous is N - 1,
    sum_to(Previous, Partial),
    Sum is Partial + N.

% Example query:
% ?- sum_to(5, Sum).
% Sum = 15.
