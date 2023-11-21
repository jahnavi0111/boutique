from flask import Flask, render_template, request, redirect
import mysql.connector
from pymysql import IntegrityError
app = Flask(__name__)

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jahnavi127*",
        database="dbmspbl",
    )

# Routes for different tables
@app.route('/')
def index():
    return render_template('home1.html')

#--------------------------------------------------------------------------------------------------------------------------------

@app.route('/cat1')
def cat1():
    return render_template('cat1.html')

@app.route('/cat2')
def cat2():
    return render_template('cat2.html')

@app.route('/cat3')
def cat3():
    return render_template('cat3.html')

@app.route('/cat4')
def cat4():
    return render_template('cat4.html')

@app.route('/cat5')
def cat5():
    return render_template('cat5.html')

@app.route('/cat6')
def cat6():
    return render_template('cat6.html')

@app.route('/cat7')
def cat7():
    return render_template('cat7.html')
#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/customers')
def customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    customers = cursor.fetchall()
    return render_template('customers.html', customers=customers)

@app.route('/customer/<customer_id>', methods=['GET', 'POST'])
def customer_details(customer_id):
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
        conn.commit()
        conn.close()
        return redirect('/customers') 
    cursor.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))
    customer = cursor.fetchone()
    return render_template('customer.html', customer=customer)
#-----------------------------------------------------------------------------------------------------------------------------
@app.route('/products')
def products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/product/<product_id>', methods=['GET', 'POST'])
def product_details(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM product WHERE product_id=%s", (product_id,))
        conn.commit()
        conn.close()
        return redirect('/products')
    cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return render_template('product.html', product=product)
#-------------------------------------------------------------------------------------------------------------------------

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        order_id = request.form['order_id']
        cursor.execute("DELETE FROM orders WHERE order_id=%s", (order_id,))
        conn.commit()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/employees')
def employees():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    return render_template('employees.html', employees=employees)

@app.route('/employee/<employee_id>', methods=['GET', 'POST'])
def employee_details(employee_id):
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute("DELETE FROM employee WHERE employee_id=%s", (employee_id,))
        conn.commit()
        conn.close()
        return redirect('/employees')
    cursor.execute("SELECT * FROM employee WHERE employee_id=%s", (employee_id,))
    employee = cursor.fetchone()
    return render_template('employee.html', employee=employee)

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/feedbacks', methods=['GET', 'POST'])
def feedbacks():
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        feedback_id = request.form['feedback_id']
        cursor.execute("DELETE FROM feedback WHERE feedback_id=%s", (feedback_id,))
        conn.commit()
    cursor.execute("SELECT * FROM feedback")
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('feedbacks.html', feedbacks=feedbacks)

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/billings', methods=['GET', 'POST'])
def billings():
    conn = create_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        order_id = request.form['order_id']
        cursor.execute("DELETE FROM billing WHERE order_id=%s", (order_id,))
        conn.commit()
    cursor.execute("SELECT * FROM billing")
    billings = cursor.fetchall()
    conn.close()
    return render_template('billings.html', billings=billings)



@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        try:
            customer_id = request.form['customer_id']
            customer_name = request.form['customer_name']
            customer_contact = request.form['customer_contact']
            customer_address = request.form['customer_address']
            conn = create_connection()
            cursor = conn.cursor()
            insert_query = "INSERT INTO customer (customer_id, customer_name, customer_contact, customer_address) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (customer_id, customer_name, customer_contact, customer_address))
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you given. Please Recheck"
    return render_template('add_customer.html')

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            product_id = request.form['product_id']
            product_name = request.form['product_name']
            product_price = request.form['product_price']
            stock = request.form['stock']
            conn = create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO product (product_id, product_name, product_price, stock) VALUES (%s, %s, %s, %s)"
            values = (product_id, product_name, product_price, stock)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you given. Please Recheck"
    return render_template('add_product.html')

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            employee_id = request.form['employee_id']
            employee_name = request.form['employee_name']
            employee_contact = request.form['employee_contact']
            employee_address = request.form['employee_address']
            conn = create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO employee (employee_id, employee_name, employee_contact, employee_address) VALUES (%s, %s, %s, %s)"
            values = (employee_id, employee_name, employee_contact, employee_address)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you given. Please Recheck"
    return render_template('add_employee.html')

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/add_orders', methods=['GET', 'POST'])
def add_orders():
    if request.method == 'POST':
        try:
            order_id = request.form['order_id']
            product_id = request.form['product_id']
            customer_id = request.form['customer_id']
            order_date = request.form['order_date']
            total_amount = request.form['total_amount']
            conn = create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO orders (order_id, product_id, customer_id, order_date, total_amount) VALUES (%s, %s, %s, %s, %s)"
            values = (order_id, product_id, customer_id, order_date, total_amount)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you given. Please Recheck"
    return render_template('add_orders.html')

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/add_feedback', methods=['GET', 'POST'])
def add_feedback():
    if request.method == 'POST':
        try:
            feedback_id = request.form['feedback_id']
            product_id = request.form['product_id']
            customer_id = request.form['customer_id']
            rating = request.form['rating']
            conn = create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO feedback (feedback_id, product_id, customer_id, rating) VALUES (%s, %s, %s, %s)"
            values = (feedback_id, product_id, customer_id, rating)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you given. Please Recheck"
    return render_template('add_feedback.html')

#-----------------------------------------------------------------------------------------------------------

@app.route('/add_billing', methods=['GET', 'POST'])
def add_billing():
    total_amount = None
    if request.method == 'POST':
        try:
            order_id = request.form['order_id']
            cost_of_item = float(request.form['cost_of_item'])
            no_of_items = int(request.form['no_of_items'])
            total_amount = cost_of_item * no_of_items
            conn = create_connection()
            cursor = conn.cursor()
            insert_query = "INSERT INTO billing (order_id, cost_of_item, no_of_items, total_amount) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (order_id, cost_of_item, no_of_items, total_amount))
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: There is an error in the data you provided. Please recheck."
    return render_template('add_billing.html', total_amount=total_amount)

#-----------------------------------------------------------------------------------------------------------------------------

@app.route('/update_customer', methods=['GET', 'POST'])
def update_customer():
    if request.method == 'POST':
        try:
            customer_id = request.form['customer_id']
            customer_name = request.form['customer_name']
            customer_contact = request.form['customer_contact']
            customer_address = request.form['customer_address']
            conn = create_connection()
            cursor = conn.cursor()
            query = "UPDATE customer SET customer_name=%s, customer_contact=%s, customer_address=%s WHERE customer_id=%s"
            values = (customer_name, customer_contact, customer_address, customer_id)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: Please Recheck the Data"
    return render_template('update_customer.html')

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/update_product', methods=['GET', 'POST'])
def update_product():
    if request.method == 'POST':
        try:
            product_id = request.form['product_id']
            product_name = request.form['product_name']
            product_price = request.form['product_price']
            stock = request.form['stock']
            conn = create_connection()
            cursor = conn.cursor()
            query = "UPDATE product SET product_name=%s, product_price=%s, stock=%s WHERE product_id=%s"
            values = (product_name,product_price, stock, product_id)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: Please Recheck the Data"
    return render_template('update_product.html')

#-----------------------------------------------------------------------------------------------------------------------------------

@app.route('/update_orders', methods=['GET', 'POST'])
def update_orders():
    if request.method == 'POST':
        try:
            order_id = request.form['order_id']
            product_id = request.form['product_id']
            customer_id = request.form['customer_id']
            order_date = request.form['order_date']
            total_amount = request.form['total_amount']
            conn = create_connection()
            cursor = conn.cursor()
            query = "UPDATE orders SET product_id=%s, customer_id=%s, order_date=%s, total_amount=%s WHERE order_id=%s"
            values = (product_id, customer_id, order_date, total_amount,order_id)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: Please Recheck the Data"
    return render_template('update_orders.html')

#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/update_employee', methods=['GET', 'POST'])
def update_employee():
    if request.method == 'POST':
        try:
            employee_id = request.form['employee_id']
            employee_name = request.form['employee_name']
            employee_contact = request.form['employee_contact']
            employee_address = request.form['employee_address']
            conn = create_connection()
            cursor = conn.cursor()
            query = "UPDATE employee SET employee_name=%s, employee_contact=%s, employee_address=%s WHERE employee_id=%s"
            values = (employee_name, employee_contact, employee_address,employee_id)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: Please Recheck the Data"
    return render_template('update_employee.html')

#-------------------------------------------------------------------------------------------------------------------------------

@app.route('/update_feedback', methods=['GET', 'POST'])
def update_feedback():
    if request.method == 'POST':
        try:
            feedback_id = request.form['feedback_id']
            product_id = request.form['product_id']
            customer_id = request.form['customer_id']
            rating = request.form['rating']
            conn = create_connection()
            cursor = conn.cursor()
            query = "UPDATE feedback SET product_id=%s, customer_id=%s, rating=%s WHERE feedback_id=%s"
            values = (feedback_id, product_id, customer_id, rating)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
        except Exception as e:
            return f"Error: Please Recheck the Data"
    return render_template('update_feedback.html')


if __name__ == '__main__':
    app.run(debug=True)
