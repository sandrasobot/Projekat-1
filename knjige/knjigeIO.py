import json

datoteka = './datoteke/knjige.json'


def sacuvaj_knjige(knjige):
    with open(datoteka, "w") as f:
        json.dump(knjige, f, indent=10)


def ucitaj_knjige():
    with open(datoteka) as f:
        return json.load(f)