
class AppConfig:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            cls._instance.settings={}
        return cls._instance
    def set_settings(self,k,value):
        self.settings[k]=value
    def get_setting(self,k):
        return self.settings.get(k)
#test
con1=AppConfig()
con2=AppConfig()
print(f"same instance?{con1 is con2}")
con1.set_settings("theme","dark")
print(f"theme from config:{con2.get_setting("theme")}")
