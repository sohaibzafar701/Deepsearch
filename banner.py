
class Banner(object):
    def LoadDeepSearchBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''
            
      __ \                  ___|                      |     
      |   |  _ \  _ \ __ \\___ \   _ \  _` |  __| __| __ \  
      |   |  __/  __/ |   |     |  __/ (   | |   (    | | | 
     ____/ \___|\___| .__/_____/ \___|\__,_|_|  \___|_| |_| 
                _|                                     
        
        
        Developed By: sohaib zafar
        https://github.com/sohaibzafar701
        Version: 1.0
              '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)
            
            

            
