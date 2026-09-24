# prompt-coach

Claude skill, který ti pomůže napsat lepší prompt. Neopraví ho za tebe: **ptá se po jedné otázce**, až sám přijdeš na to, co ve tvém zadání chybí. Tím se dlouhodobě učíš psát lépe.

Vhodné pro každého, kdo s AI mluví a nedostává odpovědi, které chce. Není potřeba žádná předchozí znalost.

## Co umí

- **Zkontroluje prompt** a řekne, jestli je v pořádku. Jednoznačné a uzavřené zadání (třeba „přelož větu do angličtiny“) nekritizuje zbytečně.
- **Vede rozhovor.** Podle toho, co chceš, si vybere vhodnou strukturu (RACE, CO-STAR, RISEN, CREATE, nebo krok za krokem) a jednou otázkou míří na to nejdůležitější, co chybí: role, kontext, cíl, publikum, formát, omezení.
- **Přepíše prompt**, když o to požádáš, a ke každé změně napíše, proč ji udělal.
- **Audit:** řekni „udělej audit“ a dostaneš všechny nedostatky najednou.
- **Deník pokroku:** na tvůj souhlas si zapisuje, co často zapomínáš. Zeptej se „co nejčastěji kazím?“.

## Příklad

> **Ty:** Zkontroluj prompt: „Napiš mi něco o klimatické změně.“
>
> **Coach:** Co by pro tebe byl ideální výstup a co s ním chceš udělat?

## Jak ho použít

1. Skill má jediný povinný soubor, `SKILL.md`, a jednu referenci, `references/prompt_engineering_best_practices.md`. Celá složka `prompt-coach/` je skill.
2. Přidej ji do Claude podle své aplikace (skill ze složky, nebo ho vlož do projektu). Přesný postup se liší podle verze aplikace a tady ho nemám ověřený.
3. Napiš třeba: „Zkontroluj prompt: …“, nebo „prompt coach: vylepši to“.

## Obsah složky

```
prompt-coach/
├── SKILL.md                                   ← pravidla a postup skillu
└── references/
    ├── prompt_engineering_best_practices.md   ← přehled frameworků a technik (stav začátek 2026)
    └── prompt-journal.md                      ← prázdný vzor deníku
```

## Poznámky

- Skill je česky. Odpovídá v jazyce, ve kterém mu píšeš.
- Přehled modelů v referenci rychle stárne, frameworky a principy zadávání ne.
- Do deníku nedávej prompty s osobními nebo firemními údaji.
- Autor: Jiří Soljak, [LinkedIn](https://www.linkedin.com/in/jirisoljak/). Volně k použití, bez záruky.
