from typing import Optional

from webdriver_manager import firefox
from webdriver_manager.core.download_manager import DownloadManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from webdriver_manager.core.os_manager import OperationSystemManager

from cnpm_webdriver_manager.drivers.firefox import GeckoDriver


class GeckoDriverManager(firefox.GeckoDriverManager):
    def __init__(
        self,
        version: Optional[str] = None,
        name: str = "geckodriver",
        url: str = "https://registry.npmmirror.com/-/binary/geckodriver/",
        latest_release_url: str = "https://registry.npmmirror.com/-/binary/geckodriver/",
        mozila_release_tag: str = "https://registry.npmmirror.com/-/binary/geckodriver/{0}/",
        download_manager: Optional[DownloadManager] = None,
        cache_manager: Optional[DriverCacheManager] = None,
        os_system_manager: Optional[OperationSystemManager] = None
    ):
        super().__init__(
            version=version,
            name=name,
            url=url,
            latest_release_url=latest_release_url,
            mozila_release_tag=mozila_release_tag,
            download_manager=download_manager,
            cache_manager=cache_manager,
            os_system_manager=os_system_manager
        )

        self.driver = GeckoDriver(
            driver_version=version,
            name=name,
            url=url,
            latest_release_url=latest_release_url,
            mozila_release_tag=mozila_release_tag,
            http_client=self.http_client,
            os_system_manager=os_system_manager
        )