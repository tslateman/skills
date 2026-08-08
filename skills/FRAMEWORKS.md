# Frameworks Index

Each skill is grounded in a named framework or authority. This index maps the intellectual foundations to the skills that apply them.

## Skills by Framework

| Framework                        | Authority                    | Skill                                                                               | Core Idea                                                                                |
| -------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Local-Fix Debt                   | This repo                    | the six `*-review` skills                                                           | Clearing a failure signal and fixing its cause are different operations                  |
| Test Desiderata                  | Kent Beck                    | `/testing`                                                                          | 12 properties every test balances; make tradeoffs deliberate                             |
| Testing Trophy                   | Kent C. Dodds                | `/testing`                                                                          | Integration tests provide the best confidence-to-cost ratio                              |
| Elements of Style                | William Strunk Jr.           | `/prose`                                                                            | Active voice, omit needless words, be specific                                           |
| ASD-STE100                       | AeroSpace and Defence        | `/ste`                                                                              | Controlled English for text a reader executes rather than considers                      |
| Naming Principles                | Benner                       | `/naming`                                                                           | Understandability, conciseness, consistency, distinguishability                          |
| API Design                       | Joshua Bloch                 | `/naming`, `/design`                                                                | Self-documenting, least astonishment, minimal surface                                    |
| Ubiquitous Language              | Eric Evans (DDD)             | `/naming`, `/lexicon`                                                               | A translation layer between domain and code is a defect                                  |
| Controlled Vocabulary            | ANSI/NISO Z39.19             | `/lexicon`                                                                          | One term, one meaning; every rejected variant points back to its preferred form          |
| ADR Format                       | Michael Nygard               | `/adr`                                                                              | Capture context and reasoning, not just the decision                                     |
| Modern Code Review               | Bacchelli & Bird             | `/code-review`                                                                      | Code review's primary value is knowledge transfer, not defect detection                  |
| Information Architecture         | Rosenfeld, Morville & Arango | `/ia`                                                                               | Organization, labeling, navigation, search for findability                               |
| Diataxis                         | Daniele Procida              | `/ia`                                                                               | Four documentation modes: tutorial, how-to, explanation, reference                       |
| LATCH                            | Richard Saul Wurman          | `/ia`                                                                               | Five and only five ways to organize: location, alphabet, time, category, hierarchy       |
| Eight Principles of IA           | Dan Brown                    | `/ia`, `/wayfinding`                                                                | Objects, choices, disclosure, exemplars, front doors, classification, navigation, growth |
| Ontology, Taxonomy, Choreography | Peter Morville               | `/ia`                                                                               | Meaning, arrangement, and behavior over time are three separable layers                  |
| The Image of the City            | Kevin Lynch                  | `/wayfinding`                                                                       | Legibility comes from paths, edges, districts, nodes, and landmarks                      |
| Information Foraging             | Pirolli & Card               | `/wayfinding`                                                                       | Readers act on scent, not content; they abandon a path before reaching it                |
| Wayfinding                       | Arthur & Passini             | `/wayfinding`                                                                       | Put the signage at the decision point, not everywhere                                    |
| C4 Model                         | Simon Brown                  | `/system-map`                                                                       | One system, four zoom levels, one audience per diagram                                   |
| A Philosophy of Software Design  | John Ousterhout              | `/ousterhout-software-design`, `/maintainability`, `/improve-codebase-architecture` | Leverage at the interface — large behaviour behind small surface                         |
| Refactoring                      | Martin Fowler                | `/refactor`, `/maintainability`                                                     | Small verified steps, observable behavior held constant                                  |
| Clean Code                       | Robert C. Martin             | `/maintainability`                                                                  | Names and functions as the unit of readability                                           |
| Seams & Adapters                 | Michael Feathers             | `/improve-codebase-architecture`                                                    | Alter behaviour without editing in place; the interface is the test surface              |
| Design It Twice                  | John Ousterhout              | `/improve-codebase-architecture`, `/design`                                         | First idea is unlikely to be best — produce radically different alternatives             |
| Deep Modules & Domain Engines    | DDD lineage                  | `/strategic-architecture-analyzer`                                                  | Procedural transliteration and anemic models leak invariants outward                     |
| Diverge Then Converge            | Design Council               | `/brainstorm`, `/spec-out`                                                          | Separate generative mode from evaluative mode                                            |
| 5 Whys                           | Sakichi Toyoda (Toyota)      | `/automagic-problem-discovery`                                                      | Dig past the symptom to the leverage point underneath it                                 |
| Judgment Linting                 | Anthropic eval methodology   | `/vibe-check`                                                                       | Higher-order code assertions that require AI reasoning, not regexes                      |
| Compression Mode                 | mattpocock/skills            | `/bro`                                                                              | Strip a reply to the claim underneath it                                                 |
| Map Before Streets               | mattpocock/skills            | `/zoom-out`                                                                         | Map callers, neighbors, and abstraction layers before reading details                    |
| Visual Recap                     | BuilderIO/skills             | `/visual-recap`                                                                     | Map a diff to structured blocks before reading raw lines                                 |
| Skill Craft                      | mattpocock/skills            | `/writing-great-skills`                                                             | Predictability via leading words, information hierarchy, and pruning                     |
| Mermaid.js v11                   | Mermaid project              | `/mermaid`                                                                          | Text-based diagrams that render natively in GitHub markdown                              |
| Excalidraw Generator             | Excalidraw project           | `/excalidraw`                                                                       | Programmatic hand-drawn diagrams via Python API                                          |

## Skills by Concern

| Concern                                  | Primary Skill                    | Supporting Skills                          |
| ---------------------------------------- | -------------------------------- | ------------------------------------------ |
| "Did the agent silence this or fix it?"  | the matching `*-review`          | `/vibe-check`, `/code-review`              |
| "Would these tests catch a regression?"  | `/test-review`                   | `/testing`                                 |
| "Is this well-tested?"                   | `/testing`                       | `/test-review`, `/code-review`             |
| "Will this stay cheap to change?"        | `/maintainability`               | `/ousterhout-software-design`, `/refactor` |
| "Where should we refactor?"              | `/improve-codebase-architecture` | `/zoom-out`, `/naming`, `/design`          |
| "Execute this restructure safely"        | `/refactor`                      | `/maintainability`, `/testing`             |
| "Is this well-designed?"                 | `/design`                        | `/naming`, `/adr`                          |
| "Is this well-named?"                    | `/naming`                        | `/design`, `/lexicon`                      |
| "Do we all mean the same thing?"         | `/lexicon`                       | `/naming`, `/ia`                           |
| "Can people find this?"                  | `/ia`                            | `/naming`, `/wayfinding`                   |
| "Can people orient once they land?"      | `/wayfinding`                    | `/ia`, `/zoom-out`                         |
| "How does this system fit together?"     | `/system-map`                    | `/zoom-out`, `/mermaid`                    |
| "I'm lost in this code"                  | `/zoom-out`                      | `/naming`, `/system-map`                   |
| "Is this well-written?"                  | `/prose`                         | `/slop-check`, `/code-review`              |
| "Could anyone have written this?"        | `/slop-check`                    | `/prose`                                   |
| "Does this sound like me?"               | `/voice`                         | `/slop-check`                              |
| "Can the reader execute it?"             | `/ste`                           | `/prose`                                   |
| "Do I understand what I just committed?" | `/narrate`                       | `/code-review`                             |
| "Should we document this decision?"      | `/adr`                           | `/code-review`, `/research`                |
| "What should we use?"                    | `/research`                      | `/adr`                                     |
| "I don't know what I want yet"           | `/spec-out`                      | `/brainstorm`                              |
| "I know the goal, not the options"       | `/brainstorm`                    | `/research`, `/design`                     |
| "What should I automate?"                | `/automagic-problem-discovery`   | `/research`, `/adr`                        |
| "Does this vibe-coded output hold up?"   | `/vibe-check`                    | `/code-review`, `/naming`                  |
| "How should I visualize this?"           | `/mermaid`                       | `/excalidraw`, `/system-map`               |
| "Show me what changed"                   | `/visual-recap`                  | `/code-review`                             |
| "Cut my output, save tokens"             | `/bro`                           | `/prose`                                   |
| "Am I writing a good skill?"             | `/writing-great-skills`          | `/prose`, `/ia`                            |

## Recipes

Recipes teach a multi-agent orchestrator how to decompose a domain task into parallel workers. Each defines worker scope boundaries, prompt templates, and a synthesis step for the manager.

| Skill           | Recipe                          | Workers | Mode       |
| --------------- | ------------------------------- | ------- | ---------- |
| `/brainstorm`   | `shape/brainstorm/RECIPE.md`    | —       | parallel   |
| `/design`       | `craft/design/RECIPE.md`        | 3       | parallel   |
| `/prose`        | `writing/prose/RECIPE.md`       | 3       | parallel   |
| `/research`     | `shape/research/RECIPE.md`      | 2       | parallel   |
| `/code-review`  | `review/code-review/RECIPE.md`  | 4       | parallel   |
| `/spec-out`     | `shape/spec-out/RECIPE.md`      | —       | sequential |
| `/testing`      | `craft/testing/RECIPE.md`       | 2       | parallel   |
| `/visual-recap` | `review/visual-recap/RECIPE.md` | —       | parallel   |

`/brainstorm` runs independent lenses concurrently; `/spec-out` runs sequentially because each round builds on the previous answers. That split is the Diverge Then Converge principle made operational.

## Cross-References

Skills that pair naturally:

- `/*-review` + `/vibe-check` — The language review hunts one debt class; vibe-check reads the whole energy of the change
- `/test-review` + `/testing` — Test-review audits whether a suite can fail; testing designs what it should cover
- `/maintainability` + `/refactor` — Maintainability names the problems; refactor executes the cure in verified steps
- `/improve-codebase-architecture` + `/zoom-out` — Render the map first, then propose which modules to deepen against it
- `/code-review` + `/naming` — Code review surfaces naming problems; naming review deepens code review
- `/naming` + `/lexicon` — Naming judges one name; lexicon judges a term set for consistency across surfaces
- `/ia` + `/wayfinding` — IA fixes the structure; wayfinding fixes orientation inside it
- `/ia` + `/naming` — IA labeling problems are naming problems
- `/wayfinding` + `/zoom-out` — Zoom-out builds the map on demand; wayfinding changes the territory so the map is unnecessary
- `/system-map` + `/mermaid` — The map is the argument; mermaid is how it renders
- `/mermaid` + `/excalidraw` — Mermaid for inline docs (GitHub-native); Excalidraw for architecture overviews (hand-drawn, editable)
- `/prose` + `/slop-check` — Slop-check scores and refuses to rewrite; prose is the fixing half
- `/slop-check` + `/voice` — Genericness first, authorship second; a draft failing the first fails the second
- `/ste` + `/prose` — STE for text a reader executes, prose for text a reader considers
- `/narrate` + `/code-review` — Narrate gates comprehension before the commit; review catches what comprehension missed
- `/adr` + `/research` — Research informs the decision; ADR captures it
- `/spec-out` + `/brainstorm` — Spec-out when you don't know what you want; brainstorm when you know what but not how
- `/automagic-problem-discovery` + `/adr` — Discovery builds the fix; the ADR records why that fix over the alternatives
- `/freeze` + any review — Scope the edits before letting an agent apply findings
