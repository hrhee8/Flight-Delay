# Flight Delay Project (Data Analysis via Python)


Calculated the probability of flight being delayed with multiple variables, using decision tree method


•  Implementation of Naive-Bayes Classifier 


     P(Ck|X) = P(Ck) * P(X|Ck) / P(X)

     where Ck is a classifier of whether the flight is delayed or not

     P(Ck|X) ∝ P(Ck) * ∏ P(xi|Ck) #series multiplication from i = 1 to n


•  Maximum a Posterior rule (MAP)

     yhat = argmax P(Ck) * ∏ P(xi|Ck) #argmax of k
     
     
•  QQ plot
     
     Used QQ plot to compare the resultant with the distribution

