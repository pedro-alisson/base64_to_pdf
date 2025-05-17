import base64
import time

with open('Base64.txt','r') as file:
   content =  file.read()

decode_file_content = base64.b64decode(content)

with open('decode_file.pdf','wb') as pdf_file:
   pdf_file.write(decode_file_content)

print('Conteúdo convertido em PDF com sucesso!')

time.sleep(5)