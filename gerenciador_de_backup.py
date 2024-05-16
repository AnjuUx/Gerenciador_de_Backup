import os
from tkinter.filedialog import askdirectory
#tkinter e uma biblioteca para fazer janelas                                
#FILEDIALOG permite você usar a janelas padrõe do computador de selecionar aquivos , pastas.
#askdirectory está perguntando qual o diretorio qual é a pasta do arquivo.
#como tkinter.filedialog  queremos importar somente a função askdirectory então de vez usarmos  tkinter.filedialog.'askdirectory
# vou usar from tkinter.filedialog import askdirectory  por que nao preciso chamar a função toda hora ! 
# ai podemos usar so a funçao assim,  askdirectory() e rodar o codigo 
import shutil
#bibblioteca usada para copiar os arquivos para o funcionamento do backup.
import datetime

nome_pasta_selecionada = askdirectory()

lista_arquivos = os.listdir(nome_pasta_selecionada)
# os.listdir É pra listar o que tem dentro do diretorio. 


nome_pasta_backup = "backup"
# nessa variavel aqui estamos definindo  o que a 'nome_pasta_backup' vai receber 
#o nome da pasta backup vai ser "backup"

nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
# aqui e onde a pasta backup está  o local do  computador onde vai se encontrar a pasta backup
if not os.path.exists(nome_completo_pasta_backup):
    # "os.path.exists ()" consegue verificar se  existe o arquivo na pasta ou não. 
    os.mkdir(nome_completo_pasta_backup)
        # com a biblioteca "os" consigo criar uma pasta que nao existe no meu computador.
    # nessa caso será a pasta backup. 

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

for arquivo in lista_arquivos:
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    # aqui a variavel "nome_completo_arquivo" vai receber outras duas variaveis  transformando ela eum uma unica variavel com informaçoes 
      
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"
    
    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"):
        os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")
    
    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
         # se backup nao for o nome de arquivo copia| caso ao contrario nao copia. 
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)
         # copia tudo que esta ali dentro, copia a arvore de arquivo.
