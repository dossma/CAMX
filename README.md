# camx
Scraping exhibitors from camx 2022 (The Composites and Advanced Materials Expo).

## Disclaimer
This is for educational purpose only.

## Motivation
Get a better, structured overview or do analysis on where the companies operate and in which fields.

## Procedure and result

The webdriver runs headless, which means the browser will actually not be visible. 
A couple of useful settings have been set:
- `"javascript.enabled", True`  It is here required that Javascript is enabled.
- `"permissions.default.image", 2,` No images will be loaded.
- `"plugin.state.flash", 0` Flash is deactivated.
- `"toolkit.telemetry.unified", False` Telemetry is deactivated.

The following data is being extracted and saved into a `csv` spreadsheet:
- Company name
- Homepage URL
- Address
- Phone and Fax number
- Product categories (the sub-fields in which they operate)
- Description (a company's profile description) 

## Get started
After the development setup has been established (see below), just run it.

## Development setup
Prominent required external libraries are
- Selenium: https://github.com/SeleniumHQ/selenium
- Geckodriver https://github.com/mozilla/geckodriver

__Selenium:__
```sh
pip install selenium
```
__Geckodriver:__
Download latest release and put it into your development folder, (i.e. C:/Users/yourUsername/Anaconda3). 
Make sure this path is set as environmental variable. 

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)
