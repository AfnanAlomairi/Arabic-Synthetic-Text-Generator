import os
import cohere
from flask import Flask, request, render_template
from interface import template  # Import the template from the interface module

#Cohere client
cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

app = Flask(__name__)

def generate_arabic_text(field, complexity, topic, number, length):
    length_mapping = {
        'short': 'A brief overview',
        'medium': 'A detailed explanation',
        'long': 'An in-depth analysis'
    }

    prompt = (
        f"Field: {field}\n"
        f"Complexity: {complexity}\n"
        f"Topic: {topic}\n"
        f"Length: {length_mapping.get(length.lower(), 'A comprehensive description')}\n\n"
        f"اكتب فقرة شاملة باللغة العربية حول الموضوع أعلاه."
    )

    print(f"Generated Prompt: {prompt}")

    try:
        response = cohere_client.generate(
            model='command',
            prompt=prompt,
            max_tokens=200,
            temperature=0.5,
            num_generations=number
        )
        texts = [generation.text for generation in response.generations]

        print(f"API Response: {response}")

        return texts

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field = request.form.get('field')
        complexity = request.form.get('complexity')
        topic = request.form.get('topic')
        number = int(request.form.get('number'))
        length = request.form.get('length')

        print(f"Field: {field}")
        print(f"Complexity: {complexity}")
        print(f"Topic: {topic}")
        print(f"Number: {number}")
        print(f"Length: {length}")

        generated_texts = generate_arabic_text(field, complexity, topic, number, length)
        print(f"Generated Texts: {generated_texts}")
        return render_template("index.html", texts=generated_texts)

    return render_template("index.html", texts=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

