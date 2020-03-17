import urllib.request, json, datetime
import matplotlib.pyplot as plt

today = datetime.date.today()
date_time = today.strftime("%Y%m%d")
with urllib.request.urlopen("https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&name=SUSD&exchange=FREE&market=N&group=F&last=300&period=1440&intraPeriod=null&isLast=false&from=20150101000000&to=" + date_time + "235900") as url:
    data = json.loads(url.read().decode())
    print(data)

list = data["dataSet"]
val = [ sub['close'] for sub in list ]
date = [ sub['date'] for sub in list ]
date2 = [x / 1000 for x in date]
date3 = [int(x) for x in date2]
date4 = [datetime.datetime.fromtimestamp(x) for x in date3]
plt.style.use('fivethirtyeight')
plt.subplots(figsize = (20,10))
plt.plot(date4, val, label='Dolar/TL')
plt.ylabel('USDTRY')
plt.legend()
plt.xticks(rotation=45)

save_string = ("usdTRY_" + date_time + ".png")
plt.savefig(save_string)

urlUER = "https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&name=SEUR&exchange=FREE&market=N&group=F&last=300&period=1440&intraPeriod=null&isLast=false&from=20180508000000&to=20181108235900"
urlGBP = "https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&name=SGBP&exchange=FREE&market=N&group=F&last=300&period=1440&intraPeriod=null&isLast=false&from=20180508000000&to=20181108235900"
urlUSD = "https://web-paragaranti-pubsub.foreks.com/web-services/historical-data?userName=undefined&name=SUSD&exchange=FREE&market=N&group=F&last=300&period=1440&intraPeriod=null&isLast=false&from=20180508000000&to=20181108235900"


    
