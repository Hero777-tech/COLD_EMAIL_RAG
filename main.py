import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# ✅ Set page config FIRST
st.set_page_config(layout="wide", page_title="Cold Email Generator")  # Must be first Streamlit command

# ✅ Branding and UI styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/custom.css")
st.image("assets/logo.png", width=150)
st.markdown("### JOB Consulting — AI-Powered Email Outreach", unsafe_allow_html=True)


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Email Generator")
    url_input = st.text_input("Enter a URL: ")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get("skills", [])
                portfolio_urls = portfolio.query_links(skills)
                email = llm.write_email(job, portfolio_urls)
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio(file_path="./sample_portfolio.csv")
    create_streamlit_app(chain, portfolio, clean_text)
