#  Bilibili Video Crawling and Synthesis Script

## 1. Introduction
This script is used to obtain video and audio resources from Bilibili and synthesize them into a complete video file. Please note that crawling and using Bilibili content must comply with relevant laws, regulations, and website usage protocols.

## 2. Environment Requirements
- Python 3.x
- Install `requests` library: used for HTTP requests
- Install `moviepy` library: used for video editing

## 3. Install Dependencies
You can use pip to install the required dependency libraries:
```bash
pip install requests moviepy
```
* Note: If you encounter an error when running the code, No module named ‘moviepy.editor’, this is because the moviepy library version you downloaded is the latest 2.x version, which may not include the editor module. It is recommended to reinstall the moviepy library. According to the information, the from moviepy.editor import * reference method is not supported after Python 3.7 version. Since it is moviepy 2.0.0 version
```
pip uninstall moviepy
pip install moviepy==1.0.3
```

## 4. Code Structure
### 1） Import Libraries
```
import requests
from moviepy.editor import *
```

* requests: used for HTTP requests, to obtain video and audio data
* moviepy.editor: used for video editing, including processing and synthesizing audio and video files
  
### 2）Define Resource Links and Request Headers
```
#Video address
url_4 = "https://cn-hbwh-fx-01-13.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-100026.m4se=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=dfba35ea6901d1e27d167c89beafc2af&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3881&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=131301&np=151388311&logo=80000000"
#Audio address
url_3 = "https://cn-hbwh-fx-01-14.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=77541264ad991b1e1712438054cd3ba1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3882&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=40017&np=151388311&logo=80000000"


# Request headers
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/112 SLBVPV/64-bit",
    "referer": "https://www.bilibili.com/video/BV1F5411L7D4/?vd_source=2cc7318b7d6a83e1149d8a8a4b791f76"
}
```
* url_4： points to the URL of the silent video resource.
* url_4：points to the URL of the silent video resource.
* headers：defines the HTTP request header information, including user-agent and referer, to simulate a browser accessing Bilibili.

### 3）Get Resource Function
```
def get_resource(url, format):
    """
    Used to crawl resources
    :param url: URL of the resource
    :param format: file name to save
    :return: None
    """
    res = requests.get(url, headers=headers)
    print(res.status_code)
    with open(format, "wb") as f:
        f.write(res.content)
```
* get_resource：this function downloads resources based on the given URL and saves them with the specified file name. It prints the status code of the request to help with debugging.

### 4）Synthesize Video Function
```
def set_audio(f1, f2, f3):
    """
     Used for audio-video synthesis
    :param f1: silent video file name
    :param f2: audio file name
    :param f3: output video file name after synthesis
    :return: None
    """
    videoclip = VideoFileClip(f1)
    audioclip = AudioFileClip(f2)
    vc = videoclip.set_audio(audioclip)
    vc.write_videofile(f3, codec="libx264", audio_codec="aac")
```
* set_audio：this function synthesizes a silent video file with an audio file and saves the result as a new video file. It uses the moviepy library to handle video and audio.

### 5）Main Program Entry
```
if __name__ == "__main__":
    get_resource(url_4, "1.mp4")
    get_resource(url_3, "2.mp3")
    set_audio("1.mp4", "2.mp3", "3.mp4")
```
* First, the get_resource function is called to download the silent video and audio, saving them as 1.mp4 and 2.mp3.
* Then, the set_audio function is called to merge these two files, ultimately generating 3.mp4.

## 5. Notes
* Please ensure that downloading and using Bilibili content complies with relevant laws, regulations, and website usage terms.
* The URLs for video and audio may change over time, requiring updates based on actual circumstances.
   
## 6. References
https://blog.csdn.net/m0_72225765/article/details/145575032?fromshare=blogdetail&sharetype=blogdetail&sharerId=145575032&sharerefer=PC&sharesource=m0_74149651&sharefrom=from_link
