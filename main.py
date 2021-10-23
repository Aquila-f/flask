from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:472841@Localhost:3306/forpytest"

db.init_app(app)

class mydf(db.Model):
    __tablename__ = 'mydf'
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)

    def __repr__(self):
        return '<Name %r>' % self.id

    def __init__(self, id, num):
        self.id = id
        self.num = num



@app.route('/db')
def db():
    title = "mysql db"
    return render_template("db.html", title = title)


@app.route('/')
def index():

    # cmd_to_database
    db.create_all()

    # cmd_to_database
    sql_cmd = """
        select *
        from mydf
        """

    query_data = db.engine.execute(sql_cmd)
    # x1 = query_data['id']
    # x2 = query_data['num']
    print(query_data)
    return "of"


if __name__ == "__main__":
    app.run()

