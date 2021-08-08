import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.Series(range(1,4))
df1 = pd.Series(range(0,3))
#print(df)
#print(df1)
print(df+df1)
#print(pd.__version__)
df2 = pd.Series([0,1,2],index=[0,2,1])
df3 = pd.Series([1,4,5,6],index=[1,2,0,3])
print(df2+df3)

df4 = pd.DataFrame(df+df1,[1])
print(df4)

#1
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\weather.csv")
print(df)

#2
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\aapl_no_dates.csv")
print(df)

#3
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
v=df["Temperature"].max()
print(v)
#4
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
v=df["EST"][df["Events"]=="Rain"]
print(v)

#5
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
v=df["WindDirDegrees"].mean()
print(v)

#6
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
rows,columns=df.shape
print(columns)

#7
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
print(df.head(2))
print(df.tail(3))

#8
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
print(df[2:7:] )

#9
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
print(df.columns)

#10
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
print(df["Temperature "])
#11
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
print(df[["DewPoint","CloudCover"]])

#12
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
v=df[df.Temperature>=40]
print(v)
#13
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\nyc_weather.csv")
v=df[df.Temperature==df["Temperature"].max()]
print(v)
#14
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather3.csv")
v=df.set_index('temperature')
print(v)
#15
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather3.csv")
v= df.set_index("date",inplace=True)
print(df.loc["5/3/2017"])

#16
import pandas as pd
n={
    "day":["1/1/2017","2/3/2018","8/2/2019"],
    "tem":[22,33,76],
    "windspeed":[8,4,2],
    "event":["snow","rain","sunny"]
}
d=pd.DataFrame(n)
print(d)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather3.csv",skiprows=1)
print(df)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(0)
print(new)


#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna({
    "temperature":0,
    "windspeed":1,
    "event":"no event"
})
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(method="ffill")
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna({
    "temperature":0,
    "windspeed":1,
    "event":"no event"
})
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(method="ffill")
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(method="bfill")
print(new)
#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(method="bfill",axis="columns")
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
new=df.fillna(method="ffill",limit=1)
print(new)

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
print(df.interpolate())

#
import pandas as pd
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather_data.csv")
s=df.dropna(thresh=3)
print(s)

#
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather.csv")
print(df.replace(65,np.NAN))

#
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather.csv")
print(df.replace([65,66],np.NAN))
#
import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather.csv")
print(df.replace({"temperature":68.0,
                  "humidity":60},np.NAN))
#import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\PRASHANTH\Desktop\Pand_test\\weather.csv")
print(df.replace("[A-Za-z]"," ",regex=True))
