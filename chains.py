import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="deepseek-r1-distill-llama-70b",
            temperature=0.3,
            max_tokens=1024,
            timeout=60,
            max_retries=3
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template("""
            You are an intelligent and precise information extractor.
            Given a block of text scraped from a job listing, extract the following fields:
            - 'role': the job title
            - 'experience': required or preferred experience level (e.g., 3+ years, entry-level)
            - 'skills': a list of relevant technical and soft skills
            - 'description': a detailed but concise paragraph summarizing the job responsibilities and expectations

            Return your output as clean and valid JSON only. No extra text or explanation is required.

            Here is the job listing text:
            {page_data}
        """)

        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={"page_data": cleaned_text})

        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Job extraction failed: Possibly malformed content or model limitations.")

        return response if isinstance(response, list) else [response]

    def write_email(self, job_description, portfolio_urls):
        prompt_email = PromptTemplate.from_template("""
            You are Aditya, an experienced and persuasive Business Development Officer at JOB Consulting,
            a forward-thinking firm specializing in delivering tailored AI and Data Science solutions.

            Your goal is to craft a professional and compelling cold email that opens a conversation with the company
            posting the job below. Showcase how your team at Mentee AI can fulfill their needs with efficiency and
            innovation while keeping costs manageable.

            Use a clear and confident tone. Start with an engaging hook and demonstrate your understanding of the client's domain.
            Integrate the most relevant portfolio URLs provided below to establish credibility.

            Please write the email using the following:
            - JOB DESCRIPTION: {job_description}
            - PORTFOLIO URLS: {portfolio_urls}

            Structure:
            1. Greeting
            2. Hook about the job posting
            3. Relevance of your firm’s expertise
            4. Portfolio highlights
            5. Clear call to action (suggesting a meeting or demo)
            6. Signature

            Keep it under 180 words, friendly yet professional.
        """)

        chain_email = prompt_email | self.llm
        response = chain_email.invoke({
            "job_description": str(job_description),
            "portfolio_urls": portfolio_urls
        })

        return response.content.strip()
