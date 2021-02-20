from flask import Flask, render_template, request
import sqlite3

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))
                con.commit()
                msg = "Employee successfully Added"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("success.html",msg = msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Employees")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)