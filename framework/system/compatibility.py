import platform

class isOS:
    def Windows():
        if platform.system() == "Windows":
            return True
        else:
            return False

    def Darwin():
        if platform.system() == "Darwin":
            return True
        else: 
            return False

    def Linux():
        if platform.system() == "Linux":
            return True
        else: 
            return False