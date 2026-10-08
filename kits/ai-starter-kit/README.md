> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit — Základ

> **Sada: 12 skillů + šablona pracovní složky** · verze **0.5.1** · česky · Mac i Windows · [**⬇ Download package** (.zip)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-5-1__2026-10-08.zip)

Startovní sada pro práci s Claudem v desktopové aplikaci (Cowork) pro lidi, kteří s AI teprve začínají. Dá ti **jednu uspořádanou pracovní složku** a skilly, se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel, pomůže ti napsat dobré zadání i vybrat model, ať zbytečně nevyčerpáš limit. Umí také **uklidit a převzít tvoje staré soubory** a zjistit, co už máš.

**Stav:** koncept. Skilly, skripty i šablona jsou zkontrolované mimo aplikaci, na cizím účtu a na Windows sada zatím zkoušena nebyla. Když něco nefunguje, napiš na LinkedIn.

## Co je nového ve verzi 0.5.1

- **Nejdřív záloha:** máš-li už složku `Claude` s vlastními soubory, zazipuj ji nebo zkopíruj jinam dřív, než cokoli uděláš.
- **Doporučené místo `Dokumenty/Claude`** i s vysvětlením: složka Dokumenty se obvykle zálohuje sama (Mac: iCloud Drive nebo Time Machine, Windows: OneDrive nebo Historie souborů). Onboarding se zeptá, kde složka leží a jestli se zálohuje.

## Co přinesla verze 0.5.0

- Onboarding nejdřív zjistí, co už máš (skilly, pravidla, seznamy) a navrhne, co ponechat, sloučit nebo nahradit.
- Zeptá se na Mac nebo Windows a dává návody jen pro tvůj systém.
- Nový skill `cleanup`: uklidí složku a po dávkách převezme tvoje staré soubory. Každou dávku jde vrátit.
- **Aktualizace jednou větou** („Aktualizuj kit“), bez samostatných opravných souborů. Tvoje části (paměť, profil, oblasti, projekty, vlastní pravidla) se nepřepisují.
- **Lehká učící smyčka:** poznámky o tom, co v kitu nefungovalo, se (s tvým souhlasem) sbírají v jednom souboru a ty je pošleš autorovi, když chceš. Opravy přijdou další aktualizací.
- Skilly mají nová jména: `workspace-architect`, `project-planner`, `file-guard`, `basic-security-guard`, `idea-inbox`, `token-economy`, `prompt-coach`.

Celé release notes jsou v balíčku (`RELEASE-NOTES.md`) a níže v části Historie verzí.

## Co je v balíčku

| Část | K čemu |
|---|---|
| `Claude/` | šablona pracovní složky: pravidla pro Clauda (`CLAUDE.md`), pět vět na začátek (`START-HERE.md`), profil, složky podle metody PARA (projekty, oblasti, zdroje, archiv) a `SYSTEM/` se vším, co spravuje Claude |
| `ai-starter-kit.plugin` | všech 12 skillů najednou |
| `skills-jednotlive/` | totéž po jednom jako `.skill` (když plugin nejde nainstalovat) |
| `README.md`, `RELEASE-NOTES.md` | popis sady, co je nového |
| `RUNBOOK.md` | postup pro toho, kdo sadu někomu předává a provádí ho první hodinou |

## Dvanáct skillů

| Skill | K čemu |
|---|---|
| `onboarding` | první spuštění a aktualizace: zjistí, co už máš, navrhne složky, mapu a pojmenování, potom profil a první projekt |
| `cleanup` | uklidí složku a převezme staré soubory do nové struktury (po dávkách, jde vrátit) |
| `file-guard` | kam soubor uložit a jak ho pojmenovat, před rizikem se zeptá |
| `workspace-architect` | projekty typu systém (mapa, stav částí, „kde jsem skončil“) a pohled přes všechny projekty: přehled, kontrola konzistence, „už to někde běží?“ |
| `project-planner` | projekty typu proces: fáze, kdo je zapojen, rozhodovací body |
| `triage` | roztřídí hromadu úkolů a nápadů (a obsah `INBOX/`) do projektů, oblastí a znalostí; nic nemaže, zapisuje po tvém souhlasu |
| `idea-inbox` | zachytí nápad nebo úkol do 30 sekund |
| `session-close` | konec práce: předání, kde jsi skončil |
| `basic-security-guard` | co do AI nevkládat, zálohy, kontrola složky na hesla a čísla karet |
| `prompt-coach` | pomůže napsat dobré zadání pro Claude a vysvětlí proč |
| `skill-builder` | vytvoří, upraví a zkontroluje tvůj vlastní skill; projde skilly, které už máš; rozdělí dlouhý skill |
| `token-economy` | poradí, na jakém modelu Claude úkol pustit, ať zbytečně nevyčerpáš limit |

## Jak začít (Mac i Windows)

1. **Máš už složku `Claude` s vlastními soubory? Nejdřív ji zazálohuj.** Zazipuj ji (Mac: pravý klik, Komprimovat · Windows: pravý klik, Odeslat, Komprimovaná složka) nebo ji zkopíruj na jiné místo (jiný disk, flashka). Trvá to minutu a o nic nepřijdeš, ani kdyby se cokoli pokazilo.
2. Klikni na **Download package** nahoře. Stáhne se jeden `.zip`.
3. Rozbal ho (dvojklik). Složku `Claude/` z něj zkopíruj do **Dokumentů** (vznikne `Dokumenty/Claude`). Mac: Cmd + C a Cmd + V. Windows: Ctrl + C a Ctrl + V, a máš-li Dokumenty ve OneDrive, kopíruj tam. **Windows:** zapni si v Průzkumníku zobrazení přípon souborů. **Proč právě Dokumenty:** složka Dokumenty se většinou zálohuje sama: na Macu přes iCloud Drive (Plocha a Dokumenty) nebo Time Machine, ve Windows přes OneDrive (zálohování složek) nebo Historii souborů. Co leží v `Dokumenty/Claude`, je tedy i zazálohované. Máš-li složku `Claude` už jinde, nech ji tam, jen si ověř, že se zálohuje.
4. V aplikaci Claude otevři konverzaci se složkou `Claude` jako pracovním prostorem.
5. Nainstaluj `ai-starter-kit.plugin` (otevři ho v aplikaci). Nejde-li to, nainstaluj soubory ze `skills-jednotlive/` po jednom a ulož je jako skilly.
6. Napiš Claudovi: **„Začínám — spusť onboarding.“** Zeptá se na tvůj systém a běžný týden, zjistí, co už máš, a navrhne strukturu. Počítej asi s hodinou.

Skripty uvnitř skillů potřebují Python 3, pouští je Claude. Když v počítači není, skilly přejdou na ruční postup a řeknou to. Nic neinstaluj jen kvůli nim.

## Už máš složku Claude s vlastními soubory?

Nejdřív ji zazálohuj (zazipuj, nebo zkopíruj jinam). Nekopíruj šablonu přes ni, přepsala by ti `CLAUDE.md`, profil a další soubory. Rozbal balíček vedle (třeba do `Dokumenty/Claude-kit`), zkopíruj ho celý do své složky `Claude/INBOX/prevzeti/kit/` a napiš Claudovi „Začínám — spusť onboarding.“ Vlastní pravidla neztratíš, `CLAUDE.md` se obohatí o naše, ne přepíše.

## Máš starší verzi sady?

1. Rozbal nový balíček.
2. V aplikaci **vypni staré přejmenované skilly** (`guard`, `safety`, `inbox`, `model-advisor`, `coach`, `architect`, `planner`), jinak se budou spouštět vedle nových.
3. Nainstaluj nové skilly (plugin, nebo `skills-jednotlive/`).
4. Napiš Claudovi: **„Aktualizuj kit.“** Před každou změnou se zeptá a předtím zazálohuje.

Starou složku z verze 0.2.0 už nepřestavuje samostatný opravný soubor, řeší ji stejná aktualizace.

## Historie verzí

| Verze | Datum | Změna |
|---|---|---|
| 0.5.1 | 2026-10-08 | Oprava dokumentace: záloha před zásahem do existující složky `Claude`, doporučené místo `Dokumenty/Claude` a proč; onboarding se v prvním kroku zeptá, kde složka leží a zda se zálohuje. |
| 0.5.0 | 2026-10-08 | Audit toho, co už máš, Mac i Windows, nový `cleanup` (převzetí starých souborů), aktualizace jednou větou, přejmenované skilly (`file-guard`, `basic-security-guard`, `idea-inbox`, `token-economy`), `coach` rozdělen: `prompt-coach` v Základu. |
| 0.4.0 | 2026-10-01 | První veřejné vydání. Nový skill `model-advisor`; Základ má 10 skillů. |
