man(socrates).
man(plato).
woman(judith).
greek(socrates).

mortal(X) :- man(X).
mortal(X) :- woman(X).

philosopher(X) :- mortal(X), greek(X).
