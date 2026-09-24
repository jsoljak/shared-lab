# moto-buy-advisor

> **Skill pro Claude** · verze **2026-07-16** · česky (český trh) · [**⬇ Download package** (moto-buy-advisor.skill)](https://raw.githubusercontent.com/jsoljak/shared-lab/main/downloads/moto-buy-advisor.skill)

Poradce při nákupu nové nebo ojeté motorky, jakékoli značky a modelu. Vezme inzerát nebo tvůj dotaz, dohledá tržní ceny a reference a řekne ti jednoznačný verdikt, ne alibistické „záleží“.

## Co umí

Skill sám pozná, co po něm chceš, a přepne se do jednoho ze čtyř režimů:

- **A: jeden inzerát.** Vložíš odkaz nebo text inzerátu. Dostaneš rozbor s verdiktem.
- **B: srovnání.** Víc kusů nebo modelů vedle sebe.
- **C: hledání na bazaru.** Najde nabídky a připraví přehled.
- **D: jaký model koupit.** Doporučení podle toho, co potřebuješ.

U každého výstupu vždy uvede pět věcí: **odpočet DPH** (cena s DPH i bez), **ABS**, **technická data** (výkon, hmotnost, výška sedla, poměr výkon/hmotnost), **postavení modelu u motorkářů** a **verdikt cena/výkon vs. stáří a nájezd**. Údaj, který z inzerátu nezjistí, označí „ověřit u prodejce“ a zařadí mezi otázky.

## Co k tomu potřebuje

- Aplikaci Claude s přístupem na web (hledání cen a referencí).
- Facebook Marketplace a některé bazary se nedají načíst z odkazu; pak vlož text inzerátu.

## Instalace

1. Stáhni balík odkazem **Download package** nahoře. Je to jeden soubor.
2. Otevři ho ve své aplikaci Claude a ulož jako skill. Kdyby aplikace chtěla `.zip`, přejmenuj příponu z `.skill` na `.zip`.
3. Napiš třeba: „Koukni na tenhle inzerát: …“.

Přesné tlačítko se liší podle verze aplikace a nemám ho ověřené na každé.

## Na co si dát pozor

Je to podpora rozhodování, ne finanční ani bezpečnostní poradenství. VIN, servisní historii, ABS i cenu si vždy ověř samostatně. Skill je psaný pro český trh (DPH, bazary, STK).

## Historie verzí

| Verze | Co se změnilo |
|---|---|
| 2026-07-16 | Aktuální znění skillu (nový obsah nepřibyl, jen přibyl balík ke stažení 2026-09-24). |
