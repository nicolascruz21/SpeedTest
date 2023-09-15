import urllib.request
import subprocess

def test_speed():
    url = "http://speedtest.net/mini/speedtest/random4000x4000.jpg"
    download_file = "/dev/null"
    upload_file = "dummy_upload_file"

    download_start = urllib.request.urlopen(url)
    urllib.request.urlretrieve(url, download_file)
    download_end = download_start.getcode()
    download_speed = download_end / 1024 / 1024

    upload_command = f"dd if=/dev/zero of={upload_file} bs=1M count=1000"
    subprocess.run(upload_command, shell=True)
    upload_speed_output = subprocess.check_output(
        f"pv {upload_file} | curl -T - ftp://speedtest.tele2.net/upload/", shell=True
    )
    upload_speed = float(upload_speed_output.decode("utf-8").split()[-2]) / 1024 / 1024

    ping_command = "ping -c 4 speedtest.net | tail -1| awk '{print $4}' | cut -d '/' -f 2"
    ping_output = subprocess.check_output(ping_command, shell=True)
    ping_time = float(ping_output.decode("utf-8"))

    print(f"Velocidade de download: {download_speed:.2f} Mbps")
    print(f"Velocidade de upload: {upload_speed:.2f} Mbps")
    print(f"Tempo de ping: {ping_time:.2f} ms")

test_speed()
