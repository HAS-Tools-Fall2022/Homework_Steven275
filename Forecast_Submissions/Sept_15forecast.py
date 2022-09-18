#%%
import numpy as np 

filename =('https://raw.githubusercontent.com/HAS-Tools-Fall2022' 
          '/Course-Materials22/main/data/verde_river_daily_flow_cfs.csv')
flows = np.loadtxt(
    filename, # The location of the text file
    delimiter=',', # character which splits data into groups
    usecols=1 # Just take column 1, which is the flows
)
print(flows) 
#%%
np.mean(flows)
# %%
first week =np.mean flows[]
# %%
np.len(flows)

# %%
print(len(flows))
# %%
last_day_of_flows=flows[-1]
print(last_day_of_flows)
# %%
flows[-2]
# %%
flows[-7]

# %%
last_week_of_flows=np.mean(flows[-7:])
# %%
week_1_prediction=np.mean(last_week_of_flows)
week_1_prediction

# %%
flows[-7:-1]
# %%
last_week_of_flows
# %%
flows[7:14]
# %%
flows[-14:-7]
# %%
second_to_last_week_of_flows=flows[-14:-7]
# %%
week_2_prediction=np.mean(second_to_last_week_of_flows)
week_2_prediction
# %%
print(week_1_prediction, ',', week_2_prediction)
# %%
