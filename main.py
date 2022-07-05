import os, threading, random, time, requests

class Sharebot():
    def __init__(self, video_id, threads, mode):
        self.video_id = video_id
        self.threads  = threads
        self.start    = time.time()
        self.mode     = mode
        
        self.sess     = requests.Session()
        self.shares   = 0
        
    def starter(self):
        while True:
            if threading.active_count() < self.threads:
                threading.Thread(target=self.send_request).start()
    
    def send_request(self):
        try:
            req = self.sess.post(
                    url     = "https://api19-core-useast5.us.tiktokv.com/aweme/v1/aweme/stats/?", 
                    headers = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": "com.zhiliaoapp.musically/2022501030 (Linux; U; Android 7.1.2; fr; SM-N976N; Build/QP1A.190711.020;tt-ok/3.12.13.1)"
                    }, 
                    params = {
                        "aid": 1988,
                        "channel": "googleplay",
                        "device_type": "SM-N976N",
                        "device_id": random.randint(1000000000000000000, 9999999999999999999),
                        "os_version": "7.1.2",
                        "version_code": 250103,
                        "app_name": "musical_ly",
                        "device_platform": "android",
                        "item_id": self.video_id,
                        self.mode: 1
                    },
                    stream = True
            )
            
            if req.json()["status_code"] == 0:
                self.shares += 1
                os.system(f"title Sent :{self.shares} ^| Speed :{round((int(self.shares) / (time.time() - self.start)), 2)}/s")
                pass
        except:
            pass

if __name__ == "__main__":

    bot = Sharebot(
        video_id = input("[?] id > "),
        threads = 5000,
        mode = "share_delta" #play_delta
    )
    
    bot.starter()
