from sqlalchemy import create_engine
import urllib
import daten_aufteilen as data

server = 'ramazanorsalsql.database.windows.net' 
database = 'crmdb'                 
username = 'ramazanorsaladmin'           
password = 'R.322655'                


# Bağlantı stringi oluştur
params = urllib.parse.quote_plus(
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server};"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)


engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


data.df_customerLookup.to_sql('CustomerLookup', engine, if_exists='replace', index=False)
data.df_territoryLookup.to_sql('TerritoryLookup', engine, if_exists='replace', index=False)
data.df_accountSubscription.to_sql('AccountSubscriptionLookup', engine, if_exists='replace', index=False)
data.df_referralLoyalty.to_sql('referralLoyalytyLookup', engine, if_exists='replace', index=False)
data.df_servicesSubscribed.to_sql('ServicesSubscribedLookup', engine, if_exists='replace', index=False)
data.df_financials.to_sql('FinancialLookup', engine, if_exists='replace', index=False)

print("✅ Veri Azure SQL'e gönderildi.")
