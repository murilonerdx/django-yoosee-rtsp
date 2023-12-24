Usei ngrok para subir o servidor

além das requiriments para o python

## django, ffmpeg, cv2, numpy...

dentro de static tem alguns arquivos importantes como:

## cam-rtsp-connection: Abre o arquivo e configure seu rtsp e depois execute com python3+, ele vai abrir uma pagina com a imagem ao vivo da sua camera
## cam-scam: vai procurar o ip da sua camera e a porta que ela está alocado
## convert-hls: é importante deixar isso executando ele transforma em um formato compativel para video, ele fica convertendo a imagem em tempo real, rode isso enquanto roda seu projeto


## dentro do arquivo convert-hls você precisa configurar o rtsp e também ajustar para a pasta do seu projeto, importante edixar dentro da pasta static 
## dentro do myproject: execute o run_server caso ele não abra, edite o arquivo mudando a porta.
