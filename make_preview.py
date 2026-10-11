"""Build preview.html from signs.html: same signs, but no Lock button, so a reviewer can't get stuck. Run after signs.html changes:
    python3 make_preview.py
"""
import pathlib

here = pathlib.Path(__file__).parent
s = (here / "signs.html").read_text(encoding="utf-8")

def swap(old, new):
    global s
    assert s.count(old) == 1, "signs.html changed shape near: " + old[:50]
    s = s.replace(old, new)

swap("<title>Event Signs — Purple Shark</title>", "<title>Event Signs Preview — Purple Shark</title>")
swap('try { locked = localStorage.getItem(LK) === "1"; } catch(e) {}', "")
swap("""\n  + '<button type="button" class="lk" data-lock="1">Lock</button>';""", ";")
swap('<div id="hint">Tap to switch</div>', '<div id="hint">Preview &middot; tap to switch signs</div>')
(here / "preview.html").write_text(s, encoding="utf-8")
print("wrote preview.html", len(s))
