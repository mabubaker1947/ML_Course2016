arc(a, b).
arc(b, c).
arc(b, d).
arc(c, d).
arc(d, a).
arc(d, e).
arc(e, a).

path(X, X, [X]).
path(X, Y, [X|Path]) :- 
   arc(X, Z), 
   path(Z, Y, Path).
