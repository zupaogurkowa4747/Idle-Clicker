# IDLE CLICKER — CHANGELOG

### v0.1 — Podstawowa mechanika
**Dodane funkcje:**
- Zdobywanie energii poprzez klikanie.
- Kupowanie ulepszeń zwiększających ilość energii za kliknięcie.
- Rosnące ceny kolejnych ulepszeń.
- Wyświetlanie podstawowych statystyk gracza.
- Możliwość zakończenia gry.

### v0.2 — System generatorów
**Dodane funkcje:**
- Kupowanie generatorów automatycznie produkujących energię.
- Produkcja energii na podstawie upływającego czasu.
- Możliwość ręcznego odbierania wyprodukowanej energii.
- Zwiększanie produkcji wraz z zakupem kolejnych generatorów.
- Rosnące ceny kolejnych generatorów.
- Rozszerzone statystyki gracza.

### v0.3 — System SAVE/LOAD
**Dodane funkcje:**
- Integracja gry z bazą danych SQLite.
- Zapisywanie statystyk i postępu gracza.
- Automatyczne wczytywanie postępu przy uruchamianiu gry.
- Automatyczne tworzenie gracza, jeśli nie istnieje.
- Zapisywanie postępu podczas wychodzenia z gry.
- Autosave co najmniej 30 sekund po poprzednim zapisie, przy kolejnej wykonanej komendzie.
- Zachowywanie zakupionych ulepszeń, generatorów i energii pomiędzy sesjami.