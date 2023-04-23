import textwrap
from gpt.completion import open_file, gpt3_completion, save_file, generate_txt_file
import sys
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Missing required arguments')
        exit(1)
    content_type = sys.argv[1]
    content_location = sys.argv[2]
    output_location = sys.argv[3]
    text_content = ''
    print('Content Type : '+content_type)
    if content_type == 'pdf':
        print('Generating text from pdf')
        print(content_location)
        text_content = generate_txt_file(content_location)
    elif content_type == 'text':
        text_content = open_file(content_location)
    elif content_type == 'url':
        request = requests.get(content_location)
        soup = BeautifulSoup(request.content, 'html.parser')
        lines = soup.find_all('p')
        for line in lines:
            text_content += line.text


    print('Starting chunking process')
    chunks = textwrap.wrap(text_content, 2000)
    result = list()
    count = 0
    print('Summarizing')
    for chunk in chunks:
        count = count + 1
        prompt = open_file('config/prompt.txt').replace('<<SUMMARY>>', chunk)
        prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
        summary = gpt3_completion(prompt)
        print('\n\n\n', count, 'of', len(chunks), ' - ', summary)
        result.append(summary)
    summary_file_name = output_location
    save_file('\n\n'.join(result), summary_file_name)
    summary_text = open_file(summary_file_name)


