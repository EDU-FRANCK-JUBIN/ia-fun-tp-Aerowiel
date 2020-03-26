import spacy
from spacy import displacy

nlp = spacy.load("fr_core_news_sm")

doc = nlp("Demain je travaille à la maison.")
for token in doc:
    #print(token)
    print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(
        token.text,
        token.idx,
        token.lemma_,
        token.is_punct,
        token.is_space,
        token.shape_,
        token.pos_,
        token.tag_,
        token.ent_type_
    ))

doc = nlp("Demain je travaille à la maison. Je vais pouvoir faire du NLP")
for sent in doc.sents:
    print(sent)

doc = nlp("Terrible désillusion pour la championne du monde")
for chunk in doc.noun_chunks:
    print(chunk.text, "-->", chunk.label_)

doc = nlp("Demain je travaille en France chez Total")
for ent in doc.ents:
    print(ent.text, ent.label_)

for token in doc:
    print("{0}/{1} <-- {2}-- {3}/{4}".format(
        token.text,
        token.tag_,
        token.dep_,
        token.head.text,
        token.head.tag_
    ))

displacy.render(doc, style="dep", jupyter=False, options={"distance":130})