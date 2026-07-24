# AI-Powered Course Assistant using Retrieval-Augmented Generation (RAG)

## Overview

The AI-Powered Course Assistant is an end-to-end Retrieval-Augmented Generation (RAG) application that transforms educational video content into a searchable knowledge base. The system enables users to ask natural language questions about course material and receive accurate, context-aware answers generated from the course transcripts instead of relying on the general knowledge of a Large Language Model.

The application extracts audio from educational videos, converts speech into text, generates semantic embeddings for transcript chunks, retrieves the most relevant information using semantic similarity search, and produces grounded responses with video references and timestamps.

---

## Features

- End-to-end RAG pipeline
- Video-to-audio conversion
- Automatic speech-to-text transcription
- Semantic text chunking
- Vector embedding generation
- Semantic similarity search
- Context-aware question answering
- Prompt engineering
- Timestamp-based responses
- Video title and video number references
- Hallucination reduction using retrieved context

---

## Tech Stack

### Programming Language

- Python

### Generative AI

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Prompt Engineering

### Machine Learning

- Sentence Transformers
- Vector Embeddings
- Cosine Similarity
- Semantic Search

### Natural Language Processing

- OpenAI Whisper
- Text Chunking
- Speech-to-Text
- Transcript Processing

### Libraries

- NumPy
- Transformers
- Sentence-Transformers
- PyTorch
- Requests
- JSON
- tqdm
- python-dotenv

### Tools

- Git
- GitHub
- VS Code
- Ollama (Local LLM)

---

## Project Workflow

```
Videos
        ↓
Audio Extraction
        ↓
Speech-to-Text (Whisper)
        ↓
Transcript Generation
        ↓
Semantic Text Chunking
        ↓
Embedding Generation
        ↓
Vector Storage
        ↓
Semantic Retrieval
        ↓
Prompt Construction
        ↓
Large Language Model
        ↓
Final Answer
```

---

## Project Structure

```
AI-Course-Assistant
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── jsons/
│
├── newjsons/
│
├── script/
│   ├── 01_video_to_voice.py
│   ├── 02_audio_to_text.py
│   ├── 03_text_to_chunks.py
│   ├── 04_read_chunks.py
│   ├── 05_process_chunks.py
│   ├── 06_merge_chunks.py
│   ├── embeddings.joblib
│   ├── output.json
│   ├── prompt.txt
│   └── response.txt
│
├── README.md
└── requirements.txt
```
---

# How to Use

## Step 1 – Collect Your Videos

Place all course or educational video files inside the `videos/` directory.

```
videos/
    lesson1.mp4
    lesson2.mp4
    lesson3.mp4
```

---

## Step 2 – Convert Videos to Audio

Run the `video_to_audio.py` script to extract audio from each video.

```bash
python video_to_audio.py
```

The extracted audio files will be saved in the `audio/` directory.

---

## Step 3 – Convert Audio to Transcript

Run the `audio_to_text.py` script to convert audio into text using OpenAI Whisper.

```bash
python audio_to_text.py
```

Each transcript is stored as a JSON file containing the transcript, timestamps, video title, and metadata.

---

## Step 4 – Generate Semantic Embeddings

Run the preprocessing scripts to split transcripts into semantic chunks and generate vector embeddings.

```bash
python text_to_chunks.py
python read_chunks.py
```

The generated embeddings are stored for semantic retrieval during inference.

---

## Step 5 – Ask Questions

Run the inference pipeline.

```bash
python process_chunks.py
```

The system performs the following operations:

1. Converts the user query into an embedding.
2. Performs semantic similarity search.
3. Retrieves the most relevant transcript chunks.
4. Constructs a prompt using the retrieved context.
5. Sends the prompt to the Large Language Model.
6. Returns an accurate answer with the corresponding video title and timestamp.

---

## Example

==================================================
AI Course Assistant
==================================================

Question:
Where is CSS taught?

Top Matching Results

1.
Video Number : 2
Video Title  : Your First HTML Website
Timestamp    : 14:10
Explanation  : The instructor introduces CSS and explains that styling will be covered in upcoming lessons.

--------------------------------------------------

2.
Video Number : 4
Video Title  : Heading, Paragraphs and Links
Timestamp    : 17:08
Explanation  : The instructor mentions that CSS will be used to style HTML elements.

--------------------------------------------------

3.
Video Number : 13
Video Title  : Entities, Code Tag and More on HTML
Timestamp    : 05:32
Explanation  : Modern CSS topics are introduced as part of the course roadmap.

==================================================
---

## Concepts Covered

### Generative AI

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Large Language Models
- Context Grounding
- Hallucination Reduction

### Machine Learning

- Sentence Embeddings
- Dense Vector Representation
- Semantic Similarity
- Information Retrieval
- Vector Search

### Natural Language Processing

- Speech-to-Text
- Transcript Processing
- Semantic Chunking
- Query Processing

### Software Engineering

- Modular Python Development
- Pipeline Design
- API Integration
- JSON Data Processing
- End-to-End AI Workflow

---

## Future Improvements

- FAISS or ChromaDB integration
- Hybrid Search (BM25 + Vector Search)
- FastAPI backend
- Streamlit or React frontend
- Multi-course support
- Voice-based interaction
- PDF document support
- Docker deployment
- Cloud deployment
- Authentication and user profiles

---

## License

This project is intended for educational purposes.
