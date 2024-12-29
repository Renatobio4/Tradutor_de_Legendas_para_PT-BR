# Tradutor_de_Legendas_para_PT-BR
Este código traduz arquivos de legenda no formato .srt do inglês para o português utilizando a biblioteca deep_translator.
Ele lê as linhas do arquivo, traduz as linhas que não contêm números ou timestamps, e salva o resultado em um novo arquivo. 

Temos dois arquivos:

Um que utiliza a CPU para tradução e outro arquivo com a diferença de que ele paraleliza a tradução das linhas utilizando  `ThreadPoolExecutor` e utiliza a GPU para acelerar o processo.

#### Instruções para Uso:

***Versão utilizando a CPU:

1. Certifique-se de ter a biblioteca `deep_translator` instalada. Você pode instalá-la utilizando `pip install deep_translator`.
    
2. Coloque seus arquivos `.srt` em inglês na mesma pasta do código.
    
3. Execute o script e ele irá traduzir os arquivos e salvar com o sufixo `_pt-br.srt`


***Versão utilizando a GPU NVIDIA:

1. Certifique-se de ter as bibliotecas `deep_translator` e `torch` instaladas. Você pode instalá-las utilizando `pip install deep_translator torch`.
    
2. Verifique se sua GPU NVIDIA RTX 3060 está configurada corretamente com os drivers e a biblioteca CUDA.
    
3. Coloque seus arquivos `.srt` em inglês na mesma pasta do código.
    
4. Execute o script e ele irá traduzir os arquivos utilizando a GPU, salvando com o sufixo `_pt-br.srt`.

   
