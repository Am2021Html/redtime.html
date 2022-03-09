import speedtest

wifi = speedtest.Speedtest()
print("wifi download speed is ", wifi.download())
print("wifi upload speed is", wifi.upload())


# این برای سرعت دانلود یا اپلود استکه ببینید که سرعت خوبه یا نه
