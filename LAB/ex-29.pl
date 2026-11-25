% Simple symptom-based educational diagnosis rules.
% This toy knowledge base is not a substitute for medical care.
symptom(patient1, sneezing).
symptom(patient1, sore_throat).
symptom(patient1, mild_cough).
symptom(patient2, fever).
symptom(patient2, body_ache).
symptom(patient2, cough).

possible_condition(Patient, common_cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, sore_throat).
possible_condition(Patient, flu_like_illness) :-
    symptom(Patient, fever),
    symptom(Patient, body_ache),
    symptom(Patient, cough).

% Queries:
% ?- possible_condition(patient1, Condition).
% ?- possible_condition(patient2, Condition).
