
class Banner(object):
    def LoadDeepSearchBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''           
            
 _____                       _____                           _     
|  __ \                     / ____|                         | |    
| |  | |  ___   ___  _ __  | (___    ___   __ _  _ __   ___ | |__  
| |  | | / _ \ / _ \| '_ \  \___ \  / _ \ / _` || '__| / __|| '_ \ 
| |__| ||  __/|  __/| |_) | ____) ||  __/| (_| || |   | (__ | | | |
|_____/  \___| \___|| .__/ |_____/  \___| \__,_||_|    \___||_| |_|
                    | |                                            
                    |_|                                            
        
        
        Developed By: sohaib zafar
        https://github.com/sohaibzafar701
        Version: 1.0
              '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)
            
            

            
