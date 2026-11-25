% Fruit and color facts for demonstrating Prolog backtracking.
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(lemon, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).

% Queries:
% ?- fruit_color(Fruit, yellow).
% Fruit = banana ;
% Fruit = lemon.
%
% ?- fruit_color(Fruit, Color).
% Prolog returns another fruit/color pair whenever you type ;
% and backtracks to the next matching fact.
