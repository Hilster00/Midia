import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError


def baixar(url=None,local=None,mensagem=True):
    
    if local == None:
        local="./Hilster"
        
        if url == None:
            url="https://www.youtube.com/watch?v=0dG9pXeOgT0"
    if not os.path.exists(local):
        os.makedirs(local)
  
    # Cria uma instância do objeto YouTube
    video=YouTube(url)
        
               
            
    # Seleciona a melhor resolução disponível
    video = video.streams.get_highest_resolution()
            
    # Baixa o vídeo
    if mensagem:
        print(f'Baixando "{video.title}"...')

    video.download(output_path=local)
    if mensagem:
        m=f'{video.title} baixado com sucesso!'
        print(m)
        return m
   
    
if __name__=="__main__":
    
    if os.path.exists('./links_videos.txt'):
        with open("links_videos.txt","r") as lks:
            lista_urls=lks.read()
        
        lista_urls=lista_urls.split('\n')
        #remove possivel linha vazia no final
        if lista_urls[-1]=="":
            lista_urls.remove("")
        m=""
        for link in lista_urls:
            print(m,end="")
            m+=baixar(link)
            m+="\n"
            os.system("cls")
        print(m)
        print("\n\n\nToda a lista de downloads foi concluida!")
        
    else:
        print("Então, para você poder baixar vídeos, crie um arquivo chamado 'links_videos.txt'")
        print("Mas como sou legal, vou te ajudar, vou criar o arquivo pra você.\nDE NADA!!")
        with open("./links_videos.txt","a") as lks:
            lks.write("https://www.youtube.com/watch?v=keMBtyjYUPQ\n")
            lks.write("https://www.youtube.com/watch?v=6hx2Ql_WmZE\n")
            lks.write("https://www.youtube.com/watch?v=NQNuxjvenNs\n")
            lks.write("https://www.youtube.com/watch?v=WJxSNbAer9M\n")
            lks.write("https://www.youtube.com/watch?v=zQRgLZDp5Ds&t=7s\n")
            
        baixar(mensagem=False)
        print("\n\n\nAté baixe uma música pra ti,espero que goste")
    print("\n\n\n\n\n\n\n\n")    
    os.system("pause")
