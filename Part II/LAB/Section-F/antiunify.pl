:-use_module(library(terms)).

% * - very simple
go(T1, T2) :-
        term_subsumer(t(a,b,1), t(a,c,3), T1),
        term_subsumer(t(t(1),b,p(a,3)), t(t(2),a,p(b,3)), T2).

% ** - simple
go1(T1, T2, T3) :-
        term_subsumer(t(X,1,p(X,3)), t(a,3, p(Y,3)), T1),
        term_subsumer(t(X,p(b,3)), t(a,p(X,3)), T2),
        term_subsumer(t(X,p(a,3),p(a,3)), t(a,Y,Y), T3).

% *** - less simple
go2(T1, T2, T3) :-
        term_subsumer(X, p(X), T1),
        term_subsumer(t(X,t(X)), t(t(X),X), T2),
        term_subsumer(t(X,t(X)), t(X,t(X)), T3). 
