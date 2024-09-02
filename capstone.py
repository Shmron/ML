import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample data
courses = {
    'Course': [
        'Backend Development', 'Machine Learning', 'Database', 'Data Analysis', 
        'Data Science', 'Cloud Computing', 'Big Data', 'Python', 
        'Frontend Development', 'Containers', 'Computer Vision', 'Chatbot', 'Blockchain'
    ],
    'Genre': [
        'Development', 'AI', 'Database', 'Data Analysis', 
        'Data Science', 'Cloud', 'Big Data', 'Programming', 
        'Development', 'DevOps', 'AI', 'AI', 'Blockchain'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(courses)

# Function to recommend courses
def recommend_courses(course_name, num_recommendations=5):
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(df['Genre'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    course_index = df[df['Course'] == course_name].index[0]
    similarity_scores = list(enumerate(cosine_sim[course_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:num_recommendations+1]
    
    course_indices = [i[0] for i in similarity_scores]
    return df['Course'].iloc[course_indices]

# Streamlit app
st.title('Course Recommender System')

# User input
selected_course = st.selectbox('Select a course you like:', df['Course'])

# Recommend courses
if st.button('Recommend'):
    recommendations = recommend_courses(selected_course)
    st.write('Courses you might like:')
    for course in recommendations:
        st.write(course)
