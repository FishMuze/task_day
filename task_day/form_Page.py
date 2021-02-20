from flask import Flask, render_template, request
import sqlite3



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_Queue")
def add():
    return render_template("add_Queue.html")

@app.route("/savedetails", methods=["POST","GET"])
def saveDetails():
    msg = "Hello"
    if request.method == 'POST':
        try:
            amba = request.form["amba"]
            queue_id = request.form["queue_id"]
            amount = request.form["amount"]
            task_counter = request.form["task_counter"]
            state = request.form["state"]
            reason = request.form["reason"]
            print(amba)

            with sqlite3.connect("amba.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into ambassador (amba, queue_id, amount, task_counter, state, reason) values (?,?,?,?,?,?)",(amba,queue_id,amount,task_counter,state,reason))
                con.commit()
                msg = "Employee added successfully"
        except:
            con.rollback()
            msg = "We cannot add the employee "

        finally:
            return render_template("success.html", msg=msg)
            con.close()



@app.route("/display")
def view():
    con = sqlite3.connect("amba.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from ambassador")
    rows = cur.fetchall()
    return render_template("display.html",rows = rows)



@app.route("/delete")
def deletedetails():
    return render_template("/delete.html")


@app.route("/deletedetails", methods=["POST"])
def deleterecord():
    amba = request.form["amba"]
    queue_id = request.form["queue_id"]
    with sqlite3.connect("amba.db") as con:
        try:
            cur = con.cursor()

            cur.execute("delete from ambassador where amba = ?", (amba,))
            cur.execute("delete from ambassador where queue_id = ?", (queue_id,))
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete.html", msg=msg)