import ffmpeg
import numpy as np
import cv2


def main(source):
    args = {
    "rtsp_transport": "udp",  # Mudar para udp ou remover completamente esta linha para auto-negociação
    "fflags": "nobuffer",
    "flags": "low_delay"
}

    # Tentativa de obter informações da stream para definir largura e altura
    try:
        probe = ffmpeg.probe(source)
        cap_info = next(x for x in probe['streams'] if x['codec_type'] == 'video')
        width = cap_info['width']
        height = cap_info['height']
    except Exception as e:
        print(f"Erro ao obter informações da stream: {e}")
        return

    # Iniciar o processo de leitura do FFmpeg
    process1 = (
        ffmpeg
        .input(source, fflags='nobuffer',flags='low_delay')
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .overwrite_output()
        .run_async(pipe_stdout=True)
    )

    while True:
        try:
            in_bytes = process1.stdout.read(width * height * 3)
            if not in_bytes:
                print("Não foi possível ler os dados do frame.")
                break
            in_frame = (
                np
                .frombuffer(in_bytes, np.uint8)
                .reshape([height, width, 3])
            )
            frame = cv2.resize(in_frame, (1280, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow("ffmpeg", frame)

            if cv2.waitKey(1) == ord('q'):
                break
        except Exception as e:
            print(f"Erro durante o processamento de frames: {e}")

    process1.kill()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    alhua_rtsp = "rtsp://admin:senha@ip:554/onvif1"
    main(alhua_rtsp)
