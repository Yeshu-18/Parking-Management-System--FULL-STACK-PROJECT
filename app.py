from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mycon

app = Flask(__name__)

# Database connection
con = mycon.connect(host='localhost', user='root', password="Yeshu@2004", database="Parking")
cur = con.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        e = request.form['v_no'].lower()
        n = request.form['name']
        d = request.form['v_type']
        s = int(request.form['charged'])
        t = "now()"
        query = "insert into TEST6(V_No,Name,V_Type,Charged,Timing) values('{}','{}','{}',{},{})".format(e, n, d, s, t)
        cur.execute(query)
        con.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ch = int(request.form['choice'])
        if ch == 1:
            cur.execute("select * from TEST6 order by Timing desc")
            result = cur.fetchall()
            return render_template('details.html', result=result)
        elif ch == 2:
            v_no = request.form['v_no']
            cur.execute("select * from TEST6 where V_No='{}' order by Timing desc".format(v_no))
            result = cur.fetchall()
            return render_template('details.html', result=result)
        elif ch == 3:
            cur.execute("select * from TEST6 where Status='{}' order by Timing desc".format('in'))
            result = cur.fetchall()
            return render_template('details.html', result=result)
    return render_template('search.html')

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    if request.method == 'POST':
        ch = int(request.form['choice'])
        if ch == 1:
            v_no = request.form['v_no']
            d = request.form['v_type']
            s = int(request.form['charged'])
            cur.execute("update TEST6 set V_Type='{}',Charged={} where V_No='{}'".format(d, s, v_no))
            con.commit()
            return redirect(url_for('index'))
        elif ch == 2:
            v_no = request.form['v_no']
            cur.execute("delete from TEST6 where V_No='{}'".format(v_no))
            con.commit()
            return redirect(url_for('index'))
        elif ch == 3:
            v_no = request.form['v_no']
            cur.execute("update TEST6 set Status='{}',Out_time={} where V_No='{}'".format('out', "now()", v_no))
            con.commit()
            return redirect(url_for('index'))
    return render_template('modify.html')

if __name__ == '__main__':
    app.run(debug=True)