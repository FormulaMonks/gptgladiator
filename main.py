import streamlit as st
import defaults
from Gladiator import GladiatorService
import dotenv
from ui import stylesheet, drafts_template, grades_template

columns = []

def grade_drafts(gladiator, responses):
    with st.spinner("Grading Drafts..."):
        columns = st.columns(3)
        for i, column in enumerate(columns):
            draft_template = drafts_template(i, responses[i])
            with column:
                st.markdown(draft_template, unsafe_allow_html=True)

        grades_json = gladiator.grade_drafts() 
        return grades_json, columns


def select_winner(grades_json, columns):
    winning_index, winning_content = gladiator.select_winner(grades_json)

    for i, column in enumerate(columns):
        is_winner = i == winning_index
        grade_template = grades_template(grades_json[i]['score'], grades_json[i]['explanation'], is_winner)
        with column:
            st.markdown(grade_template, unsafe_allow_html=True)

    st.subheader("Winning Response:")
    with st.container():
        st.write(winning_content)

def generate_drafts(gladiator):
    with st.spinner("Generating Drafts..."):
        
        responses = gladiator.generate_drafts(prompt) 
        return responses


dotenv.load_dotenv()

st.set_page_config(layout="wide")
st.markdown(stylesheet, unsafe_allow_html=True)
st.title("Gladiator: May the best response win")
prompt = st.text_area("Enter a prompt and get the best answer", defaults.default_question, height=300)


if st.button("Generate best answer"):
    gladiator = GladiatorService()
    try:
        responses = generate_drafts(gladiator)
        grades_json, columns = grade_drafts(gladiator, responses)
        select_winner(grades_json, columns)
    except Exception as e:
        print("Error: ", e)
        st.error("An error occurred: {}".format(str(e)))






