""" 这段代码的主要目的是从指定的Bilibili视频和音频地址下载资源，
并将下载的无声视频和音频合成一个带有音频的完整视频文件 """

import requests
from moviepy.editor import *
 
#  视频地址
url_4 = "https://cn-hbwh-fx-01-13.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=dfba35ea6901d1e27d167c89beafc2af&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3881&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=131301&np=151388311&logo=80000000"
#  音频网址
url_3 = "https://cn-hbwh-fx-01-14.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=77541264ad991b1e1712438054cd3ba1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3882&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=40017&np=151388311&logo=80000000"
#  请求头
headers = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/112 SLBVPV/64-bit",
    "referer":
        "https://www.bilibili.com/video/BV1F5411L7D4/?vd_source=2cc7318b7d6a83e1149d8a8a4b791f76"
}
 
 
def get_resource(url, format):
    """
    用于爬取资源
    :param url: 资源的网址
    :param format: 保存的文件名称
    :return: None
    """
    res = requests.get(url, headers=headers)
 
    print(res.status_code)
 
    with open(format, "wb") as f:
        f.write(res.content)
 
 
def set_audio(f1, f2,f3):
    """
    用于音视频合成
    :param f1: 无声视频名称
    :param f2: 音频名称
    :param f3: 合成后（输出）的视频名称
    :return: None
    """
    videoclip = VideoFileClip(f1)
    audioclip = AudioFileClip(f2)
 
    vc = videoclip.set_audio(audioclip)
 
    vc.write_videofile(f3, codec="libx264", audio_codec="aac")
 
 
if __name__ == "__main__":
    get_resource(url_4, "1.mp4")
    get_resource(url_3, "2.mp3")
    set_audio("1.mp4","2.mp3","3.mp4")