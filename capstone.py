import streamlit as st

# Sample data
courses = {
    'Backend Development': ['Python', 'Database', 'Cloud Computing'],
    'Machine Learning': ['Data Science', 'Computer Vision', 'Chatbot'],
    'Database': ['Backend Development', 'Big Data', 'Data Analysis'],
    'Data Analysis': ['Data Science', 'Machine Learning', 'Python'],
    'Data Science': ['Machine Learning', 'Big Data', 'Data Analysis'],
    'Cloud Computing': ['Containers', 'Backend Development', 'Big Data'],
    'Big Data': ['Data Science', 'Database', 'Cloud Computing'],
    'Python': ['Backend Development', 'Data Analysis', 'Machine Learning'],
    'Frontend Development': ['Backend Development', 'Containers', 'Chatbot'],
    'Containers': ['Cloud Computing', 'Backend Development', 'DevOps'],
    'Computer Vision': ['Machine Learning', 'Data Science', 'Chatbot'],
    'Chatbot': ['Machine Learning', 'Computer Vision', 'AI'],
    'Blockchain': ['Cryptocurrency', 'Smart Contracts', 'Decentralized Apps']
}

# Streamlit app
st.title('Course Recommender System')

# User input
selected_course = st.selectbox('Select a course you like:', list(courses.keys()))

# Recommend courses
if st.button('Recommend'):
    recommendations = courses.get(selected_course, [])
    st.write('Courses you might like:')
    for course in recommendations:
        st.write(course)
