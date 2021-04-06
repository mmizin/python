# Telegram Python Fundamentals.pdf
#
# Modify the constructor to increment the counter each time a new instance
# is created by adding the line WebBrowser.number_of_web_browsers += 1. This
# increments the number_of_web_browsers attribute of our class by 1 and will be
# called each time a new instance is initialized:

# class WebBrowse:
#     number_of_web_browsers = 0
#     connected = True
#
#     def __init__(self):
#         WebBrowse.number_of_web_browsers += 1
#
#
# chrome = WebBrowse()
# print(f'{chrome} ::: number_of_web_browsers = {chrome.number_of_web_browsers}')
#
# firefox = WebBrowse()
# print(f'{firefox} ::: number_of_web_browsers = {firefox.number_of_web_browsers}')

##########################################################################################################

# One common use case for class methods is when you're making factory methods. A
# factory method is one that returns objects. They can be used for returning objects
# of a different type or with different attributes. Let's add a class method called with_
# incognito() to our WebBrowser class that initializes a web browser object in incognito
# mode:

# class WebBrowser:
#
#     def __init__(self, page):
#         self.history = [page]
#         self.current_page = page
#         self.is_incognito = False
#
#     def navigate(self, new_page):
#         self.current_page = new_page
#         if not self.is_incognito:
#             self.history.append(new_page)
#
#     def clear_history(self):
#         self.history[:-1] = []
#
#     @classmethod
#     def with_incognito(cls, page):
#         instance = cls(page)
#         instance.is_incognito = True
#         instance.history = []
#         return instance
#
# print(WebBrowser.with_incognito)
#
# chrome = WebBrowser.with_incognito('inckognito_page')
# firefox = WebBrowser('simple_page')
#
# print(chrome.is_incognito)
# print(firefox.is_incognito)
#
# print(chrome.history)
# print(firefox.history)

#####################################################################################################################

# Creating Class Methods and Using Information Hiding

class MusicPlayer:
    firmware_version = 1.0

    def __init__(self):
        self.__tracks = ['papa rock', 'nirvana', 'metallica']
        self.current_track = -1
        self.state = False

    def play(self):

        if not self.state:
            self.state = True
            self.current_track += 1
            self.current_track == self.__tracks[self.current_track]
            print(f'Current track is {self.__tracks[self.current_track]}')

    def track_list(self):
        return self.__tracks

    @classmethod
    def update_firmware(cls, new_version):
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version


player = MusicPlayer()
print(player)
print(player.track_list())
player.play()
