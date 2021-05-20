# Classification Project: Predicting Diabetes Mellitus

## Question/Need:
*What is the framing question of your analysis, or the purpose of the model/system you plan to build?*

- Can analyzing novel complexity help advanced ESL learners?

*Who benefits from exploring this question or building this model/system?*  

As a learning of a second language, I have experienced the difficulty in breaking free of text book learning and diving into literature writen by and for native speakers of my target language.

I hope by analyzing text complexity of English literature, I could better guide ESL learners to novels within their language abilities.

If possible, I hope to expand this recommendation system to Chinese literature to help other students like myself, who are studying Chinese.


## Data Description:
*What dataset(s) do you plan to use, and how will you obtain the data?*  

I am currently looking through the catelog of books from [The Gutenberg Project](https://www.gutenberg.org/). The data will be the text of either entire novels or portions of at least **1000** novels.

*What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?*

An individual sample should be the text of an entire novel.

## Tools:
*How do you intend to meet the tools requirement of the project?*
- NLTK, spaCy, gensim, sklearn, or some combination of the above libraries.

- Use of dimensionality reduction, topic modeling, or clustering
- Methods will be integrated into a complete recommendation system 
- Rigorous validation and tuning

*Are you planning in advance to need or use additional tools beyond those required?*
- I hope to use Flask or a similar web app library for my recommendation system

## MVP Goal:
*What would a minimum viable product (MVP) look like for this project?*
- Data cleaned (missing values, bad formatting, etc)
- Data tokenized
- First pass complexity analysis
- First pass recommendation model
