# AI Chatbot

## Project Overview

This project is a locally hosted AI chatbot built using Python, Flask, and Hugging Face Transformers.

The chatbot uses a fine-tuned Llama 3.2 1B language model trained on a custom dataset. The model runs locally and does not use external APIs such as OpenAI, Gemini, or Claude.

The chatbot can:
- Generate poems from moods
- Provide personal advice
- Generate creative stories from user prompts

---

## Features

- Local AI chatbot
- Fine-tuned Hugging Face model
- Flask web application
- Custom dataset training
- Modern dark UI
- AI Mood-to-Poem Generator
- AI Personal Advice Chatbot
- AI Data-to-Story Generator
- No external API usage
- Text generation responses

---

## Technologies Used

- Python
- Flask
- Hugging Face Transformers
- PyTorch
- HTML
- CSS
- JavaScript

---

## Model Information

### Base Model
- Meta Llama 3.2 1B

### Fine-Tuning
- Fine-tuned using Hugging Face Transformers Trainer API
- Trained on a custom-generated dataset
- Local training without external APIs
- Uses Meta Llama 3.2 1B as the base LLM

---

## Project Structure

```bash
AI CHATBOT/
│
├── app.py
├── train.py
├── create_dataset.py
├── dataset.txt
├── requirements.txt
├── README.md
├── .gitignore
│
├── fine_tuned_model/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
```

---

## Dataset Generator

File:
- create_dataset.py

Purpose:
- Automatically generates a large custom dataset for AI training.
- Creates poem, advice, and story examples.
- Helps improve chatbot response quality.

Run:

```bash
python create_dataset.py
```

This generates:
- 300 poem examples
- 300 advice examples
- 300 story examples

Total:
- 900 training examples

---

## Installation

### 1. Clone or Download Project

Download the project files or clone from GitHub.

---

### 2. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

### 3. Generate Dataset

Run:

```bash
python create_dataset.py
```

This creates:
- dataset.txt

---

### 4. Train the AI Model

Run:

```bash
python train.py
```

Wait until:

```text
Fine-tuning complete!
```

This creates:
- fine_tuned_model/

---

### 5. Run the Chatbot Website

Run:

```bash
python app.py
```

---

### 6. Open Website

Open:

```text
http://127.0.0.1:5000
```

---

## AI Features

### 1. Mood-to-Poem Generator

Input:
- happy
- sad
- excited
- calm

Output:
- AI-generated emotional poems

---

### 2. Personal Advice Chatbot

Input:
- exam stress
- anxiety
- motivation
- confidence

Output:
- Helpful AI-generated advice

---

### 3. Data-to-Story Generator

Input:
- A robot entered a magical forest
- A dragon protected a village

Output:
- Creative AI-generated stories

---

## Fine-Tuning Process

The model was fine-tuned using:
- Hugging Face Transformers
- PyTorch
- Custom dataset

Training script:
- train.py

Dataset:
- dataset.txt

Generated dataset:
- create_dataset.py

---

## Assignment Requirement

This project satisfies the assignment requirements because:

- The chatbot uses a locally downloaded Hugging Face LLM
- The model was fine-tuned on a custom dataset
- No external commercial APIs were used
- The AI model runs locally on the user's computer
- The model size is under 3GB
- Custom datasets were used for training
- The project includes multiple AI text-generation features

---

## Future Improvements

- Better dataset quality
- Chat history memory
- Improved UI design
- Better conversational responses
- Larger language model support
- Voice input and output
- User authentication system

---

## Author

Created by:
- Nabodip Kunwar