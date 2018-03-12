from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json
import re

app = Flask(__name__)

# What database to connect ant what connector
connection_string = 'mysql+pymysql://root:12345@localhost/test'
engine = create_engine(connection_string)

Base = automap_base()
Base.prepare(engine, reflect=True)

# Skapar modeller av redan befintliga tables
Users = Base.classes.users
Crypto_data = Base.classes.crypto_data
User_preferences = Base.classes.user_preferences

session = Session(engine)


def user_row_to_dict(row):
    # changes a sqlalchemy column object to a dict for user table
    # insert values from row to a dict
    row_result = dict()
    row_result['name'] = row.name
    row_result['password'] = row.password
    return row_result


def crypto_data_row_to_dict(row):
    # changes a sqlalchemy column object to a dict for crypto_data table
    # insert values from row to a dict
    row_result = dict()

    row_result['id'] = row.id
    row_result['name'] = row.name
    row_result['symbol'] = row.symbol
    row_result['rank'] = row.rank
    row_result['price_usd'] = row.price_usd
    row_result['price_btc'] = row.price_btc
    row_result['volume_24h_usd'] = row.volume_24h_usd
    row_result['market_cap_usd'] = row.market_cap_usd
    row_result['available_supply'] = row.available_supply
    row_result['total_supply'] = row.total_supply
    row_result['percent_change_1h'] = row.percent_change_1h
    row_result['percent_change_24h'] = row.percent_change_24h
    row_result['percent_change_7d'] = row.percent_change_7d
    row_result['last_updated'] = row.last_updated

    return row_result


def user_preferences_row_to_dict(row):
    # changes a sqlalchemy column object to a dict for user_preferences table
    # insert values from row to a dict
    row_result = dict()

    row_result['name'] = row.name
    row_result['city'] = row.city
    row_result['employer'] = row.employer
    row_result['age'] = row.age

    return row_result


def result_to_json(obj_list):
    # receives a list of automap objects and returns a json version
    result_list = []
    table = obj_list[0].__table__.name
    print(table)
    # Before data can be jsonified each row must be converted to a dict
    for element in obj_list:
        if (table == 'users'):
            result_list.append(user_row_to_dict(element))

        if (table == 'crypto_data'):
            result_list.append(crypto_data_row_to_dict(element))

        if (table == 'user_preferences'):
            result_list.append(user_preferences_row_to_dict(element))

    return json.dumps(result_list)


@app.route('/get_crypto_data', methods=['GET'])
def get_crypto_data():
    # In this function we're only interested in the table crypto_data
    query = session.query(Crypto_data)
    requested = request.args.to_dict()

    if (len(requested) > 1):
        print("Wrong API")
        return 'Wrong API', 54545

    if (requested.has_key('top')):
        req = requested.get('top')
        result = query.limit(req).all()
        # add the resulting components in a dict that can be jsonified
        result_json = result_to_json(result)
        print (result_json)
        return result_json

    # Below not done. Should return a single row with the requested name
    if (requested.has_key('name')):
        req = requested.get('name')
        # DO something
        return 'success', 200
    return 'success', 200


if __name__ == '__main__':
    app.run(debug=True)
