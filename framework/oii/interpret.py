from rich import print
import os
# import api.choice as choice

import framework.oii.make as make
import framework.text.path as path

def interp(app_name: str, script: list):
    old_cwd = os.getcwd()
    os.chdir(path.get.downloaded_apps_path())
    try:
        os.mkdir(app_name)
    except FileExistsError: otk = 0
    os.chdir(os.getcwd().replace("\\","/") + "/" + app_name) 
    for line in script:
        code = str(line).split(" ")
        try:
            if code[0] == "oii-ver":
                oii_ver = code[1]

            elif code[0] == "make":
                if code[1] == "cloud": make.make_cloud(code[2], code[3]) 
                elif code[1] == "empty": make.make_empty(code[2]) 
                elif code[1] == "dir": make.make_dir(code[2])

            #elif code[0] == "prompt":
            #    question = ""
            #    for item in range(3,len(code)):
            #        question += item + " " if item != len(code) - 1 else code[item]
            #    if code[2] == "yes_or_no":
            #        choice.yes_or_no(question)
#
            #    elif code[2] == "input":
            #        choice.input_prompt(question)

            elif code[0] == "output":
                printlist = ""
                for item in range(1,len(code)): printlist += code[item] + " "
                print(printlist)

            elif code[0] == "finish":
                print("Script has been completed")
                os.chdir(old_cwd)
                print(os.getcwd())
                break
        except FileExistsError: otk = 0

    if not os.getcwd() == old_cwd:
        os.chdir(old_cwd)
