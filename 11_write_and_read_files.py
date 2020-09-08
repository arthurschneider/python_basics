#! /usr/bin/python3

"""
w = Erstelle neue Datei neuer Inhalt
a = Füge Inhalt zum alten Hinzu ansonsten neue Datei mit Inhalt
r = Lese Inhalt der Datei
"""

"""
Hierdurch wird immer eine neue Datei erstellt
und der Inhalt reingeschrieben.
Wird wieder in die Datei geschrieben mit dieser
Methode dann verschwindet der Text aus der
der vorher war. 
"""
text = "Hier ein Beispiel\nDies ist die zweite Zeile."
myfile=open('test.txt','w')
myfile.write(text)
myfile.close()


# ------------------
"""
Dies fügt den Inhalt zu der Datei hinzu.
Wenn es nicht existiert dann wird diese vorher erzeugt.
VORSICHT: Python fügt den Text dort ein wo in der Datei
aufgehört wurde. Es wird nicht standardmäßig in einer
neuen Zeile hinzugefügt.
"""
appendtext = "\nNoch einmal Geronimo!"
appendFile= open("test.txt", "a")
appendFile.write(appendtext)
appendFile.close()


# ------------------
"""
Dise Methode erlaubt es einem die Datei zu lesen.
"""
fileReader = open("test.txt","r")
content=fileReader.read()
print(content)

