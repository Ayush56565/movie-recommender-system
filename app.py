import streamlit as st
import pickle
import pandas as pd
movieList=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movieList)

def movierec(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recomList=[]
    for i in distances[1:6]:
        recomList.append(movies.iloc[i[0]].title)
    return recomList
st.title("Movie Recommendations")
movie=st.selectbox('Type the movie that you want recommendations for',
                    (movies['title'].values))

if st.button('Recommend'):
    recommendations=movierec(movie)
    for i in recommendations:
        st.write(i)