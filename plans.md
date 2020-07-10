### Updated Scraped Books
- save "series" info from title for later combining
- find which books are still missing

### Cleaning Steps
- filtering out empty descriptions
- create text column
- filtering out non-english books
    1. using the language column
    2. using pyenchant library with 50% threshhold
- filtering out books with too short descriptions
- filtering out doubles

### Modeling progress
- have run TfidfVectorizer and Gensim simple_preprocess a bit, not great results
- basic spaCy same thing
*I believe I'm going to need to do some better NLPing because this basic stuff is terrible

### Future Ideas
- get better descriptions from wikipedia where possible
- combine books from series into 1 datapoint
- can change names into more descriptive words like (man, woman, doctor, president, etc...)



