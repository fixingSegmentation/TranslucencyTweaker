import os
os.system("chmod +x launch")
route = os.getcwd()
with open("TranslucencyTweaker.desktop","w") as fh:
    with open("desktopTemplate", "r") as template:
        fh.write(template.read())
    fh.write("\nPath={path}/\n".format(path = route))
    fh.write("Exec={path}/launch\n".format(path = route))

os.system("chmod +x TranslucencyTweaker.desktop")

os.system("cp TranslucencyTweaker.desktop ~/.local/share/applications/")
