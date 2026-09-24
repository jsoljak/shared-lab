> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# Oprava: úprava složky Claude na novou strukturu (Windows 10)

Jeden textový soubor, který dáš svému Claudovi. Claude ti **zazálohuje složku `Claude`, navrhne přehlednou strukturu podle toho, jak žiješ, a po malých částech (vždy až po tvém „ano“) ji uklidí**. Nic se nemaže, nic neinstaluješ a jde to kdykoli vrátit zpět.

Určeno pro ty, kdo dostali starší verzi startovní sady (0.2.0), která měla složky `Registry`, `wiki`, `profile.md`, `inbox`, `projects`.

## Před začátkem

1. **Zapni přípony souborů.** Windows 10 je výchozím stavem skrývá. V Průzkumníku otevři záložku **Zobrazení** a zaškrtni **Přípony názvů souborů**.
2. **Zavři Word, Excel a PowerPoint** a všechny soubory ze složky `Claude`. Otevřený soubor jde špatně přesunout.
3. **OneDrive:** leží-li složka `Claude` ve OneDrive (často `OneDrive\Dokumenty\Claude`), klikni na ni pravým tlačítkem a zvol **Vždy uchovávat na tomto zařízení**.
4. **Záloha navíc:** v Průzkumníku klikni na složku `Claude` pravým tlačítkem, zvol **Kopírovat**, na ploše klikni pravým a zvol **Vložit**, složku přejmenuj na `Claude-záloha`. Claude zálohuje sám, tohle je pojistka navíc.

## Jak si soubor stáhnout

1. Otevři soubor: [OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md](OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md)
2. Vpravo nad textem klikni na ikonu **Download raw file** (šipka dolů). Soubor se uloží do složky **Stažené**.
   - Nevidíš-li ikonu: klikni na **Raw**, na otevřené stránce zmáčkni **Ctrl + S**, jako typ zvol **Všechny soubory** a soubor ulož s příponou `.md` (ne `.txt`).
3. Přesuň stažený soubor do složky `Claude` (obvykle `Dokumenty\Claude`).

## Jak ho spustit

1. Otevři konverzaci v Claudovi se složkou `Claude`.
2. Napiš: **„Přečti soubor OPRAVA a udělej, co v něm je.“**
3. Odpovídej na otázky Claude. Trvá to asi 30 až 60 minut.

Kdyby Claude řekl, že v počítači není Python, **nic neinstaluj**. Postupuje pak pomaleji, jinou cestou, a řekne ti to.

## Co se stane a co ne

- Claude nejdřív zazálohuje celou složku do jednoho zipu uvnitř ní.
- Zeptá se na tvůj běžný týden a navrhne složky (práce, škola, osobní). Ty je upravíš.
- Ukáže plán „co kam“ po malých dávkách a čeká na tvé „ano“.
- Nic se **nemaže**, jen se přesouvá a přejmenovává. Odkazy mezi soubory se opraví. Claude sahá jen do složky `Claude`.
- Vrátit vše zpět: řekni Claudovi **„Vrať opravu zpátky.“**

Kdyby se něco nepovedlo, záloha je u tebe a na konci ti Claude nabídne krátkou zprávu (bez obsahu tvých souborů), kterou můžeš poslat tomu, kdo ti odkaz dal.
