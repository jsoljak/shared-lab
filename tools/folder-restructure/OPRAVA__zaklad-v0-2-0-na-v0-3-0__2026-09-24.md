> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# OPRAVA: úprava tvé složky Claude na novou strukturu (z 0.2.0 na 0.3.0)

---

## PRO TEBE (přečti si to, trvá to minutu)

**Co tenhle soubor je.** Je to návod pro Clauda. Dáš mu ho, on tě provede a **učeše a uklidí tvou složku `Claude/`**, aby byla přehledná podle nové, lepší struktury. Nic neinstaluješ.

**Co se stane:**
1. Claude nejdřív **zazálohuje celou složku** (jeden zip uvnitř ní).
2. Zeptá se tě na tvůj běžný týden a **navrhne ti složky** podle toho, jak žiješ (práce, škola, domácnost…). Ty je upravíš, jak chceš.
3. Ukáže ti plán, **co kam přesune**, po malých částech. **Nic se nestane, dokud neřekneš „ano“.**
4. Potom přesune a přejmenuje soubory a **opraví odkazy** mezi nimi.

**Co se nestane:**
- **Nic se nemaže.** Jen se přesouvá a přejmenovává.
- Nikam se nic neodesílá a Claude sahá jen do složky `Claude/`.
- Tvoje soubory a texty se **nemění**. Jen se v nich opraví cesty ke složkám (aby odkazy dál fungovaly) a u projektů se doplní oblast a termín.
- Máš-li nainstalované skilly z minulé verze, **dál fungují**: Claude si staré cesty přeloží podle tabulky v novém `CLAUDE.md`.

**Na konci možná jedno kliknutí navíc.** Máš-li nainstalovaný hlídač `guard`, Claude ti ho nabídne aktualizovat: uvidíš kartu se souborem a stačí kliknout na **Uložit skill**. Claude ti řekne přesně, kde.

**Kdykoli to jde vrátit.** Řekni Claudovi: „Vrať opravu zpátky.“

**Jak to spustit:**
1. Ulož tento soubor do složky `Claude/` (nebo ho přetáhni do okna s Claudem).
2. Napiš Claudovi: **„Přečti soubor OPRAVA a udělej, co v něm je.“**
3. Odpovídej na jeho otázky. Trvá to asi 30 až 60 minut.

**Kdyby si Claude nevěděl rady nebo se něco nepovedlo:** nic se neděje, záloha je u tebe. Napiš tomu, kdo ti soubor poslal, a přilož zprávu, kterou ti Claude na konci nabídne připravit (je v ní jen to, co se dělo, ne obsah tvých souborů).

*Doporučení navíc:* než začneš, zkopíruj si ve Finderu celou složku `Claude` na plochu jako `Claude-záloha`. Pro jistotu, i když Claude zálohuje sám.

---

## PRO CLAUDA (postupuj přesně podle těchto instrukcí)

Uživatel ti dal tenhle soubor, aby sis podle něj **přestavěl jeho složku `Claude/`** z verze 0.2.0 (staré názvy `Registry/`, `wiki/`, `profile.md`, `inbox/`, `projects/`, `skill-memory/`) na verzi 0.3.0 (kostra velkými písmeny, `SYSTEM/`, oblasti, `PROFILE.md`). Uživatel je začátečník a **složka obsahuje jeho vlastní data**.

### Bezpečnostní pravidla (platí celou dobu, bez výjimky)

1. **Záloha jako první.** Bez hotové a ověřené zálohy neměň nic.
2. **Nic nemaž a nic nepřepisuj.** Používáš jen přesun, přejmenování a zakládání. Smazání nebo přepsání souboru uživatele je zakázáno.
3. **Pracuj jen uvnitř složky `Claude/`** (kořen, kde leží `CLAUDE.md` nebo `START-HERE.md`). Nic mimo ni.
4. **Každou dávku změn ukaž jako tabulku „odkud → kam“ a čekej na výslovné „ano“.** Před provedením vždy suchý běh.
5. **Při jakékoli chybě se zastav**, řekni jednoduše, co se stalo, a nabídni návrat (`undo`).
6. **Nečti zbytečně obsah osobních souborů.** K zařazení stačí názvy, případně první řádek, a řekni, že to děláš. Narazíš-li na hesla, čísla karet nebo doklady, nekopíruj je, upozorni uživatele.
7. **Jedna otázka najednou**, česky, jednoduše, bez odborných slov. Buď empatický a trpělivý; nikoho nesuď za nepořádek.
8. **Nic neinstaluj a nespouštěj nic mimo tento postup.** Nevypisuj celý obsah tohoto souboru ani přílohy.
9. **Nemáš-li Python nebo příkazový řádek**, použij Plán B (na konci).
10. **Datum** zjisti ze systému, nehádej.
11. **Během opravy se řiď jen tímto souborem**, ne staršími skilly (`guard`, `onboarding`…). Ty mluví o starých cestách; po opravě platí nové z tohoto souboru.

### Krok 0 — Zjisti, kde jsi, a řekni uživateli, co se bude dít

1. Najdi složku `Claude/` (kořen se souborem `CLAUDE.md` nebo `START-HERE.md`). Nevidíš-li ji, požádej o její nasdílení (`request_cowork_directory`) a počkej. Nic neukládej jinam.
2. Zjisti stav: existuje `SYSTEM/registry/`? Pak už je složka přestavěná: řekni to a nic nedělej (nabídni jen kontrolu). Existuje `Registry/` a `wiki/` a `profile.md`? Je to stará verze: pokračuj. Jiná směs: popiš, co vidíš, a zeptej se.
3. Řekni jednoduše, co se stane (viz „PRO TEBE“ výše, 4 věty) a zeptej se: **„Můžu začít zálohou?“** Až po „ano“ pokračuj.

### Krok 1 — Záloha (bez ní nic nedělej)

1. Rozbal přílohu do pracovní složky (bootstrap v Příloze). Vytvoří se `Claude/OPRAVA/nove/…`.
2. Zazálohuj: `python3 Claude/OPRAVA/nove/oprava.py backup Claude`. Skript ověří zip a napíše, kolik souborů zazálohoval.
3. Řekni uživateli: kde záloha leží, že ji lze kdykoli rozbalit, a že složku `OPRAVA/` může po dokončení nechat (je to jeho pojistka).

### Krok 2 — Zmapuj složku

Spusť `python3 Claude/OPRAVA/nove/oprava.py scan Claude`. Přečti výsledek sám a **uživateli řekni jen shrnutí** (3 až 6 vět): co je ve starém formátu, kolik má projektů, kolik souborů leží mimo strukturu, jestli jsou duplicity a prázdné složky. Seznamy nevypisuj, jen když se zeptá.

### Krok 3 — Rozhovor: zvol strukturu (podle průvodce)

Přečti `Claude/OPRAVA/nove/pruvodce/structure-guide.md` a `skeletons.md` (sekce 2 až 4 a 6 až 7 průvodce). **Postupuj stejně, jako by šlo o první spuštění, ale s tím, co už uživatel má:**
1. Empaticky se zeptej na jeho běžný týden a co mu zabírá hlavu. Zopakuj, co jsi slyšel.
2. **Navrhni hotovou kostru oblastí** (pracující, student, podnikatel/víc firem, jiné) a nech ho škrtat a upravovat. **5 až 8 oblastí, skupiny `work`, `school`, `personal`.** Každá firma vlastní oblast.
3. **Použij to, co už má:** projděte projekty ze skenu a u každého zvol oblast (navrhni, on potvrdí). Ptej se po jednom.
4. **Zvol variantu projektů** (vysvětli obě, doporuč A „jedna vrstva“, respektuj jeho volbu): A = `PROJECTS/<projekt>/`, B = `AREAS/<skupina>/<oblast>/<projekt>/`.
5. Existující projekty **nepřejmenovávej**, dokud to sám nechce (předpona `oblast-tema` platí pro nové).
6. Shrň výsledek (tabulka oblastí + varianta) a získej souhlas.

### Krok 4 — Sestav plán

Vytvoř `Claude/OPRAVA/plan.json`: seznam operací `{"batch": N, "op": "mkdir|move|install", "from": "…", "to": "…", "why": "…"}` (viz `python3 oprava.py --help`). Dávky:
1. **Systém a nové soubory:** `mkdir SYSTEM`; `move Registry → SYSTEM/registry`; `move skill-memory → SYSTEM/skill-memory`; `move wiki → RESOURCES`; `move profile.md → PROFILE.md`; potom `install` nových souborů z `OPRAVA/nove/` (`CLAUDE.md`, `START-HERE.md`, `SYSTEM/registry/folder-map.md`, `workspace-rules.md`, `project-method.md`). Starý soubor se při `install` uloží do `OPRAVA/stare-verze/`. **Soubory `projects-registry.md`, `decisions-registry.md`, `session-brain.md`, `skills-catalog.md` a uživatelovy PROFILE nepřepisuj** (jen se přesunou s Registry).
2. **Kostra:** `move inbox → INBOX`, `move projects → PROJECTS` (přejmenování jen velikosti písmen skript zvládne), `mkdir ARCHIVE/projects`, `mkdir ARCHIVE/areas`, `mkdir` složek oblastí `AREAS/<skupina>/<oblast>` (jen ty, které uživatel zvolil).
3. **Projekty (jen varianta B):** `move PROJECTS/<projekt> → AREAS/<skupina>/<oblast>/<projekt>`. U varianty A žádné přesuny.
4. **Soubory mimo strukturu:** pro **každý** soubor mimo strukturu navrhni cíl (oblast, `INBOX/`, `RESOURCES/`) a název podle pravidla `oblast__typ__tema__RRRR-MM-DD.md` (malá písmena, bez diakritiky a mezer; nejasné téma se zeptej). Duplicity nevybírej sám, přesuň obě do `INBOX/` a nech rozhodnout uživatele. **Prázdné a staré složky ponech** a na konci je jen vypiš.

Každou dávku **ukaž jako tabulku** a zeptej se „Provedu tuhle dávku?“.

### Krok 5 — Provedení po dávkách

Pro každou schválenou dávku: `python3 Claude/OPRAVA/nove/oprava.py apply Claude Claude/OPRAVA/plan.json --batch N --dry-run` (ukaž výsledek, včetně počtu oprav odkazů), po souhlasu stejný příkaz bez `--dry-run`. Skript vede deník v `OPRAVA/denik.jsonl` a opravuje odkazy mezi soubory. Po každé dávce řekni jednou větou, co se udělalo.

### Krok 6 — Doplň obsah (po přesunech, se souhlasem)

1. **`SYSTEM/registry/projects-registry.md`:** přidej sloupec **Oblast** (záhlaví `| Projekt | Druh | Oblast | Stav | Poslední práce | Složka | Poznámka |`) a doplň oblast u každého řádku. Sloupec **Složka** musí ukazovat na skutečné místo (varianta B jinou cestu).
2. **U každého projektu `state.json`:** přidej pole `"area": "<oblast>"` a `"due": "<RRRR-MM-DD nebo prázdný řetězec>"` (termín se zeptej, prázdný je v pořádku). Ostatní pole neměň.
3. **`SYSTEM/registry/decisions-registry.md`:** sloupec Soubor musí ukazovat na existující soubory (u varianty B cesty po přesunu); přesun je opravil skript, ověř.
4. **`SYSTEM/registry/folder-map.md`:** do tabulky **Moje oblasti** vyplň skupinu, oblast a „co sem patří“; řádek `**Projekty:**` nastav na `jedna vrstva` nebo `pod oblastí`; řádek `**Struktura potvrzena:**` nastav na dnešní datum.
5. **`SYSTEM/registry/session-brain.md`:** přidej krátký záznam „Složka přestavěna podle OPRAVA 0.3.0 dne …, záloha `OPRAVA/zaloha__….zip`“.
6. **Starší nainstalované skilly** (jsou-li) mluví o starých cestách; `CLAUDE.md` už nese tabulku překladu. Řekni uživateli jednou větou, že se skilly časem aktualizují.

### Krok 7 — Zapiš do mapy složek a do FileGuardu (`guard`)

„FileGuard“ (hlídání, kam se co ukládá a jak se to jmenuje) tvoří **`CLAUDE.md`**, **mapa složek** (`SYSTEM/registry/folder-map.md`), **pravidla** (`workspace-rules.md`) a skill **`guard`**. První tři jsi už zapsal; teď je dopiš a postaráš se o čtvrtý.

1. **Zastaralé cesty v mapě složek.** V `SYSTEM/registry/folder-map.md` vyplň tabulku **Zastaralé cesty** (starý řádek `_(žádné …)_` nahraď): `Registry/` → `SYSTEM/registry/`, `wiki/` → `RESOURCES/`, `profile.md` → `PROFILE.md`, `inbox/` → `INBOX/`, `projects/` → `PROJECTS/` (nebo `AREAS/<skupina>/<oblast>/` podle varianty), `skill-memory/` → `SYSTEM/skill-memory/`; sloupec „Od kdy“ dnešní datum, poznámka „přesunuto opravou 0.3.0“. Díky tomu `guard` staré cesty pozná a navrhne nové.
2. **Zjisti, zda je nainstalovaný skill `guard`:** podívej se do seznamu skillů, které máš k dispozici (název `guard`). **Není?** Řekni, že hlídání zajišťují `CLAUDE.md` a mapa složek (pravidla jsou v nich), a přeskoč zbytek kroku.
3. **Je?** Je ve staré verzi a hledá mapu složek na **starém místě** (`Registry/…`), které už není. Vysvětli to jednoduše („hlídač u tebe ještě hledá mapu na původním místě, aktualizuju ho, bude to jedno kliknutí“) a zeptej se „Můžu?“.
4. Zabal aktualizovaný skill: `python3 Claude/OPRAVA/nove/oprava.py packskill Claude/OPRAVA/nove/skills/guard Claude/OPRAVA/guard.skill`.
5. **Nabídni soubor uživateli jako kartu v chatu** (nástrojem pro předání souboru, ne jen cestu). Řekni: „Pod touhle zprávou je karta se souborem `guard.skill`. Klikni na **Uložit skill** (nebo podobné tlačítko). Zeptá-li se, jestli nahradit starý skill, potvrď.“ **Nevidí-li kartu nebo tlačítko:** řekni, kde soubor leží (`OPRAVA/guard.skill`), že se skill v aplikaci přidává v nastavení skillů (přesné tlačítko se liší podle verze aplikace), a nech si od uživatele napsat, co na obrazovce vidí; radíš krok za krokem. Bez přeinstalace se dá dál pracovat podle `CLAUDE.md`, nic se nerozbije.
6. **Ověř v nové konverzaci** (nový skill se načte až v ní). Řekni: „Otevři novou konverzaci se složkou Claude a napiš: **Kam patří soubor o rekonstrukci kuchyně?** Když hlídač odpoví cestou v nové struktuře (`PROJECTS/…` nebo `AREAS/…`), je vše v pořádku.“ Potvrdí-li to uživatel, v `SYSTEM/registry/skills-catalog.md` uprav řádek `guard` (verze `0.3.0`, poslední změna dnešní datum). Nepotvrdí-li, zapiš do `SYSTEM/registry/session-brain.md`: „guard čeká na přeinstalaci“.
7. **Další soubory `*.skill` od toho, kdo ti kit předal:** leží-li v `Claude/OPRAVA/` (nebo v `Claude/`) další soubory s příponou `.skill`, nabídni je uživateli **po jednom jako karty** stejným způsobem jako `guard` (jeden po druhém, po každém ověření). Nejsou-li, nic nehledej.
8. **Ostatní nainstalované skilly** (`onboarding`, `architect`, `planner`, `inbox`, `session-close`, `safety`, `coach`, `skill-builder`) zůstanou ve staré verzi a fungují díky tabulce překladu v `CLAUDE.md`. Jejich aktualizaci pošle ten, kdo kit předává. Zapiš to do `session-brain.md`; sám je nepřeinstalovávej (nemáš je v tomto souboru).
9. **Vznikne-li později znovu stará složka** (třeba `Registry/` nebo `inbox/`, protože starší skill zapsal na původní místo): neber to jako chybu uživatele. Řekni to, přesuň nový obsah do správné složky (`SYSTEM/registry/`, `INBOX/`) po souhlasu a připomeň, že starší skilly se ještě aktualizují.

### Krok 8 — Kontrola a předání

1. `python3 Claude/OPRAVA/nove/oprava.py check Claude`. Vyřeš `FLAG`, u `WARN` vysvětli.
2. Řekni uživateli **jednoduše, co se změnilo** (kolik souborů se přesunulo, jaké oblasti vznikly, kam patří projekty, zda se aktualizoval `guard`), **kde je záloha**, jak se vrátí (**„Vrať opravu zpátky“** → `oprava.py undo Claude --all`) a **které prázdné složky zůstaly** (smazat je může sám, ty nemaž).
3. **Nabídni zprávu pro toho, kdo ti soubor poslal.** Vytvoř `Claude/OPRAVA/zprava.md`: datum; zda proběhla záloha; kolik souborů se přesunulo a kolik oprav odkazů; zvolená varianta (`jedna vrstva` / `pod oblastí`) a **názvy** oblastí (ne obsah souborů); zda se aktualizoval `guard`; co se zaseklo nebo bylo nejasné; výsledek `check`. **Žádný obsah osobních souborů a žádná jména dokumentů.** Ukaž ji uživateli a zeptej se, zda ji chce poslat; posílá ji sám.
4. Řekni, jak příště navázat: **„Kde jsem skončil?“**, a že od teď platí nová pravidla z `CLAUDE.md`.

### Návrat zpět

Když uživatel řekne „Vrať opravu zpátky“: `python3 Claude/OPRAVA/nove/oprava.py undo Claude --all` (nebo `--batch N`). Skript vrátí přesuny a nahradí nové systémové soubory jejich původními verzemi. Potom spusť `check`. Záloha `OPRAVA/zaloha__….zip` je poslední záchrana (rozbalit ručně).

### Plán B (bez Pythonu nebo bez příkazového řádku)

Přílohu nemusíš rozbalovat skriptem: soubory z ní zapiš sám přesně tak, jak stojí, do `Claude/OPRAVA/nove/…`. Zálohu udělej tak, že uživatele požádáš, aby si složku zkopíroval ve Finderu, a počkáš na potvrzení. Přesuny dělej **jeden po druhém** příkazem přesunu souboru (`mv`), nebo nástrojem pro přesun souborů, vždy po souhlasu, a každý zapiš do `Claude/OPRAVA/denik.txt` (odkud → kam), ať jde vrátit. Odkazy opravuj ručně jen u souborů, které tvoří systém (`SYSTEM/registry/…`, `START-HERE.md`, `CLAUDE.md`). Skill `guard` v tom případě zabal příkazem `zip` tak, aby `SKILL.md` ležel na kořeni archivu (ne v podsložce). Řekni uživateli, že je to pomalejší.

---

## PŘÍLOHA (technická; nečti ji celou, jen ji rozbal)

Bootstrap (spusť jednou, vytáhne všechny soubory z přílohy do `Claude/OPRAVA/nove/`; změň cestu k tomuto souboru a ke složce `Claude`):

```bash
python3 - "CESTA/K/TOMUTO/SOUBORU.md" "CESTA/KE/SLOZCE/Claude" <<'EOF'
import re, sys, os
md, ws = sys.argv[1], sys.argv[2]
t = open(md, encoding="utf-8").read()
n = 0
for m in re.finditer(r"<!-- BEGIN FILE: ([^\n]+?) -->\n(`{3,})[a-z]*\n(.*?)\n\2\n<!-- END FILE -->", t, re.S):
    p = os.path.join(ws, "OPRAVA", "nove", m.group(1))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(m.group(3) + "\n")
    n += 1
print("rozbaleno souborů:", n)
EOF
```

Obsah přílohy (každý soubor je mezi značkami `BEGIN FILE` a `END FILE`):

- `oprava.py`
- `CLAUDE.md`
- `START-HERE.md`
- `SYSTEM/registry/folder-map.md`
- `SYSTEM/registry/workspace-rules.md`
- `SYSTEM/registry/project-method.md`
- `pruvodce/structure-guide.md`
- `pruvodce/skeletons.md`
- `skills/guard/SKILL.md`
- `skills/guard/scripts/name-check.py`

### oprava.py

<!-- BEGIN FILE: oprava.py -->
```python
#!/usr/bin/env python3
"""oprava.py — pomocný skript opravného souboru (přestavba stávající složky Claude/).

Použití (z libovolného místa; <ws> = složka Claude/):
  python3 oprava.py backup <ws>                       zazálohuje celou složku do <ws>/OPRAVA/zaloha__RRRR-MM-DD.zip
  python3 oprava.py scan   <ws>                       zmapuje složku (nic nemění), vypíše hlášení
  python3 oprava.py apply  <ws> <plan.json> --batch N [--dry-run]
                                                      provede jednu dávku plánu (suchý běh nic nemění)
  python3 oprava.py undo   <ws> [--batch N | --all]   vrátí provedené dávky podle deníku
  python3 oprava.py check  <ws>                       jednoduchá kontrola výsledku (nic nemění)
  python3 oprava.py packskill <složka-skillu> <výstup.skill>
                                                      zabalí skill do souboru .skill (SKILL.md na kořeni, jen povolené složky)

Plán (plan.json) je seznam operací: {"batch": 1, "op": "mkdir|move|install", "from": "...", "to": "...", "why": "..."}
  mkdir    založí složku "to"
  move     přesune (nebo přejmenuje) "from" na "to"; přejmenování jen velikosti písmen se udělá dvoukrokově
  install  zkopíruje nový soubor "from" (v OPRAVA/nove/) na "to"; starý soubor uloží do OPRAVA/stare-verze/
Cesty jsou relativní ke složce <ws>. Nic se nemaže: skript nikdy nepřepíše existující cíl (kromě "install"
se zálohou starého souboru) a při konfliktu se zastaví. Každá operace jde do deníku OPRAVA/denik.jsonl.
Po přesunu se opraví odkazy: staré cesty v textových souborech (.md, .json, .txt) se nahradí novými
(kromě složky OPRAVA). Výstup nikdy neobsahuje obsah souborů, jen cesty a počty.
"""
import json
import os
import re
import shutil
import sys
import time
import unicodedata
import zipfile
from pathlib import Path

WORK = "OPRAVA"
TEXT_EXT = {".md", ".json", ".txt"}
SKIP_TOP = {WORK}
NAME_OK = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*__[a-z0-9]+(?:-[a-z0-9]+)*__[a-z0-9]+(?:-[a-z0-9]+)*(?:__\d{4}-\d{2}-\d{2})?\.[a-z0-9]+$")
FIXED = {"CLAUDE.md", "START-HERE.md", "PROFILE.md", "profile.md", "README.md", "SKILL.md", "index.md", "log.md", "brief.md",
         "plan.md", "map.md", "state.json", "dashboard.html", "lessons.md", "voice.md"}
LEGACY_TOP = {"Registry", "wiki", "profile.md", "projects", "inbox", "areas", "resources", "archive", "skill-memory", "skills"}
NEW_TOP = {"INBOX", "PROJECTS", "AREAS", "RESOURCES", "ARCHIVE", "SYSTEM"}


def die(msg):
    print(f"CHYBA: {msg}", file=sys.stderr)
    sys.exit(1)


def ws_of(arg):
    p = Path(arg).expanduser().resolve()
    if not p.is_dir():
        die(f"složka {p} neexistuje")
    return p


def has(ws, name):
    """Existuje položka přesně s tímto psaním? (na macOS se jinak splete PROJECTS a projects)"""
    return name in os.listdir(ws)


def rel_iter(ws, include_work=False):
    for root, dirs, files in os.walk(ws):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and (include_work or Path(root, d) != ws / WORK))
        for f in sorted(files):
            if not f.startswith("."):
                yield Path(root, f).relative_to(ws)


def cmd_backup(ws):
    work = ws / WORK
    work.mkdir(exist_ok=True)
    dest = work / f"zaloha__{time.strftime('%Y-%m-%d')}.zip"
    if dest.exists():
        dest = work / f"zaloha__{time.strftime('%Y-%m-%d__%H%M%S')}.zip"
    n = 0
    tmp = work / (dest.name + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in rel_iter(ws):
            z.write(ws / rel, rel.as_posix())
            n += 1
    with zipfile.ZipFile(tmp) as z:
        bad = z.testzip()
        if bad or len(z.namelist()) != n:
            tmp.unlink()
            die(f"záloha se nepovedla (chyba u {bad}); nic jsem neměnil")
    tmp.replace(dest)
    print(f"OK  záloha hotová: {dest.relative_to(ws)} ({n} souborů, {dest.stat().st_size // 1024} KB). Kdykoli ji lze rozbalit zpět.")


def name_problem(name):
    if name in FIXED or NAME_OK.match(name) or re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.[a-z0-9]+$", name):
        return None
    if unicodedata.normalize("NFKD", name) != name or name != name.lower() or " " in name:
        return "velká písmena, diakritika nebo mezery"
    return "chybí tvar oblast__typ__tema[__datum]"


def cmd_scan(ws):
    top = sorted(p.name for p in ws.iterdir() if not p.name.startswith(".") and p.name != WORK)
    legacy = [t for t in top if t in LEGACY_TOP and t not in NEW_TOP]
    new = [t for t in top if t in NEW_TOP]
    print("== STAV STRUKTURY ==")
    print("nový formát (kostra velkými):", ", ".join(new) or "žádný")
    print("starý formát (názvy k převodu):", ", ".join(legacy) or "žádný")
    system_files = {"CLAUDE.md", "START-HERE.md", "PROFILE.md", "profile.md"}
    print("\n== KOŘEN ==")
    for t in top:
        p = ws / t
        if p.is_dir():
            cnt = sum(1 for _ in rel_iter(p))
            print(f"  složka {t}/ ({cnt} souborů)")
        else:
            tag = "systémový soubor" if t in system_files else "soubor mimo strukturu"
            print(f"  {tag}: {t}")
    # projekty (kandidáti)
    cands = []
    for n in ("projects", "PROJECTS"):
        if has(ws, n):
            cands += [d for d in sorted((ws / n).iterdir()) if d.is_dir()]
    if has(ws, "AREAS"):
        cands += [d for d in sorted((ws / "AREAS").glob("*/*/*")) if d.is_dir()]
    print("\n== PROJEKTY (složky se state.json nebo brief.md) ==")
    found = 0
    for d in cands:
        if (d / "state.json").is_file() or (d / "brief.md").is_file():
            info = ""
            try:
                sj = json.loads((d / "state.json").read_text(encoding="utf-8"))
                info = f" area={sj.get('area', '(chybí)')!r} due={sj.get('due', '(chybí)')!r} status={sj.get('status')!r}"
            except Exception:
                info = " state.json (nečitelný nebo chybí)"
            print(f"  {d.relative_to(ws).as_posix()}/{info}")
            found += 1
    if not found:
        print("  žádné")
    # registr
    for reg in (ws / "Registry" / "projects-registry.md", ws / "SYSTEM" / "registry" / "projects-registry.md"):
        if reg.is_file():
            head = next((l for l in reg.read_text(encoding="utf-8").splitlines() if l.startswith("| Projekt")), "")
            print(f"\n== REGISTR PROJEKTŮ: {reg.relative_to(ws).as_posix()} ==\n  záhlaví: {head or '(nenalezeno)'}")
            print("  sloupec Oblast: " + ("ANO" if "Oblast" in head else "CHYBÍ (starý formát)"))
    # názvy, duplicity, prázdné
    bad, seen, dup = [], {}, []
    for rel in rel_iter(ws):
        if rel.parts[0] in ("Registry", "SYSTEM", "wiki", "RESOURCES", "skill-memory") or rel.name in FIXED and len(rel.parts) <= 3:
            continue
        pr = name_problem(rel.name)
        if pr:
            bad.append((rel.as_posix(), pr))
        key = (rel.name.lower(), (ws / rel).stat().st_size)
        if key in seen:
            dup.append((seen[key], rel.as_posix()))
        else:
            seen[key] = rel.as_posix()
    print(f"\n== NÁZVY PORUŠUJÍCÍ PRAVIDLA ({len(bad)}) ==")
    for f, why in bad[:40]:
        print(f"  {f}  ({why})")
    if len(bad) > 40:
        print(f"  … a dalších {len(bad) - 40}")
    print(f"\n== MOŽNÉ DUPLICITY ({len(dup)}) ==")
    for a, b in dup[:20]:
        print(f"  {a}  =  {b}")
    empty = [d.relative_to(ws).as_posix() for d in sorted(ws.rglob("*")) if d.is_dir() and not any(d.iterdir()) and WORK not in d.parts]
    print(f"\n== PRÁZDNÉ SLOŽKY ({len(empty)}) ==")
    for d in empty[:30]:
        print(f"  {d}/")
    print("\nNic se neměnilo.")


def log_path(ws):
    return ws / WORK / "denik.jsonl"


def read_log(ws):
    p = log_path(ws)
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.is_file() else []


def append_log(ws, rec):
    (ws / WORK).mkdir(exist_ok=True)
    with open(log_path(ws), "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def same_path(a, b):
    try:
        return a.exists() and b.exists() and os.path.samefile(a, b)
    except OSError:
        return False


def repair_refs(ws, old, new, dry, is_dir):
    """Nahradí starou cestu novou v textových souborech. Vrací seznam (soubor, počet).
    Složka se nahrazuje jen ve tvaru "stará/…" (ne v "stara-neco.md"), soubor jen jako celý název."""
    out = []
    o = old.rstrip("/")
    n = new.rstrip("/")
    if not o or o == n:
        return out
    if is_dir:
        pat = re.compile(r"(?<![\w/.-])" + re.escape(o) + r"/")
        n = n + "/"
    else:
        pat = re.compile(r"(?<![\w/.-])" + re.escape(o) + r"(?![\w-])")
    for rel in rel_iter(ws):
        if rel.suffix.lower() not in TEXT_EXT:
            continue
        p = ws / rel
        try:
            t = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        t2, c = pat.subn(n, t)
        if c:
            out.append((rel.as_posix(), c))
            if not dry:
                p.write_text(t2, encoding="utf-8")
    return out


def do_move(ws, src, dst, dry):
    s, d = ws / src, ws / dst
    if not s.exists():
        die(f"zdroj {src} neexistuje")
    case_only = src.lower() == dst.lower() and src != dst
    if not case_only and (d.exists() and not same_path(s, d)):
        die(f"cíl {dst} už existuje; nic jsem nepřepsal")
    if dry:
        return
    d.parent.mkdir(parents=True, exist_ok=True)
    if case_only or same_path(s, d):
        tmp = s.with_name(s.name + ".__prejmenovani__")
        os.rename(s, tmp)
        os.rename(tmp, d)
    else:
        os.rename(s, d)


def cmd_apply(ws, plan_path, batch, dry):
    plan = json.loads(Path(plan_path).read_text(encoding="utf-8"))
    ops = [o for o in plan if o.get("batch") == batch]
    if not ops:
        die(f"v plánu není dávka {batch}")
    if not (ws / WORK).is_dir() or not list((ws / WORK).glob("zaloha__*.zip")):
        die("nejdřív zálohu: python3 oprava.py backup <složka>")
    print(("SUCHÝ BĚH (nic se nemění)" if dry else "PROVEDENÍ") + f" dávky {batch}: {len(ops)} operací")
    for o in ops:
        kind, src, dst = o["op"], o.get("from", ""), o["to"]
        if kind == "mkdir":
            if not dry:
                chain, cur = [], Path(dst)
                while str(cur) not in ("", ".") and not (ws / cur).exists():
                    chain.append(cur.as_posix())
                    cur = cur.parent
                (ws / dst).mkdir(parents=True, exist_ok=True)
                append_log(ws, {"batch": batch, "op": "mkdir", "to": dst, "created": chain})
            print(f"  mkdir   {dst}/")
        elif kind == "move":
            is_dir = (ws / src).is_dir()
            do_move(ws, src, dst, dry)
            refs = repair_refs(ws, src, dst, True, is_dir) if dry else None
            if not dry:
                refs = repair_refs(ws, src, dst, False, is_dir)
                append_log(ws, {"batch": batch, "op": "move", "from": src, "to": dst, "is_dir": is_dir, "refs": refs})
            n = sum(c for _, c in (refs or []))
            print(f"  move    {src}  ->  {dst}" + (f"   (odkazů k opravě: {n} v {len(refs)} souborech)" if refs else ""))
        elif kind == "install":
            new = ws / src
            if not new.is_file():
                die(f"nový soubor {src} chybí")
            tgt = ws / dst
            old_copy = None
            if not dry:
                tgt.parent.mkdir(parents=True, exist_ok=True)
                if tgt.exists():
                    old_copy = f"{WORK}/stare-verze/{dst}"
                    (ws / old_copy).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(tgt, ws / old_copy)
                shutil.copy2(new, tgt)
                append_log(ws, {"batch": batch, "op": "install", "to": dst, "old_copy": old_copy})
            print(f"  install {dst}" + ("   (starý soubor uložen do OPRAVA/stare-verze/)" if (ws / dst).exists() and not dry else ""))
        else:
            die(f"neznámá operace {kind!r}")
    print("Hotovo." if not dry else "Suchý běh dokončen.")


def cmd_undo(ws, batch, all_):
    recs = read_log(ws)
    if not recs:
        die("deník je prázdný, není co vracet")
    sel = [r for r in recs if all_ or r["batch"] == batch]
    if not sel:
        die("v deníku nic takového není")
    for r in reversed(sel):
        if r["op"] == "move":
            do_move(ws, r["to"], r["from"], dry=False)
            repair_refs(ws, r["to"], r["from"], False, r.get("is_dir", False))
            print(f"  zpět    {r['to']}  ->  {r['from']}")
        elif r["op"] == "install":
            if r.get("old_copy") and (ws / r["old_copy"]).is_file():
                shutil.copy2(ws / r["old_copy"], ws / r["to"])
                print(f"  obnoven {r['to']} ze starší verze")
            else:
                print(f"  {r['to']}: nový soubor ponechán (starší verze nebyla)")
        elif r["op"] == "mkdir":
            for made in (r.get("created") or [r["to"]]):  # od nejhlubší po nejvyšší
                d = ws / made
                if d.is_dir() and not any(d.iterdir()):
                    d.rmdir()
                    print(f"  prázdná složka {made}/ odstraněna (vytvořila ji oprava)")
    keep = [r for r in recs if r not in sel]
    log_path(ws).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep), encoding="utf-8")
    print("Vráceno.")


def cmd_check(ws):
    problems = 0

    def rep(level, msg):
        nonlocal problems
        print(f"{level:<5} {msg}")
        if level == "FLAG":
            problems += 1
    for need in ("INBOX", "PROJECTS", "AREAS", "RESOURCES", "ARCHIVE", "SYSTEM"):
        rep("OK" if has(ws, need) else "WARN", f"složka {need}/ {'existuje' if has(ws, need) else 'chybí (nebo je napsaná jinou velikostí písmen)'}")
    fm = ws / "SYSTEM" / "registry" / "folder-map.md"
    if fm.is_file():
        t = fm.read_text(encoding="utf-8")
        m = re.search(r"\*\*Struktura potvrzena:\*\*\s*(.*)", t)
        rep("OK" if m and not m.group(1).strip().startswith("zatím ne") else "WARN", "Struktura potvrzena: " + (m.group(1).strip()[:20] if m else "řádek chybí"))
        m = re.search(r"\*\*Projekty:\*\*\s*(jedna vrstva|pod oblastí)", t)
        rep("OK" if m else "WARN", "Projekty: " + (m.group(1) if m else "nezvoleno"))
    else:
        rep("FLAG", "SYSTEM/registry/folder-map.md chybí")
    reg = ws / "SYSTEM" / "registry" / "projects-registry.md"
    if reg.is_file():
        rows = [l for l in reg.read_text(encoding="utf-8").splitlines() if l.startswith("|") and not l.startswith("|--") and not l.startswith("| Projekt")]
        for l in rows:
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 6 and cells[5] and not cells[5].startswith("_"):
                folder = cells[5]
                if not (ws / folder).is_dir():
                    rep("FLAG", f"projekt {cells[0]}: složka {folder} neexistuje")
                elif not (ws / folder / "state.json").is_file():
                    rep("WARN", f"projekt {cells[0]}: chybí state.json")
                else:
                    try:
                        sj = json.loads((ws / folder / "state.json").read_text(encoding="utf-8"))
                        if not sj.get("area"):
                            rep("WARN", f"projekt {cells[0]}: state.json nemá vyplněnou oblast (area)")
                        elif sj["area"] != cells[2]:
                            rep("FLAG", f"projekt {cells[0]}: area {sj['area']!r} ve state.json ≠ {cells[2]!r} v registru")
                    except Exception:
                        rep("FLAG", f"projekt {cells[0]}: state.json nejde přečíst")
    else:
        rep("WARN", "SYSTEM/registry/projects-registry.md chybí")
    old = [n for n in ("Registry", "wiki", "profile.md", "projects", "inbox") if has(ws, n)]
    rep("WARN" if old else "OK", "zbytky starého formátu: " + (", ".join(old) if old else "žádné"))
    print(f"\nShrnutí: {problems} FLAG.")
    sys.exit(1 if problems else 0)


def cmd_packskill(src, out):
    src, out = Path(src).expanduser().resolve(), Path(out).expanduser().resolve()
    if not (src / "SKILL.md").is_file():
        die(f"{src} nemá SKILL.md")
    tmp = out.with_name(out.name + ".tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(src / "SKILL.md", "SKILL.md")
        for top in ("references", "assets", "scripts", "templates", "memory-template"):
            base = src / top
            if base.is_dir():
                for f in sorted(base.rglob("*")):
                    if f.is_file() and not f.name.startswith(".") and "__pycache__" not in f.parts:
                        z.write(f, f.relative_to(src).as_posix())
    with zipfile.ZipFile(tmp) as z:
        names = z.namelist()
        if names.count("SKILL.md") != 1 or z.testzip():
            tmp.unlink()
            die("balíček skillu není v pořádku (SKILL.md musí být právě jednou na kořeni)")
    tmp.replace(out)
    print(f"OK  skill zabalen: {out.name} ({len(names)} souborů, {out.stat().st_size // 1024} KB)")


def main(argv):
    if len(argv) < 3 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    if argv[1] == "packskill":
        if len(argv) < 4:
            die("použití: packskill <složka-skillu> <výstup.skill>")
        cmd_packskill(argv[2], argv[3])
        return 0
    cmd, ws = argv[1], ws_of(argv[2])
    if cmd == "backup":
        cmd_backup(ws)
    elif cmd == "scan":
        cmd_scan(ws)
    elif cmd == "apply":
        if len(argv) < 5 or "--batch" not in argv:
            die("použití: apply <ws> <plan.json> --batch N [--dry-run]")
        cmd_apply(ws, argv[3], int(argv[argv.index("--batch") + 1]), "--dry-run" in argv)
    elif cmd == "undo":
        cmd_undo(ws, int(argv[argv.index("--batch") + 1]) if "--batch" in argv else None, "--all" in argv)
    elif cmd == "check":
        cmd_check(ws)
    else:
        die(f"neznámý příkaz {cmd}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```
<!-- END FILE -->

### CLAUDE.md

<!-- BEGIN FILE: CLAUDE.md -->
```markdown
> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-23

# Pravidla této složky

Tuhle složku (`Claude/`) mi nasdílel(a) uživatel jako pracovní prostor. Pracuji **jen v ní**. Tento soubor se čte na začátku každé práce. Mění se jen po dohodě s uživatelem.

## Začátek práce

1. Pokud existuje `SYSTEM/registry/session-brain.md`, přečti ho: je to krátké předání z minula.
2. Pokud existuje `PROFILE.md`, přečti ho: kdo uživatel je a na čem pracuje.
3. Otevři `SYSTEM/registry/folder-map.md` a podívej se jen na sekci **Moje oblasti**. Je-li tam **„Struktura potvrzena: zatím ne“**, onboarding ještě neproběhl. **Než založíš cokoli** (projekt, složku, soubor s vlastním názvem), nabídni skill `onboarding`: nejdřív se spolu projde struktura složek, mapa a pojmenování. Rychlý zápis do `INBOX/` a čtení smí být i dřív.
4. Nic dalšího nečti předem. Ptá-li se uživatel na projekt, najdi jeho složku podle sloupce Složka v `SYSTEM/registry/projects-registry.md` (`PROJECTS/<projekt>/` nebo pod oblastí, podle řádku `Projekty` v mapě složek) a přečti `state.json` a `log.md`.

## Kam co patří a jak se to jmenuje

- **Kam:** úplná mapa je v `SYSTEM/registry/folder-map.md` (řiď se pořadím otázek v sekci „Kam co patří“: projekt, oblast, znalost, archiv, inbox). Nevymýšlej složky z hlavy.
- **Jak pojmenovat:** `oblast__typ__tema__RRRR-MM-DD.md` (malá písmena, bez diakritiky, bez mezer, datum na konci). Reference a průběžné soubory (na které se odkazuje nebo do kterých se přidává) jsou **bez data** v názvu. Celá pravidla: `SYSTEM/registry/workspace-rules.md`.
- **Před každým zápisem, přesunem nebo mazáním** spusť skill `guard`, pokud je nainstalovaný. Pokud ne, řiď se pravidly níže sám.

## Ptej se vždy, než něco uděláš

1. **smažeš** soubor nebo složku,
2. založíš **novou složku**, která není v `SYSTEM/registry/folder-map.md`,
3. zapíšeš **mimo místa v mapě**,
4. přepíšeš soubor, který vytvořil **jiný skill**,
5. změníš systémový soubor (`CLAUDE.md`, `SKILL.md`, `folder-map.md`, `workspace-rules.md`).

Zeptej se jednou větou: co, kam, proč. Bez "ano" nic z toho nedělej. Čtení a dočasné soubory (`/tmp/`, `/sessions/`) se neptají. Po každém zápisu řekni jednou větou, co a kam jsi zapsal.

## Když nemáš přístup k souboru

- Chyba `EPERM` neznamená, že soubor neexistuje, jen že k němu nemáš oprávnění. Zkus to přes bash s cestou `/sessions/.../mnt/`.
- Chyba "outside connected folders": požádej uživatele o přístup do té složky (`request_cowork_directory`).
- Teprve když nenajdeš soubor ani pak, řekni, že neexistuje.
- **Nikdy neukládej důležité věci do `/tmp/`.** Uživatel je neuvidí a zmizí. Nemáš-li přístup do `Claude/`, řekni to a počkej.

## Práce s projekty

- Cokoli, co má víc kroků a **cíl s koncem**, dostane složku projektu (`PROJECTS/<projekt>/`, nebo pod oblastí, podle volby v mapě složek). Každý projekt patří do **jedné oblasti** ze seznamu „Moje oblasti“ (pole `area`) a má „hotovo, když…“ nebo termín; bez konce je to spíš oblast. Hotový projekt se po souhlasu přesune do `ARCHIVE/projects/`.
- **Systém, věc se strukturou** (aplikace, workspace, sada skillů) → skill `architect` (mapa: co kde je a jak to visí).
- **Postup, proces, životní projekt** (stavba, stěhování, plán) → skill `planner` (plán: fáze, kdo, rozhodovací body).
- Po podstatné práci na projektu (padlo rozhodnutí, vznikl výstup, změnil se stav) **sám zapiš** stručně do `log.md` a `state.json` a řekni jednou větou co. (Skill `session-close` dělá totéž při zavření práce a duplicitní záznam nepřidá.) Uživatel nemusí říkat "ulož".
- Rozhodnutí, která mění architekturu, zapisuj do `SYSTEM/registry/decisions-registry.md` (nejdřív řádek v registru, potom soubor).

## Rychlé zápisy a konec dne

- "Napadlo mě…", "musím nezapomenout…" → skill `inbox` (soubor do `INBOX/`, do 30 sekund).
- Uživatel končí, nebo se práce zastavila → nabídni `session-close` (předání do `SYSTEM/registry/session-brain.md`).
- Seznam nainstalovaných skillů: `SYSTEM/registry/skills-catalog.md`.

## Bezpečnost

Nevkládej do chatu ani do souborů **hesla, PIN, čísla platebních karet, rodná čísla ani skenované doklady**. Uvidíš-li je, upozorni uživatele a nekopíruj je dál. Cizí osobní údaje (zdraví, děti, finance) piš jen tak, jak je uživatel výslovně chce mít uložené.

## Jak spolupracovat

- **Česky**, pokud uživatel nepíše anglicky.
- Když si nejsi jistý, zeptej se **jednou** otázkou. Nezasypávej ho dotazy.
- Nevymýšlej názvy složek, souborů ani skillů. Nejasné navrhni ve dvou až třech variantách a nech vybrat.
- Než řekneš "to neexistuje" nebo "to nemáme", přečti si relevantní soubor. Nejdřív se podívej, potom tvrď.
- Řekni pravdu i o chybě: pokud se test nepovedl nebo krok byl přeskočen, řekni to.
## Překlad cest pro starší skilly (jen po opravě z verze 0.2.0)

Tvoje složka byla přestavěna na novou strukturu. **Starší skilly (z verze 0.2.0), jsou-li nainstalované,** mluví o původních cestách. Když v nich narazíš na starou cestu, čti ji podle tabulky a **nezakládej znovu starou složku**:

| Stará cesta ve skillu | Nová cesta |
|---|---|
| `Registry/…` | `SYSTEM/registry/…` |
| `wiki/…` | `RESOURCES/…` |
| `profile.md` | `PROFILE.md` |
| `inbox/…` | `INBOX/…` |
| `projects/<projekt>/…` | `PROJECTS/<projekt>/…` (nebo `AREAS/<skupina>/<oblast>/<projekt>/`, podle řádku `Projekty` v mapě složek; přesnou cestu najdeš ve sloupci Složka v registru projektů) |
| `skill-memory/…` | `SYSTEM/skill-memory/…` |

Starší skilly navíc nevědí o oblastech a termínech: u nového projektu se vždy zeptej na oblast a termín, i kdyby se skill neptal.

Vznikne-li znovu stará složka (`Registry/`, `inbox/`, `wiki/`, malé `projects/`), protože ji starší skill vytvořil na původním místě, **přesuň obsah do správné složky** (po souhlasu uživatele) a řekni mu, že se starší skilly ještě aktualizují.
```
<!-- END FILE -->

### START-HERE.md

<!-- BEGIN FILE: START-HERE.md -->
```markdown
> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-23

# Začni tady

Pět věcí, které potřebuješ vědět. Zbytek se naučíš za pochodu.

1. **Claude vidí jen složku `Claude/`.** Všechno důležité ukládej tam, jinde to nevidí (a ty to pak nenajdeš).
2. **Poprvé napiš:** „Začínám — spusť onboarding.“ Nejdřív si spolu projdete, **jak je složka uspořádaná a jak se soubory jmenují** (to je nejdůležitější půlhodina, ať se ti nezačne hromadit bordel), potom vyplníte profil a založíte první projekt. Trvá to asi hodinu.
3. **Denně stačí tři věty:** „Napadlo mě…“ (zapíše nápad, aby nepropadl), „Chci založit projekt…“ (založí složku a plán), „Končím.“ (uloží, kde jsi skončil, ať navážeš zítra).
4. **Claude se zeptá, než něco smaže nebo založí novou složku.** Odpověz ano, nebo ne. To je pojistka, ne obtěžování.
5. **Nevkládej do chatu hesla, PIN, čísla karet ani rodná čísla.** Claude je nepotřebuje a neměly by se uložit.

## Když něco nefunguje

- Claude se chová, jako by neznal pravidla? Napiš mu: **„Přečti Claude/CLAUDE.md.“**
- Neví, co má dělat dál? Napiš: **„Kde jsem skončil?“** (přečte předání z minula).
- Nevíš, co Claude umí? Napiš: **„Jaké skilly mám?“** (ukáže seznam).
```
<!-- END FILE -->

### SYSTEM/registry/folder-map.md

<!-- BEGIN FILE: SYSTEM/registry/folder-map.md -->
````markdown
---
type: reference
version: 2026-09-24
visibility: PUBLIC
status: draft
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

> **Vrstvy skillů.** Skilly zmíněné níže jsou ve třech vrstvách: **Základ** (`onboarding`, `architect`, `planner`, `guard`, `inbox`, `session-close`, `safety`, `coach`, `skill-builder`), **Nadstavba** (`wiki`, `snapshot`, `catalog`, `triage`, `cleanup`) a **Pokročilé** (`ai-builder`, `architect-pro`). Nemáš-li skill z vyšší vrstvy nainstalovaný, jeho práci dělá Claude jednodušeji sám, nebo se přeskočí.

# Mapa složek

Kanonická mapa: kam patří jaký typ věcí. `guard` ji čte při každém zápisu. Pokud něco nemá řádek, `guard` se zeptá a řádek přidá. Pravidla pojmenování jsou v `workspace-rules.md`. Všechny cesty jsou od nasdílené složky `Claude/`.

Struktura vychází z metody **PARA** (Projects, Areas, Resources, Archive): hlavní složky se řídí tím, **co s věcí budeš dělat**, ne tím, o jakém je tématu. **Pravidlo psaní: VELKÁ PÍSMENA = kostra, na kterou nesahám. malá písmena = to, co tvořím já.**

## Moje oblasti

**Struktura potvrzena:** zatím ne _(doplní `onboarding`, až spolu projdete složky, oblasti a pojmenování)_

**Projekty:** zatím nezvoleno _(doplní `onboarding`: `jedna vrstva` = všechny projekty v `PROJECTS/` (doporučeno), nebo `pod oblastí` = projekt leží v `AREAS/<skupina>/<oblast>/<projekt>/`)_

_Řádky `Struktura potvrzena` a `Projekty` zapisuje `onboarding` na konci kroku Struktura, až člověk souhlasí._

_Poznámka pro skripty: řádky `Struktura potvrzena` a `Projekty` jsou vždy jen jeden. U `Struktura potvrzena` znamená hodnota začínající „zatím ne“ nepotvrzeno, jakákoli jiná neprázdná hodnota (datum) potvrzeno. U `Projekty` platí `jedna vrstva` nebo `pod oblastí`, cokoli jiného znamená nezvoleno._

**Oblast** je trvalá odpovědnost bez konce (firma, domácnost, zdraví, studium). Každá oblast je složka `AREAS/<skupina>/<oblast>/`. **Skupina** je jedna ze tří pevných složek: `work` (práce), `school` (škola), `personal` (osobní). Oblast je zároveň první část názvu souboru (`oblast__typ__tema__datum`), proto musí být její název **jedinečný napříč skupinami**. **Každá firma je vlastní oblast** ve skupině `work` (`firma-a`, `firma-b`).

Doporučený počet je **5 až 8 oblastí celkem**. **Nová oblast se přidává jen po dohodě**, ať se nehromadí `dum`, `domov` a `bydleni` vedle sebe. Oblasti se nesmějí překrývat; zkouška: *„Kdyby se stalo X, kam bys to šel hledat?“*

| Skupina | Oblast | Co sem patří |
|---|---|---|
| _(doplní onboarding)_ | | |

## Struktura

```
Claude/
├── CLAUDE.md            ← pravidla na jednu stranu (čte se automaticky)
├── START-HERE.md        ← pět vět pro začátek
├── PROFILE.md           ← kdo jsem, na čem pracuji
│
├── INBOX/               ← rychlé zápisy, než se vytřídí
├── PROJECTS/            ← PROJECTS: věci s cílem a koncem (varianta „jedna vrstva“)
│   └── <projekt>/           brief · plan nebo map · log · state.json · dashboard.html · decisions/
├── AREAS/               ← AREAS: trvalé odpovědnosti
│   ├── work/<oblast>/       ← pracovní oblasti (firma, zaměstnání)
│   ├── school/<oblast>/     ← školní oblasti
│   └── personal/<oblast>/   ← osobní oblasti (domácnost, finance, zdraví…)
│                              (varianta „pod oblastí“: projekty leží v <oblast>/<projekt>/)
├── RESOURCES/           ← RESOURCES: znalosti a zdroje: index.md · log.md · sources/ · pages/ · snapshots/
├── ARCHIVE/             ← ARCHIVE: hotové a odložené: projects/ · areas/
└── SYSTEM/              ← vše, co spravuje Claude
    ├── registry/            ← přehledy a pravidla: skills-catalog · projects-registry · session-brain · decisions-registry · folder-map · workspace-rules · project-method
    ├── skill-memory/        ← paměť skillů (aktualizace ji nepřepíše)
    └── skills/              ← zdroje tvých vlastních skillů (vzniká až při prvním skillu, se souhlasem)
```

Zakládají se **jen skupiny a oblasti, které člověk opravdu má**. Zaměstnanec, který nestuduje, `AREAS/school/` mít nebude: školu dětí řeší oblast `skola-deti` v `personal`, vlastní občasné kurzy oblast `rozvoj`. Skupina `school` je jen pro toho, kdo sám studuje (i vedle práce).

**Dvě varianty umístění projektů** (volí se v onboardingu, zapisuje se do řádku `Projekty`):
- **Jedna vrstva (doporučeno):** všechny projekty v `PROJECTS/<projekt>/`. K oblasti patří polem `area` ve `state.json` a sloupcem Oblast v registru; název složky doporučeně začíná oblastí (`firma-a-relaunch-webu`). Výhody: vidíš vše, co běží, na jednom místě; hotový projekt se přesune jedním krokem; projekt do dvou oblastí nic neřeší.
- **Pod oblastí:** projekt leží v `AREAS/<skupina>/<oblast>/<projekt>/`, příslušnost je vidět ve složkách. Cena: o úroveň hlouběji, ztratí se jednotný seznam projektů (nahradí ho přehled od `snapshot`), projekt patřící do dvou oblastí se zařadí do jedné.

V obou variantách platí totéž: pole `area` ve `state.json` a sloupec Oblast v registru, sloupec Složka v registru říká, kde projekt leží, a hotový projekt se po souhlasu přesune do `ARCHIVE/projects/<projekt>/`.

## Kam co patří (řiď se pořadím otázek)

1. Má to **cíl a konec** (rekonstrukce, seminárka, výlet)? → projekt (`PROJECTS/<projekt>/`, nebo pod oblastí podle volby). Nemá-li to konec, je to spíš oblast.
2. Je to **trvalá odpovědnost nebo trvalá věc oblasti** (pravidla domu, seznam pojistek, poznámky k práci)? → `AREAS/<skupina>/<oblast>/`.
3. Je to **znalost nebo zdroj**, ke kterému se budeš vracet (článek, návod, poznámky k tématu)? → `RESOURCES/`.
4. Už to **nepotřebuješ mít na očích**? → `ARCHIVE/`.
5. **Nevíš** nebo je to rychlý zápis? → `INBOX/`.

## Záznamy

`<složka-projektu>` je `PROJECTS/<projekt>/` (jedna vrstva), nebo `AREAS/<skupina>/<oblast>/<projekt>/` (pod oblastí), podle řádku `Projekty`.

| Typ výstupu | Složka | Název | Spravuje |
|---|---|---|---|
| Rychlý nápad, úkol | `INBOX/` | `RRRR-MM-DD-tema.md` | `inbox` |
| Vyřízené položky z inboxu | `INBOX/hotovo/` | původní název | `triage` (po souhlasu) |
| Trvalá věc oblasti | `AREAS/<skupina>/<oblast>/` | `oblast__typ__tema__RRRR-MM-DD.md` (referenci bez data) | ty / skill |
| Dlouhodobý klient v oblasti (jen jedna úroveň) | `AREAS/<skupina>/<oblast>/<klient>/` | stejné názvy | ty |
| Zadání projektu | `<složka-projektu>` | `brief.md` | `architect` / `planner` |
| Plán projektu (fáze, kdo, rozhodnutí) | `<složka-projektu>` | `plan.md` | `planner` |
| Mapa systému (struktura, stav komponent) | `<složka-projektu>` | `map.md` | `architect` |
| Deník projektu (jen se přidává na konec) | `<složka-projektu>` | `log.md` | `session-close` |
| Stav projektu | `<složka-projektu>` | `state.json` | `architect` / `planner` (při zavření práce i `session-close`: `updated`, `summary`, `next_actions` a stav částí nebo fází, u kterých se skutečnost změnila) |
| Ostatní výstup projektu | `<složka-projektu>` | `oblast__typ__tema__RRRR-MM-DD.md` | ty / skill |
| Rozhodnutí projektu (ADR-lite) | `<složka-projektu>decisions/` | `<projekt>__decision__<tema>__RRRR-MM-DD.md` | `architect` / `planner` |
| Rozhodnutí mimo projekt | `SYSTEM/registry/decisions/` | `oblast__decision__<tema>__RRRR-MM-DD.md` | `architect-pro` / ty |
| Zdroj znalostí | `RESOURCES/sources/` | slug s pomlčkami | `wiki` |
| Zpracovaná znalost | `RESOURCES/pages/` | slug s pomlčkami | `wiki` |
| Přehled stavu (snapshot) | `RESOURCES/snapshots/` | slug s pomlčkami | `snapshot` |
| Uzavřený projekt | `ARCHIVE/projects/<projekt>/` | beze změny | `planner` / `architect` (po souhlasu), `cleanup` |
| Uzavřená oblast | `ARCHIVE/areas/<skupina>/<oblast>/` | beze změny | `cleanup` (po souhlasu) |
| Registr rozhodnutí, projektů | `SYSTEM/registry/` | `decisions-registry.md`, `projects-registry.md` | `architect` / `planner` (při zavření práce i `session-close`: jen řádek Stav a Poslední práce) |
| Katalog skillů | `SYSTEM/registry/` | `skills-catalog.md` | `catalog` / `skill-builder` |
| Metoda projektů, pravidla | `SYSTEM/registry/` | `project-method.md`, `workspace-rules.md` | jen se čtou |
| Konec dne, předání | `SYSTEM/registry/` | `session-brain.md` | `session-close` |
| Paměť skillů | `SYSTEM/skill-memory/<skill>/` | `lessons.md`, `voice.md` | skill (jen připisuje) |
| Zdroje vlastních skillů | `SYSTEM/skills/<skill>/` | `SKILL.md` a další | `skill-builder` |

Poznámka: `snapshot` po vygenerování přehledu přidá **jeden řádek** do `RESOURCES/index.md` (sekce Přehledy) a záznam na konec `RESOURCES/log.md`. Jinak se v souborech skillu `wiki` nic nemění.

## Zastaralé cesty

| Stará cesta | Nová cesta | Od kdy | Poznámka |
|---|---|---|---|
| _(žádné — přidej sem, když přesouváš složku)_ | | | |

**Starý formát složek** (verze 0.2.0: `Registry/`, `wiki/`, `profile.md`, malé `projects/` a `inbox/`) se převádí samostatným souborem **`OPRAVA…md`**, ne ručně a ne skillem.

## Aktualizace mapy

- Potvrdíš nové místo pro nový druh věcí → přidej řádek do tabulky výše.
- Přesuneš složku → přidej řádek do „Zastaralé cesty“, ať `guard` ví, že stará cesta už neplatí. (Přesun hotového projektu do `ARCHIVE/` se sem nezapisuje, má pevné pravidlo výše.)
- Složka pod oblastí je **projekt**, jen když v ní leží `state.json` nebo `brief.md`. Klient nebo podsložka oblasti soubor `brief.md` nemá.
- Nová oblast → přidej řádek do tabulky „Moje oblasti“ (po dohodě) a založ složku `AREAS/<skupina>/<oblast>/`.
````
<!-- END FILE -->

### SYSTEM/registry/workspace-rules.md

<!-- BEGIN FILE: SYSTEM/registry/workspace-rules.md -->
````markdown
---
type: reference
version: 2026-09-23
visibility: PUBLIC
status: draft
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-23

> **Vrstvy skillů.** Skilly zmíněné níže jsou ve třech vrstvách: **Základ** (`onboarding`, `architect`, `planner`, `guard`, `inbox`, `session-close`, `safety`, `coach`, `skill-builder`), **Nadstavba** (`wiki`, `snapshot`, `catalog`, `triage`, `cleanup`) a **Pokročilé** (`ai-builder`, `architect-pro`). Nemáš-li skill z vyšší vrstvy nainstalovaný, jeho práci dělá Claude jednodušeji sám, nebo se přeskočí.

# Pravidla pojmenování a složek

Jedno místo, kde stojí, jak se v tomhle workspace **pojmenovávají soubory** a **kam se co ukládá**. `CLAUDE.md` z toho drží jednostránkový výtah, `guard` je vynucuje při zápisu a `cleanup` při úklidu. Kdyby se někde tvrdilo něco jiného, platí tenhle soubor.

Pravidla mají jediný účel: za rok najdeš, co jsi psal(a), a Claude to najde taky.

## 1. Jak pojmenovat soubor

```
oblast__typ__tema__RRRR-MM-DD.md
```

| Část | Co to je | Příklad |
|---|---|---|
| `oblast` | jedna z **tvých oblastí** ze seznamu „Moje oblasti“ v `folder-map.md` (nevymýšlí se za pochodu; jedinečná napříč skupinami `work`, `school`, `personal`) | `firma-a`, `domacnost`, `finance`, `zdravi` |
| `typ` | jaký druh dokumentu to je | `brief`, `plan`, `notes`, `decision`, `report`, `log` |
| `tema` | čeho se to týká, krátce | `rekonstrukce-kuchyne` |
| `datum` | kdy soubor vznikl | `2026-09-23` |

Celé: `domacnost__plan__rekonstrukce-kuchyne__2026-09-24.md`

**Technická pravidla** (kontroluje je `scripts/name-check.py` ve skillu `guard`):
- jen malá písmena, čísla a pomlčky; **bez diakritiky, bez mezer** (`kuchyne`, ne `Kuchyně`);
- části se oddělují dvěma podtržítky `__`, slova uvnitř části jednou pomlčkou;
- datum je vždy **na konci** ve tvaru `RRRR-MM-DD`, těsně před příponou.

*Proč:* dvě podtržítka dovolí mít v tématu pomlčky a soubory se řadí a hledají podle oblasti a typu. Datum na konci je jen pořadí vzniku.

**Doporučené typy** (`typ`): `brief` (zadání) · `plan` · `notes` (poznámky) · `decision` (rozhodnutí) · `report` · `draft` (koncept) · `list` (seznam) · `log` (deník). Nový typ je v pořádku, když žádný z nich nesedí. Nevymýšlej ale synonyma (`poznamky`, `notes`, `zapis` pro totéž).

### Dva druhy souborů: s datem a bez data

| Druh | Příklad | Datum v názvu? |
|---|---|---|
| **Výstup** — vznikne jednou a nemění se (zápis, report, plán k datu) | `domacnost__report__stav-stavby__2026-09-24.md` | **ANO** |
| **Reference nebo průběžný soubor** — přepisuje se nebo do něj přibývá, odkazují na něj jiné soubory (pravidla, deník, přehled) | `domacnost__notes__pravidla-domu.md` | **NE** — datum verze patří do záhlaví uvnitř (`version: 2026-09-23`) |

*Proč:* soubor s datem v názvu, na který odkazují jiné soubory, by se při každé aktualizaci přejmenoval a všechny odkazy by se rozbily.

### Výjimky — pevné názvy

Tyhle soubory mají stálý název, `guard` je nechá být: `CLAUDE.md`, `START-HERE.md`, `PROFILE.md`, `index.md`, `log.md`, `README.md`, `SKILL.md`, uvnitř složky projektu `brief.md`, `plan.md`, `map.md`, `state.json`, `dashboard.html`, v `SYSTEM/skill-memory/` `lessons.md` a `voice.md` a přehledy v `SYSTEM/registry/` (`skills-catalog`, `projects-registry`, `session-brain`, `decisions-registry`, `folder-map`, `workspace-rules`, `project-method`). Přechodný opravný soubor `OPRAVA…md` (z verze 0.2.0) je také pevný název.
Ve složce `INBOX/` stačí `RRRR-MM-DD-tema.md` (rychlý zápis). V `RESOURCES/` je název jen slug s pomlčkami (`karpathy-llm-wiki.md`).

## 2. Jak pojmenovat složku

- **velikost písmen se drží přesně** (`PROJECTS`, ne `projects`) a nezakládají se dvě složky lišící se jen velikostí písmen (na macOS by splynuly, jinde ne);
- malá písmena, bez diakritiky, slova spojená pomlčkou (`PROJECTS/rekonstrukce-kuchyne/`);
- **název složky projektu se nikdy nemění.** Kolem něj visí odkazy. Když ho opravdu potřebuješ změnit, nech to udělat `cleanup` (opraví odkazy);
- systémové složky (`INBOX`, `PROJECTS`, `AREAS`, `RESOURCES`, `ARCHIVE`, `SYSTEM` a v ní `registry`, `skill-memory`, `skills`) a tři skupiny oblastí (`work`, `school`, `personal`) mají anglický název a nepřejmenovávají se. Názvy **oblastí** si volí uživatel (jedno slovo, bez diakritiky, klidně česky: `domacnost`, `firma-a`).

## 3. Kam co patří (metoda PARA)

Úplná mapa je v **`SYSTEM/registry/folder-map.md`** — jediné místo, kde stojí, která složka je pro co. Řídí se tím, **co s věcí budeš dělat**, ne tím, o čem je. Čtyři hlavní složky:

| Složka | PARA | Co to je | Příklad |
|---|---|---|---|
| `PROJECTS/<projekt>/` (nebo pod oblastí, viz níže) | Projects | věc s **cílem a koncem** | rekonstrukce kuchyně, seminárka, výlet |
| `AREAS/<skupina>/<oblast>/` | Areas | **trvalá odpovědnost** bez konce | firma, domácnost, zdraví, studium |
| `RESOURCES/` | Resources | znalosti a zdroje, ke kterým se vracíš | návody, články, poznámky k tématu |
| `ARCHIVE/` | Archive | hotové a odložené věci ze všeho výše | uzavřený projekt, opuštěná firma |

Plus `INBOX/` pro rychlé zápisy a systémové složky `SYSTEM/registry/`, `SYSTEM/skill-memory/`, `SYSTEM/skills/`, o které se stará Claude.

**Zásady, které předcházejí bordelu:**
- **Projekt bez konce je oblast.** Každý projekt má „hotovo, když…“ a nejlépe termín. Nemá-li ani jedno, ptej se, jestli to není oblast.
- **Oblastí je málo:** 5 až 8 celkem. Překročíš-li to, ptej se u každé nové, jestli je to trvalá odpovědnost, nebo projekt. Oblasti se nesmějí překrývat (zkouška: *kam bys to šel hledat?*).
- **Skupina je jedna ze tří pevných složek:** `work`, `school`, `personal`. Zakládají se jen ty, které člověk opravdu má. **`school` jen pro toho, kdo sám studuje** (i vedle práce, pak je vedle `work`); jinak škola dětí patří do oblasti `skola-deti` v `personal`.
- **Klient není oblast.** Práce s koncem je projekt. Dlouhodobý klient s opakující se prací je podsložka oblasti (`AREAS/work/firma-a/klient-novak/`), jen jedna úroveň.
- **Nejvýš tři úrovně složek** uvnitř `AREAS/`. Podsložku zakládej až při zhruba 15 souborech.
- **Projekty: dvě varianty** (volí se v onboardingu, řádek `Projekty` ve `folder-map.md`). **Jedna vrstva (doporučeno):** všechny v `PROJECTS/`, název doporučeně začíná oblastí (`firma-a-relaunch-webu`); vidíš vše, co běží, na jednom místě a hotový projekt se přesune jedním krokem. **Pod oblastí:** `AREAS/<skupina>/<oblast>/<projekt>/`, příslušnost je vidět ve složkách, ale je to o úroveň hlouběji. V obou variantách má projekt pole `area`.
- **Projekt patří k jedné oblasti** (pole `area`). Patří-li ke dvěma, zvol tu, kde bys ho hledal, a druhou zmiň v popisu.
- **Hotové věci se archivují.** Uzavřený projekt jde po souhlasu do `ARCHIVE/projects/`, aby seznam projektů zůstal krátký.
- **Resources nejsou smetiště.** Drž jen to, co opravdu používáš.
- **Pracovní oblast:** dávej do ní jen to, co smíš vkládat do AI nástrojů (bez důvěrných dat firmy, klientů a kolegů). Složka tě nechrání, chrání tě jen to, co do ní vložíš.
- Nevíš kam → zeptej se `guard`, navrhne místo a zapíše ho do mapy.

## 4. Co se nedělá bez zeptání

Tyhle věci `guard` nikdy neudělá potichu:
1. smazání jakéhokoli souboru nebo složky,
2. založení nové složky, která není v `folder-map.md`,
3. zápis mimo místa v `folder-map.md`,
4. přepsání souboru, který vytvořil jiný skill,
5. změna systémových souborů (`CLAUDE.md`, `SKILL.md`, `folder-map.md`, `workspace-rules.md`).

Dočasné soubory a čtení se neptají.

*Proč:* zápis se dá vrátit jen tehdy, když víš, že k němu došlo.
````
<!-- END FILE -->

### SYSTEM/registry/project-method.md

<!-- BEGIN FILE: SYSTEM/registry/project-method.md -->
````markdown
---
type: reference
version: 2026-09-24
visibility: PUBLIC
status: draft
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

> **Vrstvy skillů.** Skilly zmíněné níže jsou ve třech vrstvách: **Základ** (`onboarding`, `architect`, `planner`, `guard`, `inbox`, `session-close`, `safety`, `coach`, `skill-builder`), **Nadstavba** (`wiki`, `snapshot`, `catalog`, `triage`, `cleanup`) a **Pokročilé** (`ai-builder`, `architect-pro`). Nemáš-li skill z vyšší vrstvy nainstalovaný, jeho práci dělá Claude jednodušeji sám, nebo se přeskočí.

# Metoda projektů

Jak se v tomhle workspace vedou projekty. Čtou ji `architect`, `planner`, `architect-pro`, `session-close`, `cleanup` a `catalog`. Kdyby skill tvrdil něco jiného, platí tenhle soubor.

## 1. Dva druhy projektu, dvě role

| Druh | Co to je | Příklad | Skill | Co vidí |
|---|---|---|---|---|
| `system` | něco, co existuje a mění se | aplikace, workspace, sada skillů, domácí síť | `architect` | **mapu**: co kde je, jak to visí, jaký je stav částí |
| `process` | něco, co proběhne a skončí | rekonstrukce, stěhování, plán studia | `planner` | **plán**: fáze, kdo je aktér, kdy se rozhoduje |

Návrh AI systému (agenti, workflow) je věc pro `ai-builder` a vždy se zapíše jako `system`.
Nikdo z nich projekt „nestaví“ sám: architekt založí kostru, planner řídí provedení.
Nejsi-li si jistý druhem, ptej se: *bude to existovat a měnit se, nebo to proběhne a skončí?* Smíšený případ jsou dva projekty s vazbou (`depends_on`).

## 2. Stavy

Jeden slovník pro všechno (komponenty, fáze, celé projekty):

| Stav | Význam u komponenty systému | Význam u fáze procesu |
|---|---|---|
| `draft` | navrženo, ještě nezačato | naplánováno, nezačalo |
| `wip` | rozpracováno | běží |
| `live` | funguje, používá se | hotovo |
| `dormant` | odloženo, může se vrátit | odloženo |
| `archived` | uzavřeno, jen pro záznam | uzavřeno nebo zrušeno |
| `missing` | **má existovat, ale chybí** (je v mapě nebo plánu, soubor nebo věc není) | totéž |

Stav se mění, **když se změnila skutečnost**, ne když se plánuje. Rozpracovanost = počet `live` děleno celkem.

## 3. Co se zapisuje kam

Složka projektu. Kde leží, určuje řádek `Projekty` ve `folder-map.md`: **jedna vrstva** = `PROJECTS/<projekt>/` (výchozí, doporučeno), **pod oblastí** = `AREAS/<skupina>/<oblast>/<projekt>/`. Příslušnost k oblasti je **vždy** v poli `area`, i když ji ve variantě „pod oblastí“ ukazuje i poloha složky:

| Soubor | Účel | Jak se píše |
|---|---|---|
| `brief.md` | proč projekt je, cíl, hranice, „hotovo, když…“ | jednou, mění se zřídka |
| `map.md` (systém) nebo `plan.md` (proces) | mapa nebo plán | přepisuje se, drží aktuální stav |
| `log.md` | deník | **jen se přidává na konec**, nikdy se nepřepisuje. Záznam: `## RRRR-MM-DD — název` a pár odrážek |
| `state.json` | strojově čitelný stav | přepisuje se (schéma níže) |
| `dashboard.html` | volitelný přehled | generuje se ze `state.json`, ručně se neupravuje |
| `decisions/` | rozhodnutí (ADR-lite) | jeden soubor na rozhodnutí |

**Pravidlo:** *stav* patří do `state.json` (přepisuje se), *co se stalo* do `log.md` (přidává se), *proč jsme se rozhodli* do `decisions/`. Nemíchej je: deník, který drží stav, se nedá číst, a stav v deníku zastará.

### Schéma `state.json`

```json
{
  "project": "rekonstrukce-kuchyne",
  "type": "system | process",
  "area": "domacnost",
  "due": "2026-12-31",
  "status": "draft | wip | live | dormant | archived",
  "updated": "2026-09-23",
  "summary": "jedna věta: kde jsme",
  "depends_on": [],
  "components": [{ "name": "", "status": "draft", "note": "" }],
  "phases": [{ "name": "", "status": "draft", "owner": "", "note": "" }],
  "open_decisions": [{ "id": "D-004", "note": "" }],
  "next_actions": [""],
  "handoff": [{ "decision": "D-007", "to": "architect", "system": "domaci-sit", "status": "open | done" }]
}
```

`components` se používá u `system`, `phases` u `process`, druhé pole zůstane prázdné (`[]`). `project` = název složky. **`area`** je oblast projektu, **musí být v seznamu „Moje oblasti“** ve `folder-map.md` (jedna oblast na projekt). **`due`** je termín (`RRRR-MM-DD`), prázdný řetězec `""`, když termín není. Projekt bez termínu a bez „hotovo, když…“ je spíš oblast než projekt; zeptej se. `note` u komponenty i fáze je volitelná poznámka nebo blokátor. `system` v `handoff` je volitelné a říká, kterého systémového projektu (složka v `PROJECTS/`) se předání týká. Neznámé pole nemaž, jen ho nech.

**`open_decisions` a ID:** otevřené rozhodnutí má vždy ID `D-…`, tedy je to řádek ve `decisions-registry.md` se stavem `proposed`. Drobnost bez ID (nestojí za zápis rozhodnutí) patří jen do `plan.md` nebo `map.md`, ne do `open_decisions`.

## 4. Rozhodnutí (ADR-lite)

**Kdy zapsat:** rozhodnutí, u kterého bys za měsíc chtěl vědět *proč*: volba mezi variantami, změna struktury, trvalý důsledek. Drobnosti ne.

**Postup (pořadí je důležité — registr PŘED souborem):**
1. Otevři `SYSTEM/registry/decisions-registry.md` a najdi nejvyšší ID. Nové je o jedna vyšší (`D-001`, `D-002`…; číslování jedno pro celý workspace).
2. Zapiš řádek do registru (sloupec **Soubor** = cesta od složky `Claude/`, třeba `PROJECTS/domaci-sit/decisions/domaci-sit__decision__router__2026-09-23.md`).
3. Teprve potom založ soubor `<složka-projektu>/decisions/<projekt>__decision__<tema>__RRRR-MM-DD.md` (rozhodnutí bez projektu jdou do `SYSTEM/registry/decisions/`).

**Šablona souboru:**

```
---
id: D-007
status: proposed | accepted | superseded
date: RRRR-MM-DD
project: <projekt>
---
# D-007 — <název rozhodnutí>
**Kontext:** proč se to řešilo.
**Rozhodnutí:** co jsme zvolili (jedna až tři věty).
**Alternativy:** co jsme zvažovali a proč ne.
**Důsledky:** co z toho plyne, co se tím uzavírá.
```

Nahrazené rozhodnutí se **nemaže**: dostane `superseded` a odkaz na nové.

## 5. Jeden přehled projektů

`SYSTEM/registry/projects-registry.md` — **jeden řádek na projekt**, detail zůstává ve složce projektu. Sloupce: `Projekt | Druh | Oblast | Stav | Poslední práce | Složka | Poznámka`. Píše ho `architect` nebo `planner` při založení a při změně stavu. Druh projektu (`system` / `process`) určuje, který skill ho vede. **Složka** je cesta ke složce projektu (`PROJECTS/<projekt>/` nebo `AREAS/<skupina>/<oblast>/<projekt>/`, podle řádku `Projekty`), u uzavřeného projektu `ARCHIVE/projects/<projekt>/`. Oblast v registru se musí shodovat s polem `area` ve `state.json`.

## 6. Tři kontroly konzistence (a jedna navíc)

1. **Sirotci:** projekt v registru bez složky; složka projektu (v `PROJECTS/` nebo pod oblastí, podle řádku `Projekty`) bez řádku v registru; rozhodnutí v registru bez souboru a naopak.
2. **Chybějící reference:** odkaz v `brief`, `map`, `plan`, `log` nebo `state.json` na soubor, projekt nebo ID (`D-…`), které neexistuje.
3. **Cykly:** projekt A závisí na B a B na A (pole `depends_on`), přímo nebo přes další.

Při **nepotvrzené struktuře** (`Struktura potvrzena: zatím ne`) skript přeskočí kontroly členství v seznamu „Moje oblasti“ a kontroly složek oblastí a hlásí jediné `WARN`; shoda pole `area` s registrem se kontroluje vždy. Oblasti se týká i to, že archivované projekty si `area` ponechávají, i když oblast ze seznamu zanikla.

Kontrola **`poloha`** hlídá, že projekt leží tam, kde říká zvolená varianta (`Projekty` ve `folder-map.md`), a u varianty „pod oblastí“ (**FLAG**) že se oblast v cestě shoduje s polem `area`. Složka pod oblastí je **projekt**, jen když obsahuje `state.json` nebo `brief.md`; klient nebo podsložka oblasti proto `brief.md` obsahovat nesmí.

Skript `consistency-check.py` k těmto třem kontrolám přidává čtvrtou, lehčí (**stav**): chybějící nebo neplatná pole ve `state.json`, neplatný stav, rozpracovaný projekt bez aktualizace přes 30 dní, nesoulad s registrem, **oblast projektu, která není v seznamu „Moje oblasti“ nebo se liší mezi `state.json` a registrem**, projekt s termínem v minulosti, uzavřený projekt mimo `ARCHIVE/projects/` a neuzavřený v něm, a oblast ze seznamu bez složky `AREAS/<skupina>/<oblast>/`, poloha složky projektu, která neodpovídá zvolené variantě (`Projekty`), a u varianty „pod oblastí“ oblast v cestě, která se liší od pole `area`. Kontrola vypíše nálezy a **nic neopravuje bez souhlasu**. Omezení: závislosti mezi *komponentami* jednoho systému drží sloupec „Závisí na“ v `map.md`, ne `state.json`, takže cykly na úrovni komponent kontrola nevidí (jen cykly mezi projekty přes `depends_on`). Spouští ji `architect` při navázání na projekt, `architect-pro` napříč celým workspace a `cleanup` při úklidu.

## 7. Předání z plánu do mapy

Rozhodnutí z plánu, které mění strukturu systému, zapíše `planner` jako ADR-lite (řádek v registru, soubor) a přidá do `state.json` řádek v `handoff` se `status: open`. `architect` ho při navázání zapracuje do `map.md` a přepne na `done`. Protože řádek leží v souboru, který vytvořil `planner`, dělá to architect **jen se souhlasem uživatele** (červená linie 4: přepis souboru jiného skillu). Pole `system` říká, kterého systému se předání týká; není-li vyplněno, projde architect `handoff` všech projektů.

## 8. Uzavření projektu (archivace)

Hotový nebo opuštěný projekt se **přesune do `ARCHIVE/projects/<projekt>/`**, aby seznam aktivních projektů zůstal krátký. Dělá to `planner` (proces) nebo `architect` (systém) **po souhlasu uživatele**:

1. Do `log.md` projektu připiš závěrečný záznam (co se povedlo, co příště).
2. Ve `state.json` nastav `status: archived` a `updated`.
3. **Přesuň složku projektu** (kdekoli leží, `PROJECTS/<projekt>/` nebo pod oblastí) do `ARCHIVE/projects/<projekt>/` (složku `ARCHIVE/projects/` založ, chybí-li, ta je v mapě).
4. V `SYSTEM/registry/projects-registry.md` změň u řádku **Stav** na `archived` a **Složku** na `ARCHIVE/projects/<projekt>/`.
5. V `SYSTEM/registry/decisions-registry.md` přepiš ve sloupci **Soubor** cesty rozhodnutí tohoto projektu (původní cesta → `ARCHIVE/projects/…`).
6. Zkontroluj konzistenci (`consistency-check.py`). Odkazy z jiných projektů na tenhle projekt, které se přesunem rozbily, jen vypiš uživateli; oprava se dělá po souhlasu (`cleanup`, je-li nainstalován).

**Obnova:** vrátit projekt z archivu je zvláštní rozhodnutí. Dělá se po souhlasu stejnými kroky obráceně (přesun zpět na původní místo, `status` jiný než `archived`, oprava řádku v registru a cest rozhodnutí, kontrola konzistence). Sloupec **Poslední práce** se archivací nemění: zůstává datem poslední skutečné práce na projektu.

Uzavřená **oblast** (opuštěná firma, dostudovaná škola) se přesune celá do `ARCHIVE/areas/<skupina>/<oblast>/`. **Projekty oblasti** (leží v `PROJECTS/` nebo pod oblastí) se uzavřou zvlášť podle kroků 1 až 6 výše do `ARCHIVE/projects/`, po souhlasu u každého. Dělá to `cleanup` po souhlasu, včetně oprav registru. Archivované projekty si ponechávají pole `area` i po zániku oblasti ze seznamu Moje oblasti.
````
<!-- END FILE -->

### pruvodce/structure-guide.md

<!-- BEGIN FILE: pruvodce/structure-guide.md -->
````markdown
---
type: reference
version: 2026-09-24
visibility: PUBLIC
status: draft
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

> Schváleno (D-017, JSO 2026-09-24). Názvy kostry: VELKÁ PÍSMENA, složka `SYSTEM/` s `registry/`, `skill-memory/`, `skills/`, soubor `PROFILE.md`. Uvnitř `ARCHIVE/` jsou podsložky malými písmeny (`projects/`, `areas/`).

# Průvodce strukturou: jak si postavit složku

Zdroj pro krok 3 v `onboarding`. Claude podle něj **vede rozhovor**, **navrhuje** a člověk **vybírá**. Nikdo nemusí nic vymýšlet od nuly. Cílem je, aby se **soubory za rok dalo najít** a nevznikl bordel.

## 1. Základní myšlenka (řekni ji jednou větou)

Složky se řídí tím, **co s věcí děláš**, ne tím, o čem je (metoda PARA):

| Složka | Co v ní je | Příklad |
|---|---|---|
| `PROJECTS/` | věci s **cílem a koncem** | rekonstrukce kuchyně, seminárka, relaunch webu |
| `AREAS/` | **trvalé oblasti** tvého života a práce | firma, domácnost, zdraví, studium |
| `RESOURCES/` | znalosti a zdroje, ke kterým se vracíš | návody, články, poznámky |
| `ARCHIVE/` | hotové a odložené | uzavřený projekt, opuštěná firma |
| `INBOX/` | rychlé zápisy, než se vytřídí | „napadlo mě…“ |
| `SYSTEM/` | vše, co spravuje Claude (přehledy, paměť skillů, vlastní skilly) | tam ručně nesahej |

**Pravidlo psaní:** **VELKÁ PÍSMENA = kostra, na kterou nesahám. malá písmena = to, co tvořím já.**

## 2. Rozhovor: poznej člověka (empaticky, po jedné otázce)

Nezačínej „jaké máš oblasti“ (to nikdo z hlavy nevymyslí).
1. „Než si navrhneme složky, chci ti porozumět. Jak vypadá tvůj běžný týden a co ti zabírá nejvíc času a hlavy?“ Pak **zopakuj, co jsi slyšel(a)**, a nesuď. Zní-li to jako přetížení, řekni to lidsky jednou větou.
2. Doptej se jen na to, co ještě nevíš (max. 3, jedna po druhé): pracuješ, studuješ (formálně: škola, univerzita), nebo obojí? Řešíš školu dětí? · pro jednu firmu, pro víc, nebo podnikáš? · žiješ sám, s partnerem, s rodinou? · co ti nefunguje nebo nemáš pod kontrolou (papíry, peníze, domácnost, učení)?

## 3. Kostra oblastí: navrhni hotovou

Vyber z `references/skeletons.md` (pracující · student · podnikatel nebo víc firem · jiné) a přizpůsob podle rozhovoru. Ukaž tabulku (skupina | oblast | co sem patří), člověk **škrtá, přidává, přejmenovává**. Pravidla:
- **5 až 8 oblastí celkem.** Víc je znamení, že se pletou projekty s oblastmi.
- Skupiny jsou tři pevné: `work`, `school`, `personal`. Zakládají se jen ty, které člověk má.
- **Skupina `school` jen pro toho, kdo sám studuje.** Studuje-li (škola, univerzita, formální studium), i vedle práce, je skupina `school` **vedle** `work`. Nestuduje-li, skupinu `school` **nezakládej**: školu dětí řeší oblast v `personal` (`skola-deti`), vlastní občasné kurzy oblast `rozvoj`.
- **Každá firma je vlastní oblast** ve skupině `work` (`firma-a`, `firma-b`). Klient není oblast (viz 7).
- Oblasti se **nesmějí překrývat**. Zkouška: *„Kdyby se stalo X, kam bys to šel hledat?“*
- Název oblasti: jedno slovo, malá písmena, bez diakritiky, **jedinečný napříč skupinami**.

## 4. VOLBA: kde budou projekty

Tady člověk **vybírá**. Nejdřív krátce vysvětli obě cesty, potom doporuč jednu podle jeho odpovědí.

### Varianta A: projekty v jedné vrstvě (doporučená)
Všechny projekty leží v `PROJECTS/`, každý ví, do které oblasti patří (`area` ve `state.json` a sloupec Oblast v registru):
```
PROJECTS/firma-a-relaunch-webu/
PROJECTS/domacnost-rekonstrukce-kuchyne/
```
**Proč doporučujeme jednu vrstvu:**
1. **Vidíš všechno, co běží, na jednom místě**, napříč firmami i domácností. Přehled „co teď dělám“ nemusíš skládat ze tří složek.
2. **Hotový projekt se přesune jedním krokem** do `ARCHIVE/projects/` a seznam zůstane krátký.
3. **Projekt patřící do dvou oblastí** (svatba = rodina i finance) nevyžaduje rozhodnutí, kam ho fyzicky dát.
4. **Nejmenší hloubka složek** a nejméně chyb: Claude i skripty hledají projekty na jednom místě.
5. Odpovídá to **běžné praxi PARA**.

**Jak pak poznáš, že projekt patří firmě A?** Podle předpony v názvu (`firma-a-…`), podle registru a přehledu po oblastech (`snapshot`), a Claude na otázku „co běží ve Firmě A?“ odpoví.

### Varianta B: projekty pod oblastí (příslušnost viditelná ve složkách)
Projekt leží uvnitř své oblasti:
```
AREAS/work/firma-a/relaunch-webu/
AREAS/personal/domacnost/rekonstrukce-kuchyne/
```
**Kdy dává smysl:** máš jednu nebo dvě dominantní oblasti a chceš **vše o firmě na jednom místě**; projektů na oblast je málo (nejvýš asi tři až čtyři); cítíš, že bez příslušnosti ve složce se ztratíš; a jednou budeš celou firmu nebo školu **archivovat najednou**. **Cena:** je to o úroveň hlubší, ztratíš jednotný seznam běžících projektů (nahradí ho přehled od `snapshot`), a projekt patřící do dvou oblastí musíš zařadit do jedné.

### Jak vybrat (tři otázky, jedna po druhé)
1. „Chceš jedním pohledem vidět **všechno, co teď běží**, napříč firmami a domácností?“ → ano: **A**.
2. „Nebo ti stačí, když **k jedné firmě najdeš všechno v její složce**?“ → ano: **B**.
3. „Kolik projektů budeš mít v jedné oblasti současně?“ → hodně (víc než tři až čtyři): **A**.

Neví-li, doporuč **A** a řekni, že jde později přejít na B (a naopak): přesun složek s opravou odkazů udělá `cleanup` po souhlasu. **Volbu zapiš** do `SYSTEM/registry/folder-map.md` (řádek `Projekty:`).

## 5. Jak pojmenovat

### Složky
| Co | Psaní | Příklad |
|---|---|---|
| Kostra (úroveň 1) | VELKÁ PÍSMENA, pevné | `PROJECTS`, `AREAS`, `SYSTEM` |
| Skupiny oblastí | malá, pevné tři | `work`, `school`, `personal` |
| Oblast | malá, bez diakritiky, jedno slovo nebo se spojovníkem | `firma-a`, `domacnost` |
| **Projekt** | malá, bez diakritiky, slova spojovníkem; **doporučeno začít oblastí** (`oblast-tema`) | `firma-a-relaunch-webu` |
| Uvnitř systému a zdrojů | malá | `SYSTEM/registry/`, `RESOURCES/pages/` |

**Název projektu se po založení nemění** (kolem něj visí odkazy). Nejdřív navrhni ve 2 až 3 variantách a nech vybrat. U varianty B předpona oblasti odpadá (oblast je ve složce nad ním).

### Soubory
`oblast__typ__tema__RRRR-MM-DD.md`: malá písmena, bez diakritiky a mezer, části dělí dvě podtržítka, slova v části pomlčka, datum na konci. **Výstup má datum, reference a průběžný soubor (na který se odkazuje nebo do kterého se přidává) ne.** Pevné názvy: `CLAUDE.md`, `START-HERE.md`, `PROFILE.md` v kořeni (velkými), uvnitř `brief.md`, `plan.md`, `state.json`. V inboxu `RRRR-MM-DD-tema.md`, v `RESOURCES/` slug s pomlčkami.

**Procvič na skutečných věcech:** „Vyber dva soubory, které bys brzy založil(a). Jak by se jmenovaly a do které oblasti patří?“ Ověř přes `guard`.

## 6. Kam co patří (pořadí otázek)
1. Má to **cíl a konec**? → projekt.
2. Je to **trvalá věc oblasti** (pravidla, seznamy, poznámky, ceník)? → `AREAS/<skupina>/<oblast>/`.
3. Je to **znalost nebo zdroj**? → `RESOURCES/`.
4. Už to **nepotřebuji na očích**? → `ARCHIVE/`.
5. **Nevím** nebo rychlý zápis? → `INBOX/`.

## 7. Pravidla proti bordelu (řekni je krátce, nepřednášej)
- **Projekt bez konce je oblast.** Každý projekt má „hotovo, když…“ a nejlépe termín.
- **Klient není oblast.** Práce s koncem je projekt. Dlouhodobý klient s opakující se prací je podsložka oblasti (jedna úroveň).
- **Nejvýš tři úrovně** složek uvnitř `AREAS/`. Podsložku až při zhruba 15 souborech.
- **Hotové věci se archivují** po souhlasu. **`RESOURCES/` nejsou smetiště**, drž jen to, co používáš.
- **První den je struktura skoro prázdná.** Zakládá se jen to, co člověk má a dělá.
- **Pracovní oblast:** jen to, co smíš vkládat do AI nástrojů (bez důvěrných dat firmy, klientů a kolegů).

## 8. Co se zapíše a co se potvrdí
Po souhlasu zapiš do `SYSTEM/registry/folder-map.md`: tabulku **Moje oblasti** (skupina | oblast | co sem patří), řádek **Projekty:** `jedna vrstva` nebo `pod oblastí`, a nakonec datum u **Struktura potvrzena**. Založ složky oblastí (jen ty, které člověk má). **Dokud není potvrzeno, nezakládej žádný projekt.** Rychlý zápis do `INBOX/` smí.

## 9. Později
- **Nová oblast:** jen po dohodě, s otázkou „trvalá odpovědnost, nebo projekt?“ a se zkouškou „kam bys to šel hledat?“.
- **Sloučení oblastí:** dvě se pletou (`domov` a `rodina`) → jedna (`domacnost`).
- **Změna volby A ↔ B:** `cleanup` přesune složky a opraví odkazy po souhlasu.
- **Uzavřená firma nebo škola:** celá oblast do `ARCHIVE/areas/`, její projekty zvlášť do `ARCHIVE/projects/`.

## 10. Zkratka pro Clauda
Poznej člověka → navrhni kostru → nech upravit → **vysvětli obě varianty projektů a doporuč jednu** → pojmenování na dvou skutečných souborech → zapiš a potvrď. Jedna otázka najednou. Nic nezakládej před potvrzením.
````
<!-- END FILE -->

### pruvodce/skeletons.md

<!-- BEGIN FILE: pruvodce/skeletons.md -->
```markdown
---
type: reference
version: 2026-09-24
visibility: PUBLIC
status: draft
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# Výchozí kostry oblastí

Podklad pro krok 3c v `onboarding`. **Člověku se nabízí hotový návrh, ne prázdný papír**: reagovat („tohle škrtni, tohle přidej“) je mnohem snazší než vymýšlet. Kostra je jen výchozí bod; upravuje se podle rozhovoru.

## Zásady návrhu

- **Oblast = trvalá odpovědnost bez konce.** Ne téma a ne kontext. Zkouška: *„Kdyby se stalo X, kam bys to šel hledat?“* Dvě oblasti se nesmějí překrývat.
- **Počet:** 5 až 8 oblastí celkem. Začni **menším počtem**; přidat jde kdykoli, uklidit hůř.
- **Skupina** je jedna ze tří pevných složek: `work`, `school`, `personal`. Zakládají se jen ty, které člověk opravdu má.
- **Skupina `school` jen pro toho, kdo sám studuje.** Studuje-li (škola, univerzita, formální studium), i vedle práce, je skupina `school` **vedle** `work`. Nestuduje-li, skupinu `school` **nezakládej**: školu dětí řeší oblast v `personal` (`skola-deti`), vlastní občasné kurzy oblast `rozvoj`.
- **Název oblasti:** jedno slovo (nebo dvě spojené pomlčkou), malá písmena, bez diakritiky, **jedinečné napříč skupinami**. Výchozí názvy níže jsou česky, protože se používají v názvech souborů; člověk si je může přejmenovat.
- **Klient není oblast.** Práce s koncem je projekt. Dlouhodobý klient s opakující se prací je podsložka oblasti (jedna úroveň).
- **Práce:** do oblasti ve skupině `work` jen to, co smí člověk vkládat do AI nástrojů (bez důvěrných dat firmy, klientů a kolegů).

## Kostra 1 — Pracující (zaměstnanec)

| Skupina | Oblast | Co sem patří |
|---|---|---|
| work | `prace` | pracovní úkoly, poznámky k práci, plán rozvoje v zaměstnání |
| personal | `domacnost` | byt a jeho chod, opravy, děti, rodiče, plány rodiny |
| personal | `finance` | rozpočet, pojištění, daně, smlouvy (bez čísel účtů a karet) |
| personal | `zdravi` | sport, lékaři, spánek, prevence |
| personal | `rozvoj` | učení, kurzy, kariérní cíle mimo současnou práci |
| personal | `volny-cas` | koníčky, cestování, přátelé |
| personal | `skola-deti` | **volitelná, jen má-li děti ve škole:** komunikace se školou, rozvrhy, akce, omluvenky |

Pracující, který už nestuduje, **skupinu `school` nemá.** Řeší-li školu dětí, je to oblast `skola-deti` v `personal`; vlastní občasné kurzy patří do `rozvoj`.

Příklady projektů (ve variantě jedna vrstva s předponou oblasti): `domacnost-rekonstrukce-kuchyne`, `prace-rocni-prezentace`, `volny-cas-letni-dovolena`.

## Kostra 2 — Student

| Skupina | Oblast | Co sem patří |
|---|---|---|
| school | `skola` | předměty, zápisky, rozvrh, zkoušky, administrativa studia |
| work | `prace` | brigáda, praxe (jen co smíš vkládat do AI) |
| personal | `domacnost` | bydlení, kolej, domácí věci, rodina |
| personal | `finance` | kapesné, stipendium, splátky, předplatná |
| personal | `zdravi` | sport, spánek, lékař |
| personal | `volny-cas` | přátelé, koníčky, cestování |

Příklady projektů: `skola-bakalarka`, `skola-zkouskove-leto`, `prace-hledani-brigady` (ve variantě pod oblastí bez předpony). Velké věci se **termínem** jsou projekty, běžné zápisky z předmětů jsou soubory oblasti `skola` (`skola__notes__matematika__2026-10-02.md`).

## Kostra 3 — Podnikatel nebo víc firem

| Skupina | Oblast | Co sem patří |
|---|---|---|
| work | `firma-a` | jedna firma (klidně jejím skutečným krátkým názvem), její klienti, nabídky, provoz |
| work | `firma-b` | druhá firma; **každá firma vlastní oblast** (jiní klienti, jiné závazky, jde je samostatně uzavřít) |
| personal | `domacnost` | byt, rodina |
| personal | `finance` | osobní finance (finance firmy patří do její oblasti) |
| personal | `zdravi` | zdraví, sport |
| personal | `rozvoj` | učení, cíle |

Klient je v názvu projektu (`firma-a-relaunch-webu-novak`) nebo, je-li dlouhodobý, podsložka oblasti (`AREAS/work/firma-a/klient-novak/`). Klientů víc než pět je signál, že ne všichni jsou dlouhodobí: zeptej se, které jsou spíš projekty.

## Kostra 4 — Jiné (složí se z rozhovoru)

Rodič doma, důchodce, člověk mezi prací a studiem, kombinace. Začni **osobním základem** a přidej jen to, co člověk popsal:

| Skupina | Oblast | Co sem patří |
|---|---|---|
| personal | `domacnost` | byt, rodina, děti, rodiče |
| personal | `finance` | rozpočet, pojištění, daně |
| personal | `zdravi` | zdraví, sport |
| personal | `volny-cas` | koníčky, cestování, přátelé |

Přidej `work` nebo `school` oblast, jen když z rozhovoru vyplynula. **Rodič s dětmi ve škole** přidá do `personal` oblast `skola-deti`, ale skupinu `school` nezakládá, pokud sám nestuduje. Nevnucuj oblasti, které člověk nemá.

## Kam co patří: příklady pro vysvětlení

| Situace | Kam |
|---|---|
| Rekonstrukce kuchyně (má cíl a konec) | projekt (v `PROJECTS/`, nebo pod oblastí podle zvolené varianty), oblast `domacnost` |
| Pravidla domácnosti, seznam pojistek | soubor oblasti `domacnost` |
| Daňové přiznání letos | projekt, oblast `finance` |
| Kurz angličtiny | projekt (do konce kurzu), oblast `rozvoj`; potřebuje-li ho člověk do práce, oblast `prace` |
| Článek, který se chci později vrátit | `RESOURCES/` |
| „Něco mě napadlo“ | `INBOX/` |
| Hotová seminárka | přesune se do `ARCHIVE/projects/` |
| Dovolená | projekt, oblast `volny-cas` |

## Kdy oblast rozdělit nebo sloučit

- Dvě oblasti se pletou (`domov` a `rodina`): sluč je (`domacnost`).
- V jedné oblasti je přes ~15 souborů: teprve pak podsložka.
- Nová oblast zní jako projekt (má konec): je to projekt, ne oblast.
```
<!-- END FILE -->

### skills/guard/SKILL.md

<!-- BEGIN FILE: skills/guard/SKILL.md -->
````markdown
---
name: guard
visibility: PUBLIC
metadata:
  status: draft
  author: Jiří Soljak
  linkedin: linkedin.com/in/jirisoljak
description: |
  Hlídá, kam se ukládají soubory a jak se jmenují. Spusť před každým zápisem, přesunem nebo mazáním souboru či složky ve sdílené složce Claude/ a kdykoli nevíš, kam výstup patří. Také na věty "kam to uložit", "kam patří X", "jak to pojmenovat", "kde to najdu", "smaž to", "přejmenuj to". Navrhne umístění (projekt, oblast, resources, archiv, inbox) podle SYSTEM/registry/folder-map.md včetně zvoleného místa projektů, zkontroluje název a psaní kostry (velká písmena) podle SYSTEM/registry/workspace-rules.md a u rizikových operací se zeptá. Nespouštěj při čtení souborů ani u dočasných souborů v /tmp/ a /sessions/.
---

> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# guard — kam to patří a jak se to jmenuje

**Co to je:** hlídač pořádku. Před zápisem navrhne správné místo a název, u rizikových věcí se zeptá. Cílem je, aby člověk za rok našel, co psal, a nemusel číst pravidla.

**Execution model:** hybridní. Pevné je hlídání (červené linie, kontrola názvu skriptem). Volné je navrhnout místo a název pro nový druh výstupu.

**Důležitá poctivost:** v Coworku nejsou hooky, `guard` nemá technické právo veta. Funguje jen proto, že ho ostatní skilly a startovní `CLAUDE.md` volají před zápisem. Když ho nějaký skill přeskočí, zápis proběhne. Proto je dobré, když `CLAUDE.md` říká: "před zápisem souboru zavolej guard".

## Před začátkem

1. Přečti `{workspace}/SYSTEM/registry/folder-map.md` (tabulka **Moje oblasti**, struktura, „Kam co patří“, záznamy) a `{workspace}/SYSTEM/registry/workspace-rules.md` (pojmenování a červené linie).
2. Když jeden z nich chybí, řekni to a nabídni založení ze šablony. Mezitím se řiď jen červenými liniemi níže a **ptej se u každého zápisu**.
3. V `folder-map.md` se podívej na sekci **Moje oblasti**. Je-li tam `Struktura potvrzena: zatím ne` nebo u řádku `Projekty` „zatím nezvoleno“, řekni to jednou větou a před zápisem čehokoli, co zakládá projekt nebo nový soubor s vlastním názvem, nabídni skill `onboarding` (struktura je první věc; není-li nainstalovaný, projdi strukturu, oblasti, volbu umístění projektů a pojmenování s uživatelem sám podle `workspace-rules.md` a potvrzení zapiš do mapy). Rychlé zápisy do `INBOX/` a čtení se neblokují.
4. **Starý formát složek:** vidíš-li v kořeni `Registry/`, `wiki/`, `profile.md` nebo malé `projects/` místo `SYSTEM/registry/`, `RESOURCES/`, `PROFILE.md`, `PROJECTS/`, řekni to jednou větou a doporuč soubor s postupem opravy (`OPRAVA…md`), který dodá ten, kdo kit nasazuje. Složky sám nepřestavuj a nic tam nezapisuj po svém.
5. Když čtení souboru selže: `EPERM` znamená, že soubor existuje, jen chybí oprávnění (zkus bash cestu `/sessions/.../mnt/`). "Outside connected folders" znamená, že složka není nasdílená, požádej o přístup (`request_cowork_directory`). Teprve když nenajdeš soubor ani pak, řekni, že neexistuje.

## Role 1 — Router: kam to uložit

Struktura vychází z metody PARA (projekty, oblasti, resources, archiv). Řiď se tím, **co s věcí člověk bude dělat**, ne tím, o čem je.

1. Zjisti, **co vzniká** (typ výstupu) a **pro co** (projekt, oblast).
2. **Ptej se v pořadí z `folder-map.md`, sekce „Kam co patří“**, a použij první „ano“:
   1. Má to **cíl a konec** (rekonstrukce, seminárka, výlet)? → projekt. **Kam s ním, říká řádek `Projekty` ve `folder-map.md`:** `jedna vrstva` = `PROJECTS/<projekt>/`, `pod oblastí` = `AREAS/<skupina>/<oblast>/<projekt>/`. Nový projekt zakládá `architect` nebo `planner`; ty jen hlídej, že leží na správném místě a že soubor projektu jde do **složky jeho projektu** (cestu najdeš ve sloupci Složka v `SYSTEM/registry/projects-registry.md`). Nemá-li to konec, je to spíš oblast.
   2. Je to **trvalá odpovědnost nebo trvalá věc oblasti** (pravidla domu, seznam pojistek, poznámky k práci)? → `AREAS/<skupina>/<oblast>/`, kde skupina je `work`, `school` nebo `personal` a oblast je z tabulky **Moje oblasti**. Oblast a skupinu si nevymýšlej; neznámou oblast neukládej, viz Role 2.
   3. Je to **znalost nebo zdroj**, ke kterému se bude vracet (článek, návod)? → `RESOURCES/` (podsložky `sources/`, `pages/`, `snapshots/` obsluhují skilly `wiki` a `snapshot`, do `RESOURCES/` nezapisuj po svém; není-li `wiki` nainstalovaný, řekni to a po souhlasu ulož jednoduše jako `RESOURCES/sources/<slug-s-pomlckami>.md`).
   4. Už to **nemá být na očích**? → `ARCHIVE/` (viz Role 3, přesun se ptá).
   5. **Neví** se, nebo je to rychlý zápis? → `INBOX/`.
3. Najdi konkrétní typ v tabulce „Záznamy“ ve `folder-map.md`.
   - **Nalezen:** navrhni cestu a název (viz Role 2).
   - **Nenalezen:** zeptej se člověka, kam to patří, a po odpovědi přidej řádek do mapy (přidání řádku je zápis do systémového souboru, tedy se souhlasem).
4. **Zastaralá cesta?** Když mapa má cestu v "Zastaralé cesty", upozorni a navrhni novou.
5. Neexistuje cílová složka? Složku oblasti, která **je** v tabulce Moje oblasti (a její skupinu), smíš založit a jednou větou to ohlásit. Jiná nová složka je červená linie 2 (viz níže): zeptej se.

## Role 2 — Název: jak to pojmenovat

1. Navrhni název podle `workspace-rules.md`: `oblast__typ__tema__RRRR-MM-DD.přípona` pro **výstup**, bez data pro **referenci nebo průběžný soubor** (na který se odkazuje nebo do kterého se přidává). Rozlišení: dá se na soubor odkazovat později a bude se aktualizovat? Pak bez data. V `INBOX/` a `RESOURCES/` platí jednodušší název (`RRRR-MM-DD-tema.md`, slug s pomlčkami).
2. **Oblast** (první část názvu) je název **složky oblasti** ze seznamu **Moje oblasti**; nevymýšlej si ji. Soubor v `AREAS/<skupina>/<oblast>/` má první část shodnou s touto složkou (soubor v oblasti `domacnost` se jmenuje `domacnost__…`). Soubor v projektu nese oblast projektu (pole `area`). Neznámá oblast: zeptej se jednou otázkou, jestli ji přidat do mapy (je to změna systémového souboru, tedy se souhlasem), nebo použít existující.
3. Ověř název skriptem (seznam oblastí vezmi z mapy, viz `--help`):

   ```bash
   python3 {skill}/scripts/name-check.py --areas domacnost,zahrada,rodina <cesta-k-souboru>
   ```

   Při FLAGu použij navržený název nebo zeptej se, co člověk myslel. `WARN` u oblasti znamená neznámou oblast (viz výše) nebo soubor uložený v jiné oblasti, než říká jeho název („soubor v oblasti X má oblast Y“; tuhle kontrolu dělá skript podle složky i bez `--areas`): buď změň název, nebo místo uložení. Obsah názvu (oblast, téma) si nevymýšlej, doptej se. V `ARCHIVE/` a ve složkách `decisions/` projektů se oblast nekontroluje.
4. **Psaní kostry: velká písmena.** Kostra je `INBOX`, `PROJECTS`, `AREAS`, `RESOURCES`, `ARCHIVE`, `SYSTEM` a soubory `CLAUDE.md`, `START-HERE.md`, `PROFILE.md` v kořeni; malými písmeny jsou to, co tvoří člověk (oblasti, projekty, soubory) a podsložky uvnitř (`SYSTEM/registry/`, `SYSTEM/skill-memory/`, `ARCHIVE/projects/`, `ARCHIVE/areas/`, skupiny `work`, `school`, `personal`). Před zápisem a před založením složky **porovnej psaní cesty** s tímhle pravidlem: začíná-li cesta `projects/`, `inbox/` nebo `Areas/`, navrhni správný tvar a **nezakládej** vedle existující složky druhou lišící se jen velikostí písmen (podívej se `ls`, jak se ta existující jmenuje). Uvnitř složky drží přesnou velikost písmen tak, jak ji vidíš (přesné chování velikosti písmen ve sdílené složce není ověřené). `name-check.py` na dvojici složek lišících se jen velikostí písmen upozorní.
5. Bez skriptu (chybí Python nebo bash) zkontroluj ručně: oblast ze seznamu a shodná se složkou, malá písmena, bez diakritiky a mezer, části oddělené `__`, datum na konci. Řekni, že šlo o ruční kontrolu.

## Role 3 — Guard: zeptej se před rizikem

**Vždy se zeptej**, i když člověk podobnou operaci už dříve schválil, pokud jde o:
1. **smazání** jakéhokoli souboru nebo složky,
2. **novou složku**, která není v `folder-map.md`,
3. **zápis mimo místa v `folder-map.md`**,
4. **přepis souboru, který vytvořil jiný skill**,
5. **změnu systémových souborů** (`CLAUDE.md`, `SKILL.md`, `folder-map.md`, `workspace-rules.md`).

**Přesun do `ARCHIVE/`** (`ARCHIVE/projects/…`, `ARCHIVE/areas/…`) se také vždy ptá: mění místo, kde věci leží, a rozbíjí odkazy. Projekt jde do `ARCHIVE/projects/<projekt>/` **odkudkoli** (z `PROJECTS/` i z oblasti). Uzavřený projekt přesouvá `planner` nebo `architect` po souhlasu podle `project-method.md`, sekce 8, úklid dělá `cleanup`; `guard` jen hlídá, že se to neděje potichu.

Formát dotazu:

```
🔒 GUARD — potvrď

Operace:  ZÁPIS / MAZÁNÍ / NOVÁ SLOŽKA / PŘESUN (i do archivu)
Kam:      <cesta>
Název:    <název>  (kontrola názvu: OK / navržená oprava)
Proč:     <jedna věta>

Povolíš? (ano / ne / uprav)
```

Bez odpovědi "ano" nic neprováděj. Ostatní zápisy (nový soubor na místě z mapy, s platným názvem) proveď a **řekni jednou větou, co a kam jsi zapsal**.

**Nikdy se neptá:** čtení souborů a dočasné soubory v `/tmp/` a `/sessions/`.

Smazaný soubor se nedá vzít zpět. Před mazáním se podívej na cíl (potřebuje ho něco? odkazuje na něj jiný soubor?) a napiš to do dotazu.

## Když něco nejde ideálně

- **Nevíš, kam to patří** → zeptej se jednou otázkou, nevymýšlej složku.
- **Člověk chce jiný název, než je v pravidlech** → řekni, čím se liší, a nech rozhodnout. Pravidla jsou pro člověka, ne naopak. Pokud chce výjimku trvale, navrhni ji zapsat do `workspace-rules.md`.
- **Chce víc, než guard umí** (například automaticky opravit odkazy po přejmenování) → přejmenování s hledáním odkazů dělá `cleanup`. Pokud není nainstalovaný, řekni, které soubory na starý název odkazují (jen vypsat), a nech opravu na člověku.
- **Trust matrix (ASK → NOTIFY po opakovaném schválení)** guard v tomhle balíčku neobsahuje. Jde o volitelné rozšíření pro pokročilé.
````
<!-- END FILE -->

### skills/guard/scripts/name-check.py

<!-- BEGIN FILE: skills/guard/scripts/name-check.py -->
```python
#!/usr/bin/env python3
"""name-check — kontrola názvů souborů a psaní kostry podle pravidel z SYSTEM/registry/workspace-rules.md.

Použití:
  python3 name-check.py [--areas dum,zahrada,rodina] [--root <workspace>] <cesta> [<cesta> ...]

  --areas  seznam oblastí z SYSTEM/registry/folder-map.md (sekce „Moje oblasti“), oddělený čárkou; zápis
           `domacnost` i `personal/domacnost` je v pořádku. Má-li název tři a více částí
           (oblast__typ__tema…), první část musí v seznamu být, jinak řádek WARN (nový soubor s neznámou
           oblastí: zeptat se, zda ji přidat do mapy, nebo použít existující). WARN nemění exit kód.
           Soubory v decisions/ projektu se nekontrolují (první část je tam název projektu).
  --root   složka Claude/, vůči které se cesty berou (jinak se kostra hledá na začátku cesty nebo za
           složkou `Claude`). Slouží jen ke kontrole psaní kostry.

Oblast ve složce (platí i bez --areas): soubor v AREAS/<skupina>/<oblast>/… s názvem o třech a více
částech musí začínat názvem té složky oblasti. Jinak WARN „soubor v oblasti X má oblast Y“ (přesun
nebo přejmenování řeší člověk, skript nic nemění). Skupina je work | school | personal. Platí i pro
projekty pod oblastí (AREAS/<skupina>/<oblast>/<projekt>/). Uvnitř ARCHIVE/ a decisions/ se oblast nekontroluje.

Psaní kostry (jen cesty, které dostane na vstupu, nic se nehledá na disku): kostra se píše VELKÝMI
PÍSMENY (INBOX, PROJECTS, AREAS, RESOURCES, ARCHIVE, SYSTEM), skupiny a vše pod nimi malými.
  WARN  cesta začíná `projects/` (nebo `Projects/`…) místo `PROJECTS/`
  WARN  na vstupu jsou dvě podoby téže složky lišící se jen velikostí písmen (`PROJECTS/` a `projects/`,
        i hlubší `firma-a/` a `Firma-A/`): na Macu jsou to jedna složka, v Linuxu dvě; sjednotit
Pevné názvy (`PROFILE.md`, `CLAUDE.md`…) se píší přesně; `profile.md` je FLAG s návrhem `PROFILE.md`.

Pro každou cestu vypíše OK nebo FLAG, u FLAGu navrhne opravu (jen mechanickou:
malá písmena, bez diakritiky, mezery → pomlčky; obsah názvu nevymýšlí).
Exit kód 1, pokud je aspoň jeden FLAG. Jen standardní knihovna.

Co je platný název (podle místa souboru):
  výstup            oblast__typ__tema__RRRR-MM-DD.přípona
  reference/průběžný  oblast__typ__tema.přípona                (bez data — odkazuje se na něj)
  INBOX/            RRRR-MM-DD-tema.přípona                    (rychlý zápis, při vytřídění se přejmenuje)
  RESOURCES/        slug-s-pomlckami.md
  pevné názvy       CLAUDE.md, START-HERE.md, PROFILE.md, index.md, log.md, brief.md, plan.md,
                    map.md, state.json, dashboard.html, SKILL.md, README.md, lessons.md, voice.md
                    a přehledy v SYSTEM/registry/ (skills-catalog, projects-registry, session-brain,
                    decisions-registry, folder-map, workspace-rules, project-method)
"""
import re
import sys
import unicodedata
from pathlib import Path

WORD = r"[a-z0-9]+(?:-[a-z0-9]+)*"
DATE = r"\d{4}-\d{2}-\d{2}"
OUTPUT = re.compile(rf"^{WORD}__{WORD}__{WORD}__({DATE})\.[a-z0-9]+$")
REFERENCE = re.compile(rf"^{WORD}__{WORD}__{WORD}\.[a-z0-9]+$")
INBOX = re.compile(rf"^{DATE}-{WORD}\.[a-z0-9]+$")
SLUG = re.compile(rf"^{WORD}\.[a-z0-9]+$")
FIXED = {
    "CLAUDE.md", "START-HERE.md", "README.md", "SKILL.md", "PROFILE.md", "index.md", "log.md",
    "brief.md", "plan.md", "map.md", "state.json", "dashboard.html", "lessons.md", "voice.md",
    "skills-catalog.md", "projects-registry.md", "session-brain.md", "decisions-registry.md",
    "folder-map.md", "workspace-rules.md", "project-method.md",
}
IGNORED = {".DS_Store", ".gitkeep"}
GROUPS = ("work", "school", "personal")
SKELETON = ("INBOX", "PROJECTS", "AREAS", "RESOURCES", "ARCHIVE", "SYSTEM")   # kostra: VELKÁ PÍSMENA


def normalize(name):
    stem, dot, ext = name.rpartition(".")
    if not dot:
        stem, ext = name, ""
    s = unicodedata.normalize("NFKD", stem)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"_{3,}", "__", s)
    s = re.sub(r"[^a-z0-9_-]", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s + ("." + ext.lower() if ext else "")


def check(path):
    p = Path(path)
    name = p.name
    if name in IGNORED or name in FIXED or re.match(r"^OPRAVA[\w.-]*\.md$", name):
        return None
    if name.lower() == "profile.md":
        return "PROFILE.md je pevný název a píše se velkými písmeny"
    parts = {x.lower() for x in p.parts[:-1]}
    if "inbox" in parts:
        if INBOX.match(name):
            return None
        return "v INBOX/ má být RRRR-MM-DD-tema.přípona"
    if "resources" in parts:
        if SLUG.match(name):
            return None
        return "v RESOURCES/ má být slug-s-pomlckami.přípona"
    if OUTPUT.match(name):
        m = OUTPUT.match(name)
        y, mo, d = map(int, m.group(1).split("-"))
        if not (1 <= mo <= 12 and 1 <= d <= 31 and 2000 <= y <= 2100):
            return f"neplatné datum {m.group(1)}"
        return None
    if REFERENCE.match(name):
        return None
    if re.search(r"\d{4}-\d{1,2}-\d{1,2}", name) and not re.search(DATE, name):
        return "datum musí mít tvar RRRR-MM-DD (měsíc i den dvouciferně)"
    if re.search(DATE, name) and not re.search(rf"__{DATE}\.[A-Za-z0-9]+$", name):
        return "datum musí být na konci názvu těsně před příponou (…__RRRR-MM-DD.přípona)"
    if name != normalize(name):
        return "malá písmena, bez diakritiky a bez mezer; slova v části spojuj pomlčkou"
    n = name.rsplit(".", 1)[0].count("__")
    return f"očekávané části oddělené __ : oblast__typ__tema[__datum] (nalezeno {n + 1})"


def folder_area(path):
    """Oblast podle složky: AREAS/<skupina>/<oblast>/… → <oblast>, jinak None."""
    parts = [x for x in Path(path).parts[:-1]]
    low = [x.lower() for x in parts]
    for i in range(len(low) - 2):
        if low[i] == "areas" and low[i + 1] in GROUPS:
            return parts[i + 2]
    return None


def area_problem(path, areas):
    p = Path(path)
    name = p.name
    parts = {x.lower() for x in p.parts[:-1]}
    if name in FIXED or name in IGNORED or "inbox" in parts or "resources" in parts or "archive" in parts:
        return None
    if "decisions" in parts and "registry" not in parts:
        return None   # rozhodnutí projektu: první část názvu je projekt (rozhodnutí mimo projekt v SYSTEM/registry/decisions/ se kontrolují)
    if not (OUTPUT.match(name) or REFERENCE.match(name)):
        return None
    first = name.split("__", 1)[0]
    where = folder_area(path)
    if where is not None and first != where:
        extra = " (a není ani v seznamu Moje oblasti)" if areas and first not in areas else ""
        return (f"soubor v oblasti {where} má oblast {first}{extra}. Patří do AREAS/…/{first}/, "
                f"nebo přejmenovat na {where}__… (přesun i přejmenování až po souhlasu).")
    if not areas or first in areas:
        return None
    return f"oblast „{first}“ není v seznamu Moje oblasti ({', '.join(sorted(areas))}). Přidat ji do mapy (po souhlasu), nebo použít existující."


def rel_parts(path, root):
    """Části cesty vůči kořeni workspace: podle --root; jinak za poslední složkou `Claude`; jinak celá cesta."""
    p = Path(path)
    parts = list(p.parts)
    if root is not None and p.is_absolute():
        try:
            return list(p.relative_to(root).parts)
        except ValueError:
            pass
    if "Claude" in parts:
        return parts[len(parts) - parts[::-1].index("Claude"):]
    return parts


def skeleton_problem(path, root):
    """Kostra psaná malými písmeny: `projects/…` místo `PROJECTS/…` (jen první složka vůči kořeni)."""
    parts = rel_parts(path, root)
    if len(parts) < 2:
        return None
    first = parts[0]
    if first.upper() in SKELETON and first not in SKELETON:
        if first.upper() == "SYSTEM" and (len(parts) < 3 or parts[1] not in ("registry", "skill-memory", "skills")):
            return None   # obyčejná složka `system` mimo kostru
        return f"kostra se píše VELKÝMI PÍSMENY: {first}/ má být {first.upper()}/"
    return None


def case_duplicates(paths, root):
    """Složky, které se na vstupu vyskytují ve dvou podobách lišících se jen velikostí písmen (nejvýš nejvyšší úroveň)."""
    spell = {}
    for path in paths:
        parts = rel_parts(path, root)
        if parts and parts[0].upper() == "SYSTEM" and parts[0] != "SYSTEM" and not (
                len(parts) >= 3 and parts[1] in ("registry", "skill-memory", "skills")):
            parts = parts[1:]   # obyčejná složka `system` mimo kostru
        for i in range(1, len(parts)):   # poslední část je soubor; složky jsou parts[:-1]
            prefix = "/".join(parts[:i])
            spell.setdefault(prefix.lower(), set()).add(prefix)
    out, done = [], []
    for key in sorted(spell, key=lambda k: (k.count("/"), k)):
        if len(spell[key]) > 1 and not any(key.startswith(d + "/") for d in done):
            done.append(key)
            out.append(sorted(spell[key]))
    return out


def main(argv):
    args = argv[1:]
    areas, root = set(), None
    while args and args[0] in ("--areas", "--root"):
        if len(args) < 2:
            print(__doc__); return 2
        if args[0] == "--areas":
            areas = {a.strip().split("/")[-1].strip() for a in args[1].split(",") if a.strip()}
        else:
            root = Path(args[1]).expanduser()
        args = args[2:]
    paths = args
    if not paths or paths[0] in {"-h", "--help"}:
        print(__doc__); return 2
    bad = 0
    for path in paths:
        problem = check(path)
        warn = area_problem(path, areas) if problem is None else None
        skel = skeleton_problem(path, root)
        if warn:
            print(f"WARN  {path}: {warn}")
        elif problem is None and not skel:
            print(f"OK    {path}")
        elif problem is not None:
            bad += 1
            fix = normalize(Path(path).name)
            if path.split("/")[-1].lower() == "profile.md":
                fix = "PROFILE.md"
            hint = f" → návrh: {fix}" if fix != Path(path).name else ""
            print(f"FLAG  {path}: {problem}{hint}")
        if skel:
            print(f"WARN  {path}: {skel}")
    for group in case_duplicates(paths, root):
        print("WARN  na vstupu jsou podoby téže složky lišící se jen velikostí písmen: "
              + ", ".join(f"{g}/" for g in group) + " — sjednoť (kostra velkými, ostatní malými)")
    print(f"\nShrnutí: {bad} FLAG z {len(paths)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```
<!-- END FILE -->

