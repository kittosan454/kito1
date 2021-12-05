import pandas as pd

# df = pd.read_csv('./crawling_data/reviews_2021.csv')
# df.info()
#
# for i in range(21,54):
#     df_temp = pd.read_csv('./crawling_data/reviews_2017_{}.csv'.format(i)) # 다음데이터부터 보여준다.
#     df_temp.dropna(inplace=True)
#     df_temp.drop_duplicates(inplace=True) # 중복제거
#     df_temp.columns = ['title', 'reviews']
#     df_temp.to_csv('./crawling_data/reviews_2017_{}.csv'.format(i), index=False) #다시저장
#     df = pd.concat([df, df_temp], ignore_index=True) # 중복인덱스 방지
#
#
# df.info()
#
# df.to_csv('./crawling_data/reviews_2017_(21-53).csv', index=False)

df= pd.DataFrame()
lst = [2015,2016,2017,2018,2019,2020,2021]
for i in lst:
    df_temp = pd.read_csv('./crawling_data/reviews_{}.csv'.format(i)) # 다음데이터부터 보여준다.
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True) # 중복제거
    df_temp.columns = ['title', 'reviews']
    df_temp.to_csv('./crawling_data/reviews_{}.csv'.format(i), index=False) #다시저장
    df = pd.concat([df, df_temp], ignore_index=True) # 중복인덱스 방지


df.drop_duplicates(inplace=True) # 중복제거
df.info()
df.to_csv('./crawling_data/reviews_2015_2021.csv', index=False)

