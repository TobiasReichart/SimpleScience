"""Audio-Direktiven mit Anti-Jump-Logik (Höhe locken, Scroll verhindern).

- {audiocard} PFAD
    → einzelner Player, optional :caption:
- {audiolist}
    → Dropdown (oben) + Player, optional :caption:
      Zeilen: "Name = PFAD" ODER nur "PFAD"
"""
from __future__ import annotations
from typing import List, Tuple
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import html as _html


# ---------- Einzelner Player --------------------------------------------------
class AudioCardDirective(Directive):
    has_content = False
    required_arguments = 1               # 1: Pfad zur Audiodatei
    option_spec = {"caption": directives.unchanged}

    def run(self) -> List[nodes.Node]:
        audio_path = self.arguments[0]
        caption    = self.options.get("caption", "")

        title_html = f'<div class="audio-title">{_html.escape(caption)}</div>' if caption else ""

        # WICHTIG: Quelle direkt per src setzen (kein <source>-Tausch → weniger Reflow)
        html = (
            '<div class="audio-card">'
            f'  {title_html}'
            '  <div class="audio-frame">'
            f'    <audio controls preload="metadata" class="audio-element" '
            f'           aria-label="{_html.escape(caption or "Audio")}" '
            f'           src="{_html.escape(audio_path)}"></audio>'
            '  </div>'
            '</div>'
            '<script>'
            # JS: Höhe einmal messen/festsetzen + Scroll-Jumps beim Play verhindern
            '(function(){'
            '  var card  = document.currentScript.previousElementSibling;'
            '  var frame = card.querySelector(".audio-frame");'
            '  var aud   = card.querySelector("audio.audio-element");'
            '  if(!aud || !frame) return;'

            # (1) Höhe fixieren, sobald die Controls ihre endgültige Höhe haben
            '  var lockHeight = function(){'
            '    var h = aud.getBoundingClientRect().height;'
            '    if(h > 0){ frame.style.minHeight = Math.round(h) + "px"; }'
            '  };'
            '  if(aud.readyState >= 1){ lockHeight(); }'
            '  aud.addEventListener("loadedmetadata", lockHeight, {passive:true});'
            '  aud.addEventListener("loadeddata", lockHeight, {passive:true});'

            # (2) Beim Start die Scroll-Position konservieren (Browser fokussiert evtl. den Player)
            '  var restoreOnPlay = function(){'
            '    var y = window.pageYOffset || document.documentElement.scrollTop || 0;'
            '    try { aud.focus({preventScroll:true}); } catch(e) { /* older browsers */ }'
            '    setTimeout(function(){ window.scrollTo(0, y); }, 0);'
            '  };'
            '  aud.addEventListener("play", restoreOnPlay);'
            '})();'
            '</script>'
        )

        latex = rf"\textbf{{Audio:}} {caption or 'Datei'} ({audio_path})"
        text  = f"Audio: {caption or 'Datei'} ({audio_path})"

        return [nodes.raw("", html, format="html"),
                nodes.raw("", latex, format="latex"),
                nodes.raw("", text,  format="text")]


# ---------- Dropdown + Player -----------------------------------------------
class AudioListDirective(Directive):
    has_content = True
    required_arguments = 0
    option_spec = {"caption": directives.unchanged}

    def run(self) -> List[nodes.Node]:
        # Zeilen „Name = Pfad“ ODER nur „Pfad“ parsen
        items: List[Tuple[str, str]] = []
        for raw in self.content:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                name, path = [p.strip() for p in line.split("=", 1)]
            else:
                name, path = line, line
            items.append((name, path))

        caption   = self.options.get("caption", "")
        first_src = items[0][1] if items else ""

        # Options bauen (erster Eintrag selektiert)
        options_html = "\n".join(
            f'<option value="{_html.escape(path)}"{(" selected" if i==0 else "")}>{_html.escape(name)}</option>'
            for i, (name, path) in enumerate(items)
        )

        sel_id     = f"audio-select-{id(self)}"
        title_html = f'<div class="audio-title">{_html.escape(caption)}</div>' if caption else ""

        html = (
            '<div class="audio-card">'
            f'  {title_html}'
            '  <div class="audio-toolbar">'
            f'    <select id="' + sel_id + '" class="audio-select" aria-label="Audio auswählen">'
            f'      {options_html}'
            '    </select>'
            '  </div>'
            '  <div class="audio-frame">'
            f'    <audio controls preload="metadata" class="audio-element" '
            f'           aria-label="{_html.escape(caption or "Audio")}" '
            f'           src="{_html.escape(first_src)}"></audio>'
            '  </div>'
            '</div>'
            '<script>'
            '(function(){'
            '  var card  = document.currentScript.previousElementSibling;'
            '  var sel   = card.querySelector("select.audio-select");'
            '  var frame = card.querySelector(".audio-frame");'
            '  var aud   = card.querySelector("audio.audio-element");'
            '  if(!sel || !aud || !frame) return;'

            # (1) Höhe fixieren, sobald bekannt
            '  var lockHeight = function(){'
            '    var h = aud.getBoundingClientRect().height;'
            '    if(h > 0){ frame.style.minHeight = Math.round(h) + "px"; }'
            '  };'
            '  if(aud.readyState >= 1){ lockHeight(); }'
            '  aud.addEventListener("loadedmetadata", lockHeight, {passive:true});'
            '  aud.addEventListener("loadeddata", lockHeight, {passive:true});'

            # (2) Quelle wechseln → src direkt setzen; Scrollposition halten
            '  sel.addEventListener("change", function(){'
            '    var y = window.pageYOffset || document.documentElement.scrollTop || 0;'
            '    aud.pause();'
            '    aud.src = sel.value;'
            '    aud.load();'
            '    try { aud.focus({preventScroll:true}); } catch(e) {}'
            '    setTimeout(function(){ window.scrollTo(0, y); }, 0);'
            '  });'

            # (3) Auch bei „Play“ nach dem Wechsel Scroll-Jumps verhindern
            '  aud.addEventListener("play", function(){'
            '    var y = window.pageYOffset || document.documentElement.scrollTop || 0;'
            '    try { aud.focus({preventScroll:true}); } catch(e) {}'
            '    setTimeout(function(){ window.scrollTo(0, y); }, 0);'
            '  });'
            '})();'
            '</script>'
        )

        latex_lines = [rf"\textbf{{Audio-Liste:}} {caption or ''}"]
        latex_lines += [f"- {name} ({path})" for name, path in items]
        text_lines  = ["Audio-Liste: " + (caption or "")]
        text_lines  += [f"- {name} ({path})" for name, path in items]

        return [nodes.raw("", html, format="html"),
                nodes.raw("", "\n".join(latex_lines), format="latex"),
                nodes.raw("", "\n".join(text_lines),  format="text")]


def setup(app):
    app.add_directive("audiocard", AudioCardDirective)
    app.add_directive("audiolist", AudioListDirective)
    return {"version": "0.4", "parallel_read_safe": True, "parallel_write_safe": True}
