> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-01

# AI Starter Kit — Základ

> **Sada: 10 skillů + šablona pracovní složky** · verze **0.4.0** · česky · [**⬇ Download package** (.zip)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-4-0__2026-10-01.zip)

Startovní sada pro práci s Claudem v desktopové aplikaci (Cowork) pro lidi, kteří s AI teprve začínají. Dá ti **jednu uspořádanou pracovní složku** a deset skillů, se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel a pomůže ti rozhodnout se, napsat dobré zadání i vybrat model, ať zbytečně nevyčerpáš limit.

**Stav:** koncept. Skilly, skripty i šablona jsou zkontrolované mimo aplikaci, na cizím účtu sada zatím zkoušena nebyla. Když něco nefunguje, napiš na LinkedIn.

## Co je v balíčku

| Část | K čemu |
|---|---|
| `Claude/` | šablona pracovní složky: pravidla pro Clauda (`CLAUDE.md`), pět vět na začátek (`START-HERE.md`), profil, složky podle metody PARA (projekty, oblasti, zdroje, archiv) a `SYSTEM/` se vším, co spravuje Claude |
| `ai-starter-kit.plugin` | všech 10 skillů najednou |
| `skills-jednotlive/` | totéž po jednom jako `.skill` (když plugin nejde nainstalovat) |
| `README.md` | popis sady a známá omezení |
| `RUNBOOK.md` | postup pro toho, kdo sadu někomu předává a provádí ho první hodinou |

## Deset skillů

| Skill | K čemu |
|---|---|
| `onboarding` | první spuštění: nejdřív složky, mapa a pojmenování, potom profil a první projekt |
| `architect` | projekty typu systém: mapa, stav částí, „kde jsem skončil“ |
| `planner` | projekty typu proces: fáze, kdo je zapojen, rozhodovací body |
| `guard` | kam soubor uložit a jak ho pojmenovat, před rizikovou operací se zeptá |
| `inbox` | zachytí nápad nebo úkol do 30 sekund |
| `session-close` | konec práce: předání, kde jsi skončil |
| `safety` | co do AI nevkládat, zálohy, kontrola složky na hesla a čísla karet |
| `coach` | pomůže rozhodnout se, nebo napsat dobré zadání (prompt) pro Claude |
| `skill-builder` | vytvoří, upraví a zkontroluje tvůj vlastní skill |
| `model-advisor` | poradí, na jakém modelu Claude úkol pustit, ať zbytečně nevyčerpáš limit předplatného |

## Jak začít

1. Klikni na **Download package** nahoře. Stáhne se jeden `.zip`.
2. Rozbal ho (dvojklik). Složku `Claude/` z něj zkopíruj do **Dokumentů**.
3. V aplikaci Claude otevři konverzaci se složkou `Claude` jako pracovním prostorem.
4. Nainstaluj `ai-starter-kit.plugin` (otevři ho v aplikaci). Nejde-li to, nainstaluj soubory ze `skills-jednotlive/` po jednom a ulož je jako skilly.
5. Napiš Claudovi: **„Začínám — spusť onboarding.“** Claude se tě nejdřív zeptá na tvůj běžný týden a navrhne strukturu složek, kterou si upravíš. Pak profil a první projekt. Počítej asi s hodinou.

Skripty uvnitř skillů potřebují Python 3. Když v počítači není, skilly přejdou na ruční postup a řeknou to. Nic neinstaluj jen kvůli nim.

**Máš starší verzi sady (0.2.0)?** Novou šablonu nekopíruj přes svoji složku. Použij [opravu složky](../../tools/folder-restructure/README.md), která tvoji složku zazálohuje a převede.

## Historie verzí

| Verze | Datum | Změna |
|---|---|---|
| 0.4.0 | 2026-10-01 | První veřejné vydání. Nový skill `model-advisor` (na jakém modelu úkol pustit); Základ má 10 skillů. |
