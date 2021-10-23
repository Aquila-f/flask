from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:472841@Localhost:3306/forpytest"

db.init_app(app)

class mydb(db.Model):
    __tablename__ = 'mydb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=True)
    # data_created = db.Column(db.DateTime, default = datetime.now)

    def __repr__(self):
        return '<Name %r>' % self.name

    def __init__(self, id, name):
        self.id = id
        self.name = name



@app.route('/')
def index():

    # cmd_to_database
    # db.create_all()

    # cmd_to_database
    # sql_cmd = """
    #     select *
    #     from mydf
    #     """

    # query_data = db.engine.execute(sql_cmd)
    # print(query_data)
    return "of"

@app.route('/db', methods = ['POST', 'GET'])
def db():
    title = "mysql db"

    db_data = mydb.query.order_by(mydb.id)
    # if request.method == "POST":
    #     db_name = request.form['name']
    #     new_db_name = mydb(name = db_name)
    #     return "aaa"
    #     #push to db
    #     # try:
    #     #     db.session.add(new_db_name)
    #     #     db.session.commit()
    #     #     return redirect('/db')
    #     # except:
    #     #     return "error"
    # else:
    #     ids = mydb.query.order_by(mydb)
    return render_template("db.html", title = title, db_data = db_data)


if __name__ == "__main__":
    app.run()

