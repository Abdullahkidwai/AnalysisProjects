# -*- coding: utf-8 -*-
"""ScreenTimeAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lW4fWa7YJsEBpR594ZsSPiZPqNfgRerj
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv("Screentime-App-Details.csv")
print(data.head())

data.isnull().sum()

print(data.describe())

"""# Amount of usage of apps"""

figure = px.bar(data_frame=data,
                x="Date",
                y="Usage",
                color="App",
                title="Usage")
figure.show()

"""# Number of notifications from apps"""

figure = px.bar(data_frame=data,
                x="Date",
                y="Notifications",
                color="App",
                title="Notification")
figure.show()

"""# No of times apps opened"""

figure = px.bar(data_frame=data,
        x="Date",
        y="Times opened",
        color="App",
        title="Times opened")
figure.show()

"""# Realtionship between no of notifications and amount of usage """

figure = px.scatter(data_frame=data,
                x="Notifications",
                y="Usage",
                size="Notifications",
                trendline="ols",
                title="Relationship Between Number of Notifications and Usage")
figure.show()

