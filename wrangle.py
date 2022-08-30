
#imports
import pandas as pd
import numpy as np
import env
import os



#sql query
sql = """
SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount,fips
FROM properties_2017
WHERE propertylandusetypeid = 261

"""


# In[12]:


#connection set ip
def conn(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[16]:


#make function to acquire from sql
def new_zillow_data():
    df = pd.read_sql(sql,conn("zillow"))
    return df
def get_zillow_data():
    if os.path.isfile("zillow.csv"):
        df = pd.read_csv("zillow.csv", index_col = 0)
    else:
        df = new_zillow_data()
        df.to_csv("zillow.csv")
    return df


# In[ ]:




