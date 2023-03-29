import streamlit as st

st.set_page_config(
    page_title="Virtual Bullying Detection App",
    page_icon="👋",
)

st.title("Virtual Bullying Detection using Machine Learning")
st.sidebar.success("Select a page above.")

st.write('''
Virtual bullying detection using machine learning is a technique that uses machine learning algorithms to identify and detect instances of cyberbullying in online interactions, such as social media, forums, and chat rooms. Cyberbullying refers to the use of digital technologies, such as the internet, social media, or mobile devices, to harass, intimidate, or harm others.

Machine learning algorithms can be trained to recognize patterns in online communication, such as the use of derogatory language, threats, or the targeting of specific individuals. These algorithms can then be used to automatically identify potential instances of cyberbullying in real-time.
''')


st.write('''


This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

expand_bar = st.expander("About")
expand_bar.markdown('''
* **Developed By:** [Karthik P & Jasper Kirubakaran J]
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')
