from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        # Extract data from the request, if needed
        # e.g., message_content = request.json.get('content')

        # Perform any actions you need (e.g., send a message to Telegram)

        # Respond with a success message
        return jsonify({'message': 'Message sent successfully'}), 200
    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

