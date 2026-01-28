(Sphinx Veröffentlichen)=
# Veröffentlichung mit GitHub Pages

## Github Pages


## Entwicklerbereich

Bei der Veröffentlichung einer Sphinx-Dokumentation stellt sich ab einer gewissen Größe häufig die Frage, wie interne Entwickler-Inhalte behandelt werden sollen.\
Typische Beispiele sind:

- persönliche Notizen
- TODO-Listen
- technische Skizzen
- unfertige Konzepte
- Build- oder Deployment-Hinweise

Diese Inhalte sollen lokal sichtbar, aber nicht öffentlich ausgeliefert werden. Sphinx bietet hierfür mit Tags und der Direktive `{only}` eine robuste und saubere Lösung.

### Grundidee: Tag-basierte Build-Trennung

Sphinx erlaubt es, Inhalte abhängig von gesetzten **Build-Tags** ein- oder auszublenden. Ein Inhalt wird nur dann gerendert, wenn der entsprechende Tag beim Build explizit gesetzt ist.

Konkret:
- **Lokaler Build**: mit Tag dev
- **Öffentlicher Build** (GitHub Pages): ohne diesen Tag

Fehlt der Tag, werden die entsprechenden Inhalte **bereits beim Parsen verworfen** und tauchen **weder im HTML noch im Suchindex** auf.