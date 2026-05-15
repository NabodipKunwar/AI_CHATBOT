from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

chatbot = pipeline(
    "text-generation",
    model="./fine_tuned_model",
    tokenizer="./fine_tuned_model"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.form["message"]
    mode = request.form["mode"]

    if mode == "poem":
        prompt = f"""
### Instruction:
Write a beautiful 8-line poem about this mood or feeling: {user_input}.
Use emotional language, simple English, and avoid repetition.

### Response:
"""

    elif mode == "advice":
        prompt = f"""
### Instruction:
Give kind and practical personal advice about this problem: {user_input}.
Give 3 clear steps and keep the advice supportive.

### Response:
"""

    elif mode == "story":
        prompt = f"""
### Instruction:
Write a creative short story about this idea: {user_input}.
The story must have a beginning, problem, and ending. Write 2 paragraphs.

### Response:
"""

    else:
        prompt = f"""
### Instruction:
Respond helpfully to this message: {user_input}

### Response:
"""

    response = chatbot(
        prompt,
        max_new_tokens=220,
        temperature=0.75,
        top_k=40,
        top_p=0.9,
        repetition_penalty=1.25,
        do_sample=True,
        truncation=True,
        pad_token_id=chatbot.tokenizer.eos_token_id,
        return_full_text=False
    )

    generated_text = response[0]["generated_text"].strip()

    return render_template(
        "index.html",
        response=generated_text
    )

if __name__ == "__main__":
    app.run(debug=True)