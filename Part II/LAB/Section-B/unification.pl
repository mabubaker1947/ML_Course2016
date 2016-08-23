% SIMULA RESEARCH LABORATORY
% Author: A. Gotlieb
% Date: 11/8/2016
% Machine Learning crash course 22-25 Aug. 2016

%(* - very simple)

%?- t(X, b, Z) = t(a, Y, 4).
% X=a, Y=b, Z=4

%?- t(X, b, Z) = t(a, X, 4).
% No  (because X cannot be unified to both atoms a and b

%?- t(X, 1, p(Y, 3)) = t(a, Z, T).
% X=a, Z=1, T=p(Y,3)



%(** -  simple) 
%?- t(X, 1, p(X, 3)) = t(a, Y, Z).
% X=a, Y=1, Z=p(a,3)

%?- t(X, 1, p(X, 3)) = t(a, Y, p(Y, Z)).
% No (because X=a, Y=1, and X=Y are impossible) 

%?- t(X, T, p(X, 3)) = t(a, Y, Y).
% X=a, T=p(a,3), Y=p(a,3)


%(*** -  less simple) 
%?- X = p(X).
% X = p(p(p(p(...))))

%?- t(X, t(Y)) = t(p(Y), X).
% No (because X=p(...) and X=t(...) are impossible)

%?- t(X, t(Y)) = t(t(Y), X).
% X=t(Y)


%?- t(X, t(Y)) = t(t(Y), X), X = Y.
% X=t(t(t(...)))
% Y=t(t(t(...)))
