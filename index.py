def zpracuj_soubor(nazev_vstupu, nazev_vystupu):
    with open(nazev_vstupu, encoding = "utf-8") as vstup,  \
        open(nazev_vystupu, "w", encoding = "utf-8") as vystup:
        for radek in vstup:
            radek = radek.strip()
            if not radek:
                continue

            jmeno, vek, pohlavi, boolean, datum, hodnoceni = radek.split('#')

            hodnoceni = float(hodnoceni)

            jeZviratko = False

            if jeZviratko == True:
                boolean = "ano"
            
            else:
                boolean = "ne"
            

            if hodnoceni > 2.5:
                dobre_hodnoceni = True

            else:
                dobre_hodnoceni = False

            if dobre_hodnoceni == True:
                vystup.write(f"jmeno: {jmeno}\tvek: {vek}\tpohlavi: {pohlavi}\tboolean: {boolean}\tdatum: {datum}\thodnoceni: {hodnoceni}\n")

if __name__ == "__main__":
    zpracuj_soubor("data/postavy.txt", "data/oblibene-postavy.txt")
          
                

            