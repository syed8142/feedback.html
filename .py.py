from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import uuid

app = Flask(__name__)

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Feedback Data").sheet1

@app.route('/', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    unique_id = str(uuid.uuid4())
    row = [unique_id, data['username'], data['phone'], data['email'], data['rating'], data['comments'], ', '.join(data.get('reason', [])), data['userType']]
    sheet.append_row(row)
    return jsonify({'status': 'success', 'id': unique_id})

if '__name__' == '__main__':
    app.run(debug=True)
