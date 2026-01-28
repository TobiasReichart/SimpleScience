document.addEventListener("DOMContentLoaded", function () {

  // Prüfen, ob Mermaid überhaupt geladen wurde
  if (typeof mermaid === "undefined") {
    console.warn("Mermaid ist nicht geladen – Diagramme werden nicht gerendert.");
    return;
  }

  // Zentrale Mermaid-Konfiguration
  mermaid.initialize({

    // Mermaid rendert Diagramme automatisch nach dem Laden der Seite
    startOnLoad: true,

    // Visuelles Grundtheme
    theme: "default",

    // Sicherheitsmodus:
    // 'loose' erlaubt Inline-HTML (z. B. <div class="mermaid">)
    // notwendig für Sphinx + MyST + lokale Assets
    securityLevel: "loose",

    // Einstellungen speziell für Flowcharts
    flowchart: {
      padding: 24,        // Innenabstand von Subgraphs (wichtig für lange Titel)
      nodeSpacing: 50,    // Horizontaler Abstand zwischen Knoten
      rankSpacing: 60,    // Vertikaler Abstand zwischen Ebenen
      useMaxWidth: true,  // Diagramm nutzt verfügbare Breite
    },

    // Einheitliche Schrift für alle Diagramme
    themeVariables: {
      fontFamily: "Inter, Helvetica, Arial, sans-serif",
      fontSize: "14px",
    },

  });
});