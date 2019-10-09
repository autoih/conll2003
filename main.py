from nltk.corpus.reader import ConllCorpusReader

train = ConllCorpusReader('CoNLL-2003', 'eng.train', ['words', 'pos', 'ignore', 'chunk'])
test = ConllCorpusReader('CoNLL-2003', 'eng.testa', ['words', 'pos', 'ignore', 'chunk'])

print(train.iob_words)

