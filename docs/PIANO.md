# Piano del progetto

## Obiettivo
Un sito pubblico, "La soffitta del Cherioni", con gli oggetti che Francesco non riesce a vendere al mercatino di paese. Ogni oggetto ha foto, titolo, sottotitolo, descrizione, specifiche, categoria, sottocategoria e prezzo. Il padre di Francesco usa il sito per copiare testi e scaricare le foto e creare gli annunci su eBay, Vinted, Subito, Wallapop e Facebook Marketplace. Poi i link degli annunci si aggiungono alla scheda dell'oggetto sul sito.

## Come funziona
```
Mercatino (inventario + foto) --> Soffitta (copia di lavoro, OneDrive)
        |
        |  competenza crea-annunci (Claude Code, sessione locale)
        v
Annunci_soffitta.xlsx  (fogli Annunci e Foto; resta su OneDrive, NON in Git)
        |
        |  python tools/build.py   (competenza aggiorna-sito)
        v
site/data/annunci.json + site/foto/<ID>/<n>.jpg   --> commit e push --> Netlify
```
Francesco modifica a mano l'Excel (prezzi, descrizioni, stato, "venduto", link) e dice "aggiorna il sito".

## Contenuto del repository
| Percorso | A cosa serve |
|---|---|
| `site/index.html` | Pagina del sito (vetrina, filtri per categoria e sottocategoria, scheda oggetto, download foto). Legge `data/annunci.json`. |
| `site/data/annunci.json` | Dati pubblici di tutti gli annunci in vendita. Generato. |
| `site/foto/<ID>/<n>.jpg` | Foto già ricentrate e ridimensionate. Generate. |
| `tools/build.py` | Excel -> dati e foto del sito. |
| `tools/crea_modello_excel.py` | Crea il modello vuoto dell'Excel. |
| `docs/Annunci_soffitta_modello.xlsx` | Modello vuoto, con tendine e legenda. |
| `docs/annunci_in_attesa_di_foto.json` | Annunci già scritti ma senza foto utilizzabile: da riusare. |
| `docs/DA_VERIFICARE.md` | Elenco dei dati ancora da controllare. |
| `.claude/skills/` | Le due competenze di Claude Code. |
| `netlify.toml` | Dice a Netlify di pubblicare la cartella `site`. |

## L'Excel Annunci_soffitta.xlsx
Foglio **Annunci**, una riga per oggetto:
ID, Titolo, Sottotitolo, Descrizione, Categoria, Sottocategoria, Specifiche (`Etichetta: valore` una per riga), Prezzo, **Prezzo minimo (privato)**, Stato (Ottimo, Buono, Discreto, Accettabile), Quantità lotto, eBay, Vinted, Subito, Wallapop, Facebook Marketplace, Stato vendita (Bozza, In vendita, Venduto), **Da verificare (privato)**, **Note interne (privato)**.

Foglio **Foto**, una riga per foto:
ID, File (relativo alla cartella Soffitta), Ordine (1 = copertina), Pubblica (Sì/No), Rotazione (gradi orari), Ritaglio (`x0,y0,x1,y1`), Sfoca (`LxA+X+Y;...`).

Le colonne private non finiscono mai nel sito né in Git. Un oggetto compare sul sito solo se è "In vendita", ha un prezzo e almeno una foto pubblica.

## Regole
Sono in `CLAUDE.md`; in sintesi: repository pubblico (mai dati privati), niente dati inventati, foto con etichette escluse o sfocate, prezzi sul venduto reale e lotti per i pezzi di poco valore, stato "Ottimo" di default, tono informale con descrizioni concrete.

## Flussi
- **Primo giro**: `crea-annunci` dall'inventario a lotti di 20-25, Francesco rivede l'Excel, poi `aggiorna-sito`.
- **Nuove foto**: le metti in `Soffitta\Nuove\` e lanci `crea-annunci`: abbina da solo agli oggetti esistenti e fa domande solo per i dubbi reali, in un messaggio solo.
- **Venduto**: cambi "Stato vendita" nell'Excel (o lo dici a Claude) e lanci `aggiorna-sito`: l'oggetto sparisce dal sito e resta nell'Excel come archivio.
- **Link di una piattaforma**: incolli l'URL nella colonna giusta (o lo dici a Claude): sul sito compare in "Dove lo trovi". Se una piattaforma vieta link esterni nell'annuncio, il rimando al sito non si mette.

## Pubblicazione su Netlify (una volta sola)
1. Account Netlify gratuito, "Add new site", "Import an existing project", scegliere GitHub e il repository `soffitta-del-cherioni`.
2. Build command vuoto, publish directory `site` (già scritto in `netlify.toml`).
3. In "Site configuration" si può cambiare il nome: l'indirizzo sarà `<nome>.netlify.app`.

## Stato attuale
- Il sito è pronto e funziona con 24 annunci (testi e prezzi proposti; vedi `docs/DA_VERIFICARE.md`).
- Gli ID (2001 e seguenti) sono provvisori: nel primo giro vero si usano gli ID dell'inventario.
- Otto annunci non hanno ancora una foto utilizzabile (`docs/annunci_in_attesa_di_foto.json`).
