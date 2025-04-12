import pandas as pd
import pandasql as sqldf
#import MysqlUtils as my

#print(pd.__version__)
import Utils.MysqlUtils

df = pd.read_excel(r'D:\pycharm professional\workSpace\PythonMLProject\MockData\test_data.xlsx')

Utils.MysqlUtils.write2DB(df=df,
            tableName="user_info",
            batchsize=100,
)