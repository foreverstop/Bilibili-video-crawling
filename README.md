# Bilibili video crawling

## 一、简介
本脚本用于从B站获取视频和音频资源，并将它们合成一个完整的视频文件。请注意，爬取和使用B站内容须遵守相关法律法规及网站使用协议。

## 二、环境要求
- Python 3.x
- 安装`requests`库：用于HTTP请求
- 安装`moviepy`库：用于视频编辑

## 三、安装依赖
您可以使用pip安装所需的依赖库：
```bash
pip install requests moviepy
```
* 注意：当运行代码报错时，No module named ‘moviepy.editor’，因为你下载的moviepy库是最新的2.x版本，可能不包含editor模块，请重新安装moviepy库。不妨试下以下代码进行重新安装。经资料显示，python3.7版本后不支持 from moviepy.editor 引用方式，由于是moviepy 2.0.0版本
```
pip uninstall moviepy
pip install moviepy==1.0.3
```

## 四、代码结构
### 1）导入库
```
import requests
from moviepy.editor import *
```

* requests：用于HTTP请求，获取视频和音频数据 
* moviepy.editor：用于视频编辑，包括音频和视频文件的处理与合成
  
### 2）定义资源链接与请求头
```
#视频地址
url_4 = "https://cn-hbwh-fx-01-13.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-100026.m4se=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=dfba35ea6901d1e27d167c89beafc2af&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3881&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=131301&np=151388311&logo=80000000"
#音频地址
url_3 = "https://cn-hbwh-fx-01-14.bilivideo.com/upgcxcode/27/89/248548927/248548927-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1742382759&gen=playurlv2&os=bcache&oi=3746251271&trid=0000aae5a0b9d91f46a1baf3468da4b58ddau&mid=3461562702498712&platform=pc&og=cos&upsig=77541264ad991b1e1712438054cd3ba1&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=3882&bvc=vod&nettype=0&orderid=0,3&buvid=9AEF060E-7BA5-F9C3-A71C-FA399E82F67972890infoc&build=0&f=u_0_0&agrr=1&bw=40017&np=151388311&logo=80000000"


# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/112 SLBVPV/64-bit",
    "referer": "https://www.bilibili.com/video/BV1F5411L7D4/?vd_source=2cc7318b7d6a83e1149d8a8a4b791f76"
}
```
* url_4：指向无声视频资源的URL。
* url_4：指向无声视频资源的URL。
* headers：定义HTTP请求的头部信息，包括用户代理和引用来源，以便模拟浏览器访问B站。

### 3）获取资源函数
```
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
```
* get_resource：该函数根据给定的URL下载资源，并保存为指定的文件名。它打印出请求的状态码以帮助调试。

### 4）合成视频函数
```
def set_audio(f1, f2, f3):
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
```
* set_audio：该函数将一个无声视频文件与一个音频文件合成，并将结果保存为一个新的视频文件。它使用moviepy库来处理视频和音频。

### 5）主程序入口
```
if __name__ == "__main__":
    get_resource(url_4, "1.mp4")
    get_resource(url_3, "2.mp3")
    set_audio("1.mp4", "2.mp3", "3.mp4")
```
* 首先调用get_resource函数分别下载无声视频和音频，保存为1.mp4和2.mp3。
* 然后调用set_audio函数将这两个文件合并，最终生成3.mp4。

## 五、注意事项
* 请确保下载和使用B站内容符合相关法律法规和网站的使用条款。
* 视频和音频的URL可能会随时间变化，需要根据实际情况更新。
   
## 六、参考资料
https://blog.csdn.net/m0_72225765/article/details/145575032?fromshare=blogdetail&sharetype=blogdetail&sharerId=145575032&sharerefer=PC&sharesource=m0_74149651&sharefrom=from_link
