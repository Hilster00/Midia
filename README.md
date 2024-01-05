# Mídia

Este repositório é dedicado a códigos relacionados a mídia

- BaixarVideo.py
# Download de Vídeos do YouTube

## Descrição
Este é um script em Python desenvolvido para baixar vídeos do YouTube a partir de uma lista de URLs pré-definida em um arquivo de texto chamado 'links_videos.txt'. O código utiliza a biblioteca `pytube` para efetuar o download dos vídeos em sua melhor resolução disponível.

## Funcionalidades
- Baixa vídeos do YouTube baseados em uma lista de URLs fornecida em um arquivo de texto.
- Cria um arquivo 'links_videos.txt' com URLs pré-definidas, caso não exista.
- Exibe mensagens de status durante o processo de download.

## Uso
### Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
- `pytube`: Responsável por baixar os vídeos do YouTube.

### Execução
- Execute o script Python em um ambiente que possua a biblioteca `pytube` instalada.
- Caso o arquivo 'links_videos.txt' não exista, o script irá criá-lo com algumas URLs pré-definidas.
- O script iniciará o processo de download dos vídeos listados no arquivo 'links_videos.txt' para o diretório './Hilster'.
- Após concluir o download de cada vídeo, exibirá uma mensagem de confirmação.
- Ao final, o script exibirá uma mensagem indicando a conclusão da lista de downloads.

### Observações
- O arquivo 'links_videos.txt' pode ser editado para incluir as URLs desejadas dos vídeos a serem baixados.
- Certifique-se de ter conexão com a internet para baixar os vídeos do YouTube.

## Instruções para Usuário
1. Certifique-se de ter as bibliotecas necessárias instaladas (`pytube`).
2. Execute o script Python em um ambiente Python compatível.
3. Verifique se o arquivo 'links_videos.txt' contendo as URLs dos vídeos a serem baixados está presente.
4. Após a execução, os vídeos serão baixados para a pasta './Hilster' e mensagens de status serão exibidas no console.

Espero que este Readme ajude a entender e a utilizar o código para baixar vídeos do YouTube.
