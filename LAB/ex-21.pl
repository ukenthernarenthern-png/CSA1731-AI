% A small database of planets in the Solar System.
% planet(Name, OrderFromSun, Type).
planet("Mercury", 1, terrestrial).
planet("Venus", 2, terrestrial).
planet("Earth", 3, terrestrial).
planet("Mars", 4, terrestrial).
planet("Jupiter", 5, gas_giant).
planet("Saturn", 6, gas_giant).
planet("Uranus", 7, ice_giant).
planet("Neptune", 8, ice_giant).

% Query examples:
% ?- planet(Name, 3, Type).
% Name = "Earth", Type = terrestrial.

% Retrieve all planets of a type:
planets_of_type(Type, Name) :-
    planet(Name, _, Type).
