> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-11-08

# AI Starter Kit — Základ

> **Sada: 13 skillů + šablona pracovní složky** · verze **0.8.1** · česky · Mac i Windows · [**⬇ Download package** (.zip)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-8-1__2026-11-08.zip)

Startovní sada pro práci s Claudem v desktopové aplikaci (Cowork) pro lidi, kteří s AI teprve začínají. Dá ti **jednu uspořádanou pracovní složku** a skilly (pomocníky), se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel, pomůže ti napsat dobré zadání i vybrat model, ať nevyčerpáš limit. Umí také **uklidit a převzít tvoje staré soubory** a zjistit, co už máš.

## Stažení celé sady nebo jednoho skillu

**Nepotřebuješ GitHub ani účet.** Klikni na odkaz, soubor se stáhne do složky Stažené. (Nepoužívej zelené tlačítko **Code** na stránce repa, to stáhne celé repo s věcmi, které nepotřebuješ.)

- **⬇ Celá sada, jeden soubor** (13 skillů + šablona složky Claude + návody): [ai-starter-kit__package__zaklad-v0-8-1__2026-11-08.zip](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__zaklad-v0-8-1__2026-11-08.zip). Doporučuju tuhle možnost, jedině s ní dostaneš složku s mapou a pravidly, na kterých skilly stojí.
- **⬇ Jeden skill zvlášť** (zkusit si jen jeden, nebo přeinstalovat jeden): tabulka níže u každého skillu, nebo [SKILLS.md](SKILLS.md). Soubor `.skill` se stáhne do Stažených. Nahraješ ho v aplikaci: **Customize** → **Skills** → **+** → **Upload skill** a vybereš ho ve Stažených. Do okna chatu ho nedávej. Kdyby aplikace chtěla `.zip`, přejmenuj příponu `.skill` na `.zip`.

## Co potřebuješ

- desktopovou aplikaci Claude (Cowork) a přihlášený účet; aplikaci stahuj jen z [claude.ai/download](https://claude.ai/download), ne z App Storu ani odjinud,
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
| **Instaluju poprvé** | [Nejdřív jedno pravidlo](#nejdřív-jedno-pravidlo-nic-nedávej-do-okna-chatu) → [Krok 0](#krok-0-záloha) → [1](#krok-1-stáhni-a-rozbal) → [2](#krok-2-složka-claude-na-správné-místo) → [3](#krok-3-nasdílej-složku-v-aplikaci) → [4](#krok-4-nainstaluj-skilly) → [5](#krok-5-první-spuštění) → [6](#krok-6-ověř-že-to-funguje) |
| **Už mám vlastní složku, skilly nebo nastavení** | [Mám vlastní prostředí](#mám-vlastní-prostředí) |
| **Aktualizace, až vyjde nová verze** | [Aktualizace](#aktualizace) |
| **Druhý mozek: wiki, Obsidian a Web Clipper** | [WIKI-OBSIDIAN.md](WIKI-OBSIDIAN.md) (co to je, instalace, synchronizace, limity) |
| **Rozšíření Pokročilé (víc projektů najednou)** | [Pokročilé](#pokročilé-rozšíření-základu) |
| **Chci všechno anglicky** | [Anglicky](#chceš-všechno-anglicky) |
| **Co je nového a proč to instalovat** | [RELEASE-NOTES.md](RELEASE-NOTES.md) |
| **Co který skill umí a co říct, aby se spustil** | [SKILLS.md](SKILLS.md) |
| **Co je v balíčku** | [Co je v balíčku](#co-je-v-balíčku) |
| **Něco nefunguje** | [Nefunguje něco?](#nefunguje-něco) |

## Nejdřív jedno pravidlo: nic nedávej do okna chatu

Stažené soubory (zip, `.plugin`, `.skill`) **nepřetahuj do okna konverzace s Claudem a nepřikládej je ke zprávě.** Claude by je jen četl, nic by se nenainstalovalo a zbytečně by to bralo limit předplatného. Všechno se dělá ve Finderu (Mac) nebo v Průzkumníku (Windows) a v nastavení aplikace, přesně podle kroků níže. Do okna chatu jen **píšeš věty** (od kroku 5).

## Krok 0: Záloha

*Jen když už máš na počítači složku `Claude` s vlastními soubory. Nemáš-li, přeskoč.*

Zazipuj ji (Mac: pravý klik na složku, **Komprimovat** · Windows: pravý klik, **Odeslat**, **Komprimovaná složka**), nebo ji zkopíruj na jiné místo (jiný disk, flashka). Trvá to minutu a o nic nepřijdeš, ani kdyby se cokoli pokazilo.

## Krok 1: Stáhni a rozbal

1. Klikni na odkaz **⬇ Download package** nahoře. Stáhne se jeden soubor `.zip` do složky **Stažené** (Mac: Finder, vlevo **Stažené** · Windows: Průzkumník, vlevo **Stažené soubory**).
2. **Rozbal ho přímo ve Stažených.** Mac: dvojklik na zip. Windows: pravý klik na zip, **Extrahovat vše**, **Extrahovat**. Vedle zipu vznikne složka se stejným jménem.
3. Otevři tu složku. Uvidíš tohle a s každou věcí uděláš jen to, co je v tabulce:

| Co ve složce vidíš | Co s tím uděláš |
|---|---|
| složka `Claude` | zkopíruješ do Dokumentů ([krok 2](#krok-2-složka-claude-na-správné-místo)) |
| soubor `ai-starter-kit.plugin` | nahraješ do aplikace Claude ([krok 4](#krok-4-nainstaluj-skilly)) |
| složka `skills-jednotlive` | nic. Jen kdyby plugin nešel nahrát (krok 4, odstavec „Ani to nešlo?“) |
| `README.md`, `RELEASE-NOTES.md`, `RUNBOOK.md`, `WIKI-OBSIDIAN.md` | nic, jsou to návody ke čtení |

Zip i rozbalená složka **zůstávají ve Stažených**. Nikam jinam je nekopíruj (výjimka: [Mám vlastní prostředí](#mám-vlastní-prostředí) a [Aktualizace](#aktualizace)).

## Krok 2: Složka Claude na správné místo

Zkopíruj **jen složku `Claude`** z rozbalené složky do **Dokumentů**. Vznikne `Dokumenty/Claude`.

- **Mac:** ve Finderu klikni na složku `Claude`, stiskni **Cmd + C**. Vlevo klikni na **Dokumenty** a stiskni **Cmd + V**.
- **Windows:** v Průzkumníku klikni na složku `Claude`, stiskni **Ctrl + C**. Vlevo klikni na **Dokumenty** (máš-li je ve OneDrive, tak tam) a stiskni **Ctrl + V**.

**Proč právě Dokumenty:** složka Dokumenty se většinou zálohuje sama: na Macu přes iCloud Drive (Plocha a Dokumenty) nebo Time Machine, ve Windows přes OneDrive (zálohování složek) nebo Historii souborů. Co leží v `Dokumenty/Claude`, je tedy i zazálohované. Desktopová aplikace pracuje se složkou `Dokumenty/Claude` sama, v nastavení se nic nenastavuje (jinou domovskou složku zvolit nejde). Máš-li složku `Claude` s vlastními soubory už jinde, nepřesouvej ji naslepo: postupuj podle [Mám vlastní prostředí](#mám-vlastní-prostředí).

**Mac s iCloudem (Plocha a Dokumenty):** ve Finderu klikni na složku `Claude` pravým tlačítkem a zvol **Vždy ponechat na tomto zařízení**, jinak ji iCloud při nedostatku místa z Macu odloží a Claude soubory nepřečte. A pozor: **iCloud není záloha.** Smazaný soubor zmizí i z iCloudu, proto měj ještě Time Machine nebo jinou kopii.

**Windows:** zapni si v Průzkumníku zobrazení přípon souborů (**Zobrazit**, **Zobrazit**, **Přípony názvů souborů**). Budeš je potřebovat v kroku 4 a jinak se při přejmenování snadno ztratí třeba `.pdf`.

## Krok 3: Nasdílej složku v aplikaci

V aplikaci Claude otevři novou konverzaci v **Coworku** a jako pracovní složku vyber **Dokumenty → Claude**. Claude vidí jen tuhle složku, takže všechno důležité se ukládá do ní. macOS se poprvé zeptá, jestli aplikace smí do složky Dokumenty: povol.

## Krok 4: Nainstaluj skilly

Skilly se instalují **v nastavení aplikace**, ne v chatu. Nahrává se **jen soubor `ai-starter-kit.plugin`**, ne celý stažený zip (ten k nahrání určený není).

1. V aplikaci Claude klikni vlevo v panelu na **Customize**. Máš-li nahoře přepínač Chat / Cowork, přepni nejdřív na **Cowork**.
2. Klikni na záložku **Plugins**.
3. Klikni na **Add** a pak na **Upload plugin**.
4. Otevře se okno pro výběr souboru. Jdi do **Stažené**, otevři rozbalenou složku a vyber soubor **`ai-starter-kit.plugin`**. Klikni na **Otevřít**.
5. Aplikace upozorní, že nahraný plugin nepochází od Anthropicu. Potvrď.
6. Hotovo: všech 13 skillů je nainstalovaných najednou. Ověříš to v kroku 6.

**U pluginu neklikej na tlačítko „Customize“** (vpravo nahoře, když plugin otevřeš). To spustí úkol, ve kterém Claude plugin upravuje, a bere to limit. K instalaci ho nepotřebuješ.

**Aplikace soubor nevzala?** Přejmenuj `ai-starter-kit.plugin` na `ai-starter-kit.zip` a nahraj ho znovu stejným postupem. Uvnitř je totéž. Mac: klikni na soubor, stiskni **Enter**, přepiš konec názvu na `.zip`, potvrď **Použít .zip**. Windows: pravý klik, **Přejmenovat** (přípony musíš mít zapnuté, krok 2).

**Ani to nešlo?** Nahraj skilly po jednom: **Customize** → **Skills** → **+** → **Upload skill** (může se jmenovat i **Create skill**, pak **Upload a skill**) a vyber jeden soubor ze složky `skills-jednotlive`. Zopakuj pro všech 13 souborů.

*Názvy tlačítek se podle verze aplikace můžou trochu lišit. Hledej vždy **Customize** vlevo a v něm nahrání (Upload).*

## Krok 5: První spuštění

Do okna chatu napiš: **„Začínám — spusť onboarding.“** Počítej asi s hodinou a čtvrt. Claude tě vede krok za krokem: po každém kroku řekne, co bude dál, a zeptá se, jestli pokračovat. Přestat můžeš kdykoli, zapamatuje si, kde jste skončili. Co se bude dít:

1. Zeptá se, jestli máš Mac, nebo Windows, a kde složka leží.
2. Projde s tebou nastavení soukromí v aplikaci (asi 5 minut): učení modelů na tvých chatech, paměť aplikace, konektory. Rozhoduješ ty.
3. Zjistí, co už máš (skilly, pravidla, seznamy), a navrhne, co ponechat nebo sloučit.
4. Vysvětlí, jak je složka uspořádaná (metoda PARA: projekty, oblasti, zdroje, archiv), rozdíl mezi projektem a oblastí ukáže **na tvých věcech** a **můžete o tom diskutovat**. Pokud chceš, nechá ti tvoje uspořádání.
5. Navrhne oblasti podle toho, jak žiješ (názvy česky, nebo anglicky, vybereš si), a dohodnete se na pojmenování souborů.
6. Nabídne převzetí tvých starých souborů (volitelné).
7. Vyplní profil a založí s tebou první projekt.
8. Ukáže ti skilly, které máš, vždycky na tvé věci: ty napíšeš jednu větu a uvidíš, co skill udělá. Dva až tři hned, zbytek kdykoli příště.
9. Na konci uloží, kde jste skončili. Přerušíš-li to dřív, příště napiš **„Kde jsem skončil?“** a pokračuje se tam, kde jste přestali.
10. Za pár dní ti nabídne **týdenní přehled „Jak používám systém?“**: co ti jde, co zlepšit a jestli by se ti na něco nehodil vlastní skill. Na placeném plánu tě provede založením naplánované úlohy v aplikaci, jinak ti to jednou týdně připomene.

Nic nesmaže bez tvého „ano“.

## Krok 6: Ověř, že to funguje

Zkus tři věty:
- **„Jaké skilly mám?“**: ukáže seznam.
- **„Napadlo mě: objednat pneumatiky.“**: zapíše nápad do `INBOX/`.
- Druhý den **„Kde jsem skončil?“**: přečte předání z minula.

Claude se chová, jako by neznal pravidla? Do okna chatu napiš: **„Přečti Claude/CLAUDE.md.“**

## Mám vlastní prostředí

*Už máš vlastní složku `Claude`, skilly nebo nastavení Clauda?* Nic nekopíruj přes ně, přepsalo by ti to tvoje soubory. Místo toho:

1. **Zazálohuj, co máš** ([krok 0](#krok-0-záloha)).
2. **Stáhni zip a rozbal ho ve Stažených** ([krok 1](#krok-1-stáhni-a-rozbal), body 1 a 2).
3. **Vytvoř složku `kit` v INBOXu.** Ve Finderu nebo v Průzkumníku otevři `Dokumenty` → `Claude` → `INBOX`. Klikni do prázdného místa pravým tlačítkem a vytvoř novou složku (Mac: **Nová složka** · Windows: **Nový**, **Složka**). Pojmenuj ji `kit`, malými písmeny. Výsledek: `Dokumenty/Claude/INBOX/kit`. Víc podsložek nevytvářej.
4. **Zkopíruj do složky `kit` všechno z rozbalené složky** (`Claude`, `ai-starter-kit.plugin`, `skills-jednotlive`, návody). Otevři rozbalenou složku ve Stažených, označ všechno (**Cmd + A** / **Ctrl + A**), zkopíruj (**Cmd + C** / **Ctrl + C**), otevři složku `kit` a vlož (**Cmd + V** / **Ctrl + V**). Proč: Claude vidí jen složku `Claude`, ze Stažených kit nepřečte.
5. **Do okna chatu napiš:** „Podívej se na tenhle kit a poraď mi, jak by se dal zapojit do mého stávajícího prostředí. Provedeš mě tím podle onboardingu.“

Claude projde, co už máš (skilly, pravidla, seznamy, soubory), navrhne, co ponechat, co sloučit a co z kitu přidat, a provede tě tím po krocích, včetně toho, kdy nahrát plugin ([krok 4](#krok-4-nainstaluj-skilly)). Před každou změnou se zeptá, nic nesmaže a tvůj `CLAUDE.md` obohatí o naše pravidla, ne přepíše. Můžeš cokoli odmítnout.

## Aktualizace

*Až vyjde nová verze sady a kit už máš:*

1. **Stáhni nový zip a rozbal ho ve Stažených** ([krok 1](#krok-1-stáhni-a-rozbal), body 1 a 2).
2. **Vyměň složku `kit`.** Otevři `Dokumenty` → `Claude` → `INBOX`. Je-li tam složka `kit` ze starší verze, smaž ji. Vytvoř novou prázdnou složku `kit` a zkopíruj do ní všechno z nové rozbalené složky, stejně jako v [Mám vlastní prostředí](#mám-vlastní-prostředí), body 3 a 4. **Pozor:** nic nekopíruj přímo do `Dokumenty/Claude` ani přes ni, přepsal(a) by sis svoje soubory.
3. **Nahraj nový plugin** jako v [kroku 4](#krok-4-nainstaluj-skilly): **Customize** → **Plugins** → **Add** → **Upload plugin** → `ai-starter-kit.plugin` ze složky `kit`. Vidíš-li pak v **Plugins** sadu dvakrát, starší odeber.
4. **Do okna chatu napiš:** „Aktualizuj kit.“ Claude si nový kit vezme ze složky `kit`, před každou změnou se zeptá a předtím zazálohuje. Tvoje projekty, profil, pravidla ani to, co jsi napsal(a), nepřepíše.

Složku `kit` můžeš po aktualizaci nechat, kde je. Claude ani úklid na ni nesahají a při další verzi ji jen vyměníš.

## Pokročilé: rozšíření Základu

Až ti Základ začne být těsný (víc projektů najednou, víc věcí na sebe čeká), přidej **Pokročilé**: samostatný balíček, který se instaluje k Základu a nepřepíše ho. **Instalace:** stáhni zip, rozbal ho ve Stažených a v aplikaci nahraj **jen soubor `ai-starter-kit-pokrocile.plugin`** stejně jako v [kroku 4](#krok-4-nainstaluj-skilly). Do složky `Claude` se z tohoto balíčku nic nekopíruje. Každý skill v něm říká, který skill Základu rozšiřuje, co přidává a **kdy ho ještě nepotřebuješ**. Skilly budou postupně přibývat.

- **⬇ Balíček Pokročilé** (potřebuje Základ 0.7.0 nebo novější): [ai-starter-kit__package__pokrocile-v0-8-1__2026-11-08.zip](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/ai-starter-kit__package__pokrocile-v0-8-1__2026-11-08.zip). Uvnitř je README s tabulkou „co přidává“.

| Skill | Rozšiřuje | Co přidává | Kdy ho ještě nepotřebuješ |
|---|---|---|---|
| `work-graph` | `project-planner`, `workspace-architect` | graf práce napříč projekty: kroky, kdo je drží, na co čekají; „Co je volné?“ a „Na čem to stojí?“; záloha před každým zápisem · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/work-graph.skill) | máš jeden nebo dva projekty |

## Chceš všechno anglicky?

Kit je napsaný česky. Nejdřív zkopíruj rozbalený balíček do složky `Dokumenty/Claude/INBOX/kit` (jako v [Mám vlastní prostředí](#mám-vlastní-prostředí), body 3 a 4; Claude z něj bere skilly k převodu). Pak do okna chatu napiš **„Chci všechno anglicky“** (nebo „Switch everything to English“): `onboarding` převede profil, úvodní soubor a skilly do angličtiny a předem řekne, co záměrně nechá česky (soubory, které čtou skripty). Všechno nejdřív zazálohuje. Anglické skilly ti připraví k instalaci. Po každé aktualizaci kitu se převod nabídne znovu, protože aktualizace vrátí české verze skillů.

## Nefunguje něco?

| Problém | Co zkusit |
|---|---|
| Plugin se nenainstaloval | Nahrával(a) jsi jen soubor `ai-starter-kit.plugin`, ne celý zip? Zkus ho přejmenovat na `.zip`, nebo nahraj skilly po jednom ([krok 4](#krok-4-nainstaluj-skilly), konec). |
| Dal(a) jsem soubory do okna chatu | Nic se nestalo, jen se nic nenainstalovalo. Instaluj podle [kroku 4](#krok-4-nainstaluj-skilly). |
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
| `ai-starter-kit.plugin` | všech 13 skillů najednou; nahrává se v aplikaci přes **Customize** → **Plugins** → **Upload plugin** |
| `skills-jednotlive/` | totéž po jednom jako `.skill` (když plugin nejde nainstalovat) |
| `README.md`, `RELEASE-NOTES.md` | popis sady, co je nového |
| `WIKI-OBSIDIAN.md` | návod na druhý mozek: wiki, Obsidian, Web Clipper, synchronizace |
| `RUNBOOK.md` | postup pro toho, kdo sadu někomu předává a provádí ho první hodinou |

Skripty uvnitř skillů potřebují Python 3, pouští je Claude. Když v počítači není, skilly přejdou na ruční postup a řeknou to. Nic neinstaluj jen kvůli nim.

## Třináct skillů ve zkratce

Podrobnosti, příklady vět a co který skill **nedělá** jsou v [SKILLS.md](SKILLS.md).

| Skill | K čemu |
|---|---|
| `onboarding` | první spuštění a aktualizace: zjistí, co už máš, navrhne složky, mapu a pojmenování, potom profil, první projekt a prohlídku skillů; vede tě celou dobu a pamatuje si, kde jsi skončil · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/onboarding.skill) |
| `cleanup` | uklidí složku a převezme staré soubory do nové struktury (po dávkách, jde vrátit) · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/cleanup.skill) |
| `file-guard` | kam soubor uložit a jak ho pojmenovat, před rizikem se zeptá · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/file-guard.skill) |
| `workspace-architect` | projekty, které trvají a mění se, a pohled přes všechny projekty: přehled, kontrola konzistence, „už to někde běží?“ · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/workspace-architect.skill) |
| `project-planner` | projekty, které proběhnou a skončí: fáze, kdo je zapojen, rozhodovací body · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/project-planner.skill) |
| `triage` | roztřídí hromadu úkolů a nápadů (a obsah `INBOX/`) do projektů, oblastí a znalostí; nic nemaže · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/triage.skill) |
| `wiki` | druhý mozek: ukládá články a poznámky, sepisuje z nich propojené stránky a odpovídá jen z nich; čte se i v Obsidianu ([návod](WIKI-OBSIDIAN.md)) · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/wiki.skill) |
| `idea-inbox` | zachytí nápad nebo úkol do 30 sekund, případně rovnou do projektu · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/idea-inbox.skill) |
| `session-close` | konec práce: předání, kde jsi skončil · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/session-close.skill) |
| `basic-security-guard` | co do AI nevkládat, zálohy, nastavení soukromí, kontrola složky na hesla a čísla karet a kontrola staženého souboru nebo cizího skillu na skryté pokyny pro AI · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/basic-security-guard.skill) |
| `prompt-coach` | pomůže napsat dobré zadání pro Claude a vysvětlí proč · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/prompt-coach.skill) |
| `skill-builder` | vytvoří, upraví a zkontroluje tvůj vlastní skill; projde skilly, které už máš · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/skill-builder.skill) |
| `token-economy` | poradí, na jakém modelu Claude úkol pustit, ať zbytečně nevyčerpáš limit · [⬇](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/token-economy.skill) |

## Co je v téhle verzi

**0.8.1:** onboarding tě vede celým začátkem a pamatuje si, kde jsi skončil(a), ukáže ti skilly na tvých věcech a po pár dnech nabídne týdenní přehled „Jak používám systém?“. Návod krok za krokem (co kam dát, čím to otevřít, nic do okna chatu), instalace přes Customize → Plugins a nová verze kitu do `Claude/INBOX/kit/`.

**0.8.0:** Claude bere cizí obsah (stažené soubory, e-maily, weby, cizí skilly) jako data, ne příkazy; `basic-security-guard` umí soubor nebo skill zvenku zkontrolovat na skryté pokyny. Onboarding nově projde nastavení soukromí v aplikaci a na Macu poradí s iCloudem. `token-economy` zná modely z listopadu 2026 a radí, jak předejít vymýšlení. Máš starší verzi? Viz [Aktualizace](#aktualizace).

Celé release notes jsou v [RELEASE-NOTES.md](RELEASE-NOTES.md). Co který skill umí, je v [SKILLS.md](SKILLS.md).

## Verze

| Verze | Datum | Změna |
|---|---|---|
| 0.8.1 | 2026-11-08 | Onboarding vede celým cyklem (po každém kroku další, pamatuje si, kde jsi skončil), prohlídka skillů na tvých věcech, po pár dnech týdenní přehled „Jak používám systém?“, názvy oblastí česky, nebo anglicky. Návod krok za krokem: co kam dát a čím to otevřít, nic do okna chatu; skilly se nahrávají přes Customize → Plugins → Upload plugin; nová verze kitu patří do `Claude/INBOX/kit/` a úklid ji přeskakuje. 13 skillů v Základu, 1 v Pokročilých. |
| 0.8.0 | 2026-11-07 | Ochrana před cizím obsahem: pravidlo v `CLAUDE.md` a nový režim CIZÍ OBSAH v `basic-security-guard` (kontrola souboru a cizího skillu). Onboarding: nastavení soukromí v aplikaci, iCloud na Macu. `token-economy` podle modelů 11/2026. 13 skillů v Základu, 1 v Pokročilých. |
| 0.7.0 | 2026-10-22 | Nová vrstva Pokročilé jako rozšíření Základu, první skill `work-graph` (graf práce napříč projekty). Základ: celý kit v angličtině přes `onboarding`, volitelný plný zápis rozhodnutí ve `workspace-architect`. 13 skillů v Základu, 1 v Pokročilých. |
| 0.6.0 | 2026-10-21 | Nový skill `wiki` (druhý mozek podle Karpathyho) a návod na Obsidian a Web Clipper; `skill-builder` před stavbou ověří, jestli podobný skill už neexistuje. 13 skillů. |
| 0.5.4 | 2026-10-08 | Doplněná historie vývoje (release notes od verze 0.5.0). Žádná změna v chování skillů. |
| 0.5.3 | 2026-10-08 | Přehledná dokumentace: README s navigací, popis každého skillu, každý skill ke stažení zvlášť. |
| 0.5.2 | 2026-10-08 | Jednodušší cesta pro ty, kdo už mají vlastní prostředí: zazálohovat, zkopírovat balíček do své složky a napsat Claudovi, ať poradí, jak kit zapojit. |
| 0.5.1 | 2026-10-08 | Záloha před zásahem do existující složky `Claude`, doporučené místo `Dokumenty/Claude` a proč; onboarding se zeptá, kde složka leží a zda se zálohuje. |
| 0.5.0 | 2026-10-08 | První vydání sady v dnešní podobě: audit toho, co už máš, Mac i Windows, `cleanup` (převzetí starých souborů), aktualizace jednou větou, 12 skillů. |
