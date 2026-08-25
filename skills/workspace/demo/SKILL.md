---
name: demo
description: Record a video demo (mp4) of a UI change working by driving the app through a shot-scraper video YAML storyboard. Use when asked to record a demo, capture video evidence of a frontend change working, or when ship runs with --demo.
argument-hint: [flow to demonstrate]
---

# Demo

Turn a UI change into a short mp4 that proves the flow works: write a YAML storyboard, let `shot-scraper video` drive Playwright through it, and deliver the recording. Every `wait_for` in the storyboard is both synchronization and evidence: the run only completes if each expected state actually appeared.

## Prerequisites

- `shot-scraper --version` must be 1.10+. If missing: `uv tool install shot-scraper && shot-scraper install` (the second command downloads Chromium).
- `--mp4` conversion needs `ffmpeg` on PATH; without it you still get the WebM.
- The storyboard format is fully documented in `shot-scraper video --help` (top-level keys, scene keys, every action). Read it before writing the first storyboard of a session instead of guessing from memory.

## Steps

### 1. Pick the flow

From `$ARGUMENTS`, or from the working diff when invoked without arguments: identify the one user-visible interaction that demonstrates the change. One tight flow, roughly 15-45 seconds. A demo shows the changed behavior, not a site tour. If the diff has no user-visible surface, say so and stop.

### 2. Get the app running

Use the project's documented dev-server command (nearest CLAUDE.md, or the `run` skill's knowledge). Two options:

- Point `url:` at an already-running server you started yourself.
- Put the launch command in the storyboard's `server:` key so shot-scraper owns the lifecycle. Prefer this; gate the opening scene with `wait_for` so cold starts don't record blank frames.

`url:` also accepts a local HTML file path (relative to the invocation cwd) for component-level demos with no server.

A `server:` command runs in the invocation cwd too. Since the storyboard lives in the scratchpad, you invoke from there, so a command written for the project root fails to spawn. Use absolute paths, or the toolchain's own escape hatch (`uv run --directory <repo>`, `npm --prefix <repo>`).

### 3. Write the storyboard

Write it in the session scratchpad. Working shape:

```yaml
output: demo.webm
url: http://localhost:8080/some/page
viewport:
  width: 1280
  height: 720
cursor: true
wait_for: "text=Page heading"
scenes:
  - name: Fill and submit the form
    do:
      - click: "#field-tci"
      - fill: { into: "#field-tci", text: "example" }
      - click: "button:has-text('Save')"
      - wait_for: "text=Saved"
      - pause: 1
```

- Scene names read like narration beats; they show in progress output.
- Gate every state transition with `wait_for` / `wait_for_url`. That is what makes the recording verification evidence rather than a hopeful screencast.
- Selectors are Playwright syntax. Prefer `text=`, `:has-text()`, and ids over deep CSS chains; those survive markup churn and fail with readable timeouts.
- Every selector runs in strict mode: matching two elements is an error, not a silent first match. Anchor each `wait_for` to something unique — `#stackcount:has-text('3 skills')` over `text=3 skills`, which also matches every ancestor — or say `>> nth=0` and mean it.

### 4. Record

```bash
shot-scraper video storyboard.yml -o demo.webm --mp4
```

Logged-in flows: capture cookies first with `shot-scraper auth <url> auth.json`, then pass `--auth auth.json`. The auth command opens a real browser for a human to log in, so ask the user to run it themselves (suggest `! shot-scraper auth ...`).

On a selector timeout, fix the selector or add a missing `wait_for` and re-run. Two failures on the same step means the assumption about the page is wrong: re-inspect the actual DOM before a third try.

### 5. Verify the recording

A completed run already proves each `wait_for` state appeared. Extract the final frame too, and look at it to confirm the video shows what it should:

```bash
ffmpeg -sseof -0.5 -i demo.mp4 -frames:v 1 -y last-frame.png
```

Read the frame image. For longer demos, add `screenshot:` actions at key states inside scenes and review those.

### 6. Deliver

Copy the mp4 to `~/Desktop/demos/` (create if needed) named `<repo>-<branch-slug>-<flow-slug>.mp4`, and report that path. GitHub PR descriptions accept a drag-dropped mp4; `gh` cannot attach videos, so leave the upload to the user.

### 7. Leave it reproducible, when the demo ships

A demo that lands in the repo — in the README, in docs, as the project's shopfront — outlives the session that recorded it and goes stale with nothing to re-run. Commit the storyboard beside the video and give it a recipe:

- Move the storyboard out of the scratchpad (`scripts/demo.yml`) and re-record from that copy, so the committed video is the committed script's output.
- Wrap the run the way the project already scripts its UI checks: same port guard, same server start, same wait on a ready endpoint.
- Pick elements by position (`article.card >> nth=0`) rather than by name, so the storyboard records whatever data a teammate has.
- Write to a gitignored path by default and publish over the committed video only on request.

For a README, commit a GIF too. GitHub strips a `<video>` pointing at a repo path — only files on its own CDN get a player — so the mp4 renders as a link and nothing more:

```bash
ffmpeg -i demo.mp4 -vf "fps=10,scale=800:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" -loop 0 demo.gif
```

At 800px and 10fps a 15-second GIF runs about 1.5 MB against 650 KB of mp4. Embed the GIF, link the mp4 under it.

## Gotchas

- `--mp4` silently requires ffmpeg; the WebM is always written regardless.
- Never pipe the command into `tail` or `head`. The server child inherits stdout, so the pipe stays open long after the run ends and the whole thing reads as a hang. Redirect to a log file and read that.
- Headless Chromium refuses `navigator.clipboard.writeText`. A button that flips to "Copied" inside a `.then()` never flips, and the scene burns the full timeout. Stub the write in top-level `javascript:`, then prove the real path ran with a `js:` action that throws unless the app handed the stub the right text.
- For local dev apps, mint the session non-interactively instead of asking the user to run `shot-scraper auth`: log in via the app's dev-login endpoint with curl and write the cookies into a Playwright storage-state JSON yourself. Include every auth-adjacent cookie (e.g. csrftoken alongside sessionid); a missing one can leave the SPA booting but silently never firing API calls.
- An SPA stuck on its loading spinner usually means a boot API call is failing, not that the page is slow. Don't diagnose with screenshots; drive the page once with a browser tool that captures console and network (a 500 from a pending migration renders as an eternal spinner).
- Generated input ids (`id="gen-id-43"`-style) change across page loads. Anchor selectors to visible label text instead, e.g. `div:has(> label:text-is("Field Label")) input`, and click the label itself for custom checkboxes whose real input is visually hidden.
- Dry-run the exact flow once in a live browser (Playwright MCP) before recording, then transcribe it into the storyboard. If the dry run saved data, reset the state before recording so the video shows the change from scratch.
- Dev servers with slow cold starts record blank frames unless the opening scene gates on `wait_for`.
- Every `pause:` second inflates the runtime and file. Use pauses only where a viewer needs a beat to read the result; keep the total under about a minute.
- Storyboards are Pydantic-validated. A validation error names the offending key exactly; read it instead of rewriting the file by feel.
- Recording at a custom viewport needs playwright 1.61+ in shot-scraper's venv. The uv tool install of shot-scraper 1.10 already satisfies this; only debug it if dimensions come out wrong.
- Do not hand the storyboard fields from memory to a teammate or doc; `shot-scraper video --help` is the source of truth and newer releases add actions.
