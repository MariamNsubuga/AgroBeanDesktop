from sqlalchemy import create_engine
import petl as etl
import sqlite3
from flask import g
db_connect = create_engine('postgres://awjzgmwqiatzjg:e4424ae3d375e2057bcc9cde832672940d44ea2c05260e28ccb04dc1575ec52d@ec2-34-204-22-76.compute-1.amazonaws.com:5432/dabbhqt4pegslv')
table = etl.fromdb(db_connect,"select * from result")
# print(etl.look(table))
connection = sqlite3.connect('example.db')
etl.todb(table, connection, 'agrobean_results')

