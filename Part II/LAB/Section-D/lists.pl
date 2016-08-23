% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 11/8/2016
% Machine Learning crash course 22-25 Aug. 2016

%(* - very simple)
lmember(X, [X|_]).
lmember(X, [Y|Ys]) :-
        X \= Y,
        lmember(X, Ys).

%| ?- lmember(3, [1,2,3]).
%yes
%| ?- lmember(4, [1,2,3]).
%no

%(** -  simple)
lappend([], L, L).
lappend([X|Xs], L, [X|L1]) :-
        lappend(Xs, L, L1).

%| ?- lappend([1,2,3], [4,5], L).
%L = [1,2,3,4,5] ? ;
%no


%(*** -  less simple)
myqs([], []).
myqs([X|Xs], Ys) :-
        partition(Xs, X, Left, Right),
        myqs(Left, Ls),
        myqs(Right, Rs),
        lappend(Ls, [X|Rs], Ys).

partition([], _Y, [], []).
partition([X|Xs], Y, [X|Ls], Rs) :-
        X =< Y,
        partition(Xs,Y,Ls,Rs).
partition([X|Xs], Y, Ls, [X|Rs]) :-
        X > Y,
        partition(Xs,Y,Ls,Rs).


% ?- myqs([9,3,7,2,1,6,6,0,6,4], L).
%L = [0,1,2,3,4,6,6,6,7,9] ?
