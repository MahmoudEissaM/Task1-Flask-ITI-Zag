from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Company
from forms import CompanyForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///companies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    if not Company.query.first():
        initial_companies = [
            Company(
                name="TechVision",
                location="Cairo, Egypt",
                description="A leading tech company specialized in AI solutions.",
                employees_count=120
            ),
            Company(
                name="GreenFarm",
                location="Alexandria, Egypt",
                description="Agricultural company focusing on organic products.",
                employees_count=85
            )
        ]
        db.session.add_all(initial_companies)
        db.session.commit()

@app.route('/')
def home():
    companies = Company.query.all()
    return render_template('company_list.html', companies=companies)

@app.route('/companies')
def get_companies():
    companies = Company.query.all()
    return render_template('company_list.html', companies=companies)

@app.route('/companies/new')
def new_company():
    form = CompanyForm()
    return render_template('create_company.html', form=form)

@app.route('/companies/create', methods=['POST'])
def create_company():
    form = CompanyForm()
    if form.validate_on_submit():
        company = Company(
            name=form.name.data,
            location=form.location.data,
            description=form.description.data,
            employees_count=form.employees_count.data
        )
        db.session.add(company)
        db.session.commit()
        flash('Company added successfully!', 'success')
        return redirect(url_for('get_companies'))
    return render_template('create_company.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
