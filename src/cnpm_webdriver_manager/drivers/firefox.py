from datetime import datetime

from webdriver_manager.core.logger import log
from webdriver_manager.drivers import firefox


class GeckoDriver(firefox.GeckoDriver):
    def __init__(
        self,
        name,
        driver_version,
        url,
        latest_release_url,
        mozila_release_tag,
        http_client,
        os_system_manager
    ):
        super().__init__(
            name=name,
            driver_version=driver_version,
            url=url,
            latest_release_url=latest_release_url,
            mozila_release_tag=mozila_release_tag,
            http_client=http_client,
            os_system_manager=os_system_manager
        )

    def get_latest_release_version(self) -> str:
        determined_browser_version = self.get_browser_version_from_os()
        log(f'Get LATEST {self._name} version for {determined_browser_version} firefox')
        resp = self._http_client.get(self.latest_release_url)
        resp = resp.json()
        resp.sort(key=lambda x: datetime.fromisoformat(x['date'].replace('Z', '+00:00')), reverse=True)
        return resp[0]['name'][:-1]

    def get_driver_download_url(self, os_type):
        '''Like https://registry.npmmirror.com/-/binary/geckodriver/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz'''
        driver_version_to_download = self.get_driver_version_to_download()
        log(f'Getting latest mozilla release info for {driver_version_to_download}')
        resp = self._http_client.get(self.tagged_release_url(driver_version_to_download))
        assets = resp.json()
        name = f'{self.get_name()}-{driver_version_to_download}-{os_type}.'
        output_dict = [asset for asset in assets if asset['name'].startswith(name)]
        return output_dict[0]['url']