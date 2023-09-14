# TikTok Video Share/Play Bot

This Python-based application represents an attempt to understand the capability to simulate the sharing or playing of a TikTok video through the TikTok mobile API.

This piece of software should be seen as a Proof of Concept and should not be used for malicious purposes.

## Requirements

#### For Python

- OS
- Threading
- Random
- Time
- Requests

This bot uses `os` to interact with the Operating System, `threading` to execute functions simultaneously, `random` to generate random numbers for `device_id`, `time` to keep track of how long the bot has been running and `requests` to send POST requests to TikTok's mobile API.

## Overview

#### TikTok API

This bot interacts with `https://api19-core-useast5.us.tiktokv.com/aweme/v1/aweme/stats/`, an endpoint from the TikTok API. This endpoint is used to update the share, play, like counts etc. on a TikTok video.

#### Threading

To maximize efficiency, we use `threading` to facilitate multiple requests being sent at the same time. This results in a quicker and more streamlined running of the bot.

#### Random 

The bot generates a random 19-digit number using the `random` function to mimic a `device_id`. This is to trick the API into believing that the request is coming from an actual mobile device. 

## Detailed Workflow

1. The `video_id` of the video you want to share/play as well as the mode, which can be either `share_delta` or `play_delta`, are passed to `Sharebot()` as parameters.

```python
bot = Sharebot(
    video_id = input("[?] id > "),
    threads = 5000,
    mode = "share_delta" #play_delta
)
```
2. `starter()` method in `Sharebot()` is called which runs an endless loop that checks the thread count and, if it's less than the set thread count in the parameters, it starts a new thread object with target function `send_request()`.
   
```python
def starter(self):
    while True:
        if threading.active_count() < self.threads:
            threading.Thread(target=self.send_request).start()
```
3. `send_request()` method sends a POST request to TikTok's API with the `aid`, `channel`, `device_type`, `device_id`, `os_version`, `version_code`, `app_name`, `device_platform`, `item_id` (which is your `video_id`) and the `mode` ('share_delta' or 'play_delta') all set as parameters.

```python
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
```


This bot is a basic illustration to understand the mechanism of TikTok's API interactions. The actual functionality to increment the share/play count might or might not succeed as it depends on the security measures and rate limit rules implemented on TikTok's API backend. Use this knowledge responsibly. It is not to be misused for exploiting or hacking purposes.
