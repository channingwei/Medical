from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load word parts from JSON
with open('data/unique_1000_medical_word_parts.json') as f:
    terms = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/match')
def match():
    return render_template('match.html')

@app.route('/api/terms')
def api_terms():
    # Organize terms by type as virtual chapters
    all_terms = []
    
    for term in terms:
        term_copy = term.copy()
        
        # Create chapter names based on type
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

from flask import Flask

app = Flask(__name__)

# Your routes here...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

