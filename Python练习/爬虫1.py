Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> response = urllib.request.urlopen("http://www.fishc.com")
 
>>> html = response.read()
>>> print(html)
b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> \n<html xmlns="http://www.w3.org/1999/xhtml"> \n<head> \n<meta http-equiv="Content-Type" content="text/html; charset=gb2312">\n<title></title> \n<!--Dr.COMWebLoginID_0.htm-->\n\n<script>document.write(\'<script type="text/javascript" src="https://\'+window.location.hostname+\':801/eportal/release/a41.js?version=1.4_\'+(new Date()).valueOf()+\'"><\\/script>\');</script>\n\n<script type="text/javascript"> \nsv=0;sv1=0;v6=\'http://[::]:9002/v6                                     \';myv6ip=\'                                       \';v4serip=\'192.168.100.11\' ;m46=0;v46ip=\'172.27.142.184\'                         ;\nvid=0   ;mip=172027142184;Gno=0000;vlanid="0"   ;AC="";                          ipm="c0a8640b";ss1="000d480639e9";ss2="0000";ss3="ac1b8eb8";ss4="000000000000";ss5="172.27.142.184" ;ss6="192.168.100.11" ;hotel=0;\nauthtype=1;authloginport=801;authloginpath=\'/eportal/?c=ACSetting&a=Login\';authloginparam=\'\';queryport=801;querypath=\'/eportal/?c=ACSetting&a=Query\';queryparam=\'\';\nauthlogoutpath=\'/eportal/?c=ACSetting&a=Logout&ver=1.0\'; authlogoutport=801;\n\nif((AC!="12345678901234567890123456")&&(AC!="")){\n\tif(hotel!=0)window.location="7.htm";\n}\nif(getQueryString(\'wlanacip\') !==null || getQueryString(\'wlanacname\') !== null){\n\tdelCookie(\'online\');\n}\n</script>\n</head>\n\n<body >\n<form name="f79" action=""+window.location.search method=post>\n<input type=hidden name=DDDDD value=0>\n<input type=hidden name=upass value=10,30>\n<input type=hidden name=R4 value=2>\n<input type=hidden name=0MKKey value=\'login\'>\n</form>\n\n<form name="f78" action=""+window.location.search method=post>\n<input type=hidden name=DDDDD value=0>\n<input type=hidden name=upass value=20,70>\n<input type=hidden name=R4 value=2>\n<input type=hidden name=0MKKey value=\'login\'>\n</form>\n\n</body>\n</html>\n<script type="text/javascript">\n// \xb7\xc3\xce\xca\xc9\xe8\xb1\xb8:0-\xc6\xe4\xcb\xfb\xa3\xbb1-PC\xa3\xbb2-\xca\xd6\xbb\xfa\xa3\xbb3-\xc6\xbd\xb0\xe5\nvar iTermType = getTermType();\n\nvar url = window.location.search;\nif(url.indexOf("?") > 0) url = url.substr(url.indexOf("?"));\nif(window.location.protocol == "http:"){\n\twindow.location.href="https://"+window.location.hostname+"/a79.htm"+url;\n}\nif(iTermType == 2){\n\tif(enPerceive == 1){\n\t\tdocument.f79.action=""+url;\n\t\tdocument.f79.submit();\n\t}\n\telse{\n\t\twindow.location.href="a30.htm"+url;\n\t}\n}\nelse{\n\tif(enPerceive == 1){\n\t\tdocument.f78.action=""+url;\n\t\tdocument.f78.submit();\n\t}\n\telse{\n\t\twindow.location.href="a70.htm"+url;\n\t}\n}\n</script>'
>>> html = html.decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    html = html.decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 1905: invalid start byte
>>> html = html.decode("utf-8")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    html = html.decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 1905: invalid start byte
>>> 
=============================== RESTART: Shell ===============================
>>> import urllib.request
>>> response = urllib.request.urlopen("https://ilovefishc.com")
>>> html = response.read()
>>> print(html)
b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="keywords" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4|\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6">\n    <meta name="description" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4\xe4\xb8\xba\xe5\xa4\xa7\xe5\xae\xb6\xe6\x8f\x90\xe4\xbe\x9b\xe6\x9c\x80\xe6\x9c\x89\xe8\xb6\xa3\xe7\x9a\x84\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6\xe3\x80\x82">\n    <meta name="author" content="\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4">\n    <title>\xe9\xb1\xbcC\xe5\xb7\xa5\xe4\xbd\x9c\xe5\xae\xa4-\xe5\x85\x8d\xe8\xb4\xb9\xe7\xbc\x96\xe7\xa8\x8b\xe8\xa7\x86\xe9\xa2\x91\xe6\x95\x99\xe5\xad\xa6|Python\xe6\x95\x99\xe5\xad\xa6|Web\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|\xe5\x85\xa8\xe6\xa0\x88\xe5\xbc\x80\xe5\x8f\x91\xe6\x95\x99\xe5\xad\xa6|C\xe8\xaf\xad\xe8\xa8\x80\xe6\x95\x99\xe5\xad\xa6|\xe6\xb1\x87\xe7\xbc\x96\xe6\x95\x99\xe5\xad\xa6|Win32\xe5\xbc\x80\xe5\x8f\x91|\xe5\x8a\xa0\xe5\xaf\x86\xe4\xb8\x8e\xe8\xa7\xa3\xe5\xaf\x86|Linux\xe6\x95\x99\xe5\xad\xa6</title>\n    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">\n    <link rel="stylesheet" href="css/styles.css">\n    <!-- <link rel="stylesheet" href="css/timeline.css"> -->\n    <script src="js/jq.js"></script>\n    <script src="js/fishcEgg.js"></script>\n    <script>\n        $(document).ready(function() {\n            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;\n\n            createStoryJS({\n                type:       \'timeline\',\n                width:      \'auto\',\n                height:     windowHeight,\n                source:     \'data.json\',\n                start_at_end:true,                          //OPTIONAL START AT LATEST DATE\n                embed_id:   \'my-timeline\'\n            });\n\n            // \xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe5\x88\xa4\xe6\x96\xad\xef\xbc\x8c\xe5\xa6\x82\xe6\x9e\x9c\xe6\x98\xafIE\xe5\xbc\xb9\xe5\x87\xba\xe6\x8f\x90\xe7\xa4\xba\xe6\xa1\x86\n            function getExplore(){\n                var Sys = {};\n                var ua = navigator.userAgent.toLowerCase();\n                var s;\n                (s = ua.match(/rv:([\\d.]+)\\) like gecko/)) ? Sys.ie = s[1] :\n                    (s = ua.match(/msie ([\\d\\.]+)/)) ? Sys.ie = s[1] :\n                        (s = ua.match(/edge\\/([\\d\\.]+)/)) ? Sys.edge = s[1] :\n                            (s = ua.match(/firefox\\/([\\d\\.]+)/)) ? Sys.firefox = s[1] :\n                                (s = ua.match(/(?:opera|opr).([\\d\\.]+)/)) ? Sys.opera = s[1] :\n                                    (s = ua.match(/chrome\\/([\\d\\.]+)/)) ? Sys.chrome = s[1] :\n                                        (s = ua.match(/version\\/([\\d\\.]+).*safari/)) ? Sys.safari = s[1] : 0;\n                // \xe6\xa0\xb9\xe6\x8d\xae\xe5\x85\xb3\xe7\xb3\xbb\xe8\xbf\x9b\xe8\xa1\x8c\xe5\x88\xa4\xe6\x96\xad\n                if (Sys.ie) alert(\'\xe8\xaf\xb7\xe4\xbd\xbf\xe7\x94\xa8\xe9\x9d\x9eIE\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe6\x89\x93\xe5\xbc\x80\xe6\x9c\xac\xe4\xb8\xbb\xe9\xa1\xb5\');\n\n            }\n            getExplore();\n\n        });\n    </script>\n    <!-- <script src="js/timeline-min.js"></script>\n    <script src="js/embed.js"></script> -->\n    <!-- <script src="https://cdn.bootcss.com/timelinejs/2.36.0/js/storyjs-embed.js"></script> -->\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js"></script>\n    <!-- END TimelineJS -->\n</head>\n<body>\n<div id="my-timeline"></div>\n</body>\n</html>'
>>> html = html.decode("utf-8")
>>> print(html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="鱼C工作室|免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学">
    <meta name="description" content="鱼C工作室为大家提供最有趣的编程视频教学。">
    <meta name="author" content="鱼C工作室">
    <title>鱼C工作室-免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学</title>
    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/styles.css">
    <!-- <link rel="stylesheet" href="css/timeline.css"> -->
    <script src="js/jq.js"></script>
    <script src="js/fishcEgg.js"></script>
    <script>
        $(document).ready(function() {
            var windowHeight = document.documentElement.clientHeight || document.body.clientHeight;

            createStoryJS({
                type:       'timeline',
                width:      'auto',
                height:     windowHeight,
                source:     'data.json',
                start_at_end:true,                          //OPTIONAL START AT LATEST DATE
                embed_id:   'my-timeline'
            });

            // 浏览器判断，如果是IE弹出提示框
            function getExplore(){
                var Sys = {};
                var ua = navigator.userAgent.toLowerCase();
                var s;
                (s = ua.match(/rv:([\d.]+)\) like gecko/)) ? Sys.ie = s[1] :
                    (s = ua.match(/msie ([\d\.]+)/)) ? Sys.ie = s[1] :
                        (s = ua.match(/edge\/([\d\.]+)/)) ? Sys.edge = s[1] :
                            (s = ua.match(/firefox\/([\d\.]+)/)) ? Sys.firefox = s[1] :
                                (s = ua.match(/(?:opera|opr).([\d\.]+)/)) ? Sys.opera = s[1] :
                                    (s = ua.match(/chrome\/([\d\.]+)/)) ? Sys.chrome = s[1] :
                                        (s = ua.match(/version\/([\d\.]+).*safari/)) ? Sys.safari = s[1] : 0;
                // 根据关系进行判断
                if (Sys.ie) alert('请使用非IE浏览器打开本主页');

            }
            getExplore();

        });
    </script>
    <!-- <script src="js/timeline-min.js"></script>
    <script src="js/embed.js"></script> -->
    <!-- <script src="https://cdn.bootcss.com/timelinejs/2.36.0/js/storyjs-embed.js"></script> -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/timelinejs/2.36.0/js/storyjs-embed.js"></script>
    <!-- END TimelineJS -->
</head>
<body>
<div id="my-timeline"></div>
</body>
</html>
>>> 
