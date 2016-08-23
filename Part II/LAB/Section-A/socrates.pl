% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 11/8/2016
% Machine Learning crash course 22-25 Aug. 2016

man(socrates).
man(plato).

woman(judith).

mortal(X) :- man(X).
mortal(X) :- woman(X).

% Atoms: socrates, plato, judith
% Variables: X
% Terms: socrates, plato, judith, X
% Clauses: 5
% Predicates: 3  (man, woman, mortal)

% ?- mortal(plato).
% ?- mortal(judith).
% ?- mortal(omer).
% ?- mortal(ANY).


