---
name: excalidraw
description: Create Excalidraw diagrams programmatically. Use when the user wants architecture diagrams, flowcharts, or any visual diagram with a hand-drawn aesthetic, where editable output and drag-and-drop editing add value over Mermaid's text-only approach.
---

# Excalidraw Diagram Generator

Generate Excalidraw diagrams programmatically using Python. Produces professional-looking, editable `.excalidraw` files instead of ASCII art.

**Output format**: editable `.excalidraw` JSON files, not ASCII art. See Viewing the Output to open them and Exporting to PNG to render images.

**Token cost note**: Excalidraw JSON is verbose (4,000-22,000+ tokens per file). Delegate diagram generation to subagents when context is tight.

## Quick Start

### Method 1: Direct Python Script (Recommended)

## Locating the library

The generator library sits in `scripts/`, in the same directory as this file.
Resolve that directory to an absolute path and use it wherever the samples below
say `SCRIPTS`.

You already know the path: it is the directory you read this skill from, plus
`/scripts`. On Claude Code that resolves to
`${CLAUDE_PLUGIN_ROOT}/skills/draw/excalidraw/scripts`.

Do not guess a path. If you cannot resolve it, say so and stop.

Write a Python script using the generator library and run it:

```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, SCRIPTS)  # see "Locating the library" above
from excalidraw_generator import Diagram, Flowchart, ArchitectureDiagram

# Create your diagram
d = Diagram()
box1 = d.box(100, 100, "Step 1", color="blue")
box2 = d.box(300, 100, "Step 2", color="green")
d.arrow_between(box1, box2, "next")
d.save("my_diagram.excalidraw")
```

Run with:

```bash
python3 /path/to/your_script.py
```

### Method 2: Inline Python Execution

```bash
python3 -c "
import sys
sys.path.insert(0, SCRIPTS)  # see "Locating the library" above
from excalidraw_generator import Diagram

d = Diagram()
a = d.box(100, 100, 'Hello', color='blue')
b = d.box(300, 100, 'World', color='green')
d.arrow_between(a, b)
d.save('hello.excalidraw')
print('Created: hello.excalidraw')
"
```

---

## API Reference

### Diagram Class

The base class for all diagrams.

```python
from excalidraw_generator import Diagram

d = Diagram(background="#ffffff")  # white background
```

#### Methods

**`box(x, y, label, width=150, height=60, color="blue", shape="rectangle", font_size=18)`**

Create a labeled shape. Returns an `Element` for connecting.

- `x, y`: Position (top-left corner)
- `label`: Text to display
- `color`: "blue", "green", "red", "yellow", "orange", "violet", "cyan", "teal", "gray", "black"
- `shape`: "rectangle", "ellipse", "diamond"

```python
box1 = d.box(100, 100, "Process A", color="blue")
box2 = d.box(100, 200, "Decision?", color="yellow", shape="diamond")
```

**`text_box(x, y, content, font_size=20, color="black")`**

Create standalone text.

```python
d.text_box(100, 50, "System Architecture", font_size=28, color="black")
```

**`arrow_between(source, target, label=None, color="black", from_side="auto", to_side="auto")`**

Draw an arrow between two elements.

- `from_side`, `to_side`: "auto", "left", "right", "top", "bottom"

```python
d.arrow_between(box1, box2, "sends data")
d.arrow_between(box1, box3, from_side="bottom", to_side="top")
```

**`line_between(source, target, color="black")`**

Draw a line (no arrowhead) between elements.

**`save(path)`**

Save the diagram. Extension `.excalidraw` added if not present.

```python
d.save("output/my_diagram")  # Creates output/my_diagram.excalidraw
```

---

### Flowchart Class

Specialized for flowcharts with automatic positioning.

```python
from excalidraw_generator import Flowchart

fc = Flowchart(direction="vertical", spacing=80)

fc.start("Begin")
fc.process("p1", "Process Data")
fc.decision("d1", "Valid?")
fc.process("p2", "Save")
fc.end("Done")

fc.connect("__start__", "p1")
fc.connect("p1", "d1")
fc.connect("d1", "p2", label="Yes")
fc.connect("d1", "__end__", label="No")

fc.save("flowchart.excalidraw")
```

#### Methods

- `start(label="Start")` - Green ellipse
- `end(label="End")` - Red ellipse
- `process(node_id, label, color="blue")` - Blue rectangle
- `decision(node_id, label, color="yellow")` - Yellow diamond
- `node(node_id, label, shape, color, width, height)` - Generic node
- `connect(from_id, to_id, label=None)` - Arrow between nodes
- `position_at(x, y)` - Set position for next node

---

### AutoLayoutFlowchart Class

For complex flowcharts with automatic hierarchical layout. Requires `grandalf` package (`pip install grandalf`).

```python
from excalidraw_generator import AutoLayoutFlowchart, DiagramStyle, FlowchartStyle, LayoutConfig

fc = AutoLayoutFlowchart(
    diagram_style=DiagramStyle(roughness=0),
    flowchart_style=FlowchartStyle(decision_color="orange"),
    layout_config=LayoutConfig(vertical_spacing=100, horizontal_spacing=80)
)

fc.add_node("start", "Start", shape="ellipse", color="green", node_type="terminal")
fc.add_node("process1", "Validate Input", node_type="process")
fc.add_node("check", "Is Valid?", shape="diamond", color="yellow", node_type="decision")
fc.add_node("success", "Process Data", node_type="process")
fc.add_node("error", "Show Error", color="red", node_type="process")
fc.add_node("end", "End", shape="ellipse", color="red", node_type="terminal")

fc.add_edge("start", "process1")
fc.add_edge("process1", "check")
fc.add_edge("check", "success", label="Yes")
fc.add_edge("check", "error", label="No")
fc.add_edge("success", "end")
fc.add_edge("error", "process1", label="Retry")

result = fc.compute_layout(two_column=True, target_aspect_ratio=0.8)
fc.save("auto_flowchart.excalidraw")
```

---

### ArchitectureDiagram Class

For system architecture diagrams.

```python
from excalidraw_generator import ArchitectureDiagram

arch = ArchitectureDiagram()

arch.user("user", "User", x=100, y=200)
arch.component("frontend", "React App", x=250, y=200, color="blue")
arch.service("api", "API Gateway", x=450, y=200, color="violet")
arch.database("db", "PostgreSQL", x=650, y=200, color="green")

arch.connect("user", "frontend", "HTTPS")
arch.connect("frontend", "api", "REST")
arch.connect("api", "db", "SQL")

arch.save("architecture.excalidraw")
```

#### Methods

- `component(id, label, x, y, width=150, height=80, color="blue")`
- `database(id, label, x, y, color="green")` - Ellipse shape
- `service(id, label, x, y, color="violet")`
- `user(id, label="User", x=100, y=100)` - Gray ellipse
- `connect(from_id, to_id, label=None, bidirectional=False)`

---

## Configuration & Styling

### DiagramStyle - Global Appearance

```python
from excalidraw_generator import Diagram, DiagramStyle

d = Diagram(diagram_style=DiagramStyle(
    roughness=0,              # 0=clean, 1=hand-drawn, 2=rough sketch
    stroke_style="solid",     # "solid", "dashed", "dotted"
    stroke_width=2,           # Line thickness (1-4)
    color_scheme="corporate"  # Named color scheme
))
```

**Roughness levels:**

- `0` - Architect: Clean, precise lines
- `1` - Artist: Normal hand-drawn look (default)
- `2` - Cartoonist: Rough, sketchy appearance

### Color Schemes

```python
d = Diagram(diagram_style=DiagramStyle(color_scheme="vibrant"))

primary = d.scheme_color("primary")
secondary = d.scheme_color("secondary")
accent = d.scheme_color("accent")
warning = d.scheme_color("warning")
danger = d.scheme_color("danger")
neutral = d.scheme_color("neutral")
```

| Scheme     | Primary | Secondary | Accent | Warning | Danger |
| ---------- | ------- | --------- | ------ | ------- | ------ |
| default    | blue    | green     | violet | yellow  | red    |
| monochrome | black   | gray      | gray   | gray    | black  |
| corporate  | blue    | teal      | violet | orange  | red    |
| vibrant    | violet  | cyan      | orange | yellow  | red    |
| earth      | teal    | green     | orange | yellow  | red    |

### Color Reference

| Color    | Stroke Hex | Use For             |
| -------- | ---------- | ------------------- |
| `blue`   | #1971c2    | Primary components  |
| `green`  | #2f9e44    | Success, databases  |
| `red`    | #e03131    | Errors, end states  |
| `yellow` | #f08c00    | Warnings, decisions |
| `orange` | #e8590c    | Highlights          |
| `violet` | #6741d9    | Services            |
| `cyan`   | #0c8599    | Network             |
| `teal`   | #099268    | Secondary           |
| `gray`   | #868e96    | Users, actors       |
| `black`  | #1e1e1e    | Text, arrows        |

---

## Complete Examples

### Example 1: Simple Flow

```python
import sys
sys.path.insert(0, SCRIPTS)  # see "Locating the library" above
from excalidraw_generator import Diagram

d = Diagram()
d.text_box(200, 30, "Data Processing Pipeline", font_size=24)

input_box = d.box(100, 100, "Input", color="gray")
process = d.box(300, 100, "Process", color="blue")
output = d.box(500, 100, "Output", color="green")

d.arrow_between(input_box, process, "raw data")
d.arrow_between(process, output, "results")

d.save("pipeline.excalidraw")
```

### Example 2: Decision Flowchart

```python
import sys
sys.path.insert(0, SCRIPTS)  # see "Locating the library" above
from excalidraw_generator import Flowchart

fc = Flowchart(direction="vertical", spacing=100)

fc.start("User Request")
fc.process("auth", "Authenticate")
fc.decision("valid", "Valid Token?")

fc.position_at(300, 340)
fc.process("proc", "Process Request")
fc.process("resp", "Return Response")

fc.position_at(100, 340)
fc.process("err", "Return 401")

fc.connect("__start__", "auth")
fc.connect("auth", "valid")
fc.connect("valid", "proc", "Yes")
fc.connect("valid", "err", "No")
fc.connect("proc", "resp")

fc.save("auth_flow.excalidraw")
```

### Example 3: Microservices Architecture

```python
import sys
sys.path.insert(0, SCRIPTS)  # see "Locating the library" above
from excalidraw_generator import ArchitectureDiagram

arch = ArchitectureDiagram()

arch.user("client", "Client", x=400, y=50)
arch.service("gateway", "API Gateway", x=350, y=180, color="violet")

arch.service("auth", "Auth Service", x=100, y=350, color="blue")
arch.service("users", "User Service", x=300, y=350, color="blue")
arch.service("orders", "Order Service", x=500, y=350, color="blue")
arch.service("notify", "Notification", x=700, y=350, color="cyan")

arch.database("authdb", "Auth DB", x=100, y=500, color="green")
arch.database("userdb", "User DB", x=300, y=500, color="green")
arch.database("orderdb", "Order DB", x=500, y=500, color="green")

arch.component("queue", "Message Queue", x=600, y=450, color="orange")

arch.connect("client", "gateway", "HTTPS")
arch.connect("gateway", "auth", "gRPC")
arch.connect("gateway", "users", "gRPC")
arch.connect("gateway", "orders", "gRPC")
arch.connect("auth", "authdb", "SQL")
arch.connect("users", "userdb", "SQL")
arch.connect("orders", "orderdb", "SQL")
arch.connect("orders", "queue", "publish")
arch.connect("queue", "notify", "subscribe")

arch.save("microservices.excalidraw")
```

---

## Viewing the Output

After generating a `.excalidraw` file:

1. **Excalidraw.com**: Go to <https://excalidraw.com> and drag the file onto the canvas
2. **VS Code**: Install the "Excalidraw" extension, then open the file
3. **CLI**: Use `open filename.excalidraw` on macOS

## Exporting to PNG

```bash
# First time setup
cd "$SCRIPTS"
npm install
npx playwright install chromium

# Export
node "$SCRIPTS/export_playwright.js" diagram.excalidraw output.png
```

## Tips

1. **Positioning**: Use a grid system. Start shapes at multiples of 50 or 100 for alignment
2. **Spacing**: Leave 50-100px between elements for clean arrows
3. **Labels**: Keep labels short (2-3 words). Use text boxes for longer descriptions
4. **Colors**: Use consistent colors for similar components (all databases green, all services blue)
5. **Layout patterns**:
   - **Horizontal flow**: x increases, y constant
   - **Vertical flow**: y increases, x constant
   - **Grid**: Combine both for complex diagrams
6. **After generation**: Open in Excalidraw to fine-tune positions and add hand-drawn elements

## See Also

- `/mermaid` - For inline documentation diagrams that render natively on GitHub
- `/design` - Design thinking applies to diagram composition and layout
- `/prose` - Diagram labels benefit from the same concision rules as prose
