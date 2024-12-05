import json

from packaging import version

from webdriver_manager.core.logger import log
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.drivers import chrome


class ChromeDriver(chrome.ChromeDriver):
    def __init__(
        self,
        name,
        driver_version,
        url,
        latest_release_url,
        http_client,
        os_system_manager,
        chrome_type=ChromeType.GOOGLE
    ):
        super().__init__(
            name=name,
            driver_version=driver_version,
            url=url,
            latest_release_url=latest_release_url,
            http_client=http_client,
            os_system_manager=os_system_manager,
            chrome_type=chrome_type
        )

    def get_latest_release_version(self):
        determined_browser_version = self.get_browser_version_from_os()
        log(f'Get LATEST {self._name} version for {self._browser_type}')
        if determined_browser_version is not None and version.parse(determined_browser_version) >= version.parse('115'):
            url = 'https://cdn.npmmirror.com/binaries/chrome-for-testing/latest-patch-versions-per-build.json'
            response = self._http_client.get(url)
            response_dict = json.loads(response.text)
            determined_browser_version = response_dict.get('builds').get(determined_browser_version).get('version')
            return determined_browser_version
        elif determined_browser_version is not None:
            # Remove the build version (the last segment) from determined_browser_version for version < 113
            determined_browser_version = '.'.join(determined_browser_version.split('.')[:3])
            latest_release_url = f'{self._latest_release_url}_{determined_browser_version}'
        else:
            latest_release_url = self._latest_release_url

        resp = self._http_client.get(url=latest_release_url)
        return resp.text.rstrip()

    def get_url_for_version_and_platform(self, browser_version, platform):
        url = 'https://cdn.npmmirror.com/binaries/chrome-for-testing/known-good-versions-with-downloads.json'
        response = self._http_client.get(url)
        data = response.json()
        versions = data['versions']

        if version.parse(browser_version) >= version.parse('115'):
            short_version = '.'.join(browser_version.split('.')[:3])
            compatible_versions = [v for v in versions if short_version in v['version']]
            if compatible_versions:
                latest_version = compatible_versions[-1]
                log(f'WebDriver version {latest_version["version"]} selected')
                downloads = latest_version['downloads']['chromedriver']
                for d in downloads:
                    if d['platform'] == platform:
                        return d['url']
        else:
            for v in versions:
                if v['version'] == browser_version:
                    downloads = v['downloads']['chromedriver']
                    for d in downloads:
                        if d['platform'] == platform:
                            return d['url']

        raise Exception(f'No such driver version {browser_version} for {platform}')