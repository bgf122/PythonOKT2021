import http_pyynto

postinumerot = http_pyynto.hae_postinumerot()

for numero, paikka in postinumerot.items():
    if paikka == 'SMART POST':
        postinumerot[numero] = 'SMARTPOST'
    elif paikka == 'SMARTPSOT':
        postinumerot[numero] = 'SMARTPOST'


def anna_syote():
    postitoimipaikka = input("Kirjoita postitoimipaikka: ").strip()

    return postitoimipaikka


def suorita(input):
    vastaus = []
    if input.upper() in postinumerot.values():
        for numero, paikka in postinumerot.items():
            if paikka == input.upper():
                vastaus.append(numero)
        vastaus.sort()
        print(*vastaus, sep=", ")
    else:
        print("Virheellinen postitoimipaikka!")

    return vastaus


if __name__ == '__main__':
    suorita(anna_syote())
