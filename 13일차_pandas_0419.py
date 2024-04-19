import pandas as pd

campaign_m = pd.read_csv('D:\Windows_user\Documents\카카오톡 받은 파일\판다스 실습파일\campaign_master.csv')
class_m = pd.read_csv('D:\Windows_user\Documents\카카오톡 받은 파일\판다스 실습파일\class_master.csv')
customer_m = pd.read_csv('D:\Windows_user\Documents\카카오톡 받은 파일\판다스 실습파일\customer_master.csv')
use_l = pd.read_csv(r'D:\Windows_user\Documents\카카오톡 받은 파일\판다스 실습파일\use_log.csv')

campaign_m.groupby('campaign_id')
# print(campaign_m.groupby('campaign_id'))

