from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'askhr-mysql.cfm04ccm0uyy.eu-north-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Arslanredemption1'
app.config['MYSQL_DB'] = 'askhr'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/leave-balance/<employee_id>', methods=['GET'])
def get_leave_balance(employee_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM leave_balance WHERE employee_id = %s", (employee_id,))
    result = cur.fetchone()
    cur.close()
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)