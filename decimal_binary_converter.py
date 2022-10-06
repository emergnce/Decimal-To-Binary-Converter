#Decimal to Binary Converter:

def binaerzahl(dezimalzahl):
    binaer_number = []
    if dezimalzahl == 0:
        print("Die Dezimalzahl",dezimalzahl, "ist die Binärzahl:", 0)
    else:
        if dezimalzahl == 1:
            binaer_number.append(1)
        else:

            while dezimalzahl > 0:

                if dezimalzahl % 2 == 0:
                    binaer_number.append(0)
                    dezimalzahl = dezimalzahl // 2

                if dezimalzahl % 2 == 1:
                    binaer_number.append(1)
                    dezimalzahl = dezimalzahl // 2

    print("Die Dezimalzahl",dezimalzahl, "ist die Binärzahl:", [i for i in reversed(binaer_number)])



binaerzahl(123456789)



