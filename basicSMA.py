import numpy as np

a = np.arange(1000)

longPeriod=200
shortPeriod=40

# Calculate Simple Moving Average (SMA)
smaLongPeriod=np.nansum(a[-longPeriod:])/longPeriod
smaShortPeriod=np.nansum(a[-shortPeriod:])/shortPeriod
    
    