def CaesarCipher():
    c=mingwen. get("0.0", "end")[:-1]
    b=""
    miwen. delete("0.0", "end")
    for i in range(len(c)):
        if ' a'<=c[i]<=' w' or ' A'<=c[i]<=' W':
            b=b+chr (ord(c[i])+3)
        elif ' x' <=c[i]<=' z' or ' X'<=c[i]<=' Z' :
            b=b+chr (ord(c[i])-23)
        else:
             b=b+c[i]
    miwen. insert("0.0", b)
