import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lifx API token
LIFX_API_TOKEN = '<TOKEN>'

# Lifx API base URL
LIFX_API_BASE_URL = 'https://api.lifx.com/v1/lights/'

# Function to send requests to Lifx API
def send_lifx_request(selector, data):
    headers = {
        'Authorization': 'Bearer ' + LIFX_API_TOKEN,
    }
    url = LIFX_API_BASE_URL + selector + '/state'
    response = requests.put(url, headers=headers, json=data)
    if response.status_code <= 207:
        print('Lifx request successful')
    else:
        print('Error sending Lifx request:', response.status_code, response.text)

# Route to handle Sleep as Android events
@app.route('/sleep', methods=['POST'])
def handle_sleep_as_android_webhook():
    # Parse JSON request body
    request_data = request.get_json()

    # Extract event name
    event_name = request_data.get('event')

    if event_name == 'alarm_alert_start':
        # Handle alarm start event
        # Example: Fading light from off to bright white over 10 minutes
        data = {
            'power': 'on',
            'brightness': 1.0,
            'color': 'kelvin:6500',
            'duration': 600,  # 10 minutes in seconds
        }
        send_lifx_request('all', data)
        return jsonify({'message': 'Alarm start event handled successfully'})

    elif event_name == 'alarm_alert_dismiss':
        # Handle alarm dismiss event
        # Example: Turn light on solid full bright white
        data = {
            'power': 'on',
            'brightness': 1.0,
            'color': 'kelvin:6500',
            'duration': 0,  # No transition
        }
        send_lifx_request('all', data)
        return jsonify({'message': 'Alarm dismiss event handled successfully'})

    else:
        # Unknown event
        print('Unknown event : ' + event_name)
        return jsonify({'error': 'Unknown event'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21122, debug=True)