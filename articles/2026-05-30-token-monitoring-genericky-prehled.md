> **Classification: PUBLIC | Distribution: UNRESTRICTED**<br>
> Author: Jiří Soljak | [linkedin.com/in/jirisoljak](https://linkedin.com/in/jirisoljak)<br>
> Version: 2026-05-30

# Claude Code: Token monitoring, routing a optimalizace — přehled nástrojů (květen 2026)

*Výzkum provedený pomocí multi-agent deep research (103+ agentů, 21 zdrojů, adversarial verifikace claims)*

---

## Proč to čteš teď

Anthropic od **15. června 2026** mění billing model. Pokud používáš Claude Code — a zvláště pokud jedete headless, v CI/CD nebo přes Agent SDK — je dobré vědět co se mění a jaké nástroje existují pro sledování spotřeby.

---

## Co se mění 15. června — stručně

Anthropic rozděluje billing do dvou oddělených poolů:

| Pool | Co sem patří | Změna |
|---|---|---|
| **Interaktivní** | Claude.ai, Claude Code CLI v terminálu, Cowork | Beze změny — stejné subscription limity |
| **Agent SDK / programmatic** | `claude -p`, Agent SDK, GitHub Actions, ACP agenti | Nový měsíční kredit za full API sazby |

**Nové kreditové částky (Agent SDK pool):**
- Pro: $20/měsíc
- Max 5x: $100/měsíc
- Max 20x: $200/měsíc
- Bez rollover. Přečerpání = opt-in do API billing za standardní API sazby.

**Kdo to pocítí:** vývojáři jedoucí headless agenty, CI/CD pipeline, GitHub Actions. Dřív to šlo ze subsidizovaného subscription poolu — teď je to metrované.

**Kdo to nepocítí:** interaktivní uživatelé CLI a Cowork — jejich limity se nemění.

Bonus, který už platí od **6. května 2026**: Anthropic zdvojnásobil 5-hodinové rate limity a zrušil peak-hour throttling pro Pro a Max.

---

## 1. Token monitoring nástroje

Všechny community nástroje níže čtou lokální JSONL soubory ze `~/.claude/projects/` a `~/.claude/transcripts/`. **Fungují pouze pro CLI sessions** — server-side sessions (Cowork, API calls přes platformy třetích stran) v lokálních souborech nejsou.

### Claude-Code-Usage-Monitor
**Nejsilnější real-time CLI monitoring**

- Refresh 0.1–20 Hz, progress bary, burn rate analýza
- Sleduje 4 typy tokenů: input, output, cache_creation, cache_read
- 8.1k GitHub stars, aktivně udržovaný (v3.1.0)
- Vhodný pro: intenzivní session kde chceš vědět jak rychle hoříš

https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

### phuryn/claude-usage
**Nejlepší vizuální dashboard**

- Web UI, SQLite backend (`~/.claude/usage.db`), 30s auto-refresh
- Per-model cost breakdown, 7-day přehled po dnech
- Vhodný pro: denní/týdenní review spotřeby

https://github.com/phuryn/claude-usage

### ccusage
**CLI analytics, per-model breakdown**

- `--breakdown` flag pro přehled per model
- **Pozor: Bug #899** — cache_creation pricing počítá 1.25x místo správného 2x → ~19% podhodnocení nákladů
- Vhodný pro: rychlý CLI přehled, ale ověř si čísla jinde

https://github.com/ryoppippi/ccusage

### tokscale
**Per-session atribuce**

- Parsuje JSONL, `--group-by session,model`
- Vhodný pro: atribuci nákladů na konkrétní session nebo projekt
- Nový nástroj (v3.0.0, 28. 5. 2026) — ekosystém teprve zraje

https://github.com/junhoyeo/tokscale

### Claude Code Counter
**Chrome extension**

- Čte `~/.claude/projects/` přes Python Native Messaging
- Zobrazuje: context window usage (vs 200k limit), session tokens, cache metriky, tool calls, session duration
- 2.5s refresh v toolbaru
- Vhodný pro: vizuální přehled přímo v browseru během práce

https://github.com/akakarantzas/claude-code-counter

### TokenTracker
**Rate-limit okna pro 22 AI nástrojů**

- Reset countdowny pro Claude, Cursor, Gemini, Copilot, Kiro a další
- Cost breakdown pro 2200+ modelů přes LiteLLM databázi, offline snapshot
- Vhodný pro: uživatele více AI nástrojů zároveň

https://github.com/mm7894215/TokenTracker

---

## 2. Token optimalizace (méně tokenů = nižší spotřeba)

### RTK — Rust Token Killer
**Komprimuje výstupy terminálu před tím než je AI přečte**

- CLI proxy v Rustu, filtruje bash výstupy o 60–90 %
- Pokrývá 100+ příkazů: git, testy, build, Docker, AWS
- Funguje pouze pro Bash tool — Read/Grep ho obchází
- Vhodný pro: vývojáři kteří hodně používají CLI (git, buildy, testy)
- Nemá smysl pro dokumentový nebo skill-heavy workflow

https://github.com/rtk-ai/rtk

### Caveman
**Zkracuje výstupy Clauda ("jeskynní styl")**

- Skill pro Claude Code — instruuje Clauda mluvit ultra-stručně
- Průměrná úspora ~65–75 % output tokenů
- `caveman-compress` dokáže zkomprimovat MEMORY soubory o ~46 %
- Studie 2026-03: stručnější odpovědi paradoxně +26 bodů přesnosti
- **Pozor:** nevhodné pro generování dokumentů — kandidátské reporty, emaily, inzeráty atd. Výstupy budou příliš zkrácené.
- Vhodný pro: navigace, routing, stavové dotazy, debugging — ne dokumenty

https://github.com/JuliusBrussee/caveman

---

## 3. Model routing (automatický výběr modelu per task)

Žádný z níže uvedených nástrojů se nativně neintegruje do Claude Code CLI — všechny vyžadují proxy vrstvu nebo infrastrukturu.

### RouteLLM (LMSYS)
- Win-rate kalkulace per prompt → silný model pouze pokud výhoda překročí threshold
- Open-source, bez přímé Claude Code integrace
- Vhodný pro: vývojáři budující vlastní AI pipeline

https://github.com/lm-sys/RouteLLM

### LiteLLM proxy
Dva routery:
- **Complexity router** — keyword detection přes 7 dimenzí (tokenCount, codePresence, reasoningMarkers, ...), sub-millisecond latency, zero external API calls
- **Semantic router** — embedding similarity s configurable threshold 0.0–1.0

Vhodný pro: týmy s vlastní LLM proxy infrastrukturou

https://docs.litellm.ai/docs/proxy/auto_routing

### OpenRouter Auto Router
- NotDiamond powered routing, parametr `cost_quality_tradeoff` 0–10 (default 7)
- 0 = nejkvalitnější model, 10 = nejlevnější
- Bez příplatku za routing nad standard per-model cenu
- Vyžaduje přesměrování API calls na OpenRouter endpoint

https://openrouter.ai/docs/guides/routing/routers/auto-router

---

## 4. Officální Anthropic

### Claude Code Analytics Admin API
- Token usage breakdown per model: input, output, cache_read, cache_creation
- Estimated cost v USD
- **Pouze daily aggregated data s až 1h zpožděním** — ne real-time
- Vhodný pro: týmové dashboardy, billing reporting, správci platformy

https://platform.claude.com/docs/en/build-with-claude/claude-code-analytics-api

---

## Chybějící mezery v ekosystému

1. **Cowork / server-side sessions** — žádný community nástroj je nevidí. Pouze Anthropic Analytics API (daily).
2. **Integrované řešení** — žádný nástroj nekombinuje monitoring tokenů + model routing doporučení v jednom workflow.
3. **Budget alert** — žádný nástroj ti neřekne "za tímto taskem si dejte pauzu, blížíš se k reset oknu."

---

## Decision guide — co použít pro jaký profil

| Profil | Doporučení |
|---|---|
| Interaktivní CLI uživatel, chce přehled | phuryn/claude-usage + TokenTracker |
| Vývojář, intenzivní session, chce real-time | Claude-Code-Usage-Monitor |
| Vývojář, hodně bash/git/build | RTK + ccusage (ber s rezervou kvůli bugu) |
| Vývojář budující AI pipeline | RouteLLM nebo LiteLLM proxy |
| Multi-tool uživatel (Cursor, Copilot, ...) | TokenTracker |
| Tým, billing reporting | Anthropic Analytics Admin API |
| Chce ušetřit output tokeny (ne dokumenty) | Caveman |

---

## Poznámky k trvanlivosti

Ekosystém se mění rychle — TokenTracker v0.30.0 vyšel 29. 5., tokscale v3.0.0 den předtím. Doporučuji tento přehled považovat za aktuální k **květnu 2026** a ověřit kompatibilitu nástrojů po případných změnách formátu Anthropic JSONL souborů.

---

*Zdroje: GitHub README jednotlivých projektů, Anthropic Help Center, Zed blog, The Decoder, XDA Developers. Claims adversarially verified (3-vote systém).*
