from flask import Flask
from sum_numbers_package.sum_prime_numbers import sumPrimer

app = Flask(__name__)


@app.route('/')
def sum_calculate():
    list_of_number = sumPrimer()
    return str(sum(list_of_number.calc_prime_number()))


app.run(host="0.0.0.0", port=5000, debug=True)
