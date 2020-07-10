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

### Future Ideas
- get better descriptions from wikipedia where possible
- combine books from series into 1 datapoint


