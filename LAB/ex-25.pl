% Illustrative educational diet suggestions by condition.
% These rules are examples for learning Prolog, not medical advice.
diet_for(diabetes, ["balanced meals", "vegetables", "water"]).
diet_for(hypertension, ["vegetables", "fruit", "lower-salt choices"]).
diet_for(common_cold, ["warm fluids", "soups", "water"]).

suggest_diet(Condition, Foods) :-
    diet_for(Condition, Foods).

% Query:
% ?- suggest_diet(hypertension, Foods).
% Foods = ["vegetables", "fruit", "lower-salt choices"].
