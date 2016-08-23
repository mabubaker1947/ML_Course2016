% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 12/8/2016
% Machine Learning crash course 22-25 Aug. 2016

%(* - very simple)
label(1).
label(2).
label(3).

% ?- label(X), label(Y), label(Z), write((X,Y,Z)), nl, fail.

%(** -  simple)

% ?- path(a,e,Path), write(Path), fail. % does not terminate!
% Simplest strategy: to limit the size of path with an arbitrary parameter K

label_paths(K) :-
        K > 0,
        retractall(val(_)),
        assert(val(0)),
        path(a, a, Path, K),
        write(Path),
        retract(val(N)),
        write('  '), write(N),
        N1 is N+1,
        asserta(val(N1)),
        nl,
        fail.

path(X, Y, [], 0):-
        X \= Y,
        fail.
path(X, X, [X], K):-
        K > 0.
path(X, Y, [X|Path], K1) :-
        K1 > 0,
        arc(X, Z),
        K2 is K1-1,
        path(Z, Y, Path, K2).

% ?- label_paths(10).   % There are 20 paths

%(*** -  less simple)
label_paths_max(K) :-
        K > 0,
        retractall(val(_)),
        assert(val(0)),
        path(a, a, Path, K),
        compute_a(Path, 0, Nba1),
        retract(val(Nba0)),
        (Nba1 > Nba0 -> asserta(val(Nba1)) ; asserta(val(Nba0) ) ),
        fail.
label_paths_max(_K) :-
        retract(val(Nba)),
        write(Nba),
        nl.

compute_a([], N, N).
compute_a([a|S], N1, N3) :-
        N2 is N1+1,
        compute_a(S, N2, N3).
compute_a([X|S], N1, N3) :-
        X \== a,
        compute_a(S, N1, N3).

% ?- label_paths_max(30).
% 10
% yes
% source_info
% | ?- label_paths_max(40).
% 14
% yes
% source_info
% | ?- label_paths_max(50).
% 17
