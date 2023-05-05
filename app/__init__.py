"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaage3hp8u791gu11kg-a.oregon-postgres.render.com",
        database="todo_e5ep",
        user="root",
        password="kxTC2StcEPvZ1dseoqri3DfoV3DfPWMz")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
