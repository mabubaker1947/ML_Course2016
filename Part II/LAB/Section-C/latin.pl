% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 11/8/2016
% Machine Learning crash course 22-25 Aug. 2016

latin(B) :-
        B = [[A1,A2,A3], [B1,B2,B3], [C1,C2,C3]],
        label(A1),label(A2),label(A3),
        label(B1),label(B2),label(B3),
        label(C1),label(C2),label(C3),
        A1 \= A2, A1 \= A3, A2 \= A3,
        B1 \= B2, B1 \= B3, B2 \= B3,
        C1 \= C2, C1 \= C3, C2 \= C3,
        A1 \= B1, A1 \= C1, B1 \= C1,
        A2 \= B2, A2 \= C2, B2 \= C2,
        A3 \= B3, A3 \= C3, B3 \= C3.

label(1).
label(2).
label(3).


% (* -  very simple) 
%Using backtracking, write a program which successfully gives the value 1, 2 and 3 to a variable X? How to use it to populate a 3x3 latin-square?
% ?- label(X).

%(** -  simple) 
%Write a program which creates all 3x3 latin-squares through backtracking. How many are they?
% ?- latin(B).
% ?- latin(B), write(B), nl, fail.
% 12 3x3 latin squares by manual counting

% Automatic counting
% ?- retractall(val(_)), assert(val(0)), latin(B), write(B), write('  '), retract(val(N)), N1 is N+1, write(N1), asserta(val(N1)), nl, fail.

%(*** -  less simple) 
%Write a program which creates all NxN latin-squares through backtracking. 

:- use_module(library(lists)).
:- use_module(library(clpfd)).
% version using clpfd, N>0
latin(N, B) :-
        create_board_with_ctrs(N, B, LV),
        labeling([], LV).


create_board_with_ctrs(1, [1], [1]).
create_board_with_ctrs(2, [[A1,A2],[B1,B2]], [A1,A2,B1,B2]) :-
        domain([A1,A2,B1,B2], 1, 2),
        A1 #\= A2, B1 #\= B2, A1 #\= B1, A2 #\= B2.
create_board_with_ctrs(N, B, LV) :-
        N>2,
        cb_rec(N, N, B, [], LV),
        transpose(B, B1),
        ctr_rec(B1).

cb_rec(1,  N, [L], LV1, LV2) :-
        length(L, N),
        domain(L, 1, N),
        all_distinct(L),
        append(L, LV1, LV2).
cb_rec(N1, N, [L|Ls], LV1, LV3) :-
        N1 > 1,
        N2 is N1 - 1,
        length(L, N),
        domain(L, 1, N),
        all_distinct(L),
        append(L, LV1, LV2),
        cb_rec(N2, N, Ls, LV2, LV3).

ctr_rec([]).
ctr_rec([L|Ls]) :-
        all_distinct(L),
        ctr_rec(Ls).

% Automatic counting
% ?- retractall(val(_)), assert(val(0)), latin(4, B), write(B), write('  '), retract(val(N)), N1 is N+1, write(N1), asserta(val(N1)), nl, fail.
% 576
