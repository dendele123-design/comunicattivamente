import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi Aziendale", page_icon="🎯", layout="centered")

# --- STILE CSS PERSONALIZZATO ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3.8em; font-weight: bold; text-transform: uppercase; white-space: normal; line-height: 1.2; }
    .area-header { background-color: #000000; color: white; padding: 15px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 20px; letter-spacing: 2px; }
    .lesson-box { background-color: #f8f9fa; color: #1a1a1a; padding: 25px; border-radius: 10px; border-left: 8px solid #ff4b4b; margin-top: 20px; font-style: italic; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    .profile-box { padding: 30px; border-radius: 15px; border: 2px solid #000; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DELLE 20 DOMANDE ---
domande = [
    # AREA 1
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?",
        "sotto": "(Attenzione: non quanto hai incassato. Quanto ti è rimasto pulito).",
        "opzioni": [
            {"testo": "🔴 NO / GUARDO SOLO IL FATTURATO", "punti": 1},
            {"testo": "🟢 SÌ, CONOSCO IL MARGINE GIORNALIERO", "punti": 0}
        ],
        "lezione": "Il fatturato è vanità. Se incassi 1.000€ ma ne hai spesi 950€ per generarli, sei un volontario, non un imprenditore. Guidare guardando solo l'incasso è come guidare guardando solo il tachimetro e non la benzina: corri forte, ma ti fermerai all'improvviso."
    },
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?",
        "sotto": "(O guardi cosa fanno i concorrenti e ti metti un po' sotto?)",
        "opzioni": [
            {"testo": "🔴 SÌ, VADO A OCCHIO / COPIO GLI ALTRI", "punti": 1},
            {"testo": "🟢 NO, HO UN CALCOLO MATEMATICO DEI COSTI", "punti": 0}
        ],
        "lezione": "Il 'prezzo di mercato' è una bugia. Se il tuo concorrente sta fallendo (e non lo sai) e tu copi i suoi prezzi, fallirai con lui. Il prezzo deve coprire i TUOI costi e garantirti il TUO margine. La matematica non ha sentimenti."
    },
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?",
        "sotto": "(Il cliente tira sul prezzo e tu cedi per 'non perderlo').",
        "opzioni": [
            {"testo": "🔴 SÌ, SPESSO", "punti": 1},
            {"testo": "🟢 MAI / SOLO IN CAMBIO DI QUALCOSA", "punti": 0}
        ],
        "lezione": "Lo sconto è la droga dei poveri. Se togli il 10% dal prezzo, spesso stai togliendo il 50% dal tuo utile netto. Se il cliente ti sceglie solo perché costi meno, ti tradirà per il primo che costa un euro in meno di te."
    },
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "SAI QUAL È IL TUO 'PUNTO DI PAREGGIO' MENSILE?",
        "sotto": "(La cifra esatta da incassare per coprire tutte le spese fisse e variabili).",
        "opzioni": [
            {"testo": "🔴 NON ESATTAMENTE / CREDO DI SÌ", "punti": 1},
            {"testo": "🟢 LO SO AL CENTESIMO", "punti": 0}
        ],
        "lezione": "Se non sai quanto ti costa tenere la serranda alzata (anche se non vendi nulla), vivi nell'ansia. Sapere il Break-Even Point ti dà la calma di dire: 'Dal giorno 20 del mese in poi, tutto quello che entra è guadagno'."
    },
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "SE I CLIENTI SMETTONO DI PAGARE OGGI, QUANTI MESI SOPRAVVIVI?",
        "sotto": "(Il test della cassa).",
        "opzioni": [
            {"testo": "🔴 MENO DI UN MESE / VADO IN ROSSO SUBITO", "punti": 1},
            {"testo": "🟢 HO ALMENO 3 MESI DI OSSIGENO", "punti": 0}
        ],
        "lezione": "Le aziende non falliscono perché non hanno utili. Falliscono perché finiscono la cassa. Se vivi 'bonifico su bonifico', sei ostaggio dei tuoi clienti. Devi costruire la riserva di guerra."
    },
    # AREA 2
    {
        "area": "AREA 2: L'OSSIGENO (IL TEMPO)",
        "testo": "LE TUE RIUNIONI HANNO UN ORDINE DEL GIORNO SCRITTO?",
        "sotto": "(Prima di entrare, tutti sanno di cosa si parla e per quanto tempo).",
        "opzioni": [
            {"testo": "🔴 NO, CI VEDIAMO E PARLIAMO", "punti": 1},
            {"testo": "🟢 SÌ, SEMPRE", "punti": 0}
        ],
        "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa. Se entrate in 5 persone in una stanza per un'ora senza un obiettivo, avete appena bruciato 200€ di stipendi per non decidere nulla."
    },
    {
        "area": "AREA 2: L'OSSIGENO (IL TEMPO)",
        "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?",
        "sotto": "(O è il 'Ding' del telefono a deciderlo per te?)",
        "opzioni": [
            {"testo": "🔴 LE LEGGO APPENA ARRIVANO", "punti": 1},
            {"testo": "🟢 LE LEGGO A BLOCCHI ORARI PREFISSATI", "punti": 0}
        ],
        "lezione": "La reattività immediata non è efficienza, è nevrosi. Il cervello impiega 15 minuti per ritrovare la concentrazione dopo un'interruzione. Se leggi 20 mail in un'ora, non hai lavorato. Hai solo reagito."
    },
    {
        "area": "AREA 2: L'OSSIGENO (IL TEMPO)",
        "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?",
        "sotto": "(Preventivi, fatture, loghi...)",
        "opzioni": [
            {"testo": "🔴 TANTO / DIPENDE DOVE SONO", "punti": 1},
            {"testo": "🟢 ZERO, SO ESATTAMENTE DOVE SONO", "punti": 0}
        ],
        "lezione": "Il 'Poltergeist Digitale' mangia circa 40 minuti al giorno a ogni dipendente. Moltiplica per un anno: sono settimane di stipendio pagate per giocare a nascondino col server."
    },
    {
        "area": "AREA 2: L'OSSIGENO (IL TEMPO)",
        "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?",
        "sotto": "(O hai un filtro/segretaria/orario dedicato?)",
        "opzioni": [
            {"testo": "🔴 RISPONDO SEMPRE", "punti": 1},
            {"testo": "🟢 HO FILTRI E ORARI", "punti": 0}
        ],
        "lezione": "Essere 'sempre disponibili' ti fa sembrare servile, non professionale. Il chirurgo non risponde al telefono mentre opera. Se stai lavorando sulla strategia, il telefono deve tacere."
    },
    {
        "area": "AREA 2: L'OSSIGENO (IL TEMPO)",
        "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?",
        "sotto": "(O ti chiedono ancora 'Sei libero martedì?' a voce?)",
        "opzioni": [
            {"testo": "🔴 NO / USIAMO WHATSAPP", "punti": 1},
            {"testo": "🟢 SÌ, GOOGLE CALENDAR È LEGGE", "punti": 0}
        ],
        "lezione": "Chiedere 'quando sei libero' genera un ping-pong di 10 messaggi inutile. Vedere il calendario occupato zittisce tutti e ottimizza gli incastri."
    },
    # AREA 3
    {
        "area": "AREA 3: I MUSCOLI (LA SQUADRA)",
        "testo": "IL TEST DELL'AUTOBUS: SE DOMANI SPARISCI PER UN MESE...",
        "sotto": "(L'azienda continua a fatturare o si ferma?)",
        "opzioni": [
            {"testo": "🔴 SI FERMA / CROLLA TUTTO", "punti": 1},
            {"testo": "🟢 VA AVANTI (MAGARI PIÙ LENTA, MA VA)", "punti": 0}
        ],
        "lezione": "Se l'azienda sei tu, non hai un'azienda. Hai un lavoro a vita da cui non puoi dimetterti. L'obiettivo dell'imprenditore è rendersi inutile per l'operatività quotidiana."
    },
    {
        "area": "AREA 3: I MUSCOLI (LA SQUADRA)",
        "testo": "HAI PROCEDURE SCRITTE PER I COMPITI RIPETITIVI?",
        "sotto": "(Come si fa una fattura, come si apre il negozio, come si risponde al telefono).",
        "opzioni": [
            {"testo": "🔴 NO, È TUTTO NELLA TESTA", "punti": 1},
            {"testo": "🟢 SÌ, ABBIAMO I MANUALI", "punti": 0}
        ],
        "lezione": "L'oralità è il medioevo. Se devi spiegare la stessa cosa due volte, hai fallito. Scrivila (o fai un video). Solo così puoi delegare senza ansia."
    },
    {
        "area": "AREA 3: I MUSCOLI (LA SQUADRA)",
        "testo": "TI SENTI SPESSO DIRE 'FACCIO PRIMA A FARLO IO'?",
        "sotto": "(E alla fine lo fai tu).",
        "opzioni": [
            {"testo": "🔴 QUASI OGNI GIORNO", "punti": 1},
            {"testo": "🟢 RARAMENTE", "punti": 0}
        ],
        "lezione": "Questa frase è la lapide della tua crescita. Facendo tu il lavoro operativo, stai rubando tempo al lavoro strategico e stai impedendo ai tuoi dipendenti di imparare (e di sbagliare)."
    },
    {
        "area": "AREA 3: I MUSCOLI (LA SQUADRA)",
        "testo": "I TUOI DIPENDENTI SANNO QUAL È L'OBIETTIVO DEL MESE?",
        "sotto": "(O vengono solo a timbrare il cartellino?)",
        "opzioni": [
            {"testo": "🔴 NON CREDO / SANNO SOLO IL LORO COMPITINO", "punti": 1},
            {"testo": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "punti": 0}
        ],
        "lezione": "Non puoi chiedere a qualcuno di aiutarti a vincere la partita se non gli dici qual è il punteggio. Condividere gli obiettivi crea alleati. Nasconderli crea mercenari."
    },
    {
        "area": "AREA 3: I MUSCOLI (LA SQUADRA)",
        "testo": "QUANDO C'È UN ERRORE, CERCHI IL COLPEVOLE O LA CAUSA?",
        "sotto": "(Onestamente).",
        "opzioni": [
            {"testo": "🔴 CHI HA SBAGLIATO?", "punti": 1},
            {"testo": "🟢 DOVE HA SBAGLIATO IL PROCESSO?", "punti": 0}
        ],
        "lezione": "Nel 90% dei casi, le persone sbagliano perché il processo è confuso. Sgridare le persone è inutile. Aggiustare la procedura è definitivo."
    },
    # AREA 4
    {
        "area": "AREA 4: IL CERVELLO (LA STRATEGIA)",
        "testo": "PRENDI LE DECISIONI BASANDOTI SUI DATI O SULL'INTUITO?",
        "sotto": "(Esempio: quale prodotto spingere, quale cliente tagliare).",
        "opzioni": [
            {"testo": "🔴 INTUITO / ESPERIENZA", "punti": 1},
            {"testo": "🟢 DATI / REPORT", "punti": 0}
        ],
        "lezione": "L'intuito è sopravvalutato. Spesso è solo un pregiudizio mascherato. I dati sono freddi, noiosi e veritieri. Fidati di Excel, non della pancia."
    },
    {
        "area": "AREA 4: IL CERVELLO (LA STRATEGIA)",
        "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE PAGANTE?",
        "sotto": "(Se è tossico, rompiscatole o fuori target).",
        "opzioni": [
            {"testo": "🔴 NO, IL FATTURATO È FATTURATO", "punti": 1},
            {"testo": "🟢 SÌ, HO LICENZIATO DEI CLIENTI", "punti": 0}
        ],
        "lezione": "Non tutti i soldi sono uguali. I soldi di un cliente tossico costano il triplo in stress e tempo. 'Licenziare' i clienti peggiori è il modo più veloce per aumentare gli utili."
    },
    {
        "area": "AREA 4: IL CERVELLO (LA STRATEGIA)",
        "testo": "CONOSCI IL TUO PRODOTTO 'BEST SELLER' PER MARGINE?",
        "sotto": "(Non quello che vendi di più. Quello che ti fa guadagnare di più).",
        "opzioni": [
            {"testo": "🔴 NON SONO SICURO", "punti": 1},
            {"testo": "🟢 SÌ, ED È QUELLO CHE SPINGO", "punti": 0}
        ],
        "lezione": "Spesso vendiamo tantissimo prodotti che ci lasciano le briciole (basso margine) e trascuriamo quelli d'oro. Se non sai cosa ti arricchisce, lavorerai tanto per guadagnare poco."
    },
    {
        "area": "AREA 4: IL CERVELLO (LA STRATEGIA)",
        "testo": "SAI QUANTO TI COSTA ACQUISIRE UN NUOVO CLIENTE?",
        "sotto": "(Marketing, tempo commerciale, pubblicità).",
        "opzioni": [
            {"testo": "🔴 BO, È IMPOSSIBILE SAPERLO", "punti": 1},
            {"testo": "🟢 SÌ, IL MIO CAC (COSTO ACQUISIZIONE) È CHIARO", "punti": 0}
        ],
        "lezione": "Se spendi 100€ per acquisire un cliente che te ne porta 50€ di margine, stai pagando per lavorare. La matematica del marketing deve tornare."
    },
    {
        "area": "AREA 4: IL CERVELLO (LA STRATEGIA)",
        "testo": "HAI UN PIANO SCRITTO PER I PROSSIMI 12 MESI?",
        "sotto": "(Non un sogno. Un piano).",
        "opzioni": [
            {"testo": "🔴 È TUTTO NELLA MIA TESTA", "punti": 1},
            {"testo": "🟢 SÌ, È SCRITTO E CONDIVISO", "punti": 0}
        ],
        "lezione": "Se è nella tua testa, è un sogno (o un'allucinazione). Se è scritto, è un progetto. Le aziende si costruiscono sui progetti, non sulle allucinazioni."
    }
]

# --- INIZIALIZZAZIONE STATO ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'show_lesson' not in st.session_state: st.session_state.show_lesson = False

# --- INTERFACCIA ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=200) 
st.title("🐹 ANSIA S.P.A.")
st.subheader("Diagnosi per Titolari Criceti")

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    st.markdown(f"<div class='area-header'>{item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(item['sotto'])
    st.divider()

    if not st.session_state.show_lesson:
        # Generiamo i bottoni in base alle opzioni specifiche della domanda
        for opt in item['opzioni']:
            if st.button(opt['testo']):
                st.session_state.score += opt['punti']
                st.session_state.show_lesson = True
                st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        
        # Testo del tasto dinamico
        testo_tasto = "VEDI LA TUA DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        
        if st.button(testo_tasto):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- RISULTATO FINALE ---
    with st.spinner("Generando la prognosi..."):
        time.sleep(1.5)
        
    score = st.session_state.score
    st.header("📊 RISULTATO DELLA DIAGNOSI")
    st.metric("PUNTEGGIO TOTALE", f"{score} Punti")

    # LOGICA PROFILI (Esattamente come da tuo testo)
    if score <= 4:
        titolo, colore = "PROFILO A: L'OROLOGIO SVIZZERO (O IL BUGIARDO)", "#d4edda"
        testo = """Complimenti. Se i tuoi dati sono veri, sei nell'1% degli imprenditori che ha capito come si gioca.
        Hai costruito un sistema che funziona, hai liquidità e probabilmente riesci anche ad andare in vacanza. Sei un caso raro.
        <br><br><b>Prognosi:</b> Ottima, ma attenzione alla 'Zona di Comfort'. Il tuo prossimo obiettivo è l'Espansione."""
    elif score <= 12:
        titolo, colore = "PROFILO B: IL CRICETO STANCO", "#fff3cd"
        testo = """Sei nella media italiana. L'azienda sta in piedi, i soldi girano, ma il motore sta fondendo. Sei stanco.
        Lavori troppo per compensare la mancanza di processi. Riesci a gestire le emergenze, ma non riesci a pianificare il futuro.
        <br><br><b>Prognosi:</b> Sei a rischio. Se il mercato tossisce, l'azienda prende la polmonite. Devi smettere di correre e iniziare a organizzare."""
    else:
        titolo, colore = "PROFILO C: L'AZIENDA POSSEDUTA", "#f8d7da"
        testo = """Allarme Rosso. Non indoriamo la pillola: sei nei guai. Non stai guidando l'azienda; sei passeggero di un treno in fiamme senza freni.
        I soldi escono senza controllo, il tempo evapora e tu sei l'unico che tiene insieme i pezzi con lo scotch.
        <br><br><b>Prognosi:</b> Riservata. Se non intervieni drasticamente con un 'Esorcismo Aziendale', il fallimento è una questione di 'quando', non di 'se'."""

    st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p style='font-size: 18px;'>{testo}</p></div>", unsafe_allow_html=True)
    st.divider()
    
    st.subheader("LA PROGNOSI NON È IL DESTINO")
    st.write("""Il Caos ha una caratteristica fisica: l'Entropia. Se lasciato a se stesso, peggiora sempre. Non guarisce col tempo. Guarisce solo con l'azione. 
    Il Kit che hai scaricato è il primo passo. Ma se vuoi ricostruire le fondamenta, serve un Architetto.""")
    
    st.write("")
    col_a, col_b = st.columns(2)
    with col_a: st.link_button("📘 SCARICA L'EBOOK", "https://yourlink.com", type="primary")
    with col_b: st.link_button("📅 PRENOTA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI
    st.write("")
    st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f1f1f1; border-radius: 10px;'>
            <b>Daniele Salvatori | comunicAttivamente</b><br>
            📧 <a href='mailto:daniele@comunicattivamente.it'>daniele@comunicattivamente.it</a> | 📞 +39 392 933 4563<br>
            🌐 <a href='http://www.comunicattivamente.it'>www.comunicAttivamente.it</a>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("---")
    if st.button("🔄 RICOMINCIA IL TEST"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
