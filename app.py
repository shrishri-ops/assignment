from flask import Flask, jsonify
from database_handler import get_latest_data, create_table
import config_parser
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Use /config after http://127.0.0.1:500"

@app.route('/config', methods=['GET'])
def get_config_data():
    data = get_latest_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "No configuration data found"}), 404

if __name__ == '__main__':
    # Ensure the database table is created before starting the server
    create_table()

    # Optionally parse and store config data on startup
    config_data = config_parser.parse_config('config.ini')
    if config_data:
        from database_handler import save_to_database
        save_to_database(json.dumps(config_data))

    # Run the Flask app
    app.run(debug=True)
