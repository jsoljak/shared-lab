> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit — co je nového

Nejnovější verze je nahoře. Každá verze říká, co se změnilo, **co s tím máš udělat ty** a co zatím nefunguje.

## 0.5.2 — 2026-10-08 (vrstva Základ, 12 skillů)

Jednodušší cesta pro ty, kdo už mají vlastní prostředí. Nic se nepřesouvá a nic se nemění ve tvé složce.

- **Jedna věta pro Clauda místo návodu.** Máš-li už vlastní složku, skilly nebo nastavení, zazálohuj je, zkopíruj rozbalený balíček do své složky `Claude/INBOX/prevzeti/kit/` a napiš: „Podívej se na tenhle kit a poraď mi, jak by se dal zapojit do mého stávajícího prostředí. Provedeš mě tím podle onboardingu.“ Onboarding projde, co máš, navrhne zapojení a před každou změnou se zeptá. Můžeš cokoli odmítnout.
- Onboarding na tuhle větu sám začne auditem tvého prostředí, ne úvodem pro úplné začátečníky.
- **Máš 0.5.1?** Přeinstaluj skilly z nového balíčku, jiné změny tě nečekají.

## 0.5.1 — 2026-10-08 (vrstva Základ, 12 skillů)

Oprava dokumentace a drobné doplnění onboardingu. Nic se nepřesouvá a nic se nemění ve tvé složce.

- **Nejdřív záloha.** README, Info stránka i onboarding teď říkají: máš-li už složku `Claude` s vlastními soubory, zazipuj ji nebo zkopíruj jinam dřív, než cokoli uděláš.
- **Doporučené místo `Dokumenty/Claude`** i s vysvětlením proč: složka Dokumenty se obvykle zálohuje sama (Mac: iCloud Drive nebo Time Machine, Windows: OneDrive nebo Historie souborů). Onboarding se v prvním kroku zeptá, kde složka leží a zda se zálohuje; nenutí, jen poradí.
- **Máš 0.5.0?** Přeinstaluj skilly z nového balíčku a napiš Claudovi „Aktualizuj kit“.

## 0.5.0 — 2026-10-08 (vrstva Základ, 12 skillů)

### Pro koho a co to je

Startovní sada pro práci s Claudem v desktopové aplikaci pro lidi, kteří s AI teprve začínají. Dostaneš uspořádanou pracovní složku `Claude/` a skilly, se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel a pomůže ti napsat dobré zadání i vybrat model, ať nevyčerpáš limit.

### Co je nového

- **Onboarding nejdřív zjistí, co už máš.** Prohlédne tvoje skilly, pravidla a seznamy a navrhne, co ponechat, co sloučit, co rozdělit nebo nahradit skillem z kitu. Nic nepřepíše a nic nesmaže bez tvého „ano“.
- **Onboarding vysvětlí metodu PARA a nechá tě o ní diskutovat.** Ukáže, kam by šly tvoje vlastní věci, rozebere hraniční případy a poctivě řekne, kdy PARA nesedí. Co si domluvíte, se zapíše do mapy složek (sekce Naše dohody), ať se `file-guard` příště neptá znovu.
- **Mac i Windows.** Na začátku se zeptá, na čem pracuješ, a dává ti návody jen pro tvůj systém (kopírování složek, zobrazení přípon souborů, záloha, OneDrive).
- **`workspace-architect` umí i pohled přes všechny projekty:** přehled po oblastech a závislostech, kontrolu konzistence (osiřelé věci, rozbité odkazy, kruhové závislosti) a ověření, jestli už něco podobného neběží, dřív než založíš nový projekt.
- **Jednodušší volba, kdy `workspace-architect` a kdy `project-planner`.** Jedna otázka stejnými slovy („Bude to fungovat dál a měnit se, nebo to proběhne a skončí?“), rozhodne Claude, uživatel žádný skill nevybírá. Pokud se spletlo, druhý skill převezme projekt a zeptá se na nic podruhé.
- **Nový skill `triage`** (třídič): vytřídí hromadu úkolů a nápadů i obsah `INBOX/` do projektů, oblastí a znalostí. Funguje i bez vyšších vrstev: nemá-li skill `wiki`, uloží zdroj přímo do `RESOURCES/sources/`.
- **Nový skill `cleanup`** uklidí složku a **převezme tvoje staré soubory** (Stažené, Plocha, stará škola) do nové struktury: nejdřív zmapuje, navrhne, kam patří, a pak je po dávkách přesune. Každou dávku jde vrátit. Nic nemaže.
- **`skill-builder` umí navíc** projít skilly, které už máš, rozdělit příliš dlouhý skill na hlavní soubor a podklady a sloučit dva skilly, které dělají totéž.
- **Kontrola a doplnění základu jedním příkazem.** Onboarding umí zkontrolovat složky, pravidla a registry a po tvém souhlasu doplnit jen to, co chybí (nic nepřepíše).
- **Tvůj `CLAUDE.md` se nepřepíše, obohatí se.** Vlastní pravidla zůstanou slovo od slova pod „Moje pravidla“, blok kitu se přidá nahoře. Totéž platí pro profil a registry. Máš-li už složku `Claude`, nekopíruj šablonu přes ni (postup je v README).
- **Aktualizace jednou cestou.** Složka teď ví, na jaké je verzi (`SYSTEM/registry/kit-version.md`). Příště napíšeš „aktualizuj kit“ a Claude doplní, co je nového, zazálohuje a nic z tvého neztratí. Žádné samostatné opravné soubory.
- **Tvoje část pravidel se při aktualizaci nepřepisuje.** V `CLAUDE.md` je sekce „Moje pravidla“, v `workspace-rules.md` sekce „Moje výjimky“.
- **`idea-inbox` umí zapsat rovnou do projektu.** Když řekneš, ke kterému projektu věc patří (nebo se právě pracovalo na jednom projektu), zapíše ji do souboru `ideas.md` ve složce projektu. Při příštím navázání ti ji projekt nabídne zpracovat. Nejasné věci jdou dál do `INBOX/`.
- **Lehká učící smyčka.** Claude ti nabídne zapsat do paměti skillu styl práce, když ho opravíš podruhé stejně, a poznatky o tom, co v kitu nefungovalo, zapíše (po tvém souhlasu) do `SYSTEM/registry/feedback-pro-autora.md`. Nic odtud neodchází samo: při „Končím“ nebo „Aktualizuj kit“ ti nabídne sestavit krátkou zprávu pro autora, kterou odešleš ty. Opravy pak přijdou další aktualizací.
- **Skripty fungují i ve Windows** (české znaky se nerozbijí, názvy se hlídají i proti Windows).

### Přejmenované a rozdělené skilly

| Dřív | Teď | Poznámka |
|---|---|---|
| `architect` | `workspace-architect` | projekty typu systém a pohled přes všechny projekty |
| `planner` | `project-planner` | projekty typu proces: fáze, rozhodovací body |
| `guard` | `file-guard` | hlídá, kam se soubor uloží a jak se jmenuje |
| `safety` | `basic-security-guard` | co nevkládat do AI, zálohy, kontrola hesel |
| `inbox` | `idea-inbox` | rychlý zápis nápadu |
| `model-advisor` | `token-economy` | na jakém modelu úkol pustit |
| `coach` | `prompt-coach` | psaní zadání pro Claude |

### Máš starší verzi? Jak aktualizovat

1. Rozbal nový balíček.
2. V aplikaci **vypni (odinstaluj) staré přejmenované skilly** (`guard`, `safety`, `inbox`, `model-advisor`, `coach`, `architect`, `planner`), jinak se budou spouštět vedle nových. Nové nainstaluj ze souboru `ai-starter-kit.plugin` (nejde-li to, ze složky `skills-jednotlive/`).
3. Napiš Claudovi: **„Aktualizuj kit.“** Postupuje po krocích, před každou změnou se zeptá a předtím zazálohuje.

Poctivě: je to první aktualizace tímto způsobem a nikdo ji zatím na cizím účtu nezkoušel. Kdyby něco nešlo, napiš autorovi.

### Známá omezení

- Sada **nebyla zkoušena na cizím účtu**. Soubory a skripty jsou zkontrolované, ale nainstalování v aplikaci a chování na Windows ukáže teprve první použití.
- V aplikaci nejsou hooky ani git: pravidla drží `CLAUDE.md` a skilly, a jen když se jimi Claude řídí.
- Skripty potřebují Python 3. Není-li k dispozici, skilly přejdou na ruční postup a řeknou to.
- Další skilly (například znalostní báze a přehledy) přijdou v další vrstvě.

## 0.4.0 — 2026-10-01 (vrstva Základ, 10 skillů)

První veřejné vydání. Uspořádaná pracovní složka (metoda PARA), onboarding, `workspace-architect`, `project-planner`, `guard`, `inbox`, `session-close`, `safety`, `coach`, `skill-builder` a `model-advisor`.
