> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit: co je v téhle verzi

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
