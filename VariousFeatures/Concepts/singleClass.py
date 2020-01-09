import os

class FileManager:
    def __init__(self, alpha, bravo):
        self.alpha=alpha
        self.bravo=bravo
    def printer(self):
        print("alpha is "+ self.alpha)
        print("bravo is "+ self.bravo)
fM=FileManager("apple","butter")
print("cock sucker class property "+ fM.alpha)
fM.printer()