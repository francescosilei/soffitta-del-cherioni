# Stile, tono e decisioni già prese

Questo file riassume quello che Francesco ha deciso parlando con Claude, per chi riprende il lavoro in un'altra sessione. Vale insieme a `CLAUDE.md` e `docs/PIANO.md`.

## Come parlare con Francesco
- Non è un tecnico: italiano semplice, un passo alla volta, niente gergo (se serve un termine come "clonare" o "push", spiegalo in una frase).
- Preferisce che il lavoro lo faccia Claude, senza chiedergli di continuo permessi o passaggi manuali. Chiedi solo quando serve davvero una sua decisione.
- Risposte brevi, con il risultato e cosa deve fare lui, se deve fare qualcosa.
- Non scrivere mai l'em dash nei testi.

## Tono delle descrizioni
Informale e curato. Le battute vanno messe **dove l'articolo si presta**, qualunque sia la categoria (elettronica compresa), e **non vanno forzate**: se non c'è una battuta naturale, la descrizione resta informale e concreta, senza. Sempre con la descrizione vera dell'oggetto: cos'è, a chi serve, com'è. Il compromesso deciso: non asettico e didascalico, non da cabaret.

Oggetti dell'infanzia: giocare sulla "seconda opportunità", un oggetto che ha accompagnato la crescita di un bambino e ora aspetta il prossimo. Umano e leggero, senza sentimentalismi.

Battuta forzata: da evitare, in qualunque categoria. Esempio: paragonare le luci di uno switch di rete alla plancia di una centrale non faceva ridere e toglieva spazio ai fatti. Dove l'oggetto non offre una battuta naturale basta un tono informale e le informazioni concrete: "Switch gestito da armadio rack, adatto a chi ha una rete cresciuta oltre le dimensioni di un router. 24 porte Gigabit, 4 slot SFP, gestione da browser." Dove invece l'oggetto si presta (un decoder chiamato Zero, una macchina da scrivere dei Mondiali del 1990, un passeggino che ha fatto tanta strada) la battuta ci sta, anche se è elettronica.

Argomenti seri (testimonianze storiche, politica): nessuna battuta.

Struttura tipica di una descrizione (2-3 capoversi brevi):
1. Cos'è e a cosa serve, con un tocco di personalità.
2. Dati concreti e stato: cosa c'è, cosa si vede nelle foto, cosa è incluso.
3. A chi può interessare, o una chiusura leggera.

Esempi riusciti:
- Olivetti Italia '90: "Notti magiche, inseguendo un foglio bianco. È l'edizione speciale Italia '90: il corpo azzurro, la targhetta con la mascotte e perfino la borsa a tema, rimasta con lei come una vera tifosa."
- Passeggino: "Ha percorso marciapiedi, ciottolati, corridoi d'aeroporto e un numero imprecisabile di passeggiate 'solo fino all'angolo'. [...] Ha accompagnato la crescita di un piccolo esploratore e adesso vuole vedere i progressi di un altro."
- Epson Perfection 1240U: "Per svuotare finalmente il cassetto delle foto di famiglia: uno scanner piano a colori con collegamento USB e risoluzione di 1200 x 2400 dpi. [...]"

Il file `site/data/annunci.json` contiene 24 annunci già scritti: usali come riferimento di stile e struttura.

## Titolo, sottotitolo, specifiche
- Titolo: marca e modello, con un breve gancio se aiuta ("Vu+ Zero, il decoder satellitare piccolo ma zapper").
- Sottotitolo: le caratteristiche principali in una riga.
- Specifiche: da 3 a 6 righe, `Etichetta: valore`, solo dati verificati. Consegna: "Ritiro a mano consigliato" per gli oggetti ingombranti.

## Categorie (fisse)
Libri, Quadri, Vintage e modernariato, Giocattoli, Infanzia, Elettronica e informatica, Casa e varie. Sottocategoria libera e breve. "Moduli RAM" per i banchi di memoria, "Componenti PC" per schede, CPU e simili.

## Prezzi
- Prezzo online "medio-alto", pensato per chi cerca proprio quell'oggetto, su prezzi **venduti** (eBay venduti, Subito), non richiesti.
- Anche libri e oggetti di poco valore: si prova un prezzo da appassionato (per un libro fuori stampa 8-15 euro se c'è interesse reale).
- Sotto circa 10 euro: lotti di pezzi uguali (per esempio RAM) per reggere la spedizione.
- Il prezzo minimo sta solo nell'Excel.

## Foto
- Tutte le foto degli oggetti in vendita devono essere sul sito. Foto con dati personali (indirizzi sulle scatole, MAC e password sulle etichette di router e adattatori, seriali) escluse o sfocate.
- Nel mercatino c'è una foto per oggetto, spesso solo l'etichetta per l'elettronica: quegli oggetti restano Bozza finché non c'è una foto dell'oggetto. Per ridurre il lavoro, rifotografare solo gli oggetti più interessanti.
- Le foto girate si raddrizzano (Rotazione). Gli oggetti vanno centrati (Ritaglio). I libri fotografati in diagonale si possono ruotare per rendere il testo orizzontale.
- Foto nuove di un oggetto già presente: abbina da solo se il modello o il titolo coincidono (la copertina nuova sostituisce la vecchia); chiedi solo per dubbi reali, tutti insieme in un messaggio.

## Cosa è stato deciso sul sito
- Nome: "La soffitta del Cherioni". Sito pubblico, senza password e senza area riservata: anche il padre di Francesco lo usa per copiare testi e scaricare foto.
- Niente telefono o email sul sito. Gli annunci rimandano alle piattaforme in cui l'oggetto è in vendita (eBay, Vinted, Subito, Wallapop, Facebook Marketplace).
- Il rimando al sito dentro gli annunci sulle piattaforme si fa solo dove è consentito.
- Oggetti venduti: spariscono dal sito e restano nell'Excel come archivio.
- Stato di default "Ottimo", modificabile (Ottimo, Buono, Discreto, Accettabile). Gli oggetti elettronici si danno per funzionanti.
- Il mercatino di paese ("Lugnano in soffitta") probabilmente non si farà più: gli oggetti si vendono online.

## Convenzioni della cartella Mercatino
- Inventario: `Inventario_mercatino.xlsx` (ID a 4 cifre, nome, categoria, foto, prezzi da mercatino).
- Foto già analizzate: `Analizzate\<Categoria>\NNNN_Sigla_Nome-oggetto.jpg`; foto non identificabili in `Problemi\`.
- Sigle categoria: Libri, Quadri, Vintage, Giocattoli, Infanzia, Elettronica, Casa.
- I prezzi dell'inventario sono prezzi da mercatino (bassi): per il sito si rifanno da capo.
