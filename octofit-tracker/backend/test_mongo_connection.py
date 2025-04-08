import logging
from pymongo import MongoClient, errors

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Connect to MongoDB
    logging.info('Connecting to MongoDB...')
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=5000)
    db = client['octofit_db']

    # Test the connection
    logging.info('Testing MongoDB connection...')
    client.server_info()  # Will raise an exception if the connection fails

    # Insert sample data into the 'users' collection
    logging.info('Inserting sample data into the users collection...')
    sample_users = [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password1"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password2"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password3"},
        {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password4"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password5"},
    ]

    # Clear existing data and insert new data
    db.users.delete_many({})  # Clear the collection
    db.users.insert_many(sample_users)  # Insert sample data

    # Retrieve and print the data to verify
    logging.info('Retrieving data from the users collection...')
    users = db.users.find()
    logging.info('Users in the database:')
    for user in users:
        logging.info(user)

except errors.ServerSelectionTimeoutError as err:
    logging.error(f'Failed to connect to MongoDB: {err}')
except Exception as e:
    logging.error(f'An error occurred: {e}')
