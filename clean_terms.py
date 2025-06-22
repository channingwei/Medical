import json
import re

# Load the data
with open('data/all_chapters_terms_by_chapter.json') as f:
    data = json.load(f)

print(f"Original total terms: {len(data)}")

# Clean up the terms
cleaned_terms = []
seen_terms = set()

for term in data:
    # Clean up the term text
    clean_term = term['term']
    
    # Fix common typos and standardize
    replacements = {
        r'gastr/\d+': 'gastr/o',
        r'dermat/\d+': 'dermat/o', 
        r'oste/\d+': 'oste/o',
        r'7ste/\d+': 'oste/o',
        r'4ste/\d+': 'oste/o',
        r'5ste/\d+': 'oste/o',
        r'3ste/\d+': 'oste/o',
        r'2ste/\d+': 'oste/o',
        r'1ste/\d+': 'oste/o',
        r'0ste/\d+': 'oste/o',
        r'8ste/\d+': 'oste/o',
        r'9ste/\d+': 'oste/o',
        r'pulm\d+n/\d+': 'pulmon/o',
        r'cyt/\d+': 'cyt/o',
        r'cardi/\d+': 'cardi/o',
        r'neur/\d+': 'neur/o',
        r'hepat/\d+': 'hepat/o',
        r'enter/\d+': 'enter/o',
        r'cephal/\d+': 'cephal/o'
    }
    
    for pattern, replacement in replacements.items():
        clean_term = re.sub(pattern, replacement, clean_term)
    
    # Create a unique key for deduplication
    term_key = f"{clean_term}_{term['meaning']}"
    
    if term_key not in seen_terms:
        seen_terms.add(term_key)
        cleaned_term = {
            'term': clean_term,
            'type': term['type'],
            'meaning': term['meaning']
        }
        cleaned_terms.append(cleaned_term)

print(f"Cleaned unique terms: {len(cleaned_terms)}")

# Show the cleaned terms
print("\nCleaned unique terms:")
for i, term in enumerate(cleaned_terms, 1):
    print(f"{i:2d}. {term['term']} ({term['type']}) - {term['meaning']}")

# Group by type
types = {}
for term in cleaned_terms:
    term_type = term['type']
    if term_type not in types:
        types[term_type] = []
    types[term_type].append(term)

print(f"\nTerms by type:")
for term_type, terms in types.items():
    print(f"{term_type}: {len(terms)} terms")

# Save cleaned data
with open('data/cleaned_terms.json', 'w') as f:
    json.dump(cleaned_terms, f, indent=2)

print(f"\nCleaned data saved to 'data/cleaned_terms.json'") 