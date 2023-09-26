from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:str_param>')
def print_string(str_param):
    # Print the string to the console
    print(str_param)
    # Display the string in the web browser
    return str_param

@app.route('/count/<int:num_param>')
def count(num_param):
    # Generate a list of numbers in the range of the parameter
    numbers = "\n".join(map(str, range(num_param + 1)))
    # Display the numbers on separate lines
    return numbers

@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    # Perform the appropriate operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
