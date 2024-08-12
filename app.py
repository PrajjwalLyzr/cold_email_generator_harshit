import os

from lyzr_agent import LyzrAgent
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LYZR_API_KEY = os.getenv("LYZR_API_KEY")

st.set_page_config(
    page_title="Lyzr Cold Email Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)


st.title("Lyzr Cold Email Generator")
st.markdown("### Welcome to the Lyzr Cold Email Generator!")

Agent = LyzrAgent(
        api_key=LYZR_API_KEY,
        llm_api_key=OPENAI_API_KEY
    )


@st.cache_resource
def create_agent():
    env_id = Agent.create_environment(
        name="Cold email",
        features=[{
            "type": "TOOL_CALLING",
            "config": {"max_tries": 3},
            "priority": 0
        }],
        tools=["perplexity_search"]

    )
    print(env_id)

    prompt = """
    **User Input and Initial Data Gathering:**
        -The user provides essential inputs, including the target audience/profile and product-related information from sources such as websites or product documents.
    **Research and Content Synthesis:**
        -The Scratchpad Agent conducts thorough research, including target research, product research, target-product fit analysis, and an online research summary.
        -The information is synthesized and displayed in the Scratchpad Display for a complete overview.
    **Email Draft Creation:**
        -Using the research from the Scratchpad, It drafts an initial email. If the email is perfect (all checks green), it is considered final.
        -If the email has faults, you have to identifies the issues and generates a To-Do list for corrections.
    **Critique and Iterative Refinement:**
        -The email draft is passed to the Critique Agent for feedback, highlighting areas that need improvement.
        -Based on the critique and the To-Do list, refine the email, rewriting it to address the identified issues.
        -The process continues iteratively, with the Critique Agent providing feedback and making necessary corrections until the email achieves a perfect status.
    **User Review and Final Approval:**
        -The refined email draft is presented to the user for final review and feedback.
        -Once the user approves, the email is finalized and ready to be sent out.
    """


    agent_id = Agent.create_agent(
        env_id=env_id['env_id'],
        system_prompt=prompt,
        name="Product Analyzer"
    )
    print(agent_id)

    return agent_id

query = st.text_area("Give Product description and target Audience")

if st.button("Generate"):
    agent = create_agent()
    print(agent)
    chat = Agent.send_message(
        agent_id=agent['agent_id'],
        user_id="default_user",
        session_id="harshit@lyzr.ai",
        message=query
    )

    st.markdown(chat['response'])

