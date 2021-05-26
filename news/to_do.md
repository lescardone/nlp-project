# Topic Modeling
Efficiently analyze large volumes of text by clustering documents into topics

Attempt to discover clusters of documents, grouped together by topic.

Up to "user" to identify what these topics actually represent
    - no way to evaluate how they did

## Latent Dirichlet Allocation 
Uses Dirichlet probability distribution
Preprocess with CountVectorize

ASSUMPTIONS:  
   - documents with similar topics use similar groups of words 
   - latent topics can be found by searching for groups of words that frequently occur together in documents across the corpus  
   
AKA:
   - documents are probability distribution over latent topics
   - topics themselves are probability distributions over words

EX: 
   - If there are 5 latent topics, each document will have a probability of belonging to each topic

NOT SAYING DEFINITIVELY A DOCUMENT BELONGS TO A CERTAIN TOPIC

   - each topic will have a probability of being associated with each word in the entire corpus

Topics are mixed across a given document and words are mixed across a given topic. -- LDA backtracks through this process.

WORKFLOW:  
Choose # of Topics to Discover:
1. sklearn.feature_extraction.text import CountVectorizer
    - cv = CountVectorizer(*kwargs)
        - max_df = 0.9 -- discards words that show up in 90% of documents
        - min_df = 2 -- discard words that that shows up in at least two documents
        - stop_words = 'english'
        
2. fit transform to entire dataset  
    - no train, test, split
    - dtm = cv.fit_transform(df['column'])

LDA to learn topic representation: 

3. from sklearn.decomposition import LatentDirichletAllocation
    - LDA = LatentDirichletAllocation(*kwargs)
        - n_components = 10 -- number of topics
        - random_state
    - LDA.fit(dtm)

4. Grab probability of words
    - cv.get_feature_names()
        - holding an instance of every single word
    - LDA.components_
        - an array of probabilities per word per topic 

5. Look at the words that have the highest probability of showing up in topic
    - topic_one = LDA.components_[0] -- first topic
    - topic_one.argsort()[-10:] -- returns the index positions for the highest probability words
        - sorts the values, and returns the index values of the sorted list
        - aka show location of high probability 
        - use index to get the word corresponding with that probability
    - top_twenty_words = topic_one.argsorg()[-20:]
    - for index in top_twenty_words:
    print(cv.get_feature_names()[index])
            
        
Interpret topics and assign to docs:
6. Grab top 15 words per topic
   - for i, topic in enumerate(LDA.components_):
   print(f'THE TOP 15 WORDS FOR TOPIC {i}:')
   print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])

7. Assign to docs
   - topic_results = LDA.transform(dtm).round(2)
   - df['topic'] = topic_results.argmax(axis=1)
   - map the topic numbers to words

## Non Negative Matrix Factorization
- Simultaneously performs dimensional reduction and clustering
- Can use in conjunction with TF-IDF to model topics across documents (preprocess with TF-IDF vectorization)

   - A: non-negative matrix, (rows = features)
   - k-dimension, # topics
   - W: basis vectors, topics in the corpus
   - H: coefficient matrix, membership weights for documents relative to each topic
   
   A =   W   *  H  
   A = (n*k) * (k*m)
   
   basis vector W = cluster
   membership of objects in clusters encoded by H

WORKFLOW: 

Construct vector space model for documents (after stopword filtering), resulting in a document-term matrix A / Apply TF-IDF term weight normalization /Normalize TF-IDF vectors to unit length

1. sklearn.feature_extraction.text import TfidfVectorizor
    - tfidf = TfidfVectorizor(*kwargs)
        - max_df = 0.9 -- discards words that show up in 90% of documents
        - min_df = 2 -- discard words that that shows up in at least two documents
        - stop_words = 'english'
        
2. fit transform to entire dataset  
    - no train, test, split
    - dtm = tfidf.fit_transform(df['column'])


3. from sklearn.decomposition import NMF
    - nmf = NMF(*kwargs)
        - n_components = 10 -- number of topics
        - random_state
    - nmf.fit(dtm)

4. Look at words/coefficients
    - tfidf.get_feature_names()
        - holding an instance of every single word
    - nfm.components_
        - an array of coefficients per word per topic 

Interpret topics based off the coefficient values of the words per topic
5. Grab 15 words with highest coefficients per topic
   - for i, topic in enumerate(nmf.components_):
   print(f'THE TOP 15 WORDS FOR TOPIC {i}:')
   print([tfidf.get_feature_names()[index] for index in topic.argsort()[-15:]])

7. Assign to docs
   - topic_results = nmf.transform(dtm).round(2)
   - df['topic'] = topic_results.argmax(axis=1)
   - map the topic numbers to words/topic descriptors

Interpret topics based off the coefficient values of the words per topic