``` python
chrome://version/
130.0.6723.59 (Official Build) (64-bit) (cohort: M130 Rollout)

python -v
Python 3.10.0 ...

pip install selenium
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
...

python web.py
------------- LOGSTART -------------
minimize_window
get https://yhdm.one/vod-play/2024334711/zheng_pian.html
get_log performance
------------- LOGSEND -------------
{'https://yhdm.one/vod-play/2024334711/zheng_pian.html': ['https://yhdm.one/_player_x_/https://v.gsuus.com/play/5eVB9wMe/index.m3u8']}

now you can copy this m3u8 path into vedio.html instead of `g_src = <m3u8 path>` var

use liveserver run vedio.html
```
