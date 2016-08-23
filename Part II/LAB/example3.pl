man(socrates).
man(plato).
woman(judith).
greek(socrates).

mortal(X) :- man(X).
mortal(X) :- woman(X).

philosopher(X) :- mortal(X), greek(X).

count(_) :-
        assert(sol(0)),
        mortal(ANY),
        retract(sol(N)),
        N1 is N+1,
        assert(sol(N1)),
        fail.
count(Nb) :-
        retract(sol(Nb)).
