import streamlit as st
import defaults
from Gladiator import Gladiator
import dotenv
from ui import stylesheet, drafts_template, grades_template


dotenv.load_dotenv()

st.set_page_config(layout="wide")
st.markdown(stylesheet, unsafe_allow_html=True)
st.title("Gladiator: May the best response win")
st.write("This is a demo of the gladiator library. It will generate multiple draft responses and then use a second model to judge the answers and pick a winner, which is then returned to the user.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    option = st.selectbox('(optional) Choose an example prompt...',('- select -', 'Refactor Code', 'second', 'third'))

if option == 'Refactor Code':
    example = defaults.refactor_code
elif option == 'second':
    example = defaults.second
elif option == 'third':
    example = defaults.third
else: 
    example = 'enter your prompt...'

prompt = st.text_area("Enter a prompt and get the best answer...", example, height=300)
columns = []
drafts = []

if st.button("Generate best answer"):
    gladiator = Gladiator()
    try:
        with st.spinner("Generating Drafts..."):
            drafts = gladiator.generate_drafts(prompt) 

        with st.spinner("Grading Drafts..."):
            columns = st.columns(3)
            for i, column in enumerate(columns):
                print("here", drafts[i])
                draft_template = drafts_template(i, drafts[i])
                print(draft_template)
                with column:
                    st.markdown(draft_template, unsafe_allow_html=True)

            grades_json = gladiator.grade_drafts(drafts) 

        winning_index, winning_content = gladiator.select_winner(drafts, grades_json)

        for i, column in enumerate(columns):
            is_winner = i == winning_index
            grade_template = grades_template(grades_json[i]['score'], grades_json[i]['explanation'], is_winner)
            with column:
                st.markdown(grade_template, unsafe_allow_html=True)

        st.subheader("Winning Response:")
        with st.container():
            st.write(winning_content)

    except Exception as e:
        print("Error: ", e)
        st.error("An error occurred: {}".format(str(e)))






