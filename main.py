import streamlit as st
import defaults
from Gladiator import GladiatorService
import dotenv
from ui import stylesheet, drafts_template, grades_template

columns = []


def get_max_line_height(responses):
    max_num_lines = 1
    for response in responses:
        content = response["content"]
        num_lines = len(content.split("\n"))
        max_num_lines = max(max_num_lines, num_lines)
    return 40 * num_lines


def grade_drafts(gladiator, responses):
    with st.spinner("Grading Drafts..."):
        columns = st.columns(3)
        max_line_height = get_max_line_height(responses=responses)
        for i, column in enumerate(columns):
            draft_template = drafts_template(i, responses[i], max_line_height)
            with column:
                st.markdown(draft_template, unsafe_allow_html=True)

        grades_json = gladiator.grade_drafts()
        return grades_json, columns


def select_winner(grades_json, columns):
    winning_index, winning_content = gladiator.select_winner(grades_json)

    for i, column in enumerate(columns):
        is_winner = i == winning_index
        grade_template = grades_template(
            grades_json[i]["score"], grades_json[i]["explanation"], is_winner
        )
        with column:
            st.markdown(grade_template, unsafe_allow_html=True)

    st.subheader("Winning Response:")
    with st.container():
        st.code(winning_content)


def generate_drafts(gladiator):
    with st.spinner("Generating Drafts..."):
        responses = gladiator.generate_drafts(prompt)
        return responses


dotenv.load_dotenv()

st.set_page_config(layout="wide")

st.markdown(stylesheet, unsafe_allow_html=True)

# Prism Library for Code Formatting
st.markdown(
    """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js"></script>
        """,
    unsafe_allow_html=True,
)

st.title("Gladiator: May the best response win")
prompt = st.text_area(
    "Enter a prompt and get the best answer", defaults.default_question, height=300
)


if st.button("Generate best answer"):
    gladiator = GladiatorService()
    try:
        responses = generate_drafts(gladiator)
        grades_json, columns = grade_drafts(gladiator, responses)
        select_winner(grades_json, columns)
    except Exception as e:
        print("Error: ", e)
        st.error("An error occurred: {}".format(str(e)))
