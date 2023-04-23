# OpenAI - GPT Summariser

This is a simple project which uses OpenAI's GPT API to summarize PDF files, Text files or URL content

## Features

- Provide any PDF file to summarize
- Provide any text file to summarize
- Provide URLs of sites to summarize. Please note that the URLs should not require any login process. Also, some websites block automated scripts to access URLs
- Generate txt file with summarized output. You can pass the generated text file again as input to generate a more concise summary

## Requirements


- [Python] - 3.10


## Installation
- You will need an OpenAI API key to get started
- Paste the key in openapikey.txt file in the config folder

```
cd summarizer
pip install requirements.txt
python main.py <type-of-content> <path-to-input> <output file>
```

Examples

```
python main.py pdf /Users/sunny/Documents/BI_DeveloperV1.1.pdf /Users/sunny/Desktop/Projects/Nan/summarizer/output/pdf.txt
python main.py url https://www.geeksforgeeks.org/python-programming-language /Users/sunny/Desktop/Projects/Nan/summarizer/output/url.txt
```


   [Python]: <https://www.python.org/downloads/>