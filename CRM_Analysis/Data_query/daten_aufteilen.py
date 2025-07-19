import pandas as pd

data=pd.read_csv('telco.csv')
df=pd.DataFrame(data)



df_territoryLookup=df[[
    'Country', 'State', 'City', 'Zip Code'
]]
df_territoryLookup = df_territoryLookup.drop_duplicates(subset=['Zip Code', 'City'], ignore_index=True)
df_territoryLookup['TerritoryKey'] = range(100, len(df_territoryLookup) + 100)
df = df.merge(df_territoryLookup, on=['Zip Code', 'City'], how='left')

df_customerLookup=df[[
    'TerritoryKey', 'Customer ID', 'Gender', 'Age', 'Under 30', 'Senior Citizen', 'Married',
    'Dependents', 'Number of Dependents'
]]


df_accountSubscription=df[[
    'Customer ID', 'Quarter', 'Tenure in Months', 'Offer', 'Contract',
    'Phone Service', 'Paperless Billing', 'Payment Method'
]]

df_referralLoyalty=df[[
    'Customer ID', 'Referred a Friend', 'Number of Referrals'
]]

df_servicesSubscribed=df[[
    'Customer ID', 'Multiple Lines', 'Internet Service', 'Internet Type',
    'Online Security', 'Online Backup', 'Device Protection Plan',
    'Premium Tech Support', 'Streaming TV', 'Streaming Movies',
    'Streaming Music', 'Unlimited Data'
]]

df_financials=df[[
    'Customer ID', 'Avg Monthly Long Distance Charges', 'Avg Monthly GB Download',
    'Monthly Charge', 'Total Charges', 'Total Refunds',
    'Total Extra Data Charges', 'Total Long Distance Charges', 'Total Revenue',
    'Satisfaction Score', 'Customer Status', 'Churn Label',
    'Churn Score', 'CLTV', 'Churn Category', 'Churn Reason'
]]




