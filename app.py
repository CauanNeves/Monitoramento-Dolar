from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def start_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--start-maximized', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'C:\\Users\\secretario',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)

    return driver
    
def main():
    driver = start_driver()
    try:
        #Entrando no site
        driver.get('https://economia.uol.com.br/cotacoes/cambio/')
        
        graphic = driver.execute_script(f'''
            return document.evaluate(
                '//div[@class= "col-sm-24 col-xs-8 chart-content "]', 
                document,
                null, 
                XPathResult.FIRST_ORDERED_NODE_TYPE, 
                null
                ).singleNodeValue;
            ''')
        driver.execute_script('arguments[0].scrollIntoView({behavior: "instant", block: "center"});', graphic)
        graphic.screenshot('graphic.png')
        
    finally:
        driver.quit()
    
if __name__ == '__main__':
    main()