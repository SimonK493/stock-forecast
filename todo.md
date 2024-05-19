# Projekt-Todo-Liste

## 1. Historische Aktiendaten mit yfinance herunterladen
- [X] Installiere die `yfinance` Bibliothek
- [X] Lade historische Aktiendaten für ausgewählte Aktien herunter

## 2. Daten mit SciKit-Learn bereinigen und vereinheitlichen
- [X] Installiere die `scikit-learn` Bibliothek
- [X] Importiere die Daten in ein pandas DataFrame
- [X] Führe notwendige Datenbereinigungsschritte durch (z.B. Entfernen von Nullwerten)
- [X] Vereinheitliche die Daten (z.B. Normalisierung/Standardisierung)

## 3. Feature Engineering
- [ ] Berechne gleitende Durchschnitte (Moving Averages) über verschiedene Zeitfenster für den Schlusskurs
- [ ] Berechne exponentielle gleitende Durchschnitte (Exponential Moving Averages) für den Schlusskurs
- [ ] Berechne die Standardabweichung der täglichen Renditen über einen bestimmten Zeitraum als Maß für die Volatilität
- [ ] Berechne Bollinger-Bänder basierend auf den gleitenden Durchschnitten und der Volatilität
- [ ] Berechne das Momentum als Differenz zwischen dem aktuellen Schlusskurs und dem Schlusskurs vor einem bestimmten Zeitraum
- [ ] Berechne den Relative Strength Index (RSI) als Maß für die Stärke der Preisbewegung
- [ ] Berechne das durchschnittliche Handelsvolumen über einen bestimmten Zeitraum
- [ ] Berechne den On-Balance-Volume (OBV) als Summe des Handelsvolumens gewichtet entsprechend der Richtung der Preisbewegung
- [ ] Berücksichtige Zeitindikatoren wie den Handelstag und den Handelswochentag
- [ ] Analysiere das Sentiment in Nachrichtenartikeln oder Social-Media-Posts, um das Marktsentiment zu bewerten
- [ ] Berücksichtige spezielle Ereignisse wie Quartalsberichte, Dividendenausschüttungen oder Produktankündigungen
- [ ] Verwende technische Indikatoren wie den MACD und den stochastischen Oszillator, um zusätzliche Einblicke zu gewinnen
- [ ] Untersuche mögliche Interaktionen zwischen verschiedenen Features, um zusätzliche Informationen zu gewinnen
- [ ] Reduziere die Dimensionalität der Daten falls notwendig, um die Modellkomplexität zu verringern

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

