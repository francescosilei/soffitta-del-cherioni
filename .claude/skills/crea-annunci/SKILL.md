---
name: crea-annunci
description: Crea o aggiorna gli annunci della Soffitta del Cherioni nell'Excel Annunci_soffitta.xlsx a partire dall'inventario del mercatino e dalle foto. Usala quando Francesco chiede di creare gli annunci, di analizzare nuove foto nella cartella Soffitta o di aggiungere oggetti.
---

# Crea annunci

Leggi prima `CLAUDE.md` e `docs/PIANO.md`: le regole lì valgono sempre.

## Dove si lavora
- Cartella `Soffitta` (percorso in `CLAUDE.md`). Se non esiste, chiedi a Francesco di copiare lì la cartella Mercatino (copia, non spostamento) e fermati.
- Excel di lavoro: `Soffitta\Annunci_soffitta.xlsx`. Se manca, crealo con `python tools/crea_modello_excel.py "<percorso>\Annunci_soffitta.xlsx"`.
- Prima di scrivere sull'Excel controlla che sia scrivibile (`open(path,'r+b')`): se è aperto in Excel o bloccato da OneDrive, chiedi di chiuderlo.

## Primo giro (dall'inventario)
1. Leggi `Inventario_mercatino.xlsx` (ID, nome, categoria, foto in `Analizzate\<Categoria>\`) e `Annunci_soffitta.xlsx`.
2. Prendi i prossimi 20-25 oggetti dell'inventario non ancora presenti negli Annunci (ordine di ID). Lavora a lotti: alla fine di ogni lotto riassumi e fermati, Francesco rivede l'Excel.
3. Per ogni oggetto:
   - Guarda la foto (ridimensionala per leggerla, ritaglia l'etichetta per le sigle piccole).
   - Cerca in rete specifiche e prezzi **venduti** (eBay venduti, Subito) del modello preciso.
   - Compila la riga: Titolo, Sottotitolo, Descrizione (2-3 frasi più specifiche), Categoria e Sottocategoria (le sette categorie fisse, sottocategoria libera e breve, "Moduli RAM" per i banchi di memoria), Specifiche (una per riga, `Etichetta: valore`), Prezzo, Stato (Ottimo), Quantità lotto se serve, Stato vendita.
   - Riusa i testi già scritti in `docs/annunci_in_attesa_di_foto.json` quando l'oggetto coincide; per gli ID usa sempre quelli dell'inventario.
4. Foglio **Foto**: una riga per foto (ID, File relativo alla cartella Soffitta, Ordine, Pubblica, Rotazione, Ritaglio, Sfoca).
   - Una foto per oggetto va in copertina (Ordine 1).
   - `Pubblica = No` per le foto con etichette, seriali, password, MAC, indirizzi, volti.
   - `Rotazione` per le foto girate (gradi orari). Per i libri fotografati in diagonale, valuta la rotazione per mettere il testo orizzontale.
   - `Ritaglio` (x0,y0,x1,y1 in pixel sull'immagine già ruotata) per centrare l'oggetto; senza ritaglio la foto viene solo adattata.
   - Un oggetto di cui hai solo la foto dell'etichetta: `Stato vendita = Bozza` e in "Note interne" scrivi "serve foto dell'oggetto".
5. Imposta `Stato vendita = In vendita` solo se hai titolo, prezzo, descrizione e almeno una foto pubblica.

## Contenuto: regole di scrittura
- Tono informale, con un tocco scherzoso dove ci sta, **senza trascurare i fatti**: ogni descrizione deve dire cos'è, a chi serve e com'è. Meno battute su elettronica tecnica e testi seri.
- Nessuna spiegazione sull'omologazione dei seggiolini o sul cancellare i dati: Francesco le conosce già.
- Se un dato non è ricavabile, **non inventarlo**: scrivilo in "Da verificare" (non viene pubblicato).
- Prezzo online medio-alto sul venduto reale, arrotondato a euro interi. Sotto circa 10 euro valuta un lotto di pezzi uguali. Libri: titoli comuni a pochi euro, titoli rari o fuori catalogo di più.
- Prezzo minimo: lascia vuoto se Francesco non lo indica.

## Foto nuove (cartella `Nuove\`)
1. Guarda tutte le foto e identifica gli oggetti.
2. Se il modello o il titolo coincide con un oggetto già presente (per esempio un router con lo stesso modello letto in foto, o un libro con lo stesso titolo): aggiungi la foto a quell'oggetto, senza chiedere. Per i libri la copertina nuova sostituisce la vecchia nella riga Foto. Gli originali restano sempre nella cartella.
3. Chiedi solo se il dubbio è reale: più pezzi identici (non sai se è un pezzo nuovo o un'altra foto dello stesso), oppure modello diverso da quello in inventario. Raccogli tutte le domande in un solo messaggio a fine analisi, con risposta sì/no.
4. Se è un oggetto nuovo, crea la riga con un nuovo ID (continua la numerazione dell'inventario).
5. Sposta le foto elaborate da `Nuove\` in `Analizzate\<Categoria>\NNNN_Sigla_Nome-oggetto.jpg`.

## A fine lavoro
Riassumi in poche righe: quanti oggetti, quali hanno dati "Da verificare", quali restano Bozza e perché, quali foto hai escluso per dati personali. Poi proponi "aggiorna il sito" (competenza `aggiorna-sito`).
