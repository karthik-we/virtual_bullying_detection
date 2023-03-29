# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle
import win32api
import random
import streamlit.components.v1 as components


# Page title
with st.columns(3)[1]:
    image = Image.open('images/logo.jpg')
    st.image(image, width= 200)
st.write('''
# Virtualbullying Detection App 
''')



# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 50)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
st.header("Entered Tweet text ")
if tweet_input:
    tweet_input
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
with st.columns(3)[1]:
    st.header("Prediction")
    if tweet_input:
        prediction = custom_input_prediction(tweet_input)
        if prediction == "Age":
            st.image("images/age_cyberbullying.png",width= 200)
            win32api.Beep(random.randint(37,10000), random.randint(750,3000))
        elif prediction == "Ethnicity":
            st.image("images/ethnicity_cyberbullying.png",width= 200)
            win32api.Beep(random.randint(37,10000), random.randint(750,3000))
        elif prediction == "Gender":
            st.image("images/gender_cyberbullying.png",width= 200)
            win32api.Beep(random.randint(37,10000), random.randint(750,3000))
        elif prediction == "Not Cyberbullying":
            st.image("images/not_cyberbullying.png",width= 200)
        elif prediction == "Other Cyberbullying":
            st.image("images/other_cyberbullying.png",width= 200)
            win32api.Beep(random.randint(37,10000), random.randint(750,3000))
        elif prediction == "Religion":
            st.image("images/religion_cyberbullying.png",width= 200)
            win32api.Beep(random.randint(37,10000), random.randint(750,3000))
    else:
        st.write('''
        ***No Tweet Text Entered!***
        ''')

st.write('''***''')

# About section

components.html("""<script src="https://cdn.botpress.cloud/webchat/v0/inject.js"></script>
<script src="https://mediafiles.botpress.cloud/11657143-627f-4206-8e1f-471d52c436f8/webchat/config.js" defer></script>
""",height=400,)