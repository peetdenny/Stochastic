# Stochastic Modeling of Bitcoin prices using Monte Carlo prediction

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
![This is what it looked like on OSX, anyway](https://github.com/peetdenny/Stochastic/blob/master/imgs/Forcast1.png)
Graph showing how the price could fluctuate across time periods (here in 10 second intervals) based on historical trends and  stochastic fluctuations (as in Brownian motion)

## TODO

At first glance, this doesn't seem to model Bitcoin's very volatile price fluctuations.
Use an ML-style approach to testing and tuning; i.e. take 60% of the data as a 'training set', and use the other 40% (the more recent prices) as the _test set_.

## Challenges
The historical data available for free is not awesome.
The chaps at bitcoincharts have helpfully provided this stuff for free, but the sample is 'every few seconds', which ranges from sub-second to 15 seconds. This means that our predications are going to be a bit out of goose.

Also, the data is not necessarily up to date, and this implementation is pretty naive, so don't use the forcasted prices to plan your whole investment strategy :)

##Further reading

https://www.youtube.com/watch?v=3gcLRU24-w0 - this short video explains the maths behind what we're doing here with basic Brownian montecarlo
http://www.turingfinance.com/random-walks-down-wall-street-stochastic-processes-in-python/ - This excellent article goes into a lot more depth Brownian and why more sophisticated algorithms like Merton Jump and Heston are better models for financial modelling
