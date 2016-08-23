% Example of weather forecast
% Weather forecast with the following attributes: 
%outlook,          with values {sunny, overcast, rain} 
%temperature, with values {cool, mild, hot} 
%humidity,        with values {high, normal}
%windy,             with values { true, false}

%Let suppose that we have only two values for classifying a set of data: either P(positive) or N(negative). For example, P means that the combination of attributes is possible (as already been observed), while N means that the combination has never been observed. 

%Let S be the following training set:
%1   sunny hot high false          N 
%2   sunny hot high true           N 
%3   overcast hot high false       P 
%4   rain mild high false          P 
%5   rain cool normal false        P 
%6   rain cool normal true         N 
%7   overcast cool normal true     P 
%8   sunny mild high false         N 
%9   sunny cool normal false       P 
%10  rain mild normal false        P 
%11  sunny mild normal true        P 
%12  overcast mild high true       P 
%13  overcast hot normal false     P 
%14  rain mild high true           N 

% Examples of possible decision trees

outlook( sunny(
               humidity(
                        high(negative),
                        normal(positive)
                       ),
         overcast(positive),
         rain(
              windy(
                    true(negative),
                    false(positive)
             )
       )


% The "decision" predicate takes as inputs the list of attributes, the classes and the list of numbers of the training set
% It outputs DECTREE which is a decision tree associated to the data
              
%Inputs:
% Argument 1
% [ att(outlook,     v(sunny, [1,2,8,9,11]),     v(overcast, [3,7,12,13]),   v(rain, [4,5,6,10,14])),
%   att(temperature, v(cool, [5,6,7,9]),         v(mild, [4,8,10,11,12,14]), v(hot, [1,2,3,13])),
%   att(humidity,    v(high, [1,2,3,4,8,12,14]), v(normal, [5,6,7,9,10,11,13]))
%   att(windy,       v(true,[2,6,7,11,12,14]),   v(false, [1,3,4,5,8,9,10,13]))
% ]
%              
% Argument 2
%   [v(positive,[3,4,5,7,9,10,11,12,13]), v(negative, [1,2,6,8,14])]
%
% Argument 3
%   [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

decision([], CLASSES, DATASET, CLASSES).
decision(ATTs, CLASSES, DATASET, CL) :-
        included(DATSET, CLASSES, CL),
        !.
decision([ATT|ATTs], CLASSES, DATASET, DECTREE) :-
        DECTREE =.. [NAME, BR1, BR2],
        ATT = att(NAME, v(VAL1, L1), v(VAL2, L2)),
        decision(ATTs, CLASSES, L1, BR1),
        decision(ATTs, CLASSES, L2, BR2).
