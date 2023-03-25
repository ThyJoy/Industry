import requests
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

response = requests.get('https://kav-api.kovalev.team/servodrive/lastActualData?servoDriveId=1')
print(response.json())
print(response.json()[0]["date"])
#print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
#print(datetime.strftime("%Y-%m-%d %H:%M"))

Velocity = response.json()[0]["actVelocity"].replace(",",".")
U = response.json()[0]["actPhaseU"].replace(",",".")
V = response.json()[0]["actPhaseV"].replace(",",".")
OutCurrent = response.json()[0]["actOutCurrent"].replace(",",".")

x = ["actVelocity", "actOutCurrent", "actPhaseU", "actPhaseV"]
y = [float(Velocity), float(OutCurrent), float(U), float(V)]

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()