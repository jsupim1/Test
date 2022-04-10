import itertools
import numpy as np


eps = 0.001;
eta = 0.25;
L = 20;
steps = 10**4;

def Initialize():

    Strategy = np.array([1/(2**(j+1)) for j in range(0,L)]);
    Strategy[L-1] = Strategy[L-2];
    print(sum(Strategy));

    return Strategy;

def EV(Strategy, StrategyOpp):

    EV = 0;
    for i in range(0, L):
        EV += Strategy[i]*sum(StrategyOpp[(i+1):])**2;
        EV += Strategy[i]*sum(StrategyOpp[0:i]**2);

    return EV;

Strategy = Initialize();

p = np.zeros((L,L))
for i in range(1, L):
    p[i][0] = 1;
    p[i][i] = -1;

for n in range(1, steps):
    Gradient = np.zeros(L);
    if n % 100 == 0: 
        print(Strategy[0:10]);
        print(EV(Strategy, Strategy));
    for i in range(1, L):
        Gradient[i] = EV(Strategy + eps*p[i], Strategy) - EV(Strategy, Strategy);

    Strategy[0] = Strategy[0] + (eta/eps)*sum(Gradient)/(n**0.33);
    for i in range(1, L):
        Strategy[i] = Strategy[i] - (eta/eps)*Gradient[i]/(n**0.33);
        if Strategy[i] < 0:
            Strategy[0] += Strategy[i];
            Strategy[i] = 0;

print(Gradient)
            
    

    

