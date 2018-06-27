import json
from flask import Flask, render_template, Response
import logging
import webbrowser

people_string = '''
{
        "people": [
                {
                        "name": "Tom Freeman",
                        "role": "Hiring Manager",
                        "email": "tfreeman@lookingglasscyber.com",
                        "local": false
                },
                {
                        "name": "Minh Nguyen",
                        "role": "Engineer",
                        "email": "mnguyen@lookingglasscyber.com",
                        "local": true
                },
                {
                        "name": "David Horn",
                        "role": "VP. Engineering",
                        "email": "dhorn@lookingglasscyber.com",
                        "local": true
                },
                {
                        "name": "Hanh Tran",
                        "role": "Engineer",
                        "email": "dhorn@lookingglasscyber.com",
                        "local": false
                }
        ]
}
'''

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/team')
def team():
        data = json.loads(people_string)
        response = Response(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
        )
        return response
        
def main():
        #logging.basicConfig(filename='log.log', level=logging.DEBUG)
        #logging.debug('Started')
        app.run(debug=True, host='0.0.0.0', port=4321)
        #logging.debug('Fisnished')

if __name__ == '__main__':
        main()


