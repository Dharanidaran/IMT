from gensim import corpora
from nltk.corpus import stopwords
import os
from gensim.corpora.dictionary import Dictionary


documents = ["Human machine interface for lab abc computer applications",
"A survey of user opinion of computer system response time",
"The EPS user interface management system",
"System and human system engineering testing of EPS",
"Relation of user perceived response time to error measurement",
"The generation of random binary unordered trees",
"The intersection graph of paths in trees",
"Graph minors IV Widths of trees and well quasi ordering",
"Graph minors A survey"
]





stoplist = set('for a of the and to in'.split())


documents_array = [[word for word in document.lower().split() if word not in stoplist]
		for document in documents]




# # # ===============================
# # # ===============================
print("Printing document array")
for doc_array in documents_array:
	print(doc_array)
print("\n\n")
# # # ===============================
# # # ===============================




# # # =============================== 
# # # Create a dictionary for the documents_array
# # # ===============================
# dictionary =  corpora.Dictionary(documents_array)
# print("Printing dictionary")
# print(dictionary)
# print("\n\n")
# # # ===============================
# # # ===============================





# # # ===============================
# # # ===============================
# print("Printing token_to_id word_id_map")
# token_to_id = dictionary.token2id
# for word,id_num in token_to_id.items():
# 	print(id_num,"\t",word)
# print("\n\n")
# # # ===============================
# # # ===============================





# # #To covert tokenized documents to vectors
# # # ===============================
# # # ===============================
# new_doc = "Human computer interaction "
# print("Itemize a string")
# print(new_doc.lower().split())
# new_vec =  dictionary.doc2bow(new_doc.lower().split())
# print (new_vec)
# print("\n\n")
# # # ===============================
# # # ===============================







# # # ===============================
# # # Vectorize the above documents_array to vector 
# # # ===============================
# corpus = [dictionary.doc2bow(row) for row in documents_array]
# corpora.MmCorpus.serialize('deerwester_step.mm', corpus)  # store to disk, for later use
# print("Print the entire corpus")
# print(corpus)
# # # ===============================
# # # ===============================





# # # ===============================
# # # Corpus Streaming - One document at a Time
# # # ===============================

# class MyCorpus(object):
# 	def __init__(self,filepath,delimiter,textColumnNo):

# 		self.filepath = filepath
# 		self.delimiter = delimiter
# 		self.textColumnNo = textColumnNo

# 	def __iter__(self):
# 		for line in open(self.filepath,'r'):
# 			print(len(line.split(";")))
# 			desiredcolumn = line.split(self.delimiter)[self.textColumnNo-1]
# 			# print(desiredcolumn.lower())
# 			yield desiredcolumn.lower().split()

# import os
# from pprint import pprint
# cwd = os.getcwd()
# filename = "OneStar.csv"
# delimiter = ";"
# textColumnNo = 20
# filepath = os.path.join(cwd,"Data",filename)
# print(filepath)


# mem_friendly_corpus_instance = MyCorpus(filepath,delimiter,textColumnNo)

# dictionary = corpora.Dictionary([row for row in mem_friendly_corpus_instance])
# print(dictionary)



# for word,word_id in dictionary.token2id.items():
# 	print(word_id,"\t",word)





# # ===============================
# # Recreate corpus from Dictionary
# # ===============================
# corpus_file = [ dictionary.doc2bow(row) for row in mem_friendly_corpus_instance ]

# for row_vec in corpus_file:
# 	print(row_vec)
# 	print("")





# # ===============================
# # Saving the corpus
# # ===============================
# corpora.MmCorpus.serialize('corpus_step.mm', corpus_file)





# # ===============================
# # Printing some of the functions
# # ===============================
# #Printing some of the functions
# print(dictionary.num_docs)
# print(dictionary.dfs)


# print(dictionary.get(1))
# print(dictionary.get(2))
# print(dictionary.get(4),dictionary.dfs.get(4))






