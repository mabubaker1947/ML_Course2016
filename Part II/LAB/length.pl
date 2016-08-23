lengt([], N) :- N=0.
lengt([H|T], N) :-
        lengt(T, N1),
        N is N1+1.

reverse(L, RL) :-
        reverse(L, [], RL).
reverse([], RL, RL).
reverse([X|Xs], RLs, RL):-
        reverse(Xs, [X|RLs], RL).

reverseN2([X], [X]).
reverseN2([X|Xs], RL):-
        reverseN2(Xs, RLs),
        conc(X, RLs, RL).

conc(X, [], [X]).
conc(X, [Y|S], [Y|R]):-
        conc(X, S, R).
