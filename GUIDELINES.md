# M5Stack Development Guidelines

## UI Library Choice

**IMPORTANT: Use M5UI (Widgets) library only - NOT M5GFX**

### Rationale
- M5UI and M5GFX do not mix well in the same project
- M5UI (via `Widgets`) provides higher-level UI components
- M5GFX is lower-level graphics operations

### Import Pattern
```python
import M5
from M5 import Widgets  # Use this for M5UI
import time
```

### DO NOT USE
```python
from M5 import *  # Avoid wildcard imports
import M5GFX     # Do not mix with M5UI
```

### Common M5UI Components
- `Widgets.fillScreen(color)` - Fill entire screen
- `Widgets.Label(text, x, y, scale, fg_color, bg_color, font)` - Create text label
- `M5.begin()` - Initialize M5Stack
- `M5.update()` - Update M5 state (call in loop)
- `M5.Touch.getCount()` - Get number of touch points
- `M5.Touch.getDetail(index)` - Get touch details

### Label Methods
- `label.setText(text)` - Update label text
- `label.setColor(fg_color, bg_color)` - Update colors
- `label.setVisible(visible)` - Show/hide label

### Color Format
Colors use 24-bit RGB hex format:
- `0xFF0000` - Red
- `0x00FF00` - Green
- `0x0000FF` - Blue
- `0xFFFFFF` - White
- `0x000000` - Black
