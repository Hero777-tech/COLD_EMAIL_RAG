from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
import uuid
import csv


class Portfolio:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.index = None  # Will store the FAISS vector index

    def read_csv_file(self):
        data = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                skills = " ".join(row[:-1])  # Combine all skills into a single string
                link = row[-1]  # Last column is the portfolio URL
                data.append(Document(page_content=skills, metadata={"portfolio_url": link}))
        return data

    def load_portfolio(self):
        if not self.index:
            documents = self.read_csv_file()
            self.index = FAISS.from_documents(documents, self.embeddings)

    def query_links(self, skills):
        if not self.index:
            raise ValueError("Index is not loaded. Call load_portfolio() first.")
        results = self.index.similarity_search(skills, k=2)
        return [r.metadata["portfolio_url"] for r in results]
