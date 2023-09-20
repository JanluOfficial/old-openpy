import os, platform, sys

class os:
    def is_windows(): return True if platform.system() == "Windows" else False
    def is_linux(): return True if platform.system() == "Linux" else False
    def is_mac(): return True if platform.system() == "Darwin" else False
    def is_unix(): return True if os.is_linux() or os.is_mac() else False
    
class architecture:
    def is_64bit(): return True if sys.maxsize > 2**32 else False 
    def is_32bit(): return True if sys.maxsize < 2**32 and sys.maxsize > 2**16 else False 
    def is_16bit(): return True if sys.maxsize < 2**16 else False 
    def is_arm(): return True if platform.machine().startswith("arm") else False 
    def is_x86(): return True if platform.machine().startswith("x86") else False 
    def is_amd64(): return True if platform.machine().startswith("AMD64") else False 
    def is_ppc(): return True if platform.machine().startswith("ppc") else False 
    def is_mips(): return True if platform.machine().startswith("mips") else False 
    def is_ppc64(): return True if platform.machine().startswith("ppc64") else False 
    def is_mips64(): return True if platform.machine().startswith("mips64") else False 
    def is_s390(): return True if platform.machine().startswith("s390") else False 
    def is_s390x(): return True if platform.machine().startswith("s390x") else False 
    def is_sparc(): return True if platform.machine().startswith("sparc") else False 
    def is_sparc64(): return True if platform.machine().startswith("sparc64") else False
    
