class Phone:
    def call(self):
        print("You can call")
    
    def message(self):
        print("You can message")

class Samsung(Phone):
    def photo(self):
        print("You can take photo")

p=Phone()
p.call()
p.message()
s=Samsung()
s.call()
s.message()
s.photo()