import torch
from transformers import pipeline

def load_markdown_file(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def answer_questions(md_file_path, questions):
    # Load the content of the Markdown file
    context = load_markdown_file(md_file_path)

    # Load the pre-trained model and tokenizer specifically fine-tuned for QA
    nlp = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad", tokenizer="distilbert-base-uncased-distilled-squad")

    # Answer each question based on the context
    answers = []
    for question in questions:
        result = nlp(question=question, context=context)
        answers.append(result['answer'])

    return answers

if __name__ == "__main__":
    md_file_path = r"C:\\Users\\AdminT\\Documents\\Research Papers\\health.md"  # Replace with the path to your .md file
    questions = [
        "What is the main topic of the document?",
        "Who is the author of the document?",
        # Add more questions as needed
    ]

    answers = answer_questions(md_file_path, questions)
    for question, answer in zip(questions, answers):
        print(f"Q: {question}")
        print(f"A: {answer}")
