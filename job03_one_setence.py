import pandas as pd

# 영화 제목 하나에 모든 리뷰 넣기
df = pd.read_csv('./crawling_data/reviews_2015_2021.csv')

one_sentences = []
for title in df['title'].unique(): # 유니크로 만들어진 리스트를 포문 돌린다.
    temp = df[df['title'] ==  title] #컬럼에서 제목 1개만 데이터 프레임으로 만든다. 나중에 이 영화의 리뷰만 뽑아 내기 위함
    temp = temp['reviews'] #리뷰들만 데이터 프레임
    one_sentence = ' '.join(temp) # 하나의 문장으로 합친다.
    one_sentences.append(one_sentence) # 각 영화별로 리뷰가 하나로 묶여서 리스트안에 들어간다.

df_one_sentences = pd.DataFrame({'titles':df['title'].unique(), 'reviews':one_sentences})
print(df_one_sentences.head())
df_one_sentences.to_csv('./crawling_data/naver_movie_reviews_onesentence_2015_2021.csv', index=False)

