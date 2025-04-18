from flask import Flask, render_template

app = Flask(__name__)

companies = [
    {
        "name": "TechVision",
        "location": "Cairo, Egypt",
        "description": "A leading tech company specialized in AI solutions.",
        "employees_count": 120
    },
    {
        "name": "GreenFarm",
        "location": "Alexandria, Egypt",
        "description": "Agricultural company focusing on organic products.",
        "employees_count": 85
    }
]

@app.route('/')
def home():
    return "Welcome to the Company Directory! Go to <a href='/companies'>companies list</a>"

@app.route('/companies')
def get_companies():
    return render_template('company_list.html', companies=companies)

if __name__ == '__main__':
    app.run(debug=True, port=5006)
