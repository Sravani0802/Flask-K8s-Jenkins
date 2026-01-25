from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

html_page = '''
<!doctype html>
<title>Calculator</title>
<h2>Calculator</h2>
<form method="POST" action="/calculate_web">
  Number 1: <input type="text" name="num1"><br><br>
  Number 2: <input type="text" name="num2"><br><br>
  Operation:
  <select name="operation">
    <option value="add">+</option>
    <option value="subtract">-</option>
    <option value="multiply">*</option>
    <option value="divide">/</option>
    <option value="remainder">%</option>
  </select><br><br>
  <input type="submit" value="Calculate">
</form>
{% if result is defined %}
<h3>Result: {{ result }}</h3>
{% endif %}
'''

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/calculate_web', methods=['POST'])
def calculate_web():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
    except:
        return "Invalid input", 400

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero", 400
        result = num1 / num2
    elif operation == "remainder":
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return render_template_string(html_page, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
