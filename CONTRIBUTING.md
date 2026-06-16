# Contributing — pro toho, kdo do repa commituje

> `shared-lab` je **veřejný** (PUBLIC) repo. Ven jde jen obecná best-practice vrstva —
> žádná persona, žádná firemní ani osobní data.

## Povinný setup po naklonování — JEDNOU

Repo má bezpečnostní pojistku (git-gate), která blokuje commit citlivých dat. Hook se
**neaktivuje sám** — `core.hooksPath` a executable bit se při `git clone` nepřenášejí.
Po každém naklonování spusť:

```bash
git config core.hooksPath hooks
chmod +x hooks/pre-commit
```

Ověření: `git config --get core.hooksPath` musí vrátit `hooks`.

## Co git-gate dělá (profil PUBLIC)

Před každým commitem proskenuje staged soubory (včetně payloadu uvnitř `.skill`) a **zablokuje**
commit, pokud najde:

- `visibility: FOUNDER/MANAGEMENT`, citlivé `audience`
- reálné klientské názvy, sazby/marže, telefony
- **jakýkoli e-mail** a **personu/firmu** (jméno autora, iniciály, interní firemní markery)

PUBLIC profil je přísnější než TEAM — ven nesmí ani jméno autora.

## Když gate zablokuje

1. **Správně** → odstraň citlivý obsah, commitni čistou verzi.
2. **Falešný poplach** → vědomý override: `git commit --no-verify -m "intentional: <důvod>"`.

## Zdroj

Git-gate = ADR-026. Skript `hooks/pre-commit` je kanonický a identický napříč SITEQ
distribučními repy; přísnost řídí `.gitgate` (zde: `PUBLIC`).
