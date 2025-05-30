from flask import Flask,render_template,request
from api import api_response


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/categroy',methods=['GET', 'POST'])
def categroy():
    recipes = []
    if request.method=='POST':
        query = request.form.get('query','')
        cuisine = request.form.get('cuisine','')
        data = api_response(query, cuisine)
        recipes = data.get('results', [])
    return render_template('categroy.html',recipes=recipes)



if __name__ == '__main__':
    
    
    app.run(debug=True)