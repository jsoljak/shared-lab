> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-11-08

# AI Starter Kit: co je v téhle verzi

## 0.8.1 — 2026-11-08 (Základ 13 skillů, Pokročilé 1 skill)

**Onboarding tě vede celou dobu.** Po každém kroku řekne, co bude dál, a zeptá se, jestli pokračovat; nikdy neskončí naprázdno. Když odbočíš (otázka mimo, chceš rozebrat profil), krátce odpoví a vrátí se: „Vracím se ke kroku 4: …“. Kde jsi, si průběžně zapisuje do předání (`SYSTEM/registry/session-brain.md`, sekce Onboarding), takže můžeš kdykoli přestat. Příště stačí napsat **„Kde jsem skončil?“** a pokračuje se tam, kde jste přestali.

**Projekty a oblasti na tvých věcech, názvy česky, nebo anglicky.** Při zakládání složek Claude vysvětlí rozdíl dvěma větami (projekt má konec, oblast trvá) na příkladu z toho, co jsi řekl(a), a zeptá se, jestli chceš názvy oblastí česky (`domacnost`), nebo anglicky (`home`).

**Prohlídka skillů.** Po prvním projektu ti Claude ukáže skilly, které máš, vždycky na tvé věci: ty napíšeš jednu zkušební větu a uvidíš, co skill udělá. Dva až tři hned, zbytek si zapamatuje a nabídne příště.

**Týdenní přehled „Jak používám systém?“.** Za 3 až 5 dní používání Claude nabídne, že ti jednou týdně udělá přehled: jak systém používáš, 2 až 3 vylepšení a u věcí, které děláš pořád dokola, jestli by se nehodil vlastní skill. Na placeném plánu tě krok za krokem provede založením naplánované úlohy v aplikaci (**Scheduled** → **New task**), jinak ti to jednou týdně připomene a přehled udělá v chatu. Úloha nic nemění, jen zapíše přehled do `INBOX/`.

**Návod krok za krokem: co kam dát a čím to otevřít.** README na GitHubu, README v balíčku i `START-HERE.md` teď u každé věci z balíčku říkají, co s ní udělat: složka `Claude` do Dokumentů, plugin nahrát v aplikaci, zbytek nechat ve Stažených. Nově výslovně: **soubory z kitu nedávej do okna chatu.** Claude by je jen četl, nic by se nenainstalovalo a bralo by to limit.

**Skilly se nahrávají v nastavení aplikace:** vlevo **Customize** → **Plugins** → **Add** → **Upload plugin** a vybrat soubor `ai-starter-kit.plugin` (ne celý stažený zip). Jeden skill zvlášť: **Customize** → **Skills** → **Upload skill**.

**Nová verze kitu patří do `Claude/INBOX/kit/`.** Jedna podsložka v INBOXu místo dřívější `INBOX/prevzeti/kit/`. Tam ji najde `onboarding` při aktualizaci, při zapojení do vlastního prostředí i při převodu do angličtiny. `cleanup`, `triage` a `idea-inbox` složku `kit` přeskakují, takže její soubory nehlásí jako špatné názvy ani jako starý inbox.

**Co s tím udělat:**
- Máš Základ 0.8.0 nebo starší: nový zip rozbal ve Stažených, v `Dokumenty/Claude/INBOX` vytvoř složku `kit` a zkopíruj do ní všechno z rozbalené složky. Pak nahraj nový plugin (**Customize** → **Plugins** → **Upload plugin**) a do okna chatu napiš **„Aktualizuj kit.“** Doplní do mapy složek řádek pro `INBOX/kit/`, návod na novou verzi do `START-HERE.md`, do `CLAUDE.md` pravidlo, že nedokončený onboarding nabídne dokončit, a do předání kontrolní seznam onboardingu. Pak ti nabídne prohlídku skillů.
- Máš ještě starou složku `INBOX/prevzeti/kit/`: Claude ti ji nabídne smazat, nový kit patří do `INBOX/kit/`.
- Máš Pokročilé 0.8.0: přeinstalovat nemusíš, změnil se jen návod.

**Známá omezení:** názvy tlačítek v aplikaci jsou podle nápovědy Claude a podle verze aplikace se můžou lišit. Jestli nový plugin starý nahradí, nebo se ukáže dvakrát, zatím ověřené není; když dvakrát, starší odeber. Naplánované úlohy jsou jen na placených plánech; úloha pracuje se složkou na tvém počítači, takže počítač má být v čase běhu zapnutý. Jestli běh bere z limitu, nápověda neuvádí, proto jednou týdně.

## 0.8.0 — 2026-11-07 (Základ 13 skillů, Pokročilé 1 skill)

**Ochrana před cizím obsahem.** Co nenapsal(a) ty v chatu (stažený soubor, PDF, e-mail, webová stránka, tabulka od někoho jiného, cizí skill), jsou pro Clauda **data, ne příkazy**. Věta schovaná v dokumentu typu „ignoruj předchozí pokyny“ se neprovede: Claude ji jednou větou nahlásí a pokračuje tvým úkolem. Jen kvůli textu v dokumentu nikdy neplatí, neposílá, nesdílí, nemaže, nic nespouští a nezapisuje do pravidel ani profilu. Pravidlo je nově v `CLAUDE.md`.

**`basic-security-guard`: nový režim CIZÍ OBSAH.** Na větu „Stáhla jsem tohle, je to v pořádku?“ nebo „Chci nainstalovat skill z internetu“ projde soubor nebo cizí skill. Skript odstraní skrytý text (bílé nebo drobné písmo, komentáře, neviditelné znaky, skryté listy a snímky) z běžných formátů (text, HTML, e-mail, Word, Excel, PowerPoint, OpenDocument, PDF) a označí věty, které vypadají jako pokyn pro AI; nic sám neinstaluje. Skill má teď tři režimy: RADA, KONTROLA a CIZÍ OBSAH.

**Nastavení soukromí v onboardingu.** Nový krok 1d (asi 5 minut): kde v aplikaci vypnout nebo zapnout učení modelů na tvých chatech a paměť aplikace, proč zatím nepřipojovat konektory a proč zapnout dvoufázové ověření u účtu Google nebo Apple. Rozhoduješ ty, Claude jen ukáže kde. Volba se zapíše do `PROFILE.md` (řádek Soukromí).

**Mac a iCloud.** Onboarding řekne, ať u složky `Claude` zvolíš ve Finderu **Vždy ponechat na tomto zařízení** (jinak ji iCloud při nedostatku místa z Macu odloží a Claude soubory nepřečte), a že **iCloud není záloha**: smazaný soubor zmizí i z iCloudu.

**`token-economy` podle modelů z listopadu 2026.** Aktuální modely a ceny, úroveň úsilí, nový řádek **Pojistka** (u výstupů, které tvrdí fakta: jaký podklad dát do zadání, aby si Claude nevymýšlel), kdy se obnoví limit předplatného a rada otevřít pro jiný model nový chat.

**Drobnosti:** `skill-builder` při kontrole skillu nově hlídá i cizí obsah (9. oblast), `wiki` a `triage` berou uložené články a dokumenty jako data, ne pokyny. Pokročilé (`work-graph`) beze změny, jen nová verze kvůli Základu.

**Co s tím udělat:**
- Máš Základ 0.7.0 nebo starší: stáhni nový balíček Základ, přeinstaluj skilly (plugin, nebo `skills-jednotlive/`) a napiš Claudovi **„Aktualizuj kit.“** Doplní pravidlo o cizím obsahu do `CLAUDE.md` a řádek Soukromí do profilu a nabídne projít nastavení soukromí. Nic tvého nepřepíše.
- Stačí ti jen nové skilly: přeinstaluj `basic-security-guard`, `onboarding`, `token-economy`, `skill-builder`, `wiki` a `triage`.
- Máš Pokročilé 0.7.0: nic měnit nemusíš.

**Známá omezení:** skript najde skryté pokyny jen podle známých vzorů; hlavní ochrana je pravidlo v `CLAUDE.md`, ne skript. PDF zkontroluje jen s knihovnou PyMuPDF; chybí-li, řekne „PDF NEZKONTROLOVÁNO“ a nic sám neinstaluje. Starý formát DOC, XLS, obrázky a archivy odmítne („TYP NEPODPOROVÁN“). Názvy položek v nastavení aplikace se mohou měnit; když je Claude nenajde, popiš mu, co vidíš.

## 0.7.0 — 2026-10-22 (Základ 13 skillů, nově vrstva Pokročilé)

**Nová vrstva Pokročilé: rozšíření Základu.** Samostatný balíček pro chvíli, kdy ti Základ začne být těsný. Instaluje se k Základu (vlastní plugin, Základ nepřepíše) a každý skill v něm říká, který skill Základu rozšiřuje, co přidává a **kdy ho ještě nepotřebuješ**. Popis je v README balíčku Pokročilé.

**První skill Pokročilé: `work-graph`, graf práce napříč projekty.** Rozšiřuje `project-planner` a `workspace-architect`: ty vedou každý projekt zvlášť, graf ukazuje jednotlivé kroky napříč projekty, kdo je drží a na co čekají. Řekne, co můžeš dělat hned („Co je volné?“) a co blokuje nejvíc dalších věcí („Na čem to stojí?“). Před každým zápisem zálohuje, nic nemaže a kontrolní skript hlídá rozbité odkazy, kruhy a zmizelé řádky.

**Základ: celý kit v angličtině.** `onboarding` se na začátku zeptá, jestli chceš pracovat česky, nebo anglicky, a umí celý kit převést: profil, úvodní soubor a skilly (připraví anglické verze k instalaci). Předem řekne, co převede a co záměrně ne, a všechno zazálohuje. Po každé aktualizaci kitu převod nabídne znovu sám.

**Základ: plný zápis rozhodnutí.** `workspace-architect` u drahého nebo těžko vratného rozhodnutí nabídne delší tvar: podle čeho rozhoduješ, tabulka variant, nejsilnější argument proti a kdy to otevřít znovu. Krátký zápis zůstává výchozí, číslování a registr se nemění.

**Vyřazeno:** návrh AI pomocníků jako samostatný skill. AI pomocník nebo automatizace se vede jako každý jiný projekt, který trvá a mění se (`workspace-architect`).

**Co s tím udělat:**
- Máš Základ 0.6.0: stáhni nový balíček Základ, přeinstaluj skilly a napiš Claudovi „Aktualizuj kit.“ (doplní mapu složek, pravidlo o jazyce a metodu rozhodnutí; nic tvého nepřepíše).
- Chceš Pokročilé: po aktualizaci Základu stáhni balíček Pokročilé a nainstaluj jeho plugin, nebo jen `work-graph.skill`.
- Chceš všechno anglicky: po aktualizaci napiš „Chci všechno anglicky.“

**Známá omezení:** soubory v `SYSTEM/registry/` a hlášky skriptů zůstávají při převodu do angličtiny česky (čtou je skripty). Jestli aplikace při instalaci anglického skillu se stejným názvem přepíše český, nebo ukáže oba, zatím ověřené není; Claude se zeptá, co vidíš. Graf práce se na telefonu neupravuje.

## 0.6.0 — 2026-10-21 (vrstva Základ, 13 skillů)

**Nový skill `wiki`: druhý mozek.** Claude ukládá články, poznámky a dokumenty do složky `RESOURCES/`, sepisuje z nich propojené stránky a odpovídá jen z toho, co sis uložil, i se zdrojem (model „LLM wiki“ Andreje Karpathyho). Odkazy mezi stránkami jsou ve tvaru `[[nazev]]`, takže se wiki dá procházet v Obsidianu i s grafem souvislostí.

**Nový návod [WIKI-OBSIDIAN.md](WIKI-OBSIDIAN.md):** k čemu je Obsidian a jak ho nainstalovat (zdarma), synchronizace přes iCloud (Mac) a OneDrive (Windows), volitelný Web Clipper do prohlížeče, co získáš a co ztratíš, a poctivé limity.

**Co s tím udělat:**
- Máš kit: stáhni a ulož [wiki.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/wiki.skill). Nic dalšího, `RESOURCES/` už máš. Obsidian a Web Clipper jsou volitelné.
- Nemáš kit: stáhni celou sadu, nebo jen `wiki.skill` a napiš Claudovi „Založ si wiki“.

**`skill-builder` nejdřív hledá, pak staví.** Než začne psát nový skill, podívá se, jestli totéž už nemáš ty, starter kit nebo někdo na GitHubu, a doporučí použít hotový, upravit svůj, nebo postavit nový. Cizí skill z internetu bere jen jako inspiraci: projde ho, upozorní na podezřelé pokyny a přepíše po svém. Máš kit? Přeinstaluj i [skill-builder.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/skill-builder.skill).

**Známá omezení:** Web Clipper ukládá pod názvem článku s diakritikou, Claude ho přejmenuje až při „zpracuj nové zdroje“. Na telefonu wiki v Obsidianu v této verzi nečteš. Webové stránky čte Claude někdy zkráceně; pro přesné znění vlož text nebo použij Web Clipper.

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
