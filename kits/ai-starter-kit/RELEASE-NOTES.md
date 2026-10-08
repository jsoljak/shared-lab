> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit: co je v téhle verzi

## 0.5.4 — 2026-10-08 (vrstva Základ, 12 skillů)

Doplněná historie vývoje: release notes od první verze, ať je vidět, jak sada postupně vznikala. Žádná změna v chování skillů. Máš 0.5.3? Přeinstalovávat nic nemusíš.

## 0.5.3 — 2026-10-08 (vrstva Základ, 12 skillů)

### Co to je

Startovní sada pro práci s Claudem v desktopové aplikaci pro lidi, kteří s AI teprve začínají. Dostaneš uspořádanou pracovní složku `Claude/` a skilly (pomocníky), se kterými si v ní postavíš cokoli: systém, proces nebo osobní projekt. Claude si pamatuje, kde jsi skončil, ukládá a pojmenovává soubory podle pravidel a pomůže ti napsat dobré zadání i vybrat model, ať nevyčerpáš limit. Funguje na Macu i na Windows.

### Co umí

- **Onboarding** zjistí, co už máš (skilly, pravidla, seznamy), vysvětlí metodu PARA a můžete o ní diskutovat, navrhne složky, mapu a pojmenování podle toho, jak žiješ, a provede tě prvním projektem. Můžeš kitovou strukturu odmítnout a nechat si svoje uspořádání. Tvůj `CLAUDE.md` se nepřepíše, obohatí se o naše pravidla.
- **Máš už vlastní prostředí?** Zazálohuj ho, zkopíruj balíček do své složky `Claude/INBOX/prevzeti/kit/` a napiš Claudovi: „Podívej se na tenhle kit a poraď mi, jak by se dal zapojit do mého stávajícího prostředí. Provedeš mě tím podle onboardingu.“
- **`cleanup`** uklidí složku a převezme tvoje staré soubory (Stažené, Plocha) do nové struktury po dávkách. Každou dávku jde vrátit. Nic nemaže.
- **`file-guard`** hlídá, kam se soubor uloží a jak se jmenuje.
- **`workspace-architect`** vede projekty, které trvají a mění se, a umí pohled přes všechny projekty: přehled, kontrola konzistence, „už to někde běží?“. **`project-planner`** vede projekty, které proběhnou a skončí. Při založení projektu se Claude zeptá jednou: „Bude to fungovat dál a měnit se, nebo to proběhne a skončí?“
- **`idea-inbox`** zachytí nápad za pár sekund, případně rovnou do projektu. **`triage`** vytřídí hromadu věcí. **`session-close`** uloží, kde jsi skončil.
- **`basic-security-guard`** hlídá, co nevkládat do AI, a umí zkontrolovat složku na hesla a čísla karet. **`token-economy`** poradí, na jakém modelu úkol pustit.
- **`prompt-coach`** pomůže napsat dobré zadání pro Claude. **`skill-builder`** pomůže vytvořit vlastní skill a projít ty, které už máš.
- **Záloha a umístění:** onboarding doporučí složku `Dokumenty/Claude` (Dokumenty se obvykle zálohují přes iCloud nebo OneDrive) a zeptá se, jestli se zálohuje.
- **Poznámky pro autora:** co v kitu nefungovalo, si Claude (po tvém souhlasu) zapíše do jednoho souboru a ty ho pošleš, kdy budeš chtít.
- **Aktualizace jednou větou:** až vyjde nová verze, napíšeš „Aktualizuj kit“ a Claude zazálohuje, ukáže změny a před každou se zeptá. Tvoje projekty, profil a pravidla nepřepíše.

### Známá omezení

- Sada **nebyla zkoušena na cizím účtu** a nikdo ji zatím nevyzkoušel na Windows. Soubory a skripty jsou zkontrolované, ale instalace v aplikaci a chování ukáže teprve první použití.
- V aplikaci nejsou hooky ani git: pravidla drží `CLAUDE.md` a skilly, a jen když se jimi Claude řídí.
- Skripty potřebují Python 3 (pouští je Claude). Není-li k dispozici, skilly přejdou na ruční postup a řeknou to.
- Další skilly (například znalostní báze a přehledy) přijdou v další vrstvě.

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

- **Onboarding nejdřív zjistí, co už máš.** Prohlédne tvoje skilly, pravidla a seznamy a navrhne, co ponechat, co sloučit, co rozdělit nebo doplnit skillem z kitu. Nic nepřepíše a nic nesmaže bez tvého „ano“.
- **Onboarding vysvětlí metodu PARA a nechá tě o ní diskutovat.** Ukáže, kam by šly tvoje vlastní věci, rozebere hraniční případy a poctivě řekne, kdy PARA nesedí. Co si domluvíte, se zapíše do mapy složek (sekce Naše dohody), ať se `file-guard` příště neptá znovu.
- **Mac i Windows.** Na začátku se zeptá, na čem pracuješ, a dává ti návody jen pro tvůj systém (kopírování složek, zobrazení přípon souborů, záloha, OneDrive).
- **`workspace-architect` umí i pohled přes všechny projekty:** přehled po oblastech a závislostech, kontrolu konzistence (osiřelé věci, rozbité odkazy, kruhové závislosti) a ověření, jestli už něco podobného neběží, dřív než založíš nový projekt.
- **Jednodušší volba, kdy `workspace-architect` a kdy `project-planner`.** Jedna otázka stejnými slovy („Bude to fungovat dál a měnit se, nebo to proběhne a skončí?“), rozhodne Claude, uživatel žádný skill nevybírá. Pokud se spletlo, druhý skill převezme projekt a zeptá se na nic podruhé.
- **`triage`** (třídič): vytřídí hromadu úkolů a nápadů i obsah `INBOX/` do projektů, oblastí a znalostí. Funguje i bez vyšších vrstev: nemá-li skill `wiki`, uloží zdroj přímo do `RESOURCES/sources/`.
- **`cleanup`** uklidí složku a **převezme tvoje staré soubory** (Stažené, Plocha, stará škola) do nové struktury: nejdřív zmapuje, navrhne, kam patří, a pak je po dávkách přesune. Každou dávku jde vrátit. Nic nemaže.
- **`skill-builder`** umí projít skilly, které už máš, rozdělit příliš dlouhý skill na hlavní soubor a podklady a sloučit dva skilly, které dělají totéž.
- **Kontrola a doplnění základu jedním příkazem.** Onboarding umí zkontrolovat složky, pravidla a registry a po tvém souhlasu doplnit jen to, co chybí (nic nepřepíše).
- **Tvůj `CLAUDE.md` se nepřepíše, obohatí se.** Vlastní pravidla zůstanou slovo od slova pod „Moje pravidla“, blok kitu se přidá nahoře. Totéž platí pro profil a registry. Máš-li už složku `Claude`, nekopíruj šablonu přes ni (postup je v README).
- **Aktualizace jednou cestou.** Složka teď ví, na jaké je verzi (`SYSTEM/registry/kit-version.md`). Příště napíšeš „aktualizuj kit“ a Claude doplní, co je nového, zazálohuje a nic z tvého neztratí.
- **Tvoje část pravidel se při aktualizaci nepřepisuje.** V `CLAUDE.md` je sekce „Moje pravidla“, v `workspace-rules.md` sekce „Moje výjimky“.
- **`idea-inbox` umí zapsat rovnou do projektu.** Když řekneš, ke kterému projektu věc patří (nebo se právě pracovalo na jednom projektu), zapíše ji do souboru `ideas.md` ve složce projektu. Při příštím navázání ti ji projekt nabídne zpracovat. Nejasné věci jdou dál do `INBOX/`.
- **Lehká učící smyčka.** Claude ti nabídne zapsat do paměti skillu styl práce, když ho opravíš podruhé stejně, a poznatky o tom, co v kitu nefungovalo, zapíše (po tvém souhlasu) do `SYSTEM/registry/feedback-pro-autora.md`. Nic odtud neodchází samo: při „Končím“ nebo „Aktualizuj kit“ ti nabídne sestavit krátkou zprávu pro autora, kterou odešleš ty. Opravy pak přijdou další aktualizací.
- **Skripty fungují i ve Windows** (české znaky se nerozbijí, názvy se hlídají i proti Windows).

### Známá omezení

- Sada **nebyla zkoušena na cizím účtu**. Soubory a skripty jsou zkontrolované, ale nainstalování v aplikaci a chování na Windows ukáže teprve první použití.
- V aplikaci nejsou hooky ani git: pravidla drží `CLAUDE.md` a skilly, a jen když se jimi Claude řídí.
- Skripty potřebují Python 3. Není-li k dispozici, skilly přejdou na ruční postup a řeknou to.
- Další skilly (například znalostní báze a přehledy) přijdou v další vrstvě.
