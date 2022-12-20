# camx
Scraping exhibitors from camx 2022 (The Composites and Advanced Materials Expo).

## Disclaimer
This is for educational purpose only.

## Motivation
Get a better, structured overview or do analysis on where the companies operate and in which fields.
Do data engineering on companies from the composite and advanced materials sector.

## Procedure
The following data is being extracted:
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

__Ad-block file: __
While this is not essential (comment out the specific line in the code if you wish), it is useful to use an ad-blocker for a more efficient procedure and anhanced privacy. For that, download an adblock file (`xpi` extension) and paste it into your project's (root) folder.
The adblock file used here was taken from https://github.com/gorhill/uBlock/releases. If you use a different file, adjust the file name in the specific line.

## Meta

Author: Jonas Dossmann

Distributed under the AGPL-3.0 license.

[https://github.com/dossma/](https://github.com/dossma/)
