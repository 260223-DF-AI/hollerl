import pandas as pd
import datetime

import analysis
import visualizations
from analysis import clean_data
from visualizations import create_dashboard

df = analysis.load_data("orders.csv")
create_dashboard(clean_data(df), "graphs.png")