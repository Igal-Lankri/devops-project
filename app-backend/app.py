from flask import Flask, jsonify
from flask_cors import CORS  # נדרש כדי לאפשר גישה מהפרונטאנד

app = Flask(__name__)
CORS(app)  # מאפשר גישה מכל דומיין (לא מאובטח לפרודקשן, מצוין לפרויקט שלנו)

# אנו שומרים את ההצבעות בזיכרון. בפרויקט אמיתי נשתמש בבסיס נתונים.
votes = {
    'cats': 0,
    'dogs': 0
}

@app.route('/vote/<option>', methods=['POST'])
def vote(option):
    """מקבל הצבעה עבור 'cats' או 'dogs' ומגדיל את הספירה."""
    if option in votes:
        votes[option] += 1
        return jsonify(votes), 200
    return jsonify({"error": "Invalid option"}), 400

@app.route('/votes', methods=['GET'])
def get_votes():
    """מחזיר את סך ההצבעות הנוכחי."""
    return jsonify(votes)

if __name__ == '__main__':
    # אנו מאזינים על 0.0.0.0 כדי להיות נגישים מחוץ לקונטיינר
    app.run(host='0.0.0.0', port=5000)
