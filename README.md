# Filhåndtering, undtagelseshåndtering og Virtual Environment

## Indledende overvejelser

Jeg har lært en pokkers masse denne uge og arbejdet med en masse ting, som jeg aldrig har prøvet kræfter med før. Dog ved jeg ikke, om jeg overhovedet har forstået opgaverne rigtigt. Det er uklart for mig, hvad man egentlig gør, når man arbejder med filer og datamigrering. Hvorfor migrerer man data fra en fil til en anden? Hvad vil det sige at opsummere data? Hvordan ved jeg, om migreringsprocessen er modstandsdygtig? Hvad skal den være modstandsdygtig imod? Hvilke scenarier skal jeg overveje? Var det meningen, at jeg skulle gøre andet end bare læse filerne, siden skrivebeskyttelse nævnes i opgavebeskrivelsen? Trods vaklende opgaveforståelse er jeg kommet frem til nogle opgaveløsninger, så om ikke andet har jeg da lært et og andet om at arbejde i Python.

## Sådan køres koden

1. Naviger til det valgte `directory`, enten `opg-1` eller `opg-2`
2. Aktiver det relevante `venv`, enten `opg-1-venv` eller `opg-2-venv`

## Opgave 1

Min opgaveløsning består af to funktioner:

1. `get_log_search_keywords`:

- Et `dict` med log-keywords defineres til brug for søgning/filtrering i logfilen.
- I et `while` loop kan brugeren vælge keywords og tilføje dem til en `keywords_list`.
- Fejlhåndtering: Eventuelle input-fejl håndteres løbende.

2. `create_log_detail_files`:

- Vha. Pythons `os` modul oprettes et nyt `directory`, `log_details`, i `current directory`.
- Nye selvstændige filer oprettes for hvert keyword; alle filer placeres i `log_details`.
- Logfilen læses, og alle rækker, som matcher et keyword fra `keywords–list`, skrives til den relevante fil.
- I et `print statement` informeres om antal nye logfiler oprettet, hvilke keywords der blev anvendt til at oprette de nye filer, og hvor de er placeret.
- Undtagelseshåndtering: Al kode, som kører logikken beskrevet ovenfor, er placeret i en `try` blok, og to `except` blokke håndtere hhv. `FileNotFoundError` og evt. andre undtagelser.

## Opgave 2

Min opgaveløsning består af to filer:

1. `data_migration.py`

- De nødvendige `permissions` tjekkes, resultaterne printes, og hvis der er `read permissions`, køres datavalideringen.
- Datafilen læses vha. `csv.DictReader` og brydes op i rækker, hvorefter hver række køres igennem flere forskellige datavalideringsfunktioner, som importeres fra `validation.py`.

2. `validation.py`

- `patterns` og `validation_functions` defineres.
- Valideringsfunktionerne tjekker formatet på fem forskellige datatyper: `customer_id`, `name`, `email`, `purchase_amount` og `phone_number`. Visse tjek foretages med `regular expressions`, visse vha. metoder og funktioner importeret fra pakkerne `email_validator` og `phonenumbers`.
- Undtagelseshåndtering: Alle valideringsfunktioner er bygget op med `try` og `except` blokke. I `try` blokken testes data mod et `pattern`, og i `except` blokken printes eventuelle anomalier med tydelig information om `row_id`, `field_name` og `field_value`.

## Overvejelser over kodens robusthed

Jeg har efter bedste evne implementeret fejl- og undtagelseshåndtering på alle niveauer i min kode. Desuden har jeg bestræbt mig på at gøre koden dynamisk og fleksibel, fx ved at anvende `os` modulet frem for at hardcode en ny `directory path`, og ved at definere `patterns` og `validation_functions`, som kan tilgås og anvendes dynamisk afhængig af datasættet.
En potentielt stor brist i min kode er, at jeg arbejder med prædefinerede `patterns`. Det medfører eksempelvis, at et datasæt med et andet format på `customer_id` end fire cifre ikke kan valideringstestes med den nuværende kode. Eventuelt bør disse `patterns` trækkes ud af `validation.py` filen og placeres i en separat fil, så det fremgår tydeligt, at alle `patterns` bør efterses og justeres efter de data, som skal valideres.

## NB

I `validation.py` får jeg en fejlmeddelelse på mine `imports`: `Import "email_validator"/"phonenumbers" could not be resolved`. Koden virker imidlertid, og pakkerne er installeret korrekt i `opg-2-venv`. Jeg har ikke kunnnet spore årsagen til fejlmeddelelserne.