from typing import Optional, Literal

from pydantic import BaseSettings, AnyUrl


EnvContext = Literal['local', 'stage', 'prod']
BrowserName = Literal['chrome', 'firefox']


class Settings(BaseSettings):
    context: EnvContext = 'local'
    browser_name: BrowserName = 'chrome'
    browser_quit_after_each_test: bool = False
    browser_window_maximize: bool = False
    browser_window_height: int = 600
    browser_window_width: int = 600
    headless: bool = False
    remote_url: Optional[AnyUrl] = None
    remote_enable_vnc: bool = True
    remote_screen_resolution: str = '1920x1080x24'


settings = Settings(_env_file=f'config.{Settings().context}.env')
