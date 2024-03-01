import os
import openai
from sys import argv
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('API_KEY')


if len(argv) != 3:
    print('1 - file to change')
    print('2 - file to save changed')
    print('Make python -m like_a_pro source.py target.py')
    quit()

if not os.path.exists(argv[1]):
    print('File dosnt exist')
    quit()

_, source_file, target_file = argv
with open(source_file,encoding='utf8') as file:
    command = 'Przekształć podany program aby był bardziej profesjonaly, dodaj pydoc oraz popraw nazwy zmiennych'
    command += '\n'.join(file.readlines())
    response = openai.completions.create(
        model="gpt-3.5-turbo",
        prompt=command,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
with open(target_file,'w') as file:
    file.write(response.choices[0].text)
print(source_file)
print(target_file)