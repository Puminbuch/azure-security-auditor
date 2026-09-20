import json

with open("testdaten.json") as f:
    daten = json.load(f)

print(daten)

for eintrag in daten:
    if eintrag["type"] == "storage_account":
        if eintrag["public_access"] or not eintrag["encryption_enabled"]:
            print(eintrag["name"], "ist UNSICHER")
        else:
            print(eintrag["name"], "ist sicher")
    elif eintrag["type"] == "vm":
        if eintrag["ssh_open_to_all"] or eintrag["rdp_open_to_all"] or not eintrag["disk_encrypted"]:
            print(eintrag["name"], "ist UNSICHER")
        else:
            print(eintrag["name"],"ist sicher")