from gensim import corpora

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey",
            "Human machine interface for lab abc computer applications",]


stoplist = []


#Tokenize words
texts = []
for document in documents:
    document_list = [word for word in document.lower().split()]
    texts.append(document_list)

print("Tokenize the document set")
print(texts)
print("\n\n")

# for document_token in texts:
# 	print(document_token)

# # texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]


print(" Printing Dictionary \n\n\n\n")

# #Create a dictionary file
dictionary = corpora.Dictionary(texts)
# dictionary.save('deerwester.dict')
print(dictionary)
print(dictionary.token2id)
print("\n\n")

# print("Getting word from Id")
print (dictionary.get(1))


print("Vectorizing Words \n")
#Vectorize document
new_doc = "Human computer interaction Human"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_doc)
print(new_vec)  # the word "interaction" does not appear in the dictionary and is ignored
print("\n\n")


print("Document Frequency distribution \n")
print(dictionary.dfs)
print("\n\n")

print("Prunning document\n")
# dictionary.filter_extremes(no_above=1)
print(dictionary)
print(dictionary.token2id)
print("\n\n")


# print("New Document Frequency Distribution \n")
# print(dictionary.dfs)
# print("\n\n")


# #Create a corpus

corpus = [dictionary.doc2bow(text)  for text in texts]
corpora.MmCorpus.serialize('corpus.mm',corpus)

print(corpus)
print("\n\n")

