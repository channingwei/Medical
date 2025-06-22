from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load word parts from JSON
with open('data/unique_1000_medical_word_parts.json') as f:
    terms = json.load(f)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Flashcards page
@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

# Quiz page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# Matching page
@app.route('/match')
def match():
    return render_template('match.html')

# API: All terms, organized by virtual chapters
@app.route('/api/terms')
def api_terms():
    all_terms = []
    for term in terms:
        term_copy = term.copy()

        # Assign virtual chapters based on type
        if term['type'] == 'prefix':
            term_copy["chapter"] = "Prefixes"
        elif term['type'] == 'root':
            term_copy["chapter"] = "Root Words"
        elif term['type'] == 'suffix':
            term_copy["chapter"] = "Suffixes"
        elif term['type'] == 'variant':
            term_copy["chapter"] = "Variants"
        else:
            term_copy["chapter"] = "Other Terms"

        all_terms.append(term_copy)

    return jsonify(all_terms)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
