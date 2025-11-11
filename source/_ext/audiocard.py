"""Audio-Direktiven mit optionaler Bildanzeige pro Auswahl.

- {audiocard} PFAD
    → einzelner Player mit optionaler :caption:
- {audiolist}
    → Dropdown (oben) + Player + (optional) zentrierte Grafik darunter
      Zeilenformat im Block:
        "Name = AUDIO_PFAD"
        "Name = AUDIO_PFAD | image=GRAFIK_PFAD"
      Beispiel:
        A4 440 Hz = _static/audio/A4_440Hz.mp3 | image=_static/img/A4.svg
"""
from __future__ import annotations
from typing import List, Tuple, Dict
from docutils import nodes
from docutils.parsers.rst import Directive, directives
import html as _html

# --- NEU: Hilfsfunktion, die Pfade relativ zur aktuellen Seite macht ---------
def _relurl(env, path: str) -> str:
    """
    Macht aus '_static/...' oder '_images/...' eine zur aktuellen Seite passende
    relative URL, z. B. '../_static/...', '../../_images/...'.
    Führende Slashes und Backslashes werden entfernt.
    """
    if not path:
        return path
    depth = env.docname.count("/")         # 'kapitel/eins' → 1 → '../'
    prefix = "../" * depth
    clean = path.lstrip("/").replace("\\", "/")
    return prefix + clean
# -----------------------------------------------------------------------------


# ----------------------- Einzelner Player ------------------------------------
class AudioCardDirective(Directive):
    has_content = False
    required_arguments = 1  # Audiodatei (mp3/wav)
    option_spec = {"caption": directives.unchanged}

    def run(self) -> List[nodes.Node]:
        env      = self.state.document.settings.env    # ← NEU: env holen
        audio_in = self.arguments[0]                   # z. B. "_static/audio/A4.mp3"
        audio    = _relurl(env, audio_in)              # ← NEU: Pfad relativieren
        caption  = self.options.get("caption", "")

        title_html = f'<div class="audio-title">{_html.escape(caption)}</div>' if caption else ""
        html = (
            '<div class="audio-card">'
            f'  {title_html}'
            '  <div class="audio-frame">'
            f'    <audio controls preload="metadata" class="audio-element" '
            f'           aria-label="{_html.escape(caption or "Audio")}" '
            f'           src="{_html.escape(audio)}"></audio>'
            '  </div>'
            '</div>'
        )

        latex = rf"\textbf{{Audio:}} {caption or 'Datei'} ({audio_in})"
        text  = f"Audio: {caption or 'Datei'} ({audio_in})"

        return [nodes.raw("", html, format="html"),
                nodes.raw("", latex, format="latex"),
                nodes.raw("", text,  format="text")]


# ----------------------- Liste: Dropdown + Player + Bild ---------------------
class AudioListDirective(Directive):
    has_content = True
    required_arguments = 0
    option_spec = {"caption": directives.unchanged}

    def _parse_line(self, line: str) -> Dict[str, str]:
        """Parst eine Zeile 'Name = audio | image=pfad' in dict."""
        entry: Dict[str, str] = {}
        if "=" in line:
            name, right = [p.strip() for p in line.split("=", 1)]
        else:
            name, right = line, line
        entry["name"] = name

        parts = [p.strip() for p in right.split("|")]
        entry["audio"] = parts[0].strip()
        for extra in parts[1:]:
            if "=" in extra:
                k, v = [x.strip() for x in extra.split("=", 1)]
                entry[k.lower()] = v
        return entry

    def run(self) -> List[nodes.Node]:
        env = self.state.document.settings.env  # ← NEU

        # Zeilen einlesen → Liste von Dicts: {"name","audio","image"?}
        items: List[Dict[str, str]] = []
        for raw in self.content:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            items.append(self._parse_line(line))

        caption   = self.options.get("caption", "")
        # ← NEU: Startquellen relativieren
        first_src = _relurl(env, items[0]["audio"]) if items else ""
        first_img_raw = items[0].get("image", "") if items else ""
        first_img = _relurl(env, first_img_raw) if first_img_raw else ""

        # Dropdown-Optionen: value = rel. Audio-URL, data-img = rel. Bild-URL
        options_html = []
        for i, it in enumerate(items):
            sel   = " selected" if i == 0 else ""
            name  = _html.escape(it["name"])
            audio = _html.escape(_relurl(env, it["audio"]))                # ← NEU
            img   = _html.escape(_relurl(env, it.get("image",""))) if it.get("image") else ""  # ← NEU
            options_html.append(
                f'<option value="{audio}" data-img="{img}"{sel}>{name}</option>'
            )
        options_html = "\n".join(options_html)

        sel_id = f"audio-select-{id(self)}"
        title_html = f'<div class="audio-title">{_html.escape(caption)}</div>' if caption else ""
        fig_style = '' if first_img else ' style="display:none"'
        first_img_attr = _html.escape(first_img) if first_img else ""

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
            f'  <figure class="audio-figure"{fig_style}>'
            f'    <img class="audio-image" src="{first_img_attr}" alt="Abbildung zum ausgewählten Ton">'
            '  </figure>'
            '</div>'
            '<script>'
            '(function(){'
            '  var card  = document.currentScript.previousElementSibling;'
            '  var sel   = card.querySelector("select.audio-select");'
            '  var frame = card.querySelector(".audio-frame");'
            '  var aud   = card.querySelector("audio.audio-element");'
            '  var fig   = card.querySelector(".audio-figure");'
            '  var img   = card.querySelector(".audio-image");'
            '  if(!sel || !aud || !frame || !fig || !img) return;'

            # Höhe stabilisieren
            '  var lockHeight = function(){'
            '    var h = aud.getBoundingClientRect().height;'
            '    if(h > 0){ frame.style.minHeight = Math.round(h) + "px"; }'
            '  };'
            '  if(aud.readyState >= 1){ lockHeight(); }'
            '  aud.addEventListener("loadedmetadata", lockHeight, {passive:true});'

            # Quelle + Bild wechseln
            '  sel.addEventListener("change", function(){'
            '    var y = window.pageYOffset || document.documentElement.scrollTop || 0;'
            '    var opt = sel.options[sel.selectedIndex];'
            '    var src = opt.value;'
            '    var pic = opt.getAttribute("data-img") || "";'
            '    aud.pause(); aud.src = src; aud.load();'
            '    try { aud.focus({preventScroll:true}); } catch(e) {}'
            '    if (pic) { img.src = pic; fig.style.display = ""; }'
            '    else { img.removeAttribute("src"); fig.style.display = "none"; }'
            '    setTimeout(function(){ window.scrollTo(0, y); }, 0);'
            '  });'

            # Erstes Play: Auto-Scroll neutralisieren
            '  aud.addEventListener("play", function(){'
            '    var y = window.pageYOffset || document.documentElement.scrollTop || 0;'
            '    try { aud.focus({preventScroll:true}); } catch(e) {}'
            '    setTimeout(function(){ window.scrollTo(0, y); }, 0);'
            '  });'
            '})();'
            '</script>'
        )

        latex_lines = [rf"\textbf{{Audio-Liste:}} {caption or ''}"]
        for it in items:
            latex_lines.append(f"- {it['name']} ({it['audio']})")
        text_lines  = ["Audio-Liste: " + (caption or "")]
        for it in items:
            text_lines.append(f"- {it['name']} ({it['audio']})")

        return [nodes.raw("", html, format="html"),
                nodes.raw("", "\n".join(latex_lines), format="latex"),
                nodes.raw("", "\n".join(text_lines),  format="text")]


def setup(app):
    app.add_directive("audiocard", AudioCardDirective)
    app.add_directive("audiolist", AudioListDirective)
    return {"version": "0.6", "parallel_read_safe": True, "parallel_write_safe": True}