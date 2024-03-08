# Filhåndtering, undtagelseshåndtering og Virtual Environment

## Indledende overvejelser

Jeg har lært en pokkers masse denne uge og arbejdet med en masse ting, som jeg aldrig har prøvet kræfter med før. Dog ved jeg ikke, om jeg overhovedet har forstået opgaverne rigtigt. Det er uklart for mig, hvad man egentlig gør, når man arbejder med filer og datamigrering. Hvorfor migrerer man data fra en fil til en anden? Hvad vil det sige at opsummere data? Hvordan ved jeg, om migreringsprocessen er modstandsdygtig? Hvad skal den være modstandsdygtig over for? Hvilke scenarier skal jeg overveje? Var det meningen, at jeg skulle gøre andet end bare læse filerne, siden skrivebeskyttelse nævnes i opgavebeskrivelsen? Trods en vaklende forståelse af opgavebeskrivelsen er jeg kommet frem til nogle løsninger, så om ikke andet har jeg da lært et og andet om at arbejde i Python.

## Sådan køres koden

1. Naviger til det ønskede `directory`, enten `opg-1` eller `opg-2`
2. Aktiver det relevante `venv`, enten `opg-1-venv` eller `opg-2-venv`
3. Installer `requirements.txt`

## Overvejelser om kodens robusthed

Jeg har efter bedste evne implementeret fejl- og undtagelseshåndtering på alle niveauer i min kode. Desuden har jeg bestræbt mig på at gøre koden dynamisk og fleksibel, fx ved at anvende `os` modulet frem for at hardcode en ny `directory path`, og ved at definere `patterns` og `validation_functions`, som kan tilgås og anvendes dynamisk afhængig af datasættet.
En potentielt stor brist i min kode er, at jeg i datavalideringen i opgave 2 arbejder med prædefinerede `patterns`. Det medfører eksempelvis, at et datasæt med et andet format på `customer_id` end fire cifre ikke kan valideringstestes med den nuværende kode. Eventuelt bør disse `patterns` trækkes ud af `validation.py` filen og placeres i en separat fil, så det fremgår tydeligt, at alle `patterns` bør efterses og justeres efter de data, som skal valideres.

## NB

I `validation.py` får jeg en fejlmeddelelse på mine `imports`: `Import "email_validator"/"phonenumbers" could not be resolved`. Koden virker imidlertid, og når jeg tjekker, hvilke pakker der er installerede, får jeg dette resultat:
```
(opg-2-venv) ajo@Ajos-mac opg-2 % pip3 list
Package         Version
--------------- -------
dnspython       2.6.1
email_validator 2.1.1
idna            3.6
phonenumbers    8.13.31
pip             24.0
setuptools      58.1.0
```
Det lader altså til, at pakkerne faktisk er installeret i Virtual Environment. Jeg har ikke kunnnet spore årsagen til fejlmeddelelserne.