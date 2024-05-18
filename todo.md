# Projekt-Todo-Liste

## 1. Historische Aktiendaten mit yfinance herunterladen
- [X] Installiere die `yfinance` Bibliothek
- [X] Lade historische Aktiendaten für ausgewählte Aktien herunter

## 2. Daten mit SciKit-Learn bereinigen und vereinheitlichen
- [X] Installiere die `scikit-learn` Bibliothek
- [X] Importiere die Daten in ein pandas DataFrame
- [ ] Führe notwendige Datenbereinigungsschritte durch (z.B. Entfernen von Nullwerten)
- [ ] Vereinheitliche die Daten (z.B. Normalisierung/Standardisierung)
- [ ] Speichere die bereinigten Daten ab

## 3. Bereinigte Daten in eine DuckDB laden
- [ ] Installiere die `duckdb` Bibliothek
- [ ] Erstelle eine neue DuckDB-Datenbank
- [ ] Importiere die bereinigten Daten in die DuckDB-Datenbank

## 4. Daten mit Tensorflow zu einem Modell trainieren
- [ ] Installiere die `tensorflow` Bibliothek
- [ ] Lade die Daten aus der DuckDB-Datenbank
- [ ] Erstelle ein neuronales Netzwerk-Modell mit Tensorflow
- [ ] Trainiere das Modell mit den geladenen Daten
- [ ] Speichere das trainierte Modell ab

## 5. Vorhersagen für Aktienkurse erstellen
- [ ] Lade das trainierte Modell
- [ ] Lade aktuelle (und neue historische) Daten herunter
- [ ] Bereinige und vereinheitliche die neuen Daten
- [ ] Erstelle Vorhersagen mit dem Modell basierend auf den neuen Daten
- [ ] Speichere die Vorhersagen ab

## 6. Graphische Darstellung der Daten und Vorhersagen
- [ ] Installiere die `matplotlib` und `seaborn` Bibliotheken
- [ ] Erstelle Plots für die historischen Daten und die Vorhersagen
- [ ] Gestalte die Plots ansprechend und informativ
- [ ] Speichere die Plots ab

## 7. Automatisierung des Prozesses
- [ ] Schreibe ein Skript, das den gesamten Prozess wöchentlich ausführt
- [ ] Verwende `cron` (Linux/macOS) oder den Aufgabenplaner (Windows) für die zeitliche Planung
- [ ] Teste das Automatisierungsskript

## Zusätzliche Schritte (optional)
- [ ] Dokumentiere den gesamten Prozess
- [ ] Erstelle eine Benutzeroberfläche für eine einfachere Interaktion
- [ ] Implementiere Benachrichtigungen (z.B. per E-Mail) für den Abschluss des wöchentlichen Prozesses

