# 🧠 Enterprise Knowledge Assistant using RAG

## 📌 Project Overview

This project implements an **Enterprise Knowledge Assistant using Retrieval-Augmented Generation (RAG)**.

The system retrieves relevant information from **structured text documents** and generates **context-grounded answers using a Large Language Model (LLM).**

Instead of relying only on the LLM’s internal knowledge, the system **injects retrieved document context before generating responses**, significantly reducing hallucinations and improving answer reliability.

🔗 **Live MVP Demo**

 https://gowthamk-dev.github.io/RAG-SYSTEMS/

---

# 🎯 Objectives

The primary objectives of this project are to:

- Improve contextual accuracy in AI-generated responses  
- Reduce hallucinations using document-grounded retrieval  
- Avoid expensive model fine-tuning  
- Enable multi-domain question answering  
- Provide confidence-aware responses  
- Demonstrate multiple real-world RAG use cases  

---

# 🏗 System Architecture

The system follows a standard **RAG pipeline**:

1. Load domain-specific text documents  
2. Split documents into manageable text chunks  
3. Convert chunks into vectors using **TF-IDF**  
4. Accept a **user query**  
5. Compute **cosine similarity** between query and document vectors  
6. Retrieve **Top-K relevant chunks**  
7. Apply a **confidence threshold**  
8. Inject retrieved context into the **LLM**  
9. Generate a grounded response  
10. Display answer with **confidence awareness**

---

# 📂 Use Cases Implemented

### 1️⃣ Internal Employee Knowledge Base (RAG)

Policies, remote work rules, leave policy, IT support, code of conduct.

### 2️⃣ Customer Support Ticket Autocomplete (RAG)

Past support tickets, issue resolution, SLA handling.

### 3️⃣ Legal & Compliance Document Audit (RAG)

Contracts, compliance clauses, termination terms, data protection.

### 4️⃣ General Knowledge Retrieval (RAG)

Landmarks, monuments, engineering achievements (Ondiputhur dataset).

### 5️⃣ Technical Documentation Support (RAG)

API documentation, authentication flows, security guidelines.

---

# 🛠 Technologies Used

- Python  
- Scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  
- NumPy  
- Flask (Web Interface)  
- Ollama  
- LLM Model: Llama3  
- Retrieval-Augmented Generation (RAG)

---

# 📁 Project Structure
RAG_Use_Cases/
│
├── Emp_Knowledge/
│ ├── templates/
│ │ └── index.html
│ ├── app.py
│ ├── employee_data.txt
│ ├── README.txt
│ └── requirements.txt
│
├── Ticket_Autocomplete/
│ ├── templates/
│ │ └── index.html
│ ├── app.py
│ ├── Customer_Ticket_Data.txt
│ ├── README.txt
│ └── requirements.txt
│
├── Compliance_Audit/
│ ├── templates/
│ │ └── index.html
│ ├── app.py
│ ├── legal.txt
│ ├── README.txt
│ └── requirements.txt
│
├── rag_phi3_textfile_project/
│ ├── templates/
│ │ └── index.html
│ ├── app.py
│ ├── ondiputhur.txt
│ ├── README.txt
│ └── requirements.txt
│
├── Docs_Assist/
│ ├── templates/
│ │ └── index.html
│ ├── app.py
│ ├── Tech_data.txt
│ ├── README.txt
│ └── requirements.txt
│
├── Working_Screens/
│ ├── 01_Employee_KB/
│ ├── 02_Ticket_RAG/
│ ├── 03_Legal_Audit/
│ ├── 04_Ondiputhur_RAG/
│ └── 05_Tech_Docs/
│
├── .gitignore
└── README.md


---

# ▶ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
2️⃣ Ensure Ollama is Running
ollama run llama3
3️⃣ Run Any Use Case

Navigate to the required use case folder:

cd Compliance_Audit
python app.py

Then open your browser and visit:

http://localhost:5000

Repeat the same steps for other use cases.

🔍 Key Features

Domain-specific document retrieval

Top-K chunk retrieval (K = 3)

Confidence-aware answer generation

Context-grounded LLM responses

Reduced hallucination

Modular architecture (one app per use case)

Screenshot-based result validation

🔢 Confidence Handling

The system evaluates the similarity score of retrieved chunks.

If similarity ≥ threshold → Answer is generated

If similarity < threshold → System avoids unreliable output

This ensures safe and trustworthy responses.

🚀 Future Enhancements

Replace TF-IDF with semantic embeddings

Integrate FAISS for scalable vector storage

Add PDF and DOCX ingestion

Implement conversational memory

Deploy as a unified web application

Add citation highlighting in responses

📌 Conclusion

This project demonstrates how Retrieval-Augmented Generation (RAG) can transform a general-purpose LLM into a reliable enterprise knowledge assistant.

By grounding responses in authorized documents, the system delivers accurate, explainable, and domain-specific answers, making it ideal for real-world enterprise applications.
