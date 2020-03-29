#TODO waffle charts with pandas

import pandas as pd 
import matplotlib as plt
from pywaffle import Waffle
df = pd.DataFrame({
    'crime_type': ['felony', 'misdemeanor', 'violation'],
    'number_of_cases': [54, 12, 8]
})
calculated = df.party.value_counts()
fig = plt.figure(
    FigureClass=Waffle, 
    rows=2, 
    values=list(calculated.values),
    labels=list(calculated.index)
)