from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/results', methods=["POST"])
def result():
    num1 = int(request.form.get("number1"))
    num2 = int(request.form.get("number2"))
    op = request.form.get("operation")
    end = "No operation selected"
    if op == "+":
        end = num1 + num2
    elif op == "-":
        end = num1 - num2
    elif op == "*":
        end = num1 * num2
    elif op == "/":
        if num2 == 0:
            end = "Divide by 0 error"
        else:
            end = num1 / num2
    return render_template("results.html", result=end)


if __name__ == '__main__':
    app.run()
