import spacy
import json
import re

# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Load domain knowledge
with open("dataset/domain_knowledge.json", "r") as f:
    domain_knowledge = json.load(f)

def extract_entities(text):
    doc = nlp(text)
    extracted_entities = {key: [] for key in domain_knowledge.keys()}

    # Dictionary lookup
    for category, keywords in domain_knowledge.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", text, re.IGNORECASE):
                extracted_entities[category].append(keyword)

    # NER extraction
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT"]:
            extracted_entities["competitors"].append(ent.text)

    return extracted_entities

if __name__ == "__main__":
    text_sample = "CompetitorX offers a better AI engine and a free trial."
    print(extract_entities(text_sample))
