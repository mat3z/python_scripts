from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline

doc1 = "Data Science Machine Learning"
doc2 = "Money fun Family Kids home"
doc3 = "Programming Java Data Structures"
doc4 = "Love food health games energy fun"
doc5 = "Algorithms Data Computers"
doc6 = "Algorithms Data Stuff"

# combine documents
doc_complete = [doc1, doc2, doc3, doc4, doc5, doc6]

vectorizer = TfidfVectorizer(stop_words='english')
# X =vectorizer.fit_transform(doc_complete)

svd_model = TruncatedSVD(n_components=18,n_iter=100, random_state=42)
# lsa.fit(X)
svd_transformer = Pipeline([('tfidf', vectorizer),
							('svd', svd_model)])
svd_matrix = svd_transformer.fit_transform(doc_complete)

terms = vectorizer.get_feature_names()

print(svd_matrix)

# combine documents
doc_complete1 = [doc1, doc2, doc3, doc4, doc5]


query_vector = svd_transformer.transform(doc_complete1)

from sklearn.metrics import pairwise_distances
distance_matrix = pairwise_distances(query_vector, 
                                     svd_matrix, 
                                     metric='cosine', 
                                     n_jobs=-1)

print(distance_matrix)



# for i,comp in enumerate(lsa.components_):
#     termsInComp = zip(terms,comp)
#     sortedterms = sorted(termsInComp, key=lambda x: x[1],reverse=True)[:10]
#     print("Concept %d:" % i)
#     for term in sortedterms:
#         print(term[0], term[1])
#     print(" ")
