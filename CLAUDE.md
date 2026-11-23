# La soffitta del Cherioni

Sito pubblico (Netlify) con gli oggetti usati che Francesco vuole vendere online. Il sito è statico: `site/` contiene la pagina, i dati (`site/data/annunci.json`) e le foto (`site/foto/<ID>/<n>.jpg`). Dati e foto si generano con `tools/build.py` a partire dall'Excel `Annunci_soffitta.xlsx`, che vive su OneDrive, non in questo repository.

Prima di lavorare leggi `docs/PIANO.md` (disegno completo), `docs/STILE.md` (tono, stile e decisioni già prese con Francesco) e le competenze in `.claude/skills/`:
- `crea-annunci`: crea o aggiorna le righe dell'Excel a partire da inventario e foto.
- `aggiorna-sito`: costruisce il sito dall'Excel e lo pubblica; gestisce anche "venduto" e i link alle piattaforme.

## Cartelle sul PC di Francesco (chiedi i percorsi al primo avvio)
Il percorso completo non è scritto qui perché il repository è pubblico: chiedilo a Francesco e usalo solo nella sessione, mai in file che vanno su Git.
- `Mercatino` (originale, non toccare): cartella su OneDrive con l'inventario del mercatino
- `Soffitta` (copia di lavoro, creata copiando Mercatino), nello stesso OneDrive:
  - `Inventario_mercatino.xlsx` e `Analizzate\<Categoria>\NNNN_Sigla_Nome.jpg`: dati e foto del primo giro
  - `Annunci_soffitta.xlsx`: l'Excel di lavoro (modello in `docs/Annunci_soffitta_modello.xlsx`)
  - `Nuove\`: foto nuove da analizzare

Se la cartella ha un altro nome, chiedi a Francesco.

## Regole che non si discutono
1. **Il repository è pubblico.** Non committare mai: Excel (`*.xlsx` tranne il modello), foto originali, prezzo minimo, note interne, colonna "Da verificare", EXIF, indirizzi, seriali, password, MAC address. Ciò che entra in Git resta nella cronologia anche se poi lo cancelli.
2. **Niente dati inventati.** Specifiche solo da foto o da fonti trovate in rete. Se non sai, scrivi nella colonna "Da verificare" e lascia fuori dal sito.
3. **Foto con dati personali o di rete** (etichette di router e adattatori con MAC e password, spedizioni con indirizzo, seriali): `Pubblica = No` oppure sfocatura in colonna "Sfoca".
4. **Oggetti con solo la foto dell'etichetta** restano `Bozza` finché non c'è una foto dell'oggetto.
5. **Prezzi**: prezzo online medio-alto basato su venduto reale (eBay venduti, Subito), non su prezzi richiesti. Oggetti di poco valore: lotti di pezzi uguali per reggere la spedizione. Prezzo minimo solo nell'Excel.
6. **Stato** di default "Ottimo" (menù a tendina: Ottimo, Buono, Discreto, Accettabile). Gli oggetti elettronici si danno per funzionanti.
7. **Tono** informale e curato. Battute dove l'articolo si presta, in qualsiasi categoria, **senza forzarle**: se non c'è una battuta naturale, descrizione informale e concreta. Sempre con la descrizione vera dell'oggetto. Argomenti seri (testimonianze, storia, politica) senza battute. Vedi `docs/STILE.md`.
8. **Foto nuove di oggetti già censiti**: abbina automaticamente se il modello o il titolo coincidono; fai domande solo se il dubbio è reale (per esempio più pezzi identici) e tutte insieme, a fine analisi, con domande sì/no. Non fare domande sistematiche.
9. Mai l'em dash nei testi: usa virgola, due punti o trattino breve.
10. Commit e push solo quando Francesco lo chiede o con il comando "aggiorna il sito".
