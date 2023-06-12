from email.mime import image
import pickle
import streamlit as st
import numpy as np
from sklearn.neighbors import NearestNeighbors
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Books Recommendation System", page_icon=":books:", layout="centered")
st.title(":violet[Book Recommendation System] :books:")
#st.header("Book Recommendation System")

#Loading Models
model = pickle.load(open('Model.pkl','rb'))
book_names = pickle.load(open('Book_names.pkl','rb'))
final_rating = pickle.load(open('final_ratings.pkl','rb'))
book_pivot = pickle.load(open('Book_pivot.pkl','rb'))
popular_df = pickle.load(open('Popular_df','rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(final_rating['Book Title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['ImageURL']
        poster_url.append(url)
    
    return poster_url

def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list,poster_url


#Main Code
#1. Horizontal Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Search Books", "Trending"],
    icons=["house", "search", "arrow-up-right-square-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)


if selected == "Home":
    st.title(f":red[Popular Books]")
    st.image(popular_df,use_column_width=1)

if selected == "Search Books":
    st.title(f":red[Search Books]")
    selected_books = st.selectbox("Type or select a book from dropdown", book_names)
    if selected_books:
        recommend_books, poster_url = recommend_book(selected_books)
        st.text(recommend_books[0])
        st.image(poster_url[0])
        st.header(":green[Recommended For you]")
        col1, col2, col3, col4, col5 = st.columns(5,gap="small")
        with col1:
            st.text(recommend_books[1])
            st.image(poster_url[1])
        with col2:
            st.text(recommend_books[2])
            st.image(poster_url[2])
        with col3:
            st.text(recommend_books[3])
            st.image(poster_url[3])
        with col4:
            st.text(recommend_books[4])
            st.image(poster_url[4])
        with col5:
            st.text(recommend_books[5])
            st.image(poster_url[5])

if selected == "Trending":
    st.title(f":red[Trending Books]")
    st.header(":green[Top Picks] :sparkler:")
    cl1, cl2, cl3, cl4, cl5 = st.columns(5)
    with cl1:
        st.image(popular_df[5])
    with cl2:
        st.image(popular_df[6])
    with cl3:
        st.image(popular_df[7])
    with cl4:
        st.image(popular_df[8])
    with cl5:
        st.image(popular_df[9])

    st.header(":green[Highest Rated Books] :sparkler:")
    a = final_rating['Book Title'].value_counts().index[0:10]
    cl6, cl7, cl8, cl9, cl10 = st.columns(5)
    with cl6:
        df = final_rating.loc[final_rating['Book Title'] == a[0]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl7:
        df = final_rating.loc[final_rating['Book Title'] == a[1]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl8:
        df = final_rating.loc[final_rating['Book Title'] == a[3]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl9:
        df = final_rating.loc[final_rating['Book Title'] == a[4]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl10:
        df = final_rating.loc[final_rating['Book Title'] == a[5]]
        b = df['ImageURL'].tolist()
        st.image(b[0])

    st.header(":green[Books by Top Authors] :sparkler:")
    x = final_rating['Book Author'].value_counts().index[0:10]
    cl11, cl12, cl13, cl14, cl15 = st.columns(5)
    with cl11:
        df = final_rating.loc[final_rating['Book Author'] == x[0]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl12:
        df = final_rating.loc[final_rating['Book Author'] == x[1]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl13:
        df = final_rating.loc[final_rating['Book Author'] == x[2]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl14:
        df = final_rating.loc[final_rating['Book Author'] == x[3]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl15:
        df = final_rating.loc[final_rating['Book Author'] == x[4]]
        b = df['ImageURL'].tolist()
        st.image(b[0])

    st.header(":green[Books by Top Publishers] :sparkler:")
    y = final_rating['Publisher'].value_counts().index[0:10]
    cl16, cl17, cl18, cl19, cl20 = st.columns(5)
    with cl16:
        df = final_rating.loc[final_rating['Publisher'] == y[0]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl17:
        df = final_rating.loc[final_rating['Publisher'] == y[1]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl18:
        df = final_rating.loc[final_rating['Publisher'] ==y[2]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl19:
        df = final_rating.loc[final_rating['Publisher'] == y[3]]
        b = df['ImageURL'].tolist()
        st.image(b[0])
    with cl20:
        df = final_rating.loc[final_rating['Publisher'] == y[4]]
        b = df['ImageURL'].tolist()
        st.image(b[0])







#if st.button('Show Recommendation'):





