> **visibility: PUBLIC | Distribution: LINK-ONLY**
> Author: Jiří Soljak | linkedin.com/in/jirisoljak
> Version: 2026-09-24

# Oprava: úprava složky Claude na novou strukturu (Windows 10)

> **Nástroj: jeden soubor pro Clauda** · verze **0.3.0** (z 0.2.0) · česky · [**⬇ Download package** (OPRAVA…md)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/tools/folder-restructure/OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md)

Jeden textový soubor, který dáš svému Claudovi. Claude ti **zazálohuje složku `Claude`, navrhne přehlednou strukturu podle toho, jak žiješ, a po malých částech (vždy až po tvém „ano“) ji uklidí**. Nic se nemaže, nic neinstaluješ a jde to kdykoli vrátit zpět.

Určeno pro ty, kdo dostali starší verzi startovní sady (0.2.0), která měla složky `Registry`, `wiki`, `profile.md`, `inbox`, `projects`.

## Před začátkem

1. **Zapni přípony souborů.** Windows 10 je výchozím stavem skrývá. V Průzkumníku otevři záložku **Zobrazení** a zaškrtni **Přípony názvů souborů**.
2. **Zavři Word, Excel a PowerPoint** a všechny soubory ze složky `Claude`. Otevřený soubor jde špatně přesunout.
3. **OneDrive:** leží-li složka `Claude` ve OneDrive (často `OneDrive\Dokumenty\Claude`), klikni na ni pravým tlačítkem a zvol **Vždy uchovávat na tomto zařízení**.
4. **Záloha navíc:** v Průzkumníku klikni na složku `Claude` pravým tlačítkem, zvol **Kopírovat**, na ploše klikni pravým a zvol **Vložit**, složku přejmenuj na `Claude-záloha`. Claude zálohuje sám, tohle je pojistka navíc.

## Jak si soubor stáhnout

1. Klikni **pravým tlačítkem** na [OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md](https://raw.githubusercontent.com/jsoljak/shared-lab/main/tools/folder-restructure/OPRAVA__zaklad-v0-2-0-na-v0-3-0__2026-09-24.md) a zvol **Uložit odkaz jako…** (Edge, Chrome).
2. Ulož ho třeba do složky **Stažené**. Zkontroluj, že název končí na `.md` (ne `.txt`); Windows 10 přípony skrývá, viz „Před začátkem“ výše. Pokud se nabízí `.txt`, přepni **Uložit jako typ** na **Všechny soubory**.
3. Přesuň soubor do své složky `Claude` (obvykle `Dokumenty\Claude`).

*Kdyby se soubor jen otevřel jako text:* zmáčkni **Ctrl + S** a ulož ho stejným způsobem.

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

## Historie verzí

| Verze | Co se změnilo |
|---|---|
| 0.3.0 (2026-09-24) | První vydání. Přechod složky ze struktury 0.2.0 na novou (kostra velkými písmeny, `SYSTEM/`, oblasti, `PROFILE.md`). Určeno pro Windows 10. |
