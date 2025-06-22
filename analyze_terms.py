import json

# Load the data
with open('data/all_chapters_terms_by_chapter.json') as f:
    data = json.load(f)

print(f"Total terms in file: {len(data)}")

# Count unique terms
unique_terms = {}
for term in data:
    term_key = term['term']
    if term_key not in unique_terms:
        unique_terms[term_key] = []
    unique_terms[term_key].append(term)

print(f"Unique terms: {len(unique_terms)}")

# Show all unique terms with their details
print("\nAll unique terms:")
for i, (term, occurrences) in enumerate(unique_terms.items(), 1):
    first_occurrence = occurrences[0]
    print(f"{i:2d}. {term} ({first_occurrence['type']}) - {first_occurrence['meaning']}")

# Group by type
types = {}
for term in data:
    term_type = term['type']
    if term_type not in types:
        types[term_type] = []
    types[term_type].append(term)

print(f"\nTerms by type:")
for term_type, terms in types.items():
    unique_terms_of_type = set(t['term'] for t in terms)
    print(f"{term_type}: {len(unique_terms_of_type)} unique terms out of {len(terms)} total") 