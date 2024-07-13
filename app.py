from flask import Flask, request, send_from_directory, redirect, url_for , send_file
import hashlib

app = Flask(__name__)

# Mock credentials and corresponding PDF file mappings
VALID_USERS = {
    "43090035": {"password": "17/09/2005", "pdf": "6cdf203a1f.pdf"},
    "123456": {"password": "17/09/2005", "pdf": "8d969eef6e.pdf"}
}

def number_to_short_token(number):
    # Convert number to bytes (assuming it's a string representation)
    number_bytes = str(number).encode('utf-8')
    
    # Hash the bytes using SHA-256 (you can choose other hash algorithms like SHA-1 or MD5)
    hashed = hashlib.sha256(number_bytes).hexdigest()
    
    # Take the first 10 characters of the hashed value
    short_token = hashed[:10]
    
    return short_token

@app.route('/')
def index():
    return send_from_directory('sist.sathyabama.ac.in', 'index.html')

@app.route('/backblue.gif')
def backblue():
    return send_from_directory('', 'backblue.gif')

@app.route('/fade.gif')
def fade():
    return send_from_directory('', 'fade.gif')

@app.route('/sist_ese_june_2024/login.html', methods=['GET', 'POST'])
def login():
    print("====")
  
    if request.method == 'POST':
      
        regno = request.form['regno']
        password = request.form['dob']
        
        # Simulating authentication
        print(f" PDF REQUEST CAME {regno} : : {password} ")
        if regno in VALID_USERS and password == VALID_USERS[regno]["password"]:  
            return redirect(url_for('serve_pdf', regno=regno))
        else:
            return "Invalid credentials, please try again.", 401

    return send_from_directory('sist.sathyabama.ac.in/sist_ese_june_2024', 'login.html')

@app.route('/pdf/<regno>')
def serve_pdf(regno):
    if regno in VALID_USERS:
        pdf_filename = VALID_USERS[regno]["pdf"]
        token = number_to_short_token(regno)
        pdf_filename = f"{token}.pdf"
        # Assuming the PDF files are stored in the same directory as your Flask app
        return send_from_directory('', pdf_filename)
    else:
        return "User not authorized to access PDF.", 401


# Catch-all for other static files
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run(debug=True)
