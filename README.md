# 项目描述

这是基于 [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager/tree/v4.0.2) 的项目，本项目使用 [淘宝 npm 镜像](https://npmmirror.com/) 来加速下载浏览器驱动，仅适用于 Chrome、Firefox 和 Opera。

### 依赖

> [!IMPORTANT]
> [webdriver-manager==4.0.2](https://github.com/SergeyPirogov/webdriver_manager/tree/v4.0.2)

## 安装

```bash
pip install cnpm-webdriver-manager
```

## 用法

### 使用 Chrome

```python
# selenium 3
from selenium import webdriver
from cnpm_webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

```python
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from cnpm_webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
```

### 使用 Firefox

```python
# selenium 3
from selenium import webdriver
from cnpm_webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
```

```python
# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from cnpm_webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
```

### 使用 Opera

```python
# selenium 3

from selenium import webdriver
from selenium.webdriver.chrome import service
from cnpm_webdriver_manager.opera import OperaDriverManager

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
```

```python
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome import service
from cnpm_webdriver_manager.opera import OperaDriverManager

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url, options=options)
```

如果 Opera 浏览器安装在 Windows 系统中，且位置处于 **C:/Program Files** 或 **C:/Program Files (x86)** 之外；同时，在所有类 Unix 系统变体以及 Mac 系统中，其安装位置处于 **/usr/bin/opera** 之外，那么请使用以下代码，

```python
options = webdriver.ChromeOptions()
options.binary_location = "opera.exe 的路径"
driver = webdriver.Remote(webdriver_service.service_url, options=options)
```

> [!IMPORTANT]
> 详细用法请查看 [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager/tree/v4.0.2) 项目文档
