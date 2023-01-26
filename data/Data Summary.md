## About Dataset
### Context
This dataset was compiled for the Philosophy Data Project and used to develop the features available on that site. As a former philosophy teacher and now data scientist, I thought it would be interesting to apply the tools of data science to the history of philosophy.

The initial goal was to build a classification model with the data. After all, a book of philosophy represents an effort to systematically organize one's thought about the world. Using the data from the history of philosophy to classify texts would thus enable us to, by proxy, classify how people think about the world. Where some projects focus on sentiment analysis, here we focus on conceptual, or ideological analysis. Once we understand a person's worldview, there is no limit to what we can do with that information - from advertising to political campaigning through to self-exploration and therapy.

After that, I built several features to help people explore philosophical ideas and do comparisons. These included a w2v model for word use comparison, a set of basic stats for each text and school, and a feature enabling users to search the corpus.

After finishing initial work on the site and its data tools, I thought it would be worthwhile to make the data publicly available so others could work with it.

### Content
The dataset contains over 300,000 sentences from over 50 texts spanning 10 major schools of philosophy. The represented schools are: Plato, Aristotle, Rationalism, Empiricism, German Idealism, Communism, Capitalism, Phenomenology, Continental Philosophy, and Analytic Philosophy.

Texts were taken either from Project Gutenberg or from my own personal library of pdfs. The dataset is updated periodically as I add new texts to the corpus.

The texts were cleaned extensively before being tokenized and organized in the way they're presented here. For information on the cleaning steps, check out the github repo for the initial project, which contains a notebook with all the cleaning steps.

### Inspiration
There are a ton of cool project ideas! Here are a few:

- use some clustering technique to see if the sentences would naturally cluster into their corresponding schools
- build a text completion or chat-bot app by training on the sources
- compare the texts to secondary literature on the philosophers to see if the secondary literature gets the interpretation right

If you come up with any cool visualizations or insights you want to share, please do contact me and we can definitely feature your work on the Philosophy Data Project website. Looking forward to seeing what you come up with :)