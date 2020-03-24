# Cyprus Corona Virus

This repository will track the progress of the Corona virus in Cyprus with an aim to statistically link the measures taken by tge government to the cases. The data have been collected from news articles so if there are any errors please let me know. 

The measures taken by the Cyrpiot goverment was first to urge people to self isolate, which most were compliant, and then a week later a lockdown similar in nature to Greece was enforced. The aim of this repository is to see if there is any statistically significant change from the first to the second week. Since most experts say that at least a week is needed to tell if the measures have been effective the effects of the first week will not have been visible before the second set of measures was enforced. The question thus becomes whether or not the extra measures were needed or not.

To test this hypothesis data until the second week of April are needed. I will add daily updates for the predictions of the next day using  different models and by the end of March I will try to answer what is the correlation between the first set of measures and the number of new cases.

## March 24

The best (based on its R2 score) model fitting to the data was a GP followed by a linear model and finally an exponential model. Predictions using these models for the 245h of March were

GP: 
>  138.82 [134.4,143.2]  

New cases using GP  
> 10.65 [6.0,15.3]

> Prediction for tomorrow using exponential fit: 156.4  
> Prediction for tomorrow using Linear fit: 118.8

Note that the number of new cases predicted from the GP model is lower than the total number of cases predicted from another GP model. This is because the number of new cases every day is a much more noisy time series than the total number of cases. 

## March 23

The best (based on its R2 score) model fitting to the data was a GP followed by a linear model and finally an exponential model. Predictions using these models for the 24th of March were

> Tomorrow's prediction using GP model: 131.14   
> 95% Confidence interval: [127.01,135.26]

> Prediction for tomorrow using exponential fit: 141.61

> Prediction for tomorrow using Linear fit: 107.35

The total number of cases for March 24 was **124**, the best prediction was by the GP model. 

