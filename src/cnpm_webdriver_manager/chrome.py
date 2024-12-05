from typing import Optional

from webdriver_manager import chrome
from webdriver_manager.core.download_manager import DownloadManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from webdriver_manager.core.os_manager import OperationSystemManager, ChromeType

from cnpm_webdriver_manager.drivers.chrome import ChromeDriver


class ChromeDriverManager(chrome.ChromeDriverManager):
    def __init__(
        self,
        driver_version: Optional[str] = None,
        name: str = 'chromedriver',
        url: str = 'https://registry.npmmirror.com/binary.html?path=chromedriver/',
        latest_release_url: str = 'https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE',
        chrome_type: str = ChromeType.GOOGLE,
        download_manager: Optional[DownloadManager] = None,
        cache_manager: Optional[DriverCacheManager] = None,
        os_system_manager: Optional[OperationSystemManager] = None
    ):
        super().__init__(
            driver_version=driver_version,
            name=name,
            url=url,
            latest_release_url=latest_release_url,
            chrome_type=chrome_type,
            download_manager=download_manager,
            cache_manager=cache_manager,
            os_system_manager=os_system_manager
        )

        self.driver = ChromeDriver(
            name=name,
            driver_version=driver_version,
            url=url,
            latest_release_url=latest_release_url,
            chrome_type=chrome_type,
            http_client=self.http_client,
            os_system_manager=os_system_manager
        )