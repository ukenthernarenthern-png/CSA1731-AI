% Simple database of people and their dates of birth.
% dob(Name, date(Year, Month, Day)).
dob("Asha", date(2003, 4, 12)).
dob("Bala", date(2002, 11, 3)).
dob("Chitra", date(2004, 7, 25)).
dob("Dinesh", date(2003, 1, 8)).

% Find a person's date of birth:
% ?- dob("Asha", Date).
% Date = date(2003, 4, 12).

% Find everyone born in a particular year:
born_in_year(Year, Name) :-
    dob(Name, date(Year, _, _)).
