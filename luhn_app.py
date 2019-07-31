from flask import Flask, request, send_from_directory
import re

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.static_folder = 'static'


@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')


@app.route('/credit-card', methods=['POST'])
def cc():
    ccnumber = request.form['credit_card']

    if re.match('^3[47][0-9]{13}$', ccnumber):
        return ccnumber + ' is an American Express Credit Card'

    elif re.match('^4[0-9]{12}(?:[0-9]{3})?$', ccnumber):
        return ccnumber + ' is a Visa Credit Card'

    elif re.match('^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$',
                  ccnumber):
        return ccnumber + ' is a MasterCard Credit Card'

    print("Post method called:" + ccnumber)

    return ccnumber + ' Not a valid credit card number'


if __name__ == "__main__":
    app.run(debug=True)
