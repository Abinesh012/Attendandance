# import pymongo
from flask import Flask, request, jsonify, redirect #,session
from flask_pymongo import PyMongo
from flask_cors import CORS
# from bson import ObjectId
# from flask_session import Session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pinaca'  # Replace with your desired secret key
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'  # Replace with your MongoDB connection URI
app.config['SESSION_TYPE'] = 'mongodb'  # Use MongoDB to store session data
CORS_ALLOW_ALL_ORIGINS = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Session(app)
mongo = PyMongo(app)

# Signup API endpoint
@app.route('/api/signup', methods=['POST'])
def signup():
    # Get the user details from the request
    user_data = {
        'roll_number': request.json['roll_number'],
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'department': request.json['department'],
        'user_type': request.json['user_type'],
        'email': request.json['email'],
        'phone_number': request.json['phone'],
        'password': request.json['password']
    }
    # Check if the roll number, email, or phone number already exists
    existing_user = mongo.db.users.find_one({
        '$or': [
            {'roll_number': user_data['roll_number']},
            {'email': user_data['email']},
            {'phone_number': user_data['phone_number']}
        ]
    })
    if existing_user:
        if existing_user.get('roll_number') == user_data['roll_number']:
            return jsonify({'message': 'Roll number already used'}), 409
        elif existing_user.get('email') == user_data['email']:
            return jsonify({'message': 'Email already used'}), 409
        elif existing_user.get('phone_number') == user_data['phone_number']:
            return jsonify({'message': 'Phone number already used'}), 409
    # Insert the user into the 'users' collection
    mongo.db.users.insert_one(user_data)

    return jsonify({'message': 'User registered successfully'}), 201


# @app.route('/api/delete_collections', methods=['DELETE'])
# def delete_collections():
#     try:
#         # Get the list of collection names in the database
#         collection_names = mongo.db.list_collection_names()
#         # Delete each collection in the database
#         for collection_name in collection_names:
#             mongo.db.drop_collection(collection_name)
#         return jsonify({'message': 'All collections deleted successfully'})
#     except Exception as e:
#         return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


# API endpoint to get a list of users by type
@app.route('/api/users/<user_type>', methods=['GET'])
def get_users_by_type(user_type):
    # Find users with the specified user type
    users = mongo.db.users.find({'user_type': user_type})

    # Prepare the response data
    user_list = []
    for user in users:
        user_data = {
            'roll_number': user['roll_number'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'user_type': user['user_type'],
            'email': user['email'],
            'phone_number': user['phone_number']
        }
        user_list.append(user_data)
    return jsonify(user_list)

# @app.route('/api/login', methods=['POST'])
# def login():
#     # Get the user credentials from the request
#     login_data = {
#         'roll_number': request.json['roll_number'],
#         'password': request.json['password']
#     }
#     # Find the user with matching roll number and password
#     user = mongo.db.users.find_one({'roll_number': login_data['roll_number'], 'password': login_data['password']})
#     if user:
#         # Prepare the response data with restricted fields
#         user_data = {
#             'roll_number': user['roll_number'],
#             'first_name': user['first_name'],
#             'last_name': user['last_name'],
#             'user_type': user['user_type']
#         }
#         return jsonify(user_data)
#     else:
#         return jsonify({'message': 'Invalid credentials'}), 401

# @app.route('/api/login', methods=['POST'])
# def login():
#     # Get the login credentials from the request
#     login_data = {
#         'roll_number': request.json['roll_number'],
#         'password': request.json['password']
#     }
#
#     # Check if the user exists and the password is correct
#     user = mongo.db.users.find_one({'roll_number': login_data['roll_number']})
#     if not user or user['password'] != login_data['password']:
#         return jsonify({'message': 'Invalid credentials'}), 401
#
#     # Create a session for the logged-in user
#     session['roll_number'] = user['roll_number']
#     session['first_name'] = user['first_name']
#     session['last_name'] = user['last_name']
#     session['user_type'] = user['user_type']
#
#     return jsonify({'message': 'Login successful'}), 200

# Login API endpoint
# @app.route('/api/login', methods=['POST'])
# def login():
#     # Get the login credentials from the request
#     login_data = {
#         'roll_number': request.json['roll_number'],
#         'password': request.json['password']
#     }
#
#     # Check if the user exists and the password is correct
#     user = mongo.db.users.find_one({'roll_number': login_data['roll_number']})
#     if not user or user['password'] != login_data['password']:
#         return jsonify({'message': 'Invalid credentials'}), 401
#
#     # Create a session for the logged-in user
#     session['roll_number'] = user['roll_number']
#     session['first_name'] = user['first_name']
#     session['last_name'] = user['last_name']
#     session['user_type'] = user['user_type']
#
#     # Return the user data in the response
#     user_data = {
#         'roll_number': user['roll_number'],
#         'first_name': user['first_name'],
#         'last_name': user['last_name'],
#         'user_type': user['user_type']
#     }
#     return jsonify(user_data), 200

# Login API endpoint
# @app.route('/api/login', methods=['POST'])
# def login():
#     # Get the login credentials from the request
#     login_data = {
#         'roll_number': request.form.get('roll_number'),
#         'password': request.form.get('password')
#     }
#
#     # Check if the user exists and the password is correct
#     # user = mongo.db.users.find_one({'roll_number': login_data('roll_number')})
#     # if not user or user['password'] != login_data['password']:
#     #     return jsonify({'message': 'Invalid credentials'}), 401
#
#     user = mongo.db.users.find_one({'roll_number': login_data['roll_number']})
#     if not user or user['password'] != login_data['password']:
#         return jsonify({'message': 'Invalid credentials'}), 401
#
#     # Create a session for the logged-in user
#     session['user_id'] = str(user['_id'])
#
#     # Return the user data in the response
#     user_data = {
#         'roll_number': user['roll_number'],
#         'first_name': user['first_name'],
#         'last_name': user['last_name'],
#         'user_type': user['user_type']
#     }
#     return jsonify(user_data), 200

from bson import ObjectId

# @app.route('/api/login', methods=['POST','GET'])
# def login():
#     # Get the login credentials from the request form data
#     roll_number = request.form.get('roll_number')
#     password = request.form.get('password')
#     print(type(roll_number))
#     print(type(password))
#     # Check if the required fields are present
#     if not roll_number or not password:
#         return jsonify({'message': 'Invalid request'}), 400
#
#     # Check if the user exists and the password is correct
#     user = mongo.db.users.find_one({'roll_number': roll_number})
#     if not user or user['password'] != password:
#         return jsonify({'message': 'Invalid credentials'}), 401
#
#     # Convert ObjectId to string for serialization
#     user['_id'] = str(user['_id'])
#
#     return jsonify(user), 200
#
# API endpoint for user login
# @app.route('/api/login', methods=['POST'])
# def login():
#     # Get the login credentials from the request
#     roll_number = request.json['roll_number']
#     password = request.json['password']
#
#     # Find the user with the provided roll number
#     user = mongo.db.users.find_one({'roll_number': roll_number})
#
#     # Check if the user exists and the password matches
#     if user and user['password'] == password:
#         # Prepare the response with limited user details
#         response = {
#             'roll_number': user['roll_number'],
#             'first_name': user['first_name'],
#             'last_name': user['last_name'],
#             'user_type': user['user_type']
#         }
#         return jsonify(response), 200
#
#     # Return error message if login credentials are invalid
#     return jsonify({'message': 'Invalid roll number or password'}), 401

@app.route('/api/login/status', methods=['POST'])
def login_status():
    # Get the login credentials from the request
    roll_number = request.json['roll_number']
    password = request.json['password']
    # Find the user with the provided roll number
    user = mongo.db.users.find_one({'roll_number': roll_number})
    # Check if the user exists and the password matches
    if user and user['password'] == password:
        # Redirect to another page
        return redirect('/api/details?roll_number=' + roll_number)
    return jsonify({'status': 'failed'}), 401

@app.route('/api/details', methods=['GET'])
def login_details():
    # Get the roll number from the query parameters
    roll_number = request.args.get('roll_number')
    # Find the user with the provided roll number
    user = mongo.db.users.find_one({'roll_number': roll_number})
    # Check if the user exists
    if user:
        # Prepare the response with user details
        response = {
            'roll_number': user['roll_number'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'user_type': user['user_type']
        }
        return jsonify(response), 200
    return jsonify({'message': 'User not found'}), 404





# Example protected API endpoint that requires authentication
# @app.route('/api/protected', methods=['GET'])
# def protected():
#     if 'user_id' not in session:
#         return jsonify({'message': 'Authentication required'}), 401
#
#     # Fetch user data based on the stored user_id
#     user = mongo.db.users.find_one({'_id': session['user_id']})
#
#     # Return the protected data
#     protected_data = {
#         'roll_number': user['roll_number'],
#         'first_name': user['first_name'],
#         'last_name': user['last_name'],
#         'user_type': user['user_type'],
#         'protected_info': 'This is protected data accessible only to authenticated users.'
#     }
#     return jsonify(protected_data), 200



# Attendance API endpoint
@app.route('/api/mark_attendance', methods=['POST'])
def mark_attendance():
    # Get the attendance details from the request
    attendance_data = {
        'roll_number': request.json['roll_number'],
        'date': request.json['date'],
        'is_present': request.json['is_present']
    }

    # Check if the user exists
    user = mongo.db.users.find_one({'roll_number': attendance_data['roll_number']})
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Check if attendance record already exists for the user and date
    existing_attendance = mongo.db.attendance.find_one({'roll_number': attendance_data['roll_number'],
                                                        'date': attendance_data['date']})
    if existing_attendance:
        # Update the existing attendance record
        mongo.db.attendance.update_one({'_id': existing_attendance['_id']},
                                       {'$set': {'is_present': attendance_data['is_present']}})
    else:
        # Insert a new attendance record
        attendance = {
            'roll_number': attendance_data['roll_number'],
            'date': attendance_data['date'],
            'is_present': attendance_data['is_present']
        }
        mongo.db.attendance.insert_one(attendance)

    return jsonify({'message': 'Attendance marked successfully'}), 201


@app.route('/api/attendance/<roll_number>', methods=['GET'])
def get_attendance_details(roll_number):
    # Find attendance details for the specified roll number
    attendance = mongo.db.attendance.find({'roll_number': roll_number})

    # Prepare the response data
    attendance_list = []
    for record in attendance:
        attendance_data = {
            'date': record['date'],
            'is_present': record['is_present']
        }
        attendance_list.append(attendance_data)

    return jsonify(attendance_list)

@app.route('/api/attendance/department/<department>/date/<date>', methods=['GET'])
def get_attendance_by_department_and_date(department, date):
    # Find attendance records for the specified department and date
    attendance = mongo.db.attendance.find({'department': department, 'date': date})

    # Prepare the response
    result = []
    for record in attendance:
        result.append({
            'roll_number': record['roll_number'],
            'present': record['present']
        })

    return jsonify(result), 200


@app.route('/api/attendance/department/<department>/start_date/<start_date>/end_date/<end_date>', methods=['GET'])
def get_attendance_by_department_and_date_range(department, start_date, end_date):
    # Find attendance records for the specified department and date range
    attendance = mongo.db.attendance.find({
        'department': department,
        'date': {'$gte': start_date, '$lte': end_date}
    })

    # Prepare the response
    result = []
    for record in attendance:
        result.append({
            'roll_number': record['roll_number'],
            'date': record['date'],
            'present': record['present']
        })

    return jsonify(result), 200

# # API endpoint to get list of users' roll numbers based on type
# @app.route('/api/users/type_roll_number', methods=['GET'])
# def type_roll_number(user_type):
#     # Find users with the specified user type
#     users = mongo.db.users.find({'user_type': user_type}, {'roll_number': 1, '_id': 0})
#
#     # Extract roll numbers from the users
#     roll_numbers = [user['roll_number'] for user in users]
#
#     return jsonify({'roll_numbers': roll_numbers}), 200
#
# # API endpoint to get user details by roll number
# @app.route('/api/users/roll_number/<roll_number>', methods=['GET'])
# def get_user_by_roll_number(roll_number):
#     # Find the user with the specified roll number
#     user = mongo.db.users.find_one({'roll_number': roll_number})
#
#     if not user:
#         return jsonify({'message': 'User not found'}), 404
#
#     # Prepare the response data
#     user_data = {
#         'roll_number': user['roll_number'],
#         'first_name': user['first_name'],
#         'last_name': user['last_name'],
#         'user_type': user['user_type'],
#         'email': user['email'],
#         'phone_number': user['phone_number']
#     }
#     return jsonify(user_data)

# # Delete all attendance records API endpoint
# @app.route('/api/delete_all_attendance', methods=['DELETE'])
# def delete_all_attendance():
#     # Delete all attendance records
#     mongo.db.attendance.delete_many({})
#
#     return jsonify({'message': 'All attendance records deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
