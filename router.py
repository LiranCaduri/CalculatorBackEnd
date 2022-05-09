from flask import Flask, request
from CalculationsFunctions import get_calculation_methods


app = Flask(__name__)

operations = get_calculation_methods()
cache = {
    "last_answer": 0
}


@app.route('/')
def cache_answer():
    return str(cache['last_answer'])


@app.route('/', methods=['POST'])
def calc():
    try:
        if len(dict(request.form)) < 3:
            answer = one_number_calculation()
        else:
            answer = two_number_calculation()
       
        if(type(answer) is ZeroDivisionError):
            # response for Division in zero
            return "Error: Division in 0"

        # save last answer to allow continues calculations
        cache["last_answer"] = float(answer)

        return repr(answer)  # repr - solve str rounding

    except (ValueError, KeyError):
        """ catch:
            ValueError - if user didn't provide a number
            KeyError -  if user did didn't provide enough variables or a valid operator
        """

        return """ERORR
                Please enter only TWO valid numbers and ONE operator
                or ONE number and ONE operator to continue a Calculation!"""


def two_number_calculation():
    operator = request.form['operator']
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])

    answer = operations[operator](number1=number1, number2=number2)
    
    return answer


def one_number_calculation():
    recent_answer = cache["last_answer"]

    operator = request.form['operator']
    number = float(request.form['number1'])

    answer = operations[operator](number1=recent_answer, number2=number)

    return answer
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)


"""
Request Body

{
    "operator": <char: (/, *, -, +)>
    "number1": <number>
    "number2": <number>, optional
}
"""