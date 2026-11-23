---
name: aggiorna-sito
description: Ricostruisce il sito La soffitta del Cherioni dall'Excel Annunci_soffitta.xlsx e lo pubblica su GitHub e Netlify. Usala per "aggiorna il sito", "ho venduto X", "ecco il link eBay di X" e quando Francesco ha modificato l'Excel.
---

# Aggiorna sito

Leggi prima `CLAUDE.md`.

## Se Francesco dice "venduto" o dà un link
1. Individua l'oggetto per ID o per nome. Se ci sono più candidati, chiedi.
2. Scrivi nell'Excel: `Stato vendita = Venduto`, oppure l'URL nella colonna della piattaforma (eBay, Vinted, Subito, Wallapop, Facebook Marketplace). Non toccare altre celle.
3. Se Excel è bloccato (aperto o in sincronizzazione), chiedi di chiuderlo.

## Costruire e pubblicare
1. `pip install -r tools/requirements.txt` (solo la prima volta).
2. `python tools/build.py --excel "<Soffitta>\Annunci_soffitta.xlsx" --foto-dir "<Soffitta>"`.
3. Leggi gli avvisi: oggetti senza foto o senza prezzo, ID duplicati, foto non trovate, righe "Da verificare". Riferiscili a Francesco; non correggere di tua iniziativa dati dell'Excel.
4. Prova il sito in locale: `python -m http.server 8000 --directory site`, apri una scheda e controlla che la vetrina si carichi senza errori.
5. Controlla cosa finirebbe su GitHub con `git status` e `git diff --stat`: devono cambiare solo `site/data/annunci.json` e `site/foto/`. Se compare altro (xlsx, originali, EXIF), fermati. Verifica che `site/data/annunci.json` non contenga "Prezzo minimo", "Note interne" o "Da verificare".
6. Commit (messaggio breve in italiano, per esempio "Aggiorna annunci: 3 nuovi, 1 venduto") e `git push origin main`. Netlify pubblica da solo in circa un minuto.
7. Riferisci a Francesco l'indirizzo del sito e il riepilogo (pubblicati, nuovi, venduti, avvisi).

## Se qualcosa va storto
- Push rifiutato: `git pull --rebase origin main` e riprova una volta; se ci sono conflitti, fermati e racconta.
- Errore su una foto: segnalalo, il resto del sito si pubblica comunque.
