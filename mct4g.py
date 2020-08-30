import re
import os
'''
   @author Scimen_Phy
   @credit latex.codecogs.com
'''
def transmd(fileName, path=os.getcwd()+r'\\'):
    def transfer(matched):
        latexCode = re.sub(r"\$", '', matched.group())
        latexCode = re.sub(r"\\", r'\\\\', latexCode)
        return "![](https://latex.codecogs.com/png.latex?"+latexCode+")"
    p = re.compile(r"(\$\$.*?\$\$)|(\$.*?\$)")
    text = ''.join(open(path + fileName, 'r', encoding='utf8').readlines())
    textBackUp = text
    text = re.sub(p, transfer, text)
    open(path+fileName+".bak", "w", encoding='utf8').write(textBackUp)
    open(path+fileName, "w", encoding='utf8').write(text)

transmd("0.md")
