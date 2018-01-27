from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/info/<name>')
def info(name):
	return render_template('infopage.html', name=name)

@app.route('/<name>')
def home(name = None):
	return render_template('index.html')

@app.route('/domprops')
def domprops():
	return render_template('domprops.html')

@app.route('/markpage')
def markpage():
	return render_template('markpage.html')

def home(name = None):
	return render_template('index.html')

def home(name = None):
	return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/about')
def about():
    return render_template('aboutus.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4321)

