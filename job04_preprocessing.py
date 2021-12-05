import pandas as pd
from konlpy.tag import Okt
import konlpy
import re


df = pd.read_csv('./crawling_data/cleaned_review_2015_2021.csv')
# print(df.head())

# from konlpy.tag import Komoran
# komoran = Komoran(max_heap_size= 1024 * 6) # 반드시 전역 변수에서 한번만 실행하자
# def konlpy_morp_analy(text):
# 	try:
# 		result = komoran.pos(text)
# 	except Exception as e:
# 		return None
# 	return result
stopwords = pd.read_csv('./crawling_data/naver_movie_reviews_onesentence_2015_2021.csv', index_col = 0)
stopwords.info()
cleaned_sentences = []
# for cleaned_sentence in df2.cleaned_sentences:
#     cleaned_sentence_words = cleaned_sentence.split()
#     words =[]
#     for word in cleaned_sentence_words:
#         if word not in list(stopwords['stopword']):
#             words.append(word)
#     cleaned_sentence = ' '.join(words)
#     cleaned_sentences.append(cleaned_sentence)
# df2['cleaned_sentences'] = cleaned_sentences
# df2.to_csv('./crawling_data/cleaned_review_2015_2021.csv', index=False)
# exit()
okt =Okt()


count = 0

for sentence in df.reviews: # df['reviews']와 같다.
    count +=1
    if count % 10 == 0:
        print('a', end='')
    if count % 100 ==0:
        print()

    sentence = re.sub('[^가-힣 ]', '', sentence)
    token = okt.pos(sentence, stem=True) # 품사랑 형태소랑 쌍으로 묶어준다. stem 값을 True로 주면 용언(동사, 형용사, 보조용언이 속한다. 변하지 않는 부분인 어간과 변하는 부분인 어미로 구성된다.)의 형태소가 어간으로 변환돼 출력됨 튜플로 묶어줌
    df_token = pd.DataFrame(token, columns = ['word', 'class']) # 데이터 프레임화 시킨다.
    df_cleaned_token = df_token[(df_token['class'] =='Noun') | (df_token['class'] =='Verb') | (df_token['class'] =='Adjective')] # 명사 동사 형용사만 쓰겠다.

    words = []
    for word in df_cleaned_token['word']:
       if len(word) > 1: #두개이상의 단어만 선택
           if word not in list(stopwords['stopword']): # 스탑워즈에 없다면
               words.append(word) #추가한다.

    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
print(df.head())
df.info()
df= df[['titles', 'cleaned_sentences']]

df.to_csv('./crawling_data/cleaned_review_2015_2021.csv', index=False)

# print(df.loc[0, 'reviews'])
# print(re.sub('[^가-힣]', '', df.loc[0, 'reviews']))


# sentence = re.sub('[^가-힣 ]', ' ', df.loc[0, 'reviews'])
# print(sentence)
# token = okt.pos(sentence, stem=True)
# print(token)
# df.drop('reviews', inplace=True, axis=1)