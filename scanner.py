import json

with open("testdaten.json") as f:
    daten = json.load(f)

print(daten)

for eintrag in daten:
    if eintrag["public_access"] or not eintrag["encryption_enabled"]:
        print(eintrag["name"], "ist UNSICHER")
    else:
        print(eintrag["name"], "ist sicher")