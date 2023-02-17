Goal
===========================

My chinese video doorbell may stream audio from built-in mic to client. This feature available only in mobile App client. It is also available on PC through web UI but IE browser as client and ActiveX installed required. Since Microsoft drops IE (https://blogs.windows.com/windowsexperience/2022/06/15/internet-explorer-11-has-retired-and-is-officially-out-of-support-what-you-need-to-know/) i started to find a solution how to stream audio to PC without IE.

This solution is based on https://github.com/smartin015/KaicongWiFiCameraControl. For this purpose i've adopted KaicongAudio.py. I get rid from urllib2 as 

1. It is no longer available in latest Python.
2. I ecounter with problem that my doorbell uses "fake" HTTP and (at least) new urllib implementation can't recognize HTTP response that doorbell send (https://stackoverflow.com/questions/75469992/python-status-code-missing-in-http-response). I have to replace urllib with sockets to workaround this.

Usage
===========================
python StreamAudio.py \<doorbell ip or host name\>

Dependencies:
===========================
* Python 2.7
* Python OpenCV
* PyAudio
* PyGame

Links: 
===========================
Original author post: http://www.instructables.com/id/Hack-a-30-WiFi-Pan-Tilt-Camera-Video-Audio-and-Mot/).
