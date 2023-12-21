import subprocess

def convert_rtsp_to_hls(rtsp_url, output_dir):
    command = [
        'ffmpeg',
        '-i', rtsp_url,
        '-c:v', 'libx264',
        '-hls_time', '2',
        '-hls_list_size', '3',
        '-hls_flags', 'delete_segments',
        '-f', 'hls',
        f'{output_dir}/stream.m3u8'
    ]
    subprocess.run(command)

if __name__ == "__main__":
    rtsp_url = 'rtsp://admin:senha@ip:554/onvif1'  # Substitua pela URL RTSP
    output_dir = 'C:/Users/<USUARIO>/Desktop/myproject/static'  # Substitua pelo diretório pai onde deseja que os arquivos HLS sejam criados
    convert_rtsp_to_hls(rtsp_url, output_dir)
