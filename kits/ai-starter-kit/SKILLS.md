> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-10-08

# AI Starter Kit: co který skill umí

Skill je pomocník, kterého Claude spustí, když řekneš správnou větu. Nemusíš znát jejich názvy: stačí napsat, co potřebuješ, a Claude vybere. Tady je přehled **po situacích**, ke každému skillu příklady vět a také co **nedělá**. Zpět na [úvodní stránku](README.md) · [co je nového](RELEASE-NOTES.md).

**Jak stáhnout:** klikni na odkaz **⬇ Stáhnout jen tenhle skill** u skillu, soubor se uloží do složky Stažené (GitHub ani účet nepotřebuješ). Otevři ho v aplikaci Claude a ulož jako skill. **Celou sadu** (všech 12 skillů + šablonu složky) stáhneš jedním odkazem na [úvodní stránce](README.md#stažení-celé-sady-nebo-jednoho-skillu). Samostatně dobře fungují `prompt-coach` a `token-economy`; ostatní skilly počítají se složkou `Claude/` z balíčku (mapa složek, pravidla, registry), tak je stahuj až spolu s ní.

| Když… | Skilly |
|---|---|
| začínáš a chceš mít pořádek | [onboarding](#onboarding) · [cleanup](#cleanup) · [file-guard](#file-guard) |
| každý den něco zapisuješ a třídíš | [idea-inbox](#idea-inbox) · [triage](#triage) · [session-close](#session-close) |
| vedeš projekty | [workspace-architect](#workspace-architect) · [project-planner](#project-planner) |
| chceš být v bezpečí a šetřit limit | [basic-security-guard](#basic-security-guard) · [token-economy](#token-economy) |
| se chceš naučit víc | [prompt-coach](#prompt-coach) · [skill-builder](#skill-builder) |

---

## Když začínáš

### onboarding
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/onboarding.skill)

**K čemu:** provede tě prvním nastavením, nebo zapojením kitu do toho, co už máš. Trvá zhruba hodinu a jde přerušit.
**Řekni třeba:** „Začínám — spusť onboarding.“ · „Podívej se na tenhle kit a poraď mi, jak by se dal zapojit do mého stávajícího prostředí.“ · „Aktualizuj kit.“
**Co udělá:** zjistí, jestli máš Mac, nebo Windows, projde, co už máš (skilly, pravidla, seznamy), vysvětlí, jak je složka uspořádaná, a navrhne složky a oblasti podle toho, jak žiješ. Pak vyplní profil a založí s tebou první projekt. Na konci uloží, kde jste skončili.
**Co nedělá:** nic nesmaže a nic nepřepíše bez tvého „ano“. Můžeš odmítnout kitovou strukturu a nechat si svoje uspořádání. Tvůj vlastní `CLAUDE.md` obohatí, ne přepíše.

### cleanup
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/cleanup.skill)

**K čemu:** uklidí složku a převezme tvoje staré soubory (Stažené, Plocha, stará škola) do nové struktury.
**Řekni třeba:** „Ukliď to tady.“ · „Roztřiď moje staré soubory.“ · „Najdi duplicity.“ · „Přesuň hotové projekty do archivu.“
**Co udělá:** nejdřív se zeptá na zálohu, pak zmapuje, co kde leží, navrhne, kam co patří, a přesouvá po dávkách. **Každou dávku jde vrátit.** Hlídá i názvy, které by na Windows nešly.
**Co nedělá:** nemaže. Co vypadá zbytečně, jen odloží do složky k pozdějšímu rozhodnutí. Bez mapy složek a pravidel pojmenování jen prohlíží.

### file-guard
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/file-guard.skill)

**K čemu:** hlídá, kam se soubor uloží a jak se jmenuje.
**Řekni třeba:** „Kam to uložit?“ · „Jak to pojmenovat?“ · „Kam patří tahle smlouva?“
**Co udělá:** podle tvé mapy složek navrhne místo, zkontroluje název a před rizikovou věcí (smazání, nová složka, přepsání) se zeptá. Spustí se i sám před zápisem.
**Co nedělá:** nehlídá čtení souborů ani dočasné soubory. Odmítneš-li kitovou strukturu, ptá se u každého zápisu a cesty nenavrhuje.

## Každý den

### idea-inbox
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/idea-inbox.skill)

**K čemu:** zachytí nápad nebo úkol za pár sekund, aby nepropadl, a vrátí tě k práci.
**Řekni třeba:** „Napadlo mě…“ · „Zapiš si: objednat pneumatiky.“ · „Do rekonstrukce kuchyně dej: objednat dlaždice.“ · „Ukaž inbox.“
**Co udělá:** zapíše jednu řádku do složky `INBOX/`. Řekneš-li, ke kterému projektu věc patří (nebo se právě pracovalo na jednom), zapíše ji rovnou do `ideas.md` v tom projektu.
**Co nedělá:** netřídí, nesmaže a nezakládá projekty. Třídění je práce `triage`.

### triage
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/triage.skill)

**K čemu:** vytřídí hromadu věcí, o kterých nevíš, kam s nimi.
**Řekni třeba:** „Mám hromadu věcí a nevím kam s nimi.“ · „Vytřiď inbox.“ · „Roztřiď tyhle úkoly.“
**Co udělá:** ke každé věci napíše, kam patří a proč (tabulka), a zapíše **teprve po tvém souhlasu**, po dávkách. Pozná projekt, trvalou věc oblasti, zdroj, nápad na později nebo „udělej hned“.
**Co nedělá:** nemaže, nezpracovává jednu věc (na to je `idea-inbox`) a nerozhoduje mezi variantami.

### session-close
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/session-close.skill)

**K čemu:** uloží, kde jsi skončil(a), aby šlo příště navázat. Claude si mezi konverzacemi nic nepamatuje, pamatují se jen soubory.
**Řekni třeba:** „Končím.“ · „Hotovo na dnes.“ · příště „Kde jsem skončil?“ (to jen čte).
**Co udělá:** zapíše deník a stav každého projektu, na kterém se pracovalo, a krátké předání. Nabídne se sám po podstatné práci. Selže-li některý zápis, předání uloží i tak a řekne, co se nezapsalo.
**Co nedělá:** nezapisuje prázdné záznamy, když se nic nestalo. Git k tomu nepotřebuješ.

## Projekty

Při založení projektu se Claude zeptá jednou: „Bude to fungovat dál a měnit se, nebo to proběhne a skončí?“ a podle odpovědi použije jeden z těchto dvou skillů. Nemusíš vybírat sám.

### workspace-architect
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/workspace-architect.skill)

**K čemu:** vede projekty, které **trvají a mění se** (domácí síť, evidence záruk, aplikace, zahrada), a umí pohled přes **všechny** projekty.
**Řekni třeba:** „Chci postavit evidenci záruk.“ · „Kde jsme skončili s domácí sítí?“ · „Jaké mám projekty a co na čem závisí?“ · „Je tohle už někde rozjeté?“ · „Zkontroluj, jestli mi v projektech něco nesedí.“
**Co udělá:** založí projekt a zařadí ho do oblasti, vede mapu částí a jejich stav, zapisuje rozhodnutí, ověří, že podobný projekt už neběží, a zkontroluje celý workspace (osiřelé věci, rozbité odkazy, kruhové závislosti).
**Co nedělá:** neřeší věci, které proběhnou a skončí (to je `project-planner`), a nic neopravuje bez tvého souhlasu.

### project-planner
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/project-planner.skill)

**K čemu:** vede projekty, které **proběhnou a skončí** (rekonstrukce, stěhování, svatba, výlet, plán studia).
**Řekni třeba:** „Plánuju rekonstrukci koupelny.“ · „Co blokuje stěhování?“ · „Fáze je hotová.“ · „Končíme projekt.“
**Co udělá:** ujasní, kdy je hotovo a do kdy, rozdělí projekt na fáze, řekne, kdo za co odpovídá a kde se rozhoduje. Při navázání ukáže, co běží, co blokuje a co je další krok.
**Co nedělá:** nevede věci, které trvají a mění se (to je `workspace-architect`), a neplánuje za tebe.

## Bezpečí a limit

### basic-security-guard
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/basic-security-guard.skill)

**K čemu:** hlídá, co se nemá vkládat do chatu a do souborů (hesla, PIN, čísla karet, rodná čísla, skeny dokladů, zdravotní údaje třetích osob a dětí).
**Řekni třeba:** „Můžu sem vložit tuhle fotku dokladu?“ · „Jak to zálohovat?“ · „Zkontroluj složku na hesla.“
**Co udělá:** poradí, a umí zkontrolovat složku na omylem uložená tajemství. Kontrola vypíše jen soubor a řádek, **nikdy samotnou hodnotu**.
**Co nedělá:** není to právní poradna a neřeší běžné plánování ani psaní.

### token-economy
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/token-economy.skill)

**K čemu:** poradí, na jakém modelu Claude úkol pustit, aby ses nevyčerpal(a) limit předplatného.
**Řekni třeba:** „Jaký model na tohle?“ · „Opus, nebo Sonnet?“ · „Došel mi limit.“
**Co udělá:** odpoví čtyřmi krátkými řádky: který model, proč, jak ho přepnout a kdy zvolit silnější.
**Co nedělá:** model sám nepřepíná, rozhoduješ ty. U běžných úkolů se nehlásí.

## Naučit se víc

### prompt-coach
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/prompt-coach.skill)

**K čemu:** pomůže ti napsat dobré zadání pro Claude, a vysvětlí proč, abys to příště uměl(a) sám.
**Řekni třeba:** „Odpověď je k ničemu, jak mám napsat zadání?“ · „Přepiš mi ten prompt.“ · „Zkontroluj moje zadání.“
**Co udělá:** zeptá se na cíl, kontext, formát a omezení a ukáže zadání **před a po**. Dobré zadání nepřepisuje.
**Co nedělá:** nepíše za tebe texty (e-maily, články, překlady) a nerozhoduje mezi variantami.

### skill-builder
⬇ [Stáhnout jen tenhle skill](https://raw.githubusercontent.com/jsoljak/shared-lab/main/kits/ai-starter-kit/skills/skill-builder.skill)

**K čemu:** pomůže ti vytvořit vlastní skill, nebo zkontrolovat ty, které už máš.
**Řekni třeba:** „Chci si udělat skill.“ · „Projdi moje skilly.“ · „Je můj skill moc dlouhý?“ · „Rozděl ten skill.“
**Co udělá:** vede tě po krocích (účel, spouštěcí věty, krátký popis, zkouška na třech větách, zabalení), umí projít existující skilly, rozdělit dlouhý skill a sloučit dva, které dělají totéž.
**Co nedělá:** nic nemaže. Pro jednorázové úkoly skill nepotřebuješ.
