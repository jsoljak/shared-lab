> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-21

# Druhý mozek: wiki s Claudem a Obsidian

Návod pro každého, kdo si chce s Claudem vést vlastní knihovnu znalostí. Nepotřebuješ nic umět, jen mít aplikaci Claude na počítači.

## Co to je

Čteš články, díváš se na videa, děláš si poznámky z kurzu, hledáš recenze na auto. Za půl roku už nevíš, kde to bylo. **Wiki** je složka ve tvém počítači, kam Claude tyhle věci ukládá a sepisuje z nich přehledné stránky. Když se pak zeptáš „co jsem si zjistil o tepelných čerpadlech?“, odpoví **jen z toho, co sis uložil**, a řekne, odkud to má. Co ve wiki není, si nedomýšlí.

Myšlenku popsal Andrej Karpathy (jeden ze zakladatelů OpenAI) jako „LLM wiki“: ty dodáváš zdroje, AI dělá papírování, tedy třídí, propojuje a hlídá pořádek.

**Obsidian** je volitelný program na prohlížení té složky. Wiki funguje i bez něj.

## Co ti to přinese

- **Paměť, která nezapomíná.** Běžný chat s Claudem po čase zapomene, co jsi mu poslal. Wiki zůstává na tvém počítači.
- **Odpovědi se zdrojem.** U každé věty vidíš, ze kterého článku nebo poznámky pochází.
- **Pořádek bez práce.** Pojmenování, třídění a propojování dělá Claude.
- **Rozpory na stole.** Když si dva články odporují, Claude ti ukáže obě verze.

Příklady použití: zahrada, vaření, opravy v domě, návody k vybavení · větší rozhodnutí (auto, pojištění, hypotéka, škola) · poznámky ze studia a kurzů · články o zdraví a stravě, ke kterým se vracíš (ne zdravotní dokumentace).

## Instalace wiki

### A) Starter kit už máš

1. Stáhni skill [wiki.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/wiki.skill).
2. Otevři ho v aplikaci Claude a ulož jako skill.
3. Hotovo. Složku `RESOURCES/` ve své složce `Claude` už máš. Napiš Claudovi „Ulož si tenhle článek“ a vlož text.

### B) Starter kit nemáš

**Doporučuju stáhnout celý kit**, wiki je jeho součástí: [návod a stažení](README.md). Dostaneš uspořádanou složku a skilly, které na wiki navazují (třídění, projekty, pořádek).

Chceš jen wiki:
1. V Dokumentech si založ složku `Claude` (vznikne `Dokumenty/Claude`).
2. V aplikaci Claude ji nasdílej (v nové konverzaci zvol práci se složkou a vyber `Claude`).
3. Stáhni [wiki.skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/wiki.skill), otevři ho v aplikaci Claude a ulož jako skill.
4. Napiš Claudovi: „Založ si wiki.“ Vytvoří složku `RESOURCES/` s rozcestníkem a deníkem.

### Jak s wiki mluvit

| Řekneš | Co se stane |
|---|---|
| „Ulož si tenhle článek“ + text, odkaz nebo dokument | uloží zdroj a sepíše nebo doplní stránky |
| „Co jsem si uložil o …?“ / „Zeptej se wiki …“ | odpoví jen z wiki, se zdroji |
| „Zpracuj nové zdroje“ | zpracuje, co jsi uložil Web Clipperem nebo přetáhl do složky |
| „Zkontroluj wiki“ | najde nepořádek a navrhne opravy, nic sám nemaže |

**Prvních pět věcí, které si ulož:** návod k něčemu doma, co občas řešíš · článek k rozhodnutí, které tě čeká · poznámky z posledního kurzu nebo školení · recept, který chceš umět · cokoli, co jsi minulý měsíc hledal dvakrát. Wiki začne být užitečná po pár desítkách zdrojů.

## Obsidian: k čemu ti bude

Představ si wiki jako knihovnu. Claude je knihovník, který knihy zařazuje a píše k nim kartičky. **Obsidian jsou dveře do té knihovny**: otevřeš je a procházíš.

- **Čteš stránky jako v knize**, s nadpisy a odkazy, na které klikneš a přeskočíš na související téma.
- **Vidíš graf**: mapu, jak spolu tvoje témata souvisí. Časem z něj poznáš, čemu se věnuješ nejvíc.
- **Hledáš ve všem najednou**, i ve svých projektech a poznámkách mimo wiki.
- **Můžeš sám opravit nebo dopsat stránku.** Claude tvou úpravu respektuje.

Co Obsidian **neumí**: nemá v sobě Clauda. Ukládání a odpovídání pořád děláš v aplikaci Claude. Obsidian je okno, nic víc.

**Je zdarma**, i pro práci (od února 2025 nepotřebuješ ani firemní licenci). Nepotřebuješ účet. Placené jsou jen doplňkové služby Sync a Publish a ty nepotřebuješ: synchronizaci řeší iCloud nebo OneDrive (níže). Soubory zůstávají tvoje obyčejné soubory ve složce `Claude`. Když Obsidian smažeš, nepřijdeš o nic.

## Instalace Obsidianu

1. Jdi na [obsidian.md](https://obsidian.md) a klikni na **Download**. Stránka sama nabídne verzi pro tvůj počítač.
   - **Mac:** otevři stažený soubor `.dmg` a ikonu Obsidianu přetáhni do složky **Aplikace**.
   - **Windows:** spusť stažený instalátor `.exe` a odklikej ho.
2. Spusť Obsidian. Na úvodní obrazovce zvol **Open folder as vault** (Otevřít složku jako trezor; „trezor“ je jen Obsidianovo slovo pro složku s poznámkami).
3. Vyber **celou složku `Claude`**, tu, kterou máš nasdílenou v aplikaci Claude (většinou `Dokumenty/Claude`, ale může ležet i jinde). Ne jen `RESOURCES`: uvidíš pak wiki i své projekty pohromadě.
4. Tři nastavení (ozubené kolečko vlevo dole, **Settings**):
   - **Files and links → Excluded files:** přidej složku `SYSTEM`. Je v ní strojovna kitu (pravidla, seznamy a paměť skillů), o kterou se stará Claude. Ve stromu složek ji dál uvidíš, jen se nebude plést do hledání a grafu. (Bez kitu ji nemáš, krok přeskoč.)
   - **Files and links → Default location for new attachments:** zvol „In the folder specified below“ a napiš `RESOURCES/sources/attachments`. Obrázky pak padají ke zdrojům.
   - **Files and links → Automatically update internal links:** zapni. Když něco přejmenuješ, odkazy se opraví samy.
5. **Komunitní pluginy nezapínej.** Po instalaci jsou vypnuté (Settings → Community plugins) a tak je nech. Všechno potřebné (odkazy, graf, hledání) umí Obsidian sám. Doplňky od cizích autorů mají přístup k tvým souborům.

Máš-li Obsidian v češtině, názvy v nastavení se mohou trochu lišit, poloha je stejná.

### Jak se v něm vyznat

- **Začni stránkou `RESOURCES/index.md`**, to je rozcestník celé wiki.
- **Graf:** ikona sítě v levém panelu, nebo Cmd + G (Mac) / Ctrl + G (Windows).
- **Rychle otevřít stránku:** Cmd + O / Ctrl + O a napiš kus názvu.
- **Hledat v textu všude:** Cmd + Shift + F / Ctrl + Shift + F.
- Fialové `[[odkazy]]` jsou proklik na jinou stránku. Šedé vedou na stránku, která zatím neexistuje.

## Synchronizace a záloha

Kit doporučuje mít složku `Claude` v Dokumentech, protože Dokumenty se umí zálohovat a synchronizovat samy. Máš-li ji jinde, platí totéž pro tu složku: ověř, že se zálohuje. Máš-li starter kit, máš to nejspíš nastavené už od instalace.

### Mac: iCloud

1. **Nastavení systému → [tvé jméno] → iCloud → iCloud Drive** a zapni **Složky Plocha a Dokumenty**. Dokumenty (i složka `Claude`) se pak zálohují do iCloudu a jsou na všech tvých Macích.
2. **Důležité:** ve Finderu klikni na složku `Claude` pravým tlačítkem a zvol **Ponechat staženo** (anglicky Keep Downloaded). Jinak může Mac při nedostatku místa nechat soubory jen v iCloudu a Claude ani Obsidian je pak nepřečtou. Pokud tu volbu nemáš (starší macOS), vypni v nastavení iCloud Drive **Optimalizovat úložiště Macu**.

### Windows: OneDrive (Microsoft 365)

1. V OneDrivu zapni **zálohování složky Dokumenty** (ikona OneDrive vedle hodin → Nastavení → Synchronizace a zálohování → Spravovat zálohování → Dokumenty).
2. **Důležité:** v Průzkumníkovi klikni na složku `Claude` pravým tlačítkem a zvol **Vždy ponechat na tomto zařízení**. Jinak může OneDrive nechat soubory jen v cloudu a Claude ani Obsidian je nepřečtou.

### Na co si dát pozor

- **Jedna synchronizace stačí.** Nekombinuj iCloud nebo OneDrive s Obsidian Sync, Dropboxem ani jiným programem na stejnou složku.
- **Nepracuj na dvou počítačích zároveň.** Když se stejný soubor změní na dvou místech dřív, než se srovná, vznikne kopie (`kompost 2.md` na Macu, `kompost (1).md` nebo se jménem počítače na Windows). Nic nemaž, řekni Claudovi „zkontroluj wiki“ a pomůže vybrat.
- **Telefon v této verzi ne.** Obsidian na iPhonu otevře jen složku uloženou v jeho vlastním místě v iCloudu, ne v Dokumentech. Přesouvat kvůli tomu celou složku nedoporučuju.

## Web Clipper (volitelné)

**Co to je:** doplněk do prohlížeče od tvůrců Obsidianu, zdarma. Při čtení článku klikneš na ikonu a článek se uloží celý do tvé wiki, aniž bys otevíral Clauda.

**Kdy ho použít:** když chceš mít článek z webu **přesně a celý**. Claude totiž webové stránky čte přes nástroj, který text často zkrátí nebo převede, takže uložené znění nemusí být slovo od slova. Web Clipper uloží přesně to, co vidíš, i se stránkami za přihlášením nebo předplatným, kam se Claude nedostane.

**Kdy ho nepotřebuješ:** ukládáš z webu jen občas. Pak stačí článek označit, zkopírovat a vložit Claudovi s „ulož si to“. Výsledek je stejně přesný.

**Instalace:**
1. Obsidian musí být nainstalovaný a mít otevřenou složku `Claude` (viz výše).
2. Na stránce [obsidian.md/clipper](https://obsidian.md/clipper) vyber svůj prohlížeč (Chrome, Edge, Firefox, Safari, Brave a další) a doplněk přidej.
3. V nastavení doplňku vyber trezor `Claude` a jako **Note location** napiš `RESOURCES/sources`.
4. Pak už jen: čteš, klikneš na ikonu, uložíš. Jednou za čas řekni Claudovi **„Zpracuj nové zdroje“**.

**Co Web Clipperem získáš a co ztratíš:**

| Získáš | Ztratíš (proti ukládání přes Clauda) |
|---|---|
| celé a přesné znění článku | okamžité zpracování: výstřižek čeká, než řekneš „zpracuj nové zdroje“ |
| stránky za přihlášením nebo předplatným | rozhovor nad článkem hned při ukládání |
| uložení jedním kliknutím, bez spotřeby limitu Clauda | kontrolu, jestli to už nemáš nebo jestli to tam patří |
| adresu, autora a datum automaticky | správný název souboru (ten opraví Claude až při zpracování) |

Největší past: naklipovat stovku článků a nikdy je nezpracovat. Hodnota wiki je ve zpracovaných stránkách, ne v hromadě výstřižků.

## Limity (poctivě)

- **Názvy souborů mají pravidla.** Malá písmena, bez háčků a čárek, slova spojená pomlčkou (`zavlazovani-zahrady`). Claude a Obsidian podle nich hledají odkazy. Web Clipper ukládá pod názvem článku (`Jak kompostovat – průvodce.md`) a Claude ho při zpracování přejmenuje. **Přejmenovávání nech na Claudovi**, ať se nerozbijí odkazy a nevzniknou dva soubory stejného jména.
- **Každý název jen jednou.** Odkaz `[[kompost]]` musí vést na jediný soubor. Proto mají zdroje na konci druh (`-clanek`, `-poznamky`, `-kniha`).
- **Zdroje neupravuj.** Uložený článek je originál, podle kterého se ověřuje, co v něm opravdu stálo. Opravovat a dopisovat můžeš stránky (`pages/`).
- **Wiki ví jen to, co jí dáš.** Na obecné otázky odpoví „ve wiki nic nemám“. Odpověď z obecných znalostí dostaneš jen na vyžádání a označenou „MIMO WIKI“.
- **Odkaz bez textu nemusí stačit.** Stránky za přihlášením Claude nepřečte a dlouhé stránky může zkrátit. Řekne ti to.
- **Citlivé věci do wiki nepatří**: hesla, rodná čísla, doklady, cizí zdravotní údaje, důvěrné věci z práce. Claude je odmítne uložit.
- **Hodnota přichází postupně.** Prvních pár zdrojů vypadá jako obyčejná složka. Smysl se ukáže po desítkách zdrojů a měsících.
- **Velikost:** stovky stránek jsou v pořádku. Když rozcestník přeroste, Claude navrhne rozdělit ho podle témat.

## Nefunguje něco?

| Problém | Řešení |
|---|---|
| Claude říká, že soubor nejde přečíst, ale ve složce je | soubor je jen v cloudu: nastav složce `Claude` „Ponechat staženo“ / „Vždy ponechat na tomto zařízení“ (Synchronizace výše) |
| Obsidian ukazuje odkaz šedě | stránka zatím neexistuje, nebo je přejmenovaná. Řekni Claudovi „zkontroluj wiki“ |
| Výstřižky se neukládají do wiki | v nastavení Web Clipperu zkontroluj trezor `Claude` a Note location `RESOURCES/sources`. Obsidian musí běžet |
| Ve wiki jsou soubory s ` 2` nebo `(1)` v názvu | konflikt synchronizace, nic nemaž: „zkontroluj wiki“ |
| Cokoli jiného | napiš mi na LinkedIn (linkedin.com/in/jirisoljak) |
