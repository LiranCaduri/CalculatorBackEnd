from flask import Flask, request
from CalculationsFunctions import get_calculation_methods

'''
TODOS

1. floats only ✔
2. manual unpacking ✔
3. make in efficient
4. code review
5. make sure cache cannot be corapted ✔
6. spelling (comments)

'''

app = Flask(__name__)

cache = {
    "last_answer": 0
}

@app.route('/', methods=['POST'])
def calc():
    if len(dict(request.form)) < 3:
        return one_number_calculation()

    return two_number_calculation()


@app.route('/')
def cache_answer():
    return str(cache['last_answer'])


def two_number_calculation():

    operations = get_calculation_methods()

    try:

        operator = request.form['operator']
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])

    except ValueError:
        return """ERORR
                Please enter only TWO valid numbers and ONE operator
                or ONE number and ONE operator for continue a Calculation!"""

    else:
        try:
            answer = operations[operator](number1=number1, number2=number2)

            cache["last_answer"] = 0  # reset the last calculation
            cache["last_answer"] = float(answer)  # save last answer to allow continues calculations
            return repr(answer)  # repr - solve str rounding

        except KeyError:
            return "Please enter a valid math operator!"


def one_number_calculation():

    operations = get_calculation_methods()
    recent_answer = cache["last_answer"]

    try:
        operator = request.form['operator']
        number = float(request.form['number1'])

    except ValueError:
        return """ERORR
                Please enter only TWO valid numbers and ONE operator
                or ONE number and ONE operator for continue a Calculation!"""

    else:
        try:
            answer = operations[operator](
                number1=recent_answer, number2=number)

            cache["last_answer"] = answer
            return repr(answer)  # repr - solve str rounding

        except KeyError:
            return "Please enter a valid math operator!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)