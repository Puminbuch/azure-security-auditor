import json
def prüfe_storage_account(eintrag):
    if eintrag["public_access"] or not eintrag["encryption_enabled"]:
        return True
    else:
        return False
def prüfe_vm(eintrag):
    if eintrag["ssh_open_to_all"] or eintrag["rdp_open_to_all"] or not eintrag["disk_encrypted"]:
        return True
    else:
        return False

with open("testdaten.json") as f:
    daten = json.load(f)

print(daten)

for eintrag in daten:
    if eintrag["type"] == "storage_account":
        if prüfe_storage_account(eintrag):
            print(eintrag["name"], "ist UNSICHER")
        else:
            print(eintrag["name"], "ist sicher")
    elif eintrag["type"] == "vm":
        if prüfe_vm(eintrag):
            print(eintrag["name"], "ist UNSICHER")
        else:
            print(eintrag["name"],"ist sicher")