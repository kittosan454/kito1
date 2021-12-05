import pandas as pd
from gensim.models import Word2Vec
# back over word: 형태소들을 하나로 묶는다.
# word 2 vec 모델

review_word = pd.read_csv('./crawling_data/cleaned_review_2015_2021.csv')
review_word.info()

cleaned_token_review = list(review_word['cleaned_sentences'])

cleaned_tokens = []
for sentence in cleaned_token_review:
    token = sentence.split() # 공백문자 기준으로 짜른다. 디폴트 값이 공백문자
    cleaned_tokens.append(token) # 토큰들의 리스트 문장단위로 들어간다.
print(cleaned_tokens) # 오류 뜰땐 conda install -c conda-forge python-levenshtein
embedding_model = Word2Vec(cleaned_tokens, size=100, window =4, min_count=20, workers =4, iter = 100, sg=1)
# 벡터화 모델학습 widow는 커널 갯수 mincount는 20번 이상 중복되는 애들만 학습, workers는 cpu코어 갯수 vector_size는 100개의 차원으로 축소
# 4.0.0 버전 이후에는 vector_size 와 iter대신 epoch를 써야한다.
embedding_model.save('./models/word2VecModel_2015_2021.model')
print(embedding_model.wv.vocab.keys()) # print(list(embedding_model.wv.index_to_key)) 4.0에서
print(len(embedding_model.wv.vocab.keys()))  # print(len(list(embedding_model.wv.index_to_key)))