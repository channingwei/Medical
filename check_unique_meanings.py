import json
import re

# Load the original data
with open('data/all_chapters_terms_by_chapter.json') as f:
    data = json.load(f)

print(f"Original total terms: {len(data)}")

# Group by cleaned term and check for different meanings
term_meanings = {}

for term in data:
    # Clean up the term text (same as before)
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
    
    if clean_term not in term_meanings:
        term_meanings[clean_term] = set()
    
    term_meanings[clean_term].add(term['meaning'])

# Show terms with multiple meanings
print("\nTerms with multiple meanings:")
multi_meaning_terms = []
for term, meanings in term_meanings.items():
    if len(meanings) > 1:
        print(f"{term}: {meanings}")
        multi_meaning_terms.append((term, meanings))

print(f"\nTotal terms with multiple meanings: {len(multi_meaning_terms)}")

# Create expanded dataset with all unique meanings
expanded_terms = []
for term, meanings in term_meanings.items():
    for meaning in meanings:
        # Find the first occurrence of this term-meaning combination
        for original_term in data:
            clean_original = original_term['term']
            for pattern, replacement in replacements.items():
                clean_original = re.sub(pattern, replacement, clean_original)
            
            if clean_original == term and original_term['meaning'] == meaning:
                expanded_terms.append({
                    'term': term,
                    'type': original_term['type'],
                    'meaning': meaning
                })
                break

print(f"\nExpanded unique terms (preserving different meanings): {len(expanded_terms)}")

# Show the expanded terms
print("\nExpanded unique terms:")
for i, term in enumerate(expanded_terms, 1):
    print(f"{i:2d}. {term['term']} ({term['type']}) - {term['meaning']}")

# Save expanded data
with open('data/expanded_terms.json', 'w') as f:
    json.dump(expanded_terms, f, indent=2)

print(f"\nExpanded data saved to 'data/expanded_terms.json'") 