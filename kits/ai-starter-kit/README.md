> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit — Základ

> **Sada: 12 skillů + šablona pracovní složky** · verze **0.5.2** · česky · Mac i Windows · [**⬇ Download package** (.zip)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-5-2__2026-10-08.zip)

Startovní sada pro práci s Claudem v desktopové aplikaci (Cowork) pro lidi, kteří s AI teprve začínají. Dá ti **jednu uspořádanou pracovní složku** a skilly (pomocníky), se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel, pomůže ti napsat dobré zadání i vybrat model, ať nevyčerpáš limit. Umí také **uklidit a převzít tvoje staré soubory** a zjistit, co už máš.

## Stažení celé sady nebo jednoho skillu

**Nepotřebuješ GitHub ani účet.** Klikni na odkaz, soubor se stáhne do složky Stažené. (Nepoužívej zelené tlačítko **Code** na stránce repa, to stáhne celé repo s věcmi, které nepotřebuješ.)

- **⬇ Celá sada, jeden soubor** (12 skillů + šablona složky Claude + návody): [ai-starter-kit__package__zaklad-v0-5-2__2026-10-08.zip](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-5-2__2026-10-08.zip). Doporučuju tuhle možnost, jedině s ní dostaneš složku s mapou a pravidly, na kterých skilly stojí.
- **⬇ Jeden skill zvlášť** (zkusit si jen jeden, nebo přeinstalovat jeden): tabulka níže u každého skillu, nebo [SKILLS.md](SKILLS.md). Soubor `.skill` otevři v aplikaci Claude a ulož jako skill. Kdyby aplikace chtěla `.zip`, přejmenuj příponu.

## Co potřebuješ

- desktopovou aplikaci Claude (Cowork) a přihlášený účet,
- Mac, nebo Windows (funguje na obou),
- asi 20 minut na instalaci a pak hodinu s Claudem. Python ani nic dalšího instalovat nemusíš.

## Co za to dostaneš

Po první hodině máš domluvené složky, první projekt a Claude ví, kde jsi skončil. Příště stačí napsat „Kde jsem skončil?“.

## Poctivě

Je to koncept. Skilly, skripty i šablona jsou zkontrolované mimo aplikaci, ale **na cizím účtu a na Windows sada zatím zkoušena nebyla**, takže jsi vlastně první. Když cokoli nefunguje nebo ti něco nedává smysl, napiš mi na LinkedIn a opravím to.

## Co hledáš?

| Potřebuješ | Kam |
|---|---|
| **Stáhnout celou sadu, nebo jeden skill** | [Stažení](#stažení-celé-sady-nebo-jednoho-skillu) |
| **Instaluju poprvé** | [Krok 0](#krok-0-záloha) → [1](#krok-1-stáhni-a-rozbal) → [2](#krok-2-složka-claude-na-správné-místo) → [3](#krok-3-nasdílej-složku-v-aplikaci) → [4](#krok-4-nainstaluj-skilly) → [5](#krok-5-první-spuštění) → [6](#krok-6-ověř-že-to-funguje) |
| **Už mám vlastní složku, skilly nebo nastavení** | [Mám vlastní prostředí](#mám-vlastní-prostředí) |
| **Aktualizuju starší verzi** | [Aktualizace](#aktualizace) |
| **Co je nového a proč to instalovat** | [RELEASE-NOTES.md](RELEASE-NOTES.md) |
| **Co který skill umí a co říct, aby se spustil** | [SKILLS.md](SKILLS.md) |
| **Co je v balíčku** | [Co je v balíčku](#co-je-v-balíčku) |
| **Něco nefunguje** | [Nefunguje něco?](#nefunguje-něco) |

## Krok 0: Záloha

*Jen když už máš na počítači složku `Claude` s vlastními soubory. Nemáš-li, přeskoč.*

Zazipuj ji (Mac: pravý klik, Komprimovat · Windows: pravý klik, Odeslat, Komprimovaná složka), nebo ji zkopíruj na jiné místo (jiný disk, flashka). Trvá to minutu a o nic nepřijdeš, ani kdyby se cokoli pokazilo.

## Krok 1: Stáhni a rozbal

Klikni na **Download package** nahoře. Stáhne se jeden `.zip`. Rozbal ho (dvojklik).

## Krok 2: Složka Claude na správné místo

Složku `Claude/` z balíčku zkopíruj do **Dokumentů** (vznikne `Dokumenty/Claude`). Mac: označ a Cmd + C, v Dokumentech Cmd + V. Windows: Ctrl + C a Ctrl + V; máš-li Dokumenty ve OneDrive, kopíruj tam.

**Proč právě Dokumenty:** složka Dokumenty se většinou zálohuje sama: na Macu přes iCloud Drive (Plocha a Dokumenty) nebo Time Machine, ve Windows přes OneDrive (zálohování složek) nebo Historii souborů. Co leží v `Dokumenty/Claude`, je tedy i zazálohované. Máš-li složku `Claude` už jinde, nech ji tam, jen si ověř, že se zálohuje.

**Windows:** zapni si v Průzkumníku zobrazení přípon souborů (Zobrazit, Zobrazit, Přípony názvů souborů). Jinak se při přejmenování snadno ztratí `.pdf` a soubor se přestane otevírat.

## Krok 3: Nasdílej složku v aplikaci

V aplikaci Claude otevři novou konverzaci a jako pracovní složku vyber `Claude`. Claude vidí jen tuhle složku, takže všechno důležité se ukládá do ní.

## Krok 4: Nainstaluj skilly

Otevři soubor `ai-starter-kit.plugin` (dvojklik, v aplikaci). Všech 12 skillů se nainstaluje najednou. Nejde-li to, nainstaluj soubory ze složky `skills-jednotlive/` po jednom.

## Krok 5: První spuštění

Napiš Claudovi: **„Začínám — spusť onboarding.“** Počítej asi s hodinou, jde přerušit a později navázat. Co se bude dít:

1. Zeptá se, jestli máš Mac, nebo Windows, a kde složka leží.
2. Zjistí, co už máš (skilly, pravidla, seznamy), a navrhne, co ponechat nebo sloučit.
3. Vysvětlí, jak je složka uspořádaná (metoda PARA: projekty, oblasti, zdroje, archiv), a **můžete o ní diskutovat**. Pokud chceš, nechá ti tvoje uspořádání.
4. Navrhne oblasti podle toho, jak žiješ, a dohodnete se na pojmenování souborů.
5. Nabídne převzetí tvých starých souborů (volitelné).
6. Vyplní profil a založí s tebou první projekt. Na konci uloží, kde jste skončili.

Nic nesmaže bez tvého „ano“.

## Krok 6: Ověř, že to funguje

Zkus tři věty:
- **„Jaké skilly mám?“**: ukáže seznam.
- **„Napadlo mě: objednat pneumatiky.“**: zapíše nápad do `INBOX/`.
- Druhý den **„Kde jsem skončil?“**: přečte předání z minula.

Claude se chová, jako by neznal pravidla? Napiš mu: **„Přečti Claude/CLAUDE.md.“**

## Mám vlastní prostředí

*Už máš vlastní složku, skilly nebo nastavení Clauda?* Nic nekopíruj přes ně, přepsalo by ti to tvoje soubory. Místo toho:
1. **Zazálohuj, co máš** (zazipuj složku, nebo ji zkopíruj jinam).
2. **Rozbal balíček** a zkopíruj ho celý do své složky `Claude/INBOX/prevzeti/kit/` (Claude vidí jen nasdílenou složku).
3. **Napiš Claudovi:** „Podívej se na tenhle kit a poraď mi, jak by se dal zapojit do mého stávajícího prostředí. Provedeš mě tím podle onboardingu.“

Claude projde, co už máš (skilly, pravidla, seznamy, soubory), navrhne, co ponechat, co sloučit a co z kitu přidat, a provede tě tím po krocích. Před každou změnou se zeptá, nic nesmaže a tvůj `CLAUDE.md` obohatí o naše pravidla, ne přepíše. Můžeš cokoli odmítnout.

## Aktualizace

*Máš starší verzi sady?*
1. Rozbal nový balíček.
2. V aplikaci **vypni staré přejmenované skilly** (`guard`, `safety`, `inbox`, `model-advisor`, `coach`, `architect`, `planner`), jinak se budou spouštět vedle nových. Seznam, co se jak jmenuje, je v [RELEASE-NOTES.md](RELEASE-NOTES.md).
3. Nainstaluj nové skilly (plugin, nebo `skills-jednotlive/`).
4. Napiš Claudovi: **„Aktualizuj kit.“** Před každou změnou se zeptá a předtím zazálohuje. Tvoje projekty, profil ani to, co jsi napsal(a), nepřepíše.

## Nefunguje něco?

| Problém | Co zkusit |
|---|---|
| Plugin se nenainstaloval | Instaluj `.skill` soubory ze složky `skills-jednotlive/` po jednom. |
| Claude nezná pravidla složky | Napiš: „Přečti Claude/CLAUDE.md.“ |
| Neví, co dál | Napiš: „Kde jsem skončil?“ |
| Nevíš, co Claude umí | Napiš: „Jaké skilly mám?“, nebo se podívej do [SKILLS.md](SKILLS.md). |
| Přestal se otevírat soubor po přejmenování (Windows) | Zapni si zobrazení přípon a vrať příponu. |
| Skript hlásí chybu | Nic neinstaluj. Skilly přejdou na ruční postup a řeknou to. |
| Složka je zmatená po mém zásahu | Claude umí vrátit poslední dávku přesunů („vrať dávku“). |

Nic z toho nepomohlo? Napiš na LinkedIn, ať to můžu opravit.

## Co je v balíčku

| Část | K čemu |
|---|---|
| `Claude/` | šablona pracovní složky: pravidla pro Clauda (`CLAUDE.md`), pět vět na začátek (`START-HERE.md`), profil, složky podle metody PARA a `SYSTEM/` se vším, co spravuje Claude |
| `ai-starter-kit.plugin` | všech 12 skillů najednou |
| `skills-jednotlive/` | totéž po jednom jako `.skill` (když plugin nejde nainstalovat) |
| `README.md`, `RELEASE-NOTES.md` | popis sady, co je nového |
| `RUNBOOK.md` | postup pro toho, kdo sadu někomu předává a provádí ho první hodinou |

Skripty uvnitř skillů potřebují Python 3, pouští je Claude. Když v počítači není, skilly přejdou na ruční postup a řeknou to. Nic neinstaluj jen kvůli nim.

## Dvanáct skillů ve zkratce

Podrobnosti, příklady vět a co který skill **nedělá** jsou v [SKILLS.md](SKILLS.md).

| Skill | K čemu |
|---|---|
| `onboarding` | první spuštění a aktualizace: zjistí, co už máš, navrhne složky, mapu a pojmenování, potom profil a první projekt · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/onboarding.skill) |
| `cleanup` | uklidí složku a převezme staré soubory do nové struktury (po dávkách, jde vrátit) · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/cleanup.skill) |
| `file-guard` | kam soubor uložit a jak ho pojmenovat, před rizikem se zeptá · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/file-guard.skill) |
| `workspace-architect` | projekty, které trvají a mění se, a pohled přes všechny projekty: přehled, kontrola konzistence, „už to někde běží?“ · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/workspace-architect.skill) |
| `project-planner` | projekty, které proběhnou a skončí: fáze, kdo je zapojen, rozhodovací body · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/project-planner.skill) |
| `triage` | roztřídí hromadu úkolů a nápadů (a obsah `INBOX/`) do projektů, oblastí a znalostí; nic nemaže · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/triage.skill) |
| `idea-inbox` | zachytí nápad nebo úkol do 30 sekund, případně rovnou do projektu · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/idea-inbox.skill) |
| `session-close` | konec práce: předání, kde jsi skončil · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/session-close.skill) |
| `basic-security-guard` | co do AI nevkládat, zálohy, kontrola složky na hesla a čísla karet · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/basic-security-guard.skill) |
| `prompt-coach` | pomůže napsat dobré zadání pro Claude a vysvětlí proč · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/prompt-coach.skill) |
| `skill-builder` | vytvoří, upraví a zkontroluje tvůj vlastní skill; projde skilly, které už máš · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/skill-builder.skill) |
| `token-economy` | poradí, na jakém modelu Claude úkol pustit, ať zbytečně nevyčerpáš limit · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/token-economy.skill) |

## Co je nového

Celé release notes jsou v [RELEASE-NOTES.md](RELEASE-NOTES.md). Ve zkratce ve verzi 0.5.2: **máš-li vlastní prostředí, stačí jedna věta pro Clauda** (viz [Mám vlastní prostředí](#mám-vlastní-prostředí)). Ve verzi 0.5.1 přibyla **záloha před zásahem do existující složky** a doporučené místo `Dokumenty/Claude` s vysvětlením.

## Historie verzí

| Verze | Datum | Změna |
|---|---|---|
| 0.5.2 | 2026-10-08 | Jednodušší cesta pro ty, kdo už mají vlastní prostředí: zazálohovat, zkopírovat balíček do své složky a napsat Claudovi, ať poradí, jak kit zapojit. Onboarding na tuhle větu začne auditem. |
| 0.5.1 | 2026-10-08 | Oprava dokumentace: záloha před zásahem do existující složky `Claude`, doporučené místo `Dokumenty/Claude` a proč; onboarding se v prvním kroku zeptá, kde složka leží a zda se zálohuje. |
| 0.5.0 | 2026-10-08 | Audit toho, co už máš, Mac i Windows, nový `cleanup` (převzetí starých souborů), aktualizace jednou větou, přejmenované skilly (`file-guard`, `basic-security-guard`, `idea-inbox`, `token-economy`, `workspace-architect`, `project-planner`), `prompt-coach` v Základu. |
| 0.4.0 | 2026-10-01 | První veřejné vydání. Nový skill `model-advisor`; Základ má 10 skillů. |
