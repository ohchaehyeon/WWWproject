from PIL import Image
import pytesseract
from konlpy.tag import Okt
import os
import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

f = open('./imagetogenre.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(['순위', '장르', '코미디', '호러', '로맨스', '드라마', '판타지', '화려한공연'])
musical = "뮤지컬"
play = "연극"

comedy_list = []
comedy = pd.read_csv('./keywordlist/horror_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
comedy_list = comedy['장르']
comedy_list = comedy_list.values
horror_list = []
horror = pd.read_csv('./keywordlist/horror_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
horror_list = horror['장르']
horror_list = horror_list.values
romance_list = []
romance = pd.read_csv('./keywordlist/romance_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
romance_list = romance['장르']
romance_list = romance_list.values
drama_list = []
drama = pd.read_csv('./keywordlist/drama_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
drama_list = drama['장르']
drama_list = drama_list.values
fantasy_list = []
fantasy = pd.read_csv('./keywordlist/fantasy_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
fantasy_list = fantasy['장르']
fantasy_list = fantasy_list.values
new_list = []
new = pd.read_csv('./keywordlist/new_list1.csv', encoding='utf-8', names=['장르', '빈도수'])
new_list = new['장르']
new_list = new_list.values

#뮤지컬
a = "./musical"
musical_list = os.listdir(a)
print(musical_list)
try:
    for dir_musical in musical_list:

        path = os.path.join(a, dir_musical)
        print(path)
        print(dir_musical)
        files_musical = os.listdir(path)
        print(files_musical)
        nounlist = []
        try:
            for file_musical in files_musical:
                print(file_musical)
                path1 = os.path.join(path, file_musical)
                text = pytesseract.image_to_string(Image.open(path1), lang="kor")
                text = text.replace(" ", "")
                okt = Okt()
                noun=[]
                noun = okt.nouns(text)
                for i, v in enumerate(noun):
                    if len(v) < 2:
                        noun.pop(i)
                nounlist = nounlist + noun
        except:
            None
        print(nounlist)

        try:
            comedy_distances = 5.0
            for i in range(len(comedy_list)):
                for j in range(len(nounlist)):
                    compare_list = [comedy_list[i], nounlist[j]]
                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]

                    comedy_distances = comedy_distances + distances
                    if comedy_distances >= 10.0:
                        comedy_distances = 10.0
            print('코미디', comedy_distances)
        except:
            None


        try:
            horror_distances = 5.0
            for i in range(len(horror_list)):
                 for j in range(len(nounlist)):
                    compare_list = [horror_list[i], nounlist[j]]
                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]

                    horror_distances = horror_distances + distances
                    if horror_distances >= 10.0:
                        horror_distances = 10.0
            print('호러', horror_distances)
        except:
            None


        try:
            romance_distances = 5.0
            for i in range(len(romance_list)):
                for j in range(len(nounlist)):
                    compare_list = [romance_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    romance_distances = romance_distances + distances
                    if romance_distances >= 10.0:
                        romance_distances = 10.0
            print('로맨스', romance_distances)
        except:
            None

        try:
            drama_distances = 5.0
            for i in range(len(drama_list)):
                for j in range(len(nounlist)):
                    compare_list = [drama_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    drama_distances = drama_distances + distances
                    if drama_distances >= 10.0:
                        drama_distances = 10.0
            print('드라마', drama_distances)
        except:
            None

        try:
            fantasy_distances = 5.0
            for i in range(len(fantasy_list)):
                for j in range(len(nounlist)):
                    compare_list = [fantasy_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    fantasy_distances = fantasy_distances + distances
                    if fantasy_distances >= 10.0:
                        fantasy_distances = 10.0
            print('판타지', fantasy_distances)
        except:
            None

        try:
            new_distances = 5.0
            for i in range(len(new_list)):

               for j in range(len(nounlist)):
                    compare_list = [new_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    new_distances = new_distances + distances
                    if new_distances >= 10.0:
                        new_distances = 10.0
            print('화려한공연', new_distances)

        except:
            None
        wr.writerow([dir_musical, musical, comedy_distances, horror_distances, romance_distances, drama_distances, fantasy_distances, new_distances])
except:
    None

#연극
b = "./play"
play_list = os.listdir(b)
try:
    for dir_play in play_list:
        path_play = os.path.join(b, dir_play)
        print(path_play)
        print(dir_play)
        files_play = os.listdir(path_play)
        print(files_play)
        nounlist = []
        try:
            for file_play in files_play:
                print(file_play)
                path1_play = os.path.join(path_play, file_play)
                text = pytesseract.image_to_string(Image.open(path1_play), lang="kor")
                text = text.replace(" ", "")
                okt = Okt()
                noun=[]
                noun = okt.nouns(text)
                for i, v in enumerate(noun):
                    if len(v) < 2:
                        noun.pop(i)
                nounlist = nounlist + noun
        except:
            None
        print(nounlist)

        try:
            comedy_distances = 5.0
            for i in range(len(comedy_list)):
                for j in range(len(nounlist)):
                    compare_list = [comedy_list[i], nounlist[j]]
                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]

                    comedy_distances = comedy_distances + distances
                    if comedy_distances >= 10.0:
                        comedy_distances = 10.0
            print('코미디', comedy_distances)
        except:
            None
        try:
            horror_distances = 5.0
            for i in range(len(horror_list)):
                 for j in range(len(nounlist)):
                    compare_list = [horror_list[i], nounlist[j]]
                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]

                    horror_distances = horror_distances + distances
                    if horror_distances >= 10.0:
                        horror_distances = 10.0
            print('호러', horror_distances)
        except:
            None

        try:
            romance_distances = 5.0
            for i in range(len(romance_list)):
                for j in range(len(nounlist)):
                    compare_list = [romance_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    romance_distances = romance_distances + distances
                    if romance_distances >= 10.0:
                        romance_distances = 10.0
            print('로맨스', romance_distances)
        except:
            None

        try:
            drama_distances = 5.0
            for i in range(len(drama_list)):
                for j in range(len(nounlist)):
                    compare_list = [drama_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    drama_distances = drama_distances + distances
                    if drama_distances >= 10.0:
                        drama_distances = 10.0
            print('드라마', drama_distances)
        except:
            None

        try:
            fantasy_distances = 5.0
            for i in range(len(fantasy_list)):
                for j in range(len(nounlist)):
                    compare_list = [fantasy_list[i], nounlist[j]]

                    tfidf_vectorizer = TfidfVectorizer(min_df=1)
                    tfidf_matrix = tfidf_vectorizer.fit_transform(compare_list)

                    distances = (tfidf_matrix * tfidf_matrix.T)
                    distances = distances.toarray()[0][1]
                    fantasy_distances = fantasy_distances + distances
                    if fantasy_distances >= 10.0:
                        fantasy_distances = 10.0
            print('판타지', fantasy_distances)
            print(dir_play,play,comedy_distances,horror_distances,romance_distances,drama_distances,fantasy_distances)

        except:
            None
        wr.writerow([dir_play, play, comedy_distances, horror_distances, romance_distances, drama_distances, fantasy_distances, ""])
except:
    None
f.close()


df1 = pd.read_csv('./interpark.csv')
df2 = pd.read_csv('./imagetogenre.csv')
play_result = pd.merge(df1, df2, on=['순위','장르'],how='outer')
play_result.loc[play_result['제목'].str.contains('코미디'),'코미디'] = 10
play_result.loc[play_result['제목'].str.contains('코믹'),'코미디'] = 10
play_result.loc[play_result['제목'].str.contains('공포'),'호러'] = 10
play_result.loc[play_result['제목'].str.contains('스릴러'),'호러'] = 10
play_result = play_result.set_index('순위')
play_result.to_csv('./interpark_all.csv')
