'''
vader是专门对社交媒体进行情感分析的工具，目前支持英文文本以及UTF-8编码中的
emoji表情
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# vader is freely avaiable at https://github.com/cjhutto/vaderSentiment
import pandas as pd

def analyze(df):
    data=df.values.tolist()
    analyzer=SentimentIntensityAnalyzer()
    for element in data:
        vs=analyzer.polarity_scores(str(element[0])) # 对每行中待分析字段（假设index为1）进行分析
        element.append(str((vs['compound'])))
    return pd.DataFrame(data)

output_path=r" " # 输出文件路径（csv）
input_path=r" " # 输入文件路径（csv）
data=pd.read_csv(input_path) # dataframe

data=analyze(data)
data.columns=['sentence','emotion','grade'] # 修改csv表头
data.to_csv(output_path)
