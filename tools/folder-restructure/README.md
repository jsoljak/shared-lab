> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# Oprava: úprava složky Claude na novou strukturu

Jeden textový soubor, který dáš svému Claudovi. Claude ti **zazálohuje složku `Claude/`, navrhne přehlednou strukturu podle toho, jak žiješ, a po malých částech (vždy až po tvém „ano“) ji uklidí**. Nic se nemaže, nic se neinstaluje a jde to kdykoli vrátit zpět.

Určeno pro ty, kdo dostali starší verzi startovní sady (0.2.0), která měla složky `Registry/`, `wiki/`, `profile.md`, `inbox/`, `projects/`.

## Jak si soubor stáhnout

1. Otevři soubor: [OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md](OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md)
2. Vpravo nad textem klikni na ikonu **Download raw file** (šipka dolů). Soubor se uloží do složky Stažené.
   - Nevidíš-li ikonu: klikni na **Raw**, na otevřené stránce zmáčkni **Ctrl + S** (Mac: **Cmd + S**) a ulož jako soubor s příponou `.md` (ve Windows v okně ukládání přepni „Uložit jako typ“ na **Všechny soubory**, ať se nepřipíše `.txt`).
3. Přesuň stažený soubor do své složky `Claude/` (nebo ho později přetáhni do okna s Claudem). Ve Windows to bývá `Dokumenty\Claude`, na Macu `Dokumenty/Claude`.

## Jak ho spustit

1. Otevři konverzaci v Claudovi se složkou `Claude/`.
2. Přetáhni tam soubor, nebo napiš, kde leží.
3. Napiš: **„Přečti soubor OPRAVA a udělej, co v něm je.“**
4. Odpovídej na otázky Claude. Trvá to asi 30 až 60 minut.

**Doporučení navíc:** než začneš, zkopíruj si celou složku `Claude` na plochu jako `Claude-záloha` (Windows: v Průzkumníku pravým tlačítkem **Kopírovat**, na ploše **Vložit**; Mac: ve Finderu), i když zálohuje Claude sám.

### Máš Windows?

Funguje to stejně. Před začátkem:
- **Zavři Word, Excel a PowerPoint** a soubory ze složky `Claude`. Otevřený soubor jde špatně přesunout.
- Leží-li složka `Claude` ve **OneDrive**, klikni na ni pravým tlačítkem a zvol **Vždy uchovávat na tomto zařízení**.
- Nic neinstaluj. Kdyby Claude řekl, že nemá Python, postupuje pomaleji jinou cestou.

## Co se stane a co ne

- Claude nejdřív zazálohuje celou složku do jednoho zipu uvnitř ní.
- Zeptá se na tvůj běžný týden a navrhne složky (práce, škola, osobní). Ty je upravíš.
- Ukáže plán „co kam“ po malých dávkách a čeká na tvé „ano“.
- Nic se **nemaže**, jen se přesouvá a přejmenovává. Odkazy mezi soubory se opraví. Claude sahá jen do složky `Claude/`.
- Vrátit vše zpět: řekni Claudovi **„Vrať opravu zpátky.“**

Kdyby se něco nepovedlo, záloha je u tebe a na konci ti Claude nabídne krátkou zprávu (bez obsahu tvých souborů), kterou můžeš poslat tomu, kdo ti odkaz dal.
