from flask import Flask, render_template
# render_template is to  get the html file into flask

app = Flask('website')

#to connect html file on the Flask
@app.route('/home')  #@app is the variable name above stored as app

def home():
    return render_template('tutorial.html')
# Flask default looks for templates folder in your route
#  that's why we are moving the html file into templates

#if you need another page do the same and create html file

@app.route('/about/') # In tutorial page  we have created about cell
                        #if we click it shows error so, we are going to add this about
                        # to the tutorial.html file if you click about in web it will come here and acess the html about
                        # to create url we wrote as /about/ double slash
def about():
    return render_template('about.html')

app.run(debug=True) # debug=True is to see error on web page