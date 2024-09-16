from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



# Lists to store data
main_data = []
feedback_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission from main page
        name = request.form.get('name')
        mobile = request.form.get('mobile')
        bill_number = request.form.get('billNumber')
        experience = request.form.get('experience')
        
        # Store data in the main_data list
        main_data.append({
            'name': name,
            'mobile': mobile,
            'bill_number': bill_number,
            'experience': experience
        })
        
        if experience == 'negative':
            # Redirect to feedback page if experience is negative
            now = datetime.now()
            # Format date as Y-M-D
            cdate = now.strftime("%Y-%m-%d")
            # Format time as XX:XX
            ctime = now.strftime("%H:%M")
            return redirect(url_for('feedback', name=name, mobile=mobile, billNumber=bill_number))




        else:
            # Redirect to Google review page if experience is positive
            return redirect('https://search.google.com/local/writereview?placeid=ChIJA7Zo0DFxqDsRmk9BBAmeXN8')
    
    return render_template('main.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Handle form submission from feedback page
        name = request.form.get('name')
        mobile = request.form.get('mobile')
        bill_number = request.form.get('billNumber')
        feedback_text = request.form.get('feedback')
        improvement_areas = request.form.getlist('improvementAreas')
        
        # Store feedback data in the feedback_data list
        feedback_data.append({
            'name': name,
            'mobile': mobile,
            'bill_number': bill_number,
            'feedback': feedback_text,
            'improvement_areas': improvement_areas
        })
        
        return jsonify({'message': 'Feedback submitted successfully'})
    
    # For GET requests, render the feedback form
    name = request.args.get('name')
    mobile = request.args.get('mobile')
    bill_number = request.args.get('billNumber')
    return render_template('feedback.html', name=name, mobile=mobile, bill_number=bill_number)

@app.route('/data', methods=['GET'])
def get_data():
    # Route to view stored data (for demonstration purposes)
    return jsonify({
        'main_data': main_data,
        'feedback_data': feedback_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
