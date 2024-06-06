with open("questions.tex", "r") as f:
    lines = f.readlines()
    lines.insert(3, "\\usepackage{fontspec}\n")
    lines.insert(4, "\\setmainfont{OpenDyslexic}\n")
with open("questions-dyslexia.tex", "w") as f:
    f.writelines(lines)
