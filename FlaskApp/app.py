from flask import Flask, render_template, request
import sqlite3 

def retrieveUsers():
    con = sqlite3.connect("bmtc.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM routes where bus_id='busid' and route_id='routeid'")
    users = cur.fetchall()
    con.close()
    return users

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method=='POST':
        busid = request.form['busid']
   	routeid = request.form['routeid']	
   	users = retrieveUsers()
	return render_template('index.html', users=users)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()