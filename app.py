from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

# Uygulama açıldığında tabloyu oluştur
database.create_table()


@app.route("/")
def index():
    students = database.get_all_students()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    database.add_student(name)
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    database.delete_student(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
