import matplotlib.pyplot as plt
import monty.StochasticModeler as modeler

forecasts = modeler.forecast(1000, 100)
plt.style.use(['bmh'])
for f in forecasts:
    plt.plot(f)
plt.ylabel('Price ($/BTC)')
plt.xlabel('Period (Yesterday +n)')
plt.show()
