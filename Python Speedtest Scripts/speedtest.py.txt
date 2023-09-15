import speedtest

def run_speed_test():
    s = speedtest.Speedtest()
    s.get_best_server()

    print("Testando a velocidade de download...")
    download_speed = s.download() / 10**6 
    print("Velocidade de download:", round(download_speed, 2), "Mbps")

    print("Testando a velocidade de upload...")
    upload_speed = s.upload() / 10**6 
    print("Velocidade de upload:", round(upload_speed, 2), "Mbps")

    print("Testando o ping...")
    ping = s.results.ping 
    print("Ping:", round(ping, 2), "ms")

run_speed_test()
