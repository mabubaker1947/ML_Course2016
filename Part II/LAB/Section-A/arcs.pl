% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 11/8/2016
% Machine Learning crash course 22-25 Aug. 2016

arc(a, b).
arc(b, c).
arc(b, d).
arc(c, d).
arc(d, e).

path(X, X, [X]).
path(X, Y, [X|Path]) :- 
   arc(X, Z), 
   path(Z, Y, Path).


% ?- path(a,e, Path).
% ?- path(b, Y, Path).
% ?- path(X, e, Path).

% Generate all paths from a to e
% ?- path(a,e, Path), write(Path), nl, fail. 
