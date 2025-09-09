
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
piano_class_text = (
    "he lives in New York City."  
"She works for Google." 
"Her birthday is on December 5th."  
"He bought a new car for $20,000. "  
"she visited Paris last summer."  
"The Eiffel Tower is very tall."  
"Amazon is a big company."  
"She went to school in Mumbai." 
"They plan to travel in December."  
"Mount Fuji is in Japan."
)
piano_class_doc = nlp(piano_class_text)
for ent in piano_class_doc.ents:
    print(
        f"""
ent.text = {ent.text}
ent.start_char = {ent.start_char}
ent.end_char = {ent.end_char}
ent.label_ = {ent.label_}
spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}
"""
    )
displacy.serve(piano_class_doc, style="ent")
