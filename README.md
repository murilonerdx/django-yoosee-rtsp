Primeiramente para funcionar em sua maquina, baixe o VLC e as dependencias abaixo para o python 3+

ffmpeg, numpy, cv2, django

Elas serão importantes para nós conseguirmos converter a imagem para um formato de video

Eu usei também ngrok para subir um servidor de teste mas nada demais.


além das requirements para o python



dentro de static tem alguns arquivos importantes como:

## cam-rtsp-connection 
Abre o arquivo e configure seu rtsp e depois execute com python3+, ele vai abrir uma pagina com a imagem ao vivo da sua camera
## cam-scam
vai procurar o ip da sua camera e a porta que ela está alocado
## convert-hls
é importante deixar isso executando ele transforma em um formato compativel para video, ele fica convertendo a imagem em tempo real, rode isso enquanto roda seu projeto


## dentro do arquivo convert-hls 
você precisa configurar o rtsp e também ajustar para a pasta do seu projeto, importante edixar dentro da pasta static 
## dentro do myproject
execute o run_server caso ele não abra, edite o arquivo mudando a porta.

Link para acessar o portal web django com a livestream aberta: http://localhost:8080/stream/


Nas pastas você consegue observar, modifique os arquivos de configuração tanto cam-rtsp-connection como cam-scam com seu ip da sua maquina, convert-hls com o ip do rtsp no meu caso eu peguei no proprio aplicativo do yoosee

## cam-rstp-connection arquivo.py
Altere a ultima linha para as configurações que precisa a porta fixa se não me engano é 554, com o cam-scam você muda para o ip da sua maquina utilizando ipconfig ou ifconfig la vai verificar se essa porta está aberta na sua rede

```python
if __name__ == "__main__":
    alhua_rtsp = "rtsp://admin:admin@<seu ip>:554/onvif1"
    main(alhua_rtsp)
```

## cam-scam
Você vai fazer o mesmo substituindo para seu ip para verificar se essa porta está aberta na sua rede
/24 significa um range das maquinas .1 - .24

```python
# Substitute '192.168.1.1/24' with your local network range
ip_range = '<ip da sua rede e não da maquina>/24'
hosts = scan_ip_range(ip_range)

for host in hosts:
    open_ports = check_camera_ports(host['ip'])
    if open_ports:
        print(f"Host {host['ip']} has open ports: {open_ports}")
```

## convert-hls
Por ultimo setamos as configurações para onde ele vai gerar o arquivo referente a live

```python
if __name__ == "__main__":
    rtsp_url = 'rtsp://admin:admin@<seu ip>:554/onvif1'  # Substitua pela URL RTSP
    output_dir = '<localizacao do projeto>/myproject/static'  # Substitua pelo diretório pai onde deseja que os arquivos HLS sejam criados
    convert_rtsp_to_hls(rtsp_url, output_dir)
```
