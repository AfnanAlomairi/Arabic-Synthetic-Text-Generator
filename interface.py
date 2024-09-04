#interface.py
template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>مولد النصوص العربية الاصطناعية</title>
    <style>
        body { font-family: Arial, sans-serif; direction: rtl; padding: 20px; }
        .container { max-width: 800px; margin: auto; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input, select, textarea { width: 100%; padding: 8px; }
        button { padding: 10px 20px; }
        .output { margin-top: 30px; }
        .paragraph { background-color: #f9f9f9; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>مولد النصوص العربية الاصطناعية</h1>
        <form method="POST">
            <div class="form-group">
                <label for="field">المجال:</label>
                <input type="text" id="field" name="field" required>
            </div>
            <div class="form-group">
                <label for="complexity">مستوى التعقيد:</label>
                <select id="complexity" name="complexity" required>
                    <option value="مبتدئ">مبتدئ</option>
                    <option value="متوسط">متوسط</option>
                    <option value="متقدم">متقدم</option>
                </select>
            </div>
            <div class="form-group">
                <label for="topic">الموضوع:</label>
                <input type="text" id="topic" name="topic" required>
            </div>
            <div class="form-group">
                <label for="number">عدد الفقرات:</label>
                <input type="number" id="number" name="number" min="1" max="10" required>
            </div>
            <div class="form-group">
                <label for="length">الطول:</label>
                <select id="length" name="length" required>
                    <option value="short">قصير</option>
                    <option value="medium">متوسط</option>
                    <option value="long">طويل</option>
                </select>
            </div>
            <button type="submit">إنشاء النص</button>
        </form>

        {% if texts %}
            <div class="output">
                <h2>النصوص المولدة:</h2>
                {% for text in texts %}
                    <div class="paragraph">{{ text }}</div>
                {% endfor %}
            </div>
        {% else %}
            <div class="output">
                <h2>لم يتم توليد نصوص بعد.</h2>
            </div>
        {% endif %}
    </div>
</body>
</html>
'''

