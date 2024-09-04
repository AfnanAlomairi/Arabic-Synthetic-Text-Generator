import os
import cohere
from flask import Flask, request, render_template, send_file


cohere_api_key = os.getenv("COHERE_API_KEY")
cohere_client = cohere.Client(cohere_api_key)

app = Flask(__name__)

def generate_arabic_text(field, complexity, topic, number, length, save_to_file=False):
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

    try:
        response = cohere_client.generate(
            model='command',
            prompt=prompt,
            max_tokens=200,
            temperature=0.5,
            num_generations=number
        )
        texts = [generation.text for generation in response.generations]

        if save_to_file:
            filename = f"{topic.replace(' ', '_')}_generated_texts.txt"
            with open(filename, 'w', encoding='utf-8') as file:
                for text in texts:
                    file.write(text + "\n\n")
            return texts, filename

        return texts, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field = request.form.get('field')
        complexity = request.form.get('complexity')
        topic = request.form.get('topic')
        number = int(request.form.get('number'))
        length = request.form.get('length')
        save = request.form.get('save') == 'on'

        generated_texts, filename = generate_arabic_text(field, complexity, topic, number, length, save_to_file=save)

        if filename:
            return send_file(filename, as_attachment=True)

        return render_template('index.html', texts=generated_texts)

    return render_template('index.html', texts=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
