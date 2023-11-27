from flask import Flask, render_template
import pandas as pd
# render_template is to  get the html file into flask

app = Flask(__name__) #__name__ = the name of the file in this case file name is ((((main)))
# we need to show the station_id and station_name in the web page for user choise

stations = pd.read_csv('data_small/stations.txt',skiprows=17)
stations = stations[['STAID','STANAME                                 ']]
#to connect html file on the Flask
# @app.route('/home')  #@app is the variable name above stored as app
#
# def home():
#     return render_template('tutorial.html')
# # Flask default looks for templates folder in your route
# #  that's why we are moving the html file into templates
#
# #if you need another page do the same and create html file
#
# @app.route('/about/') # In tutorial page  we have created about cell
#                         #if we click it shows error so, we are going to add this about
#                         # to the tutorial.html file if you click about in web it will come here and acess the html about
#                         # to create url we wrote as /about/ double slash
# def about():
#     return render_template('about.html')
#
# app.run(debug=True) # debug=True is to see error on web page

# above created is just how flask work on web page
# Now, we are going to implement additonal optimize and visitile thing to our code
# we droped about and tutorila html file from templates to venu
# create a new homehtml file in templates
# beacuase evertime the user have to mention home or about in then api
@app.route('/')

def home():
    return render_template('home.html',data=stations.to_html())#this data is move to home.html file
#to show the datas in web paragraph{{data|safe}} in home.html file

@app.route('/api/vi/<station>/<date>') #<paramter> user can enter what ever they need
def about(station,date):
    filename = 'data_small/TG_STAID' + str(station).zfill(6)+'.txt' #zfill will fill with last 6 digit
    df = pd.read_csv(filename, skiprows =20, parse_dates=["    DATE"]) # skiprows = file starts from 20 th row
    # parase_date has 4 spaces before date beacasue our column in the dataframe as 4 space before it.(input column)

    #extract temperature for the paticular date.
    temperature = df.loc[df['    DATE'] == date]['    TG'].squeeze()/10 # squeeze is to get scalar type #eg: df to series of single column
    return {'station':station,
            'date':date,
            'temperature':temperature}

# it works fine now, we have to get data from user for one particular year or station (hole data)
#eg: if user need station of 10 we need to give all the 10 data
#so we to create another route
@app.route('/api/vi/<station>')
def all_data(station):
    filename = 'data_small/TG_STAID' + str(station).zfill(6)+'.txt' #zfill will fill with last 6 digit
    df = pd.read_csv(filename, skiprows =20, parse_dates=["    DATE"])
    result = df.to_dict(orient='records') # convert df to dictionary, orient='records' = convert to json
    return result
#station and only year to add in api not the date nd month
@app.route('/api/vi/yearly/<station>/<year>')
def yearly(station,year):
    filename = 'data_small/TG_STAID' + str(station).zfill(6)+'.txt'
    df = pd.read_csv(filename, skiprows=20)#, parse_dates=["    DATE"]) we are removing it becoz it changeing into year,month ans date
    # convert date column to str
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    return result

if __name__ == "__main__ ":
    app.run(debug=True)