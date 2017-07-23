# Stochastic Modeling Demo using Monte Carlo prediction of Bitcoin prices

## Approach
To predict today's closing price ```st```, we take the previous day's closing price ```sy``` and raise multiply it by ```e^r```
where ```r``` is a long term _drift_ plus a random offset.

```st = sy * e^(drift + offset)```

To calculate the long term drift, we use the historical prices. In this demo, we're using the prices of Bitcoin, which are readily available from several sources.

We use daily data downloaded from: http://api.bitcoincharts.com/v1/csv/

## PDR - Periodic Daily Return 
```ln(Today's closing price / Yesterday's closing price)```

We use three other figures based on this PDR
* Mean
* Variance
* Standard Deviation


## Drift
This is calculated like so:
```mean - (variance/2)``` and represents the thrust of where the price is heading

## Stochastic offset
We're adding an offset to the drift. This is selected at random from within the normal distribution.
The ```ppf()``` (percent point function) from ```scipy.stats``` allows to us match an percentage of the area under the Gaussian distribution graph
to a standard deviation.
```stats.ppf(0.95)``` will return 1.645, which means that 1.645 standard deviations from the mean will contain 95% of the space


## Sample output
```
Yesterday's price was $2208/BTC
Price forecast for day +1 is $2206
Price forecast for day +2 is $2222
Price forecast for day +3 is $2220
Price forecast for day +4 is $2227
Price forecast for day +5 is $2227
Price forecast for day +6 is $2221
Price forecast for day +7 is $2234
Price forecast for day +8 is $2233
Price forecast for day +9 is $2237
```
