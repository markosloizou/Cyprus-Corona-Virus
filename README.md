# Cyprus Corona Virus

This repository will track the progress of the Corona virus in Cyprus with an aim to statistically link the measures taken by tge government to the cases. The data have been collected from news articles so if there are any errors please let me know. 

The measures taken by the Cyrpiot goverment was first to urge people to self isolate, which most were compliant, and then a week later a lockdown similar in nature to Greece was enforced. The aim of this repository is to see if there is any statistically significant change from the first to the second week. Since most experts say that at least a week is needed to tell if the measures have been effective the effects of the first week will not have been visible before the second set of measures was enforced. The question thus becomes whether or not the extra measures were needed or not.

To test this hypothesis data until the second week of April are needed. I will add daily updates for the predictions of the next day using  different models and by the end of March I will try to answer what is the correlation between the first set of measures and the number of new cases.

# Correlation and Causality between measures and daily percentage increase of cases

There is some early hints that there is negative correlation between the govermental measures against the virus and the daily percentage increase in cases. Meaning that they measures do have some effect. However more data are neede for more concrete results. 

Granger's causality also seems to be statistically significant between the measures and the daily percentage increase. 


# SIR model

 SIR is a model mades up from 3 differential equations describing the rate of change of the number of susceptible , infected and recovered(meaning not susceptible or infected, this number includes the deceased). The solution of the model depends on the initial conditions and the transmitivity and recovery rate of the virus. The initial conditions used are the conditions in Cyprus when the outbreak begun. The transmitivity and recovery rate are optimized so that the solution of the system of equations represent the growth of the epidemic in Cyprus. Due to the limited amount fitting the parameters cannot be done accureately. 
 
 # Other Models
 
 Added another file comparing some basic models of growth. An exponential fit, a sigmoid fit and an epsilon exponential f(t)=a * e^( b*eps^(-ct) )
 
 ## March 31

GP: 
> 289.0 [283.1, 294.9]

GP New Cases:
> 23.8 [17.6,30.1]

>Prediction for tomorrow using exponential fit: 281.2

>Prediction for tomorrow using Linear fit: 222.2
 
## March 30

GP: 
> 254.4 [248.3, 260.4]

GP New Cases:
> 20.3 [13.9,36.7]

>Prediction for tomorrow using exponential fit: 249.9

>Prediction for tomorrow using Linear fit: 202.1

The total number of cases for March 31 was **262**, 32 new cases

## March 29

GP: 
> 247.9 [240.2, 253.8]

GP New Cases:
> 24.5 [18.2,30.7]

>Prediction for tomorrow using exponential fit: 224.6

>Prediction for tomorrow using Linear fit: 184.7

The total number of cases for March 30 was **230**, 16 new cases
 
 ## March 28

GP: 
> 189.9 [186.2, 193.5]

GP New Cases:
> 13.8 [9.3,18.3]

>Prediction for tomorrow using exponential fit:  196.1

>Prediction for tomorrow using Linear fit: 167.2

The total number of cases for March 29 was **214**, 35 new cases. Probably an outlier as a single person infected 15

## March 27

The R2 score of the exponential fit is now better than that of the Linear fit. 

GP: 
> 172.8 [169.2, 176.5]

GP New Cases:
> 12.0 [7.4,16.6]

>Prediction for tomorrow using exponential fit: 179.0

>Prediction for tomorrow using Linear fit: 153.7

The total number of cases for March 28 was **179**, 17 new cases

## March 26
GP: 
> 152.6 [148.1, 157.2]

GP New Cases:
> 10.3 [5.8,14.8]

>Prediction for tomorrow using exponential fit: 182.90

>Prediction for tomorrow using Linear fit: 141.2

The total number of cases for March 27 was **162**, 16 new cases


## March 25
GP: 
>139.0 [134.4,143.6]

GP New Cases:
> 9.2[4.7,13.7]

>Prediction for tomorrow using exponential fit: 168.7

>Prediction for tomorrow using Linear fit: 129.6


The total number of cases for March 26 was **146**, 14 new cases


## March 24

The best (based on its R2 score) model fitting to the data was a GP followed by a linear model and finally an exponential model. Predictions using these models for the 25h of March were

GP: 
>  138.82 [134.4,143.2]  

New cases using GP  
> 10.65 [6.0,15.3]

> Prediction for tomorrow using exponential fit: 156.4  
> Prediction for tomorrow using Linear fit: 118.8

Note that the number of new cases predicted from the GP model is lower than the total number of cases predicted from another GP model. This is because the number of new cases every day is a much more noisy time series than the total number of cases. 

The total number of cases for March 25 was **132**

## March 23

The best (based on its R2 score) model fitting to the data was a GP followed by a linear model and finally an exponential model. Predictions using these models for the 24th of March were

> Tomorrow's prediction using GP model: 131.14   
> 95% Confidence interval: [127.01,135.26]

> Prediction for tomorrow using exponential fit: 141.61

> Prediction for tomorrow using Linear fit: 107.35

The total number of cases for March 24 was **124**, the best prediction was by the GP model. 

