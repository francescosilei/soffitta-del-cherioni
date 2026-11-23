#!/usr/bin/env python3
"""Crea il modello vuoto di Annunci_soffitta.xlsx (fogli Annunci, Foto, Legenda).

Uso: python tools/crea_modello_excel.py [percorso_di_uscita.xlsx]
"""
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

CATEGORIE = ["Libri", "Quadri", "Vintage e modernariato", "Giocattoli", "Infanzia", "Elettronica e informatica", "Casa e varie"]
STATI = ["Ottimo", "Buono", "Discreto", "Accettabile"]
STATI_VENDITA = ["Bozza", "In vendita", "Venduto"]

ANNUNCI = [
    ("ID", 8), ("Titolo", 40), ("Sottotitolo", 40), ("Descrizione", 70), ("Categoria", 24), ("Sottocategoria", 22),
    ("Specifiche", 50), ("Prezzo", 10), ("Prezzo minimo", 13), ("Stato", 12), ("Quantità lotto", 10),
    ("eBay", 28), ("Vinted", 28), ("Subito", 28), ("Wallapop", 28), ("Facebook Marketplace", 28),
    ("Stato vendita", 14), ("Da verificare", 40), ("Note interne", 40),
]
FOTO = [("ID", 8), ("File", 60), ("Ordine", 8), ("Pubblica", 10), ("Rotazione", 10), ("Ritaglio", 22), ("Sfoca", 30)]

LEGENDA = [
    ("Foglio Annunci", "Una riga per oggetto. Compare sul sito solo se 'Stato vendita' è 'In vendita', c'è il prezzo e c'è almeno una foto pubblica."),
    ("ID", "Lo stesso ID dell'inventario del mercatino (4 cifre)."),
    ("Specifiche", "Una per riga, nella forma 'Etichetta: valore'. Esempio: 'Peso: circa 7 kg'."),
    ("Prezzo", "Prezzo online proposto, in euro."),
    ("Prezzo minimo", "PRIVATO: non viene mai pubblicato."),
    ("Stato", "Ottimo (default), Buono, Discreto, Accettabile."),
    ("Quantità lotto", "Numero di pezzi se venduti insieme (2 o più). Vuoto se pezzo singolo."),
    ("Link piattaforme", "Incolla qui il link dell'annuncio quando è online. Sul sito compare in 'Dove lo trovi'."),
    ("Stato vendita", "Bozza, In vendita, Venduto. Un oggetto Venduto sparisce dal sito e resta qui come archivio."),
    ("Da verificare", "Dati incerti o mancanti: NON vengono pubblicati. Svuota la cella quando hai verificato."),
    ("Note interne", "Non pubblicate."),
    ("Foglio Foto", "Una riga per foto. 'File' è il percorso relativo alla cartella Soffitta, per esempio Analizzate\\Infanzia\\0123_Passeggini_Inglesina.jpg."),
    ("Ordine", "1 = foto di copertina."),
    ("Pubblica", "Sì o No. Metti No per le foto con etichette, seriali, password, indirizzi, volti."),
    ("Rotazione", "Gradi in senso orario (90, 180, 270) per raddrizzare una foto girata."),
    ("Ritaglio", "x0,y0,x1,y1 in pixel (sull'immagine già ruotata): il riquadro che contiene l'oggetto, per centrarlo."),
    ("Sfoca", "Regioni da sfocare, nella forma LxA+X+Y separate da ';' (pixel dell'immagine già ruotata)."),
]


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "docs" / "Annunci_soffitta_modello.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Annunci"
    for i, (nome, larg) in enumerate(ANNUNCI, 1):
        c = ws.cell(row=1, column=i, value=nome)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="14213D")
        c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.freeze_panes = "C2"
    col = {n: get_column_letter(i) for i, (n, _) in enumerate(ANNUNCI, 1)}

    def tendina(colonna, valori, righe=500):
        dv = DataValidation(type="list", formula1='"' + ",".join(valori) + '"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{col[colonna]}2:{col[colonna]}{righe}")

    tendina("Categoria", CATEGORIE)
    tendina("Stato", STATI)
    tendina("Stato vendita", STATI_VENDITA)
    for riga in range(2, 502):
        ws[f"{col['Descrizione']}{riga}"].alignment = Alignment(wrap_text=True, vertical="top")
        ws[f"{col['Specifiche']}{riga}"].alignment = Alignment(wrap_text=True, vertical="top")

    wf = wb.create_sheet("Foto")
    for i, (nome, larg) in enumerate(FOTO, 1):
        c = wf.cell(row=1, column=i, value=nome)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="14213D")
        wf.column_dimensions[get_column_letter(i)].width = larg
    wf.freeze_panes = "A2"
    dv = DataValidation(type="list", formula1='"Sì,No"', allow_blank=True)
    wf.add_data_validation(dv)
    dv.add("D2:D2000")

    wl = wb.create_sheet("Legenda")
    wl.column_dimensions["A"].width = 22
    wl.column_dimensions["B"].width = 110
    for i, (a, b) in enumerate(LEGENDA, 1):
        wl.cell(row=i, column=1, value=a).font = Font(bold=True)
        c = wl.cell(row=i, column=2, value=b)
        c.alignment = Alignment(wrap_text=True, vertical="top")

    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print("Creato", out)


if __name__ == "__main__":
    main()
