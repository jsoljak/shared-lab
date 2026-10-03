> **Classification: PUBLIC | Distribution: UNRESTRICTED**<br>
> Author: Jiří Soljak | [linkedin.com/in/jirisoljak](https://linkedin.com/in/jirisoljak)<br>
> Version: 2026-10-03

# Kolik tokenů pálím a kde? Nástroje na měření spotřeby AI (říjen 2026)

*Navazuje na květnový přehled ([2026-05-30](2026-05-30-token-monitoring-genericky-prehled.md)). Údaje ověřené k říjnu 2026 z dokumentace Anthropicu a README jednotlivých projektů.*

---

## Co se od května změnilo

1. **Claude Code umí většinu sám.** Příkaz `/usage` dnes ukazuje nejen spotřebu session, ale i to, *co* ji spotřebovalo: podíl skillů, subagentů, pluginů a jednotlivých MCP serverů, plánované úlohy (`/loop`) a varování typu „dlouhý kontext" nebo „cache misses". Status line dostává přímo procenta 5hodinového a týdenního limitu. Dřív to šlo jen přes nástroje třetích stran.
2. **Lidé nepoužívají jen Claude.** Typický AI builder dnes střídá Claude Code, Codex, Cursor, Gemini CLI nebo Copilot. Nejrychleji rostou nástroje, které ukazují spotřebu a limity *napříč všemi* na jednom místě.
3. **Otázka se posunula od „kolik" k „proč".** Nejvíc tokenů dnes nežerou odpovědi, ale kontext: dlouhé session, vypršená cache po pauze, subagenti, MCP servery, plánované úlohy, které posílají celý kontext znovu a znovu. Nástroje na úsporu se proto přesunuly od „ať Claude mluví stručně" k hygieně kontextu.

---

## Krátce: co bych dnes nastavil

1. **Zdarma a hned:** v Claude Code spusť `/usage` (spotřeba a co ji způsobilo) a `/context` (co ti zabírá kontextové okno). Nic se neinstaluje.
2. **Jeden nástroj na pozadí: TokenTracker.** Lokální přehled tokenů a nákladů napříč ~40 AI nástroji, app pro macOS, Windows i Linux, bez účtu.
3. **Když chceš limit pořád na očích:** status line (ccstatusline) nebo ikona v menu baru (CodexBar).

Zbytek níže je pro ty, kdo chtějí hlouběji, nebo staví vlastní agenty a týmová řešení.

---

## 1. Vestavěné v Claude Code — začni tady

| Příkaz / funkce | Co ukáže |
|---|---|
| `/usage` | Tokeny a odhad ceny za session, statistiku prompt cache (kolik vstupu šlo z cache, kolik bylo misses a proč). Na předplatném (Pro, Max, Team, Enterprise) i lišty limitů a rozpad posledních 24 h / 7 dní podle skillů, subagentů, pluginů, MCP serverů a plánovaných úloh. |
| `/context` | Co právě zabírá kontextové okno (instrukce, nástroje, MCP, konverzace). |
| `/insights` | HTML report o tom, *jak* pracuješ — na čem, kde se zasekáváš, co dělat jinak. Sám spotřebuje tokeny. |
| Status line | Vlastní skript dostává za běhu procenta 5hodinového a týdenního limitu včetně času resetu, zaplnění kontextu a cenu session. |
| `--max-budget-usd` | Strop útraty pro jeden běh (užitečné u headless a skriptů). |

**Limit:** všechno počítá jen z této jedné instalace. Spotřebu z jiných zařízení, z webového Claude ani z jiných AI nástrojů nevidí.

Dokumentace: https://code.claude.com/docs/en/costs

---

## 2. Stále na očích — limity a spotřeba během práce

### TokenTracker ⭐ doporučení
**Lokální přehled tokenů a nákladů napříč AI nástroji**

- ~40 nástrojů: Claude Code, Codex, Cursor, Gemini, Copilot a další
- Čte lokální logy, bez účtu a API klíčů; ukládá jen počty tokenů a časy, ne obsah promptů
- macOS app v menu baru s widgety, Windows, Linux (AppImage), CLI
- Dashboard s trendy a náklady, odpočty limitů; sdílení na žebříček jen volitelně
- Velmi aktivní vývoj (nové verze týdně), MIT

```bash
npx tokentracker-cli                                   # kdekoli s Node.js
brew install --cask xiufengsun/tokentracker/tokentracker  # macOS app
```

https://github.com/xiufengsun/TokenTracker

### CodexBar
**Limity všech AI předplatných v menu baru — nejrozšířenější volba na Macu**

- 60+ poskytovatelů (Claude, OpenAI/Codex, Copilot, Cursor, Gemini, OpenRouter a další)
- Bere údaje přímo od poskytovatelů přes tvoje přihlášení (OAuth, API klíče, cookies prohlížeče) — ukazuje tedy skutečné limity účtu, ne odhad z logů
- macOS 14+, CLI pro macOS a Linux; ~21k stars
- Instalace: `brew install --cask codexbar`

https://github.com/steipete/CodexBar

**TokenTracker vs. CodexBar:** TokenTracker počítá z lokálních logů tokeny a peníze a běží i na Windows a Linuxu. CodexBar ukazuje oficiální stav limitů účtu, ale jen na Macu a potřebuje přístup k tvým přihlášením. Mnoho lidí má oba.

### ccstatusline
**Limity a kontext přímo ve spodním řádku Claude Code**

- Session a týdenní limit, odpočet resetu, zaplnění kontextu, cena session, model, git větev
- Nastavení přes interaktivního průvodce: `npx -y ccstatusline@latest`; ~12k stars

https://github.com/sirmalloc/ccstatusline

*Alternativa:* Token Monitor — desktopový widget pro 40+ nástrojů s volitelnou synchronizací mezi zařízeními (https://github.com/Javis603/token-monitor).

---

## 3. Historie a analýza

### ccusage
- Nejpoužívanější CLI (~19k stars): denní, týdenní, měsíční reporty a 5hodinové bloky, export do JSON
- Dnes i pro Codex, OpenCode a další agentní CLI
- Spuštění: `npx ccusage@latest`
- **Pozor:** chyba #899 (k říjnu 2026 otevřená) — zápis do 1hodinové cache počítá levněji, náklady vychází asi o 19 % nižší

https://github.com/ccusage/ccusage

### Claude-Code-Usage-Monitor
- Živý terminálový dashboard s burn rate a predikcí, kdy narazíš na limit
- Od verze 4 trvalá historie i po 30 dnech, kdy Claude Code staré logy maže; export JSON/CSV
- `uv tool install claude-monitor`

https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

### Další
- **tokscale** — TUI pro 50+ agentů, ceny přes LiteLLM, volitelně veřejný žebříček: `npx tokscale@latest` (https://github.com/junhoyeo/tokscale)
- **phuryn/claude-usage** — jednoduchý lokální web dashboard jen pro Claude Code, bez závislostí, i jako rozšíření do VS Code (https://github.com/phuryn/claude-usage)

---

## 4. Pro buildery agentů a týmy

Tady už nejde o jednoho člověka u terminálu, ale o agenty běžící na pozadí a o celé týmy.

- **OpenTelemetry přímo v Claude Code.** Po nastavení `CLAUDE_CODE_ENABLE_TELEMETRY=1` a exportéru posílá Claude Code metriky tokenů, nákladů, sessions a událostí (prompty, volání nástrojů, MCP, skilly) do tvého monitoringu — Grafana, Datadog, Honeycomb… Pro Grafanu existují hotové dashboardy. Dokumentace: https://code.claude.com/docs/en/monitoring-usage
- **Agent SDK.** Každý běh vrací `total_cost_usd` a rozpis tokenů, takže náklad jde zapsat ke konkrétnímu úkolu nebo zákazníkovi. Dokumentace: https://code.claude.com/docs/en/agent-sdk/cost-tracking
- **Langfuse** — open-source observabilita. Claude Code napojíš přes hook, dostaneš trace každé session s náklady a voláními nástrojů, i napříč Codexem nebo Copilotem. Nevidí ale, jaké skilly a pravidla se do kontextu načetly. https://langfuse.com/resources/engineering/coding-agent-tracing
- **Gateway (LiteLLM nebo Claude apps gateway)** — veškerý provoz jde přes proxy, která počítá útratu na uživatele nebo klíč a umí nastavit limity. Smysl to má u týmů a u Claude přes AWS, Google Cloud nebo Azure.
- **Oficiální přehledy:** Team/Enterprise mají spend report v adminu (CSV), Enterprise i Analytics API; API zákazníci Console a Claude Code Analytics API (denní data, ne real-time).

---

## 5. Kde dnes tokeny mizí a jak ušetřit

Podle dokumentace Anthropicu nejvíc spotřeby v dlouhé session dělá:

- **dlouhý kontext** — každá zpráva i každé volání nástroje posílá celou konverzaci znovu
- **pauza delší než životnost cache** — první zpráva po ní zpracuje celý kontext načisto
- **plánované úlohy, zprávy mezi sessions, subagenti a agent týmy** — každý posílá vlastní požadavky
- **compaction** — shrnutí velkého kontextu je samo velký požadavek

Co pomáhá (zdarma): `/clear` mezi nesouvisejícími úkoly, specializované instrukce přesunout z CLAUDE.md do skillů (načítají se jen když jsou potřeba), vypnout nepoužívané MCP servery, levnější model pro subagenty, nižší `/effort` u jednoduchých úkolů. `/usage` ti sám označí chování, které tvoří 10 % a víc spotřeby.

Nástroje navíc:
- **token-optimizer** — hledá „ghost tokens" (nepoužívané skilly, přebujelé konfigurace, upovídané výstupy), komprimuje kontext a drží rozhodnutí přes compaction. Plugin: `/plugin marketplace add alexgreensh/token-optimizer` (https://github.com/alexgreensh/token-optimizer)
- **RTK** — zkracuje výstupy terminálových příkazů (git, testy, build) dřív, než je model přečte; smysl má u vývojářské práce (https://github.com/rtk-ai/rtk)
- **Caveman** — nutí model odpovídat ultra stručně; dobré na navigaci a debugging, nevhodné na psaní dokumentů a e-mailů (https://github.com/JuliusBrussee/caveman)

---

## Co použít pro jaký profil

| Profil | Doporučení |
|---|---|
| Chci jen vědět, kde jsem | `/usage` + `/context` (vestavěné) |
| Chci jeden nástroj na pozadí | **TokenTracker** |
| Používám víc AI předplatných, mám Mac | CodexBar (+ TokenTracker na náklady) |
| Pracuju v terminálu a chci limit pořád vidět | ccstatusline |
| Chci reporty a historii | ccusage nebo Claude-Code-Usage-Monitor |
| Stavím agenty / headless běhy | Agent SDK `total_cost_usd` + OpenTelemetry nebo Langfuse |
| Spravuju tým | Admin spend report / Analytics API, OpenTelemetry, případně gateway |
| Chci ušetřit | `/usage` varování + `/clear`, skilly místo CLAUDE.md, token-optimizer |

---

## Poznámky k trvanlivosti

Komunitní nástroje vydávají nové verze i několikrát týdně a Claude Code přidává do `/usage` a status line nové údaje průběžně. Počty hvězd a funkce odpovídají **říjnu 2026**. Všechny komunitní nástroje jsou nezávislé na Anthropicu; ty, které čtou lokální logy, vidí jen spotřebu z daného počítače.

---

*Zdroje: dokumentace Claude Code (Manage costs, Status line, Monitoring usage, Agent SDK cost tracking), README a releases jednotlivých projektů na GitHubu, Langfuse, srovnání na notchy.dev, starmorph.com a toriihq.com.*
