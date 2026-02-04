import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🐹", layout="centered")

# --- STILE CSS (Look Professionale & Aggressivo - Anti Dark Mode) ---
st.markdown("""
    <style>
    /* FORZA IL COLORE DEL TESTO E DELLO SFONDO PER EVITARE PROBLEMI CON DARK MODE */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {
        color: #1a1a1a !important; /* Grigio quasi nero */
    }
    
    .stApp {
        background-color: #ffffff !important;
    }

    /* BOTTONI */
    .stButton>button { 
        width: 100%; 
        border-radius: 5px; 
        height: 3.5em; 
        font-weight: bold; 
        text-transform: uppercase; 
        background-color: #f0f2f6 !important;
        color: #1a1a1a !important;
    }
    
    /* BOTTONE PRIMARIO (PROSSIMA DOMANDA) */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #ff4b4b !important;
        color: white !important;
    }

    /* AREA HEADER */
    .area-header { 
        background-color: #000000 !important; 
        color: white !important; 
        padding: 15px; 
        text-align: center; 
        font-weight: bold; 
        border-radius: 5px; 
        margin-bottom: 20px; 
        letter-spacing: 2px; 
    }

    /* LEZIONE ESORCISTA */
    .lesson-box { 
        background-color: #f8f9fa !important; 
        color: #1a1a1a !important; 
        padding: 25px; 
        border-radius: 10px; 
        border-left: 8px solid #ff4b4b !important; 
        margin-top: 20px; 
        font-style: italic; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
    }

    /* PROFILI FINALI */
    .profile-box { 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #000 !important; 
        margin-top: 20px; 
        color: #1a1a1a !important;
    }

    /* KIT DI SOPRAVVIVENZA */
    .survival-kit { 
        background-color: #fff3cd !important; 
        padding: 20px; 
        border-radius: 10px; 
        border: 2px dashed #856404 !important; 
        margin-top: 20px; 
        color: #856404 !important;
    }
    
    /* CONTATTI */
    .contact-box {
        text-align: center; 
        padding: 25px; 
        background-color: #f1f1f1 !important; 
        border-radius: 10px;
        margin-top: 40px;
    }
    
    .phone-link {
        white-space: nowrap !important;
        color: #ff4b4b !important;
        text-decoration: none !important;
        font-weight: bold !important;
        font-size: 1.2em;
    }

    /* NASCONDE ELEMENTI DI SISTEMA */
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stAppDeployButton {display:none !important;}
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DELLE 20 DOMANDE ---
domande = [
    # AREA 1: SOLDI
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "(Non quanto hai incassato. Quanto ti è rimasto pulito).", "opzioni": [{"testo": "🔴 NO / GUARDO IL FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, CONOSCO IL MARGINE", "punti": 0}], "lezione": "Il fatturato è vanità. Guidare guardando solo l'incasso è come guardare il tachimetro senza benzina: corri forte, ma ti fermerai all'improvviso."},
    {"area": "SOLDI", "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?", "sotto": "(O guardi i concorrenti e ti metti un po' sotto?)", "opzioni": [{"testo": "🔴 SÌ, VADO A OCCHIO", "punti": 1}, {"testo": "🟢 NO, HO UN CALCOLO MATEMATICO", "punti": 0}], "lezione": "Il 'prezzo di mercato' è una bugia. Se il tuo concorrente sta fallendo e tu lo copi, fallirai con lui. La matematica non ha sentimenti."},
    {"area": "SOLDI", "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?", "sotto": "(Cedi per non perdere il cliente?)", "opzioni": [{"testo": "🔴 SÌ, SPESSO", "punti": 1}, {"testo": "🟢 MAI / SOLO IN CAMBIO DI ALTRO", "punti": 0}], "lezione": "Lo sconto è la droga dei poveri. Se togli il 10% dal prezzo, spesso togli il 50% dal tuo utile netto."},
    {"area": "SOLDI", "testo": "SAI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "(La cifra esatta per coprire tutte le spese).", "opzioni": [{"testo": "🔴 NON ESATTAMENTE", "punti": 1}, {"testo": "🟢 LO SO AL CENTESIMO", "punti": 0}], "lezione": "Sapere il Break-Even ti dà la calma di dire: 'Dal giorno 20 del mese in poi, tutto quello che entra è guadagno'."},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "(Il test della cassa).", "opzioni": [{"testo": "🔴 MENO DI UN MESE", "punti": 1}, {"testo": "🟢 ALMENO 3 MESI", "punti": 0}], "lezione": "Le aziende falliscono perché finiscono la cassa, non gli utili. Devi costruire la riserva di guerra."},
    
    # AREA 2: TEMPO
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "(Tutti sanno di cosa si parla e per quanto?)", "opzioni": [{"testo": "🔴 NO, PARLIAMO E BASTA", "punti": 1}, {"testo": "🟢 SÌ, SEMPRE", "punti": 0}], "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa. Bruciate stipendi per non decidere nulla."},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "(O è il 'Ding' del telefono a deciderlo?)", "opzioni": [{"testo": "🔴 APPENA ARRIVANO", "punti": 1}, {"testo": "🟢 A BLOCCHI ORARI PREFISSATI", "punti": 0}], "lezione": "Il cervello impiega 15 minuti per riconcentrarsi dopo un'interruzione. Se leggi 20 mail in un'ora, non hai lavorato. Hai solo reagito."},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "(Preventivi, loghi, fatture...)", "opzioni": [{"testo": "🔴 TANTO / DIPENDE", "punti": 1}, {"testo": "🟢 ZERO, SO DOVE SONO", "punti": 0}], "lezione": "Cercare file mangia 40 minuti al giorno. Sono settimane di stipendio pagate per giocare a nascondino col server."},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "(O hai un filtro o orari dedicati?)", "opzioni": [{"testo": "🔴 RISPONDO SEMPRE", "punti": 1}, {"testo": "🟢 HO FILTRI E ORARI", "punti": 0}], "lezione": "Essere sempre disponibili ti fa sembrare servile. Il chirurgo non risponde al telefono mentre opera."},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "(O ti chiedono ancora 'Sei libero martedì'?)", "opzioni": [{"testo": "🔴 NO / USIAMO WHATSAPP", "punti": 1}, {"testo": "🟢 SÌ, GOOGLE CALENDAR", "punti": 0}], "lezione": "Chiedere 'quando sei libero' genera un ping-pong inutile. Il calendario occupato zittisce tutti."},

    # AREA 3: SQUADRA
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE...", "sotto": "(L'azienda continua o si ferma?)", "opzioni": [{"testo": "🔴 SI FERMA / CROLLA", "punti": 1}, {"testo": "🟢 VA AVANTI", "punti": 0}], "lezione": "Se l'azienda sei tu, hai un lavoro a vita da cui non puoi dimetterti. L'obiettivo è rendersi inutili operativamente."},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "(Manuali su come si fanno le cose)", "opzioni": [{"testo": "🔴 NO, È NELLA TESTA", "punti": 1}, {"testo": "🟢 SÌ, ABBIAMO I MANUALI", "punti": 0}], "lezione": "L'oralità è il medioevo. Se devi spiegare una cosa due volte, hai fallito. Scrivila o fai un video."},
    {"area": "SQUADRA", "testo": "TI SENTI DIRE 'FACCIO PRIMA A FARLO IO'?", "sotto": "(E alla fine lo fai tu)", "opzioni": [{"testo": "🔴 QUASI OGNI GIORNO", "punti": 1}, {"testo": "🟢 RARAMENTE", "punti": 0}], "lezione": "Questa frase è la lapide della tua crescita. Rubando tempo alla strategia, impedisci ai dipendenti di imparare."},
    {"area": "SQUADRA", "testo": "I DIPENDENTI SANNO L'OBIETTIVO DEL MESE?", "sotto": "(O sanno solo il loro compitino?)", "opzioni": [{"testo": "🔴 NON CREDO", "punti": 1}, {"testo": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "punti": 0}], "lezione": "Non puoi chiedere di vincere la partita se non dici qual è il punteggio. Condividere gli obiettivi crea alleati, nascondere crea mercenari."},
    {"area": "SQUADRA", "testo": "ERRORE: CERCHI IL COLPEVOLE O LA CAUSA?", "sotto": "(Onestamente)", "opzioni": [{"testo": "🔴 CHI HA SBAGLIATO?", "punti": 1}, {"testo": "🟢 DOVE HA SBAGLIATO IL PROCESSO?", "punti": 0}], "lezione": "Le persone sbagliano se il processo è confuso. Sgridare è inutile, aggiustare la procedura è definitivo."},

    # AREA 4: STRATEGIA
    {"area": "STRATEGIA", "testo": "DECISIONI: DATI O INTUITO?", "sotto": "(Cosa spingere, chi tagliare...)", "opzioni": [{"testo": "🔴 INTUITO / PANCIA", "punti": 1}, {"testo": "🟢 DATI / REPORT", "punti": 0}], "lezione": "L'intuito è spesso un pregiudizio mascherato. I dati sono freddi e veritieri. Fidati di Excel."},
    {"area": "STRATEGIA", "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE?", "sotto": "(Se è tossico o fuori target)", "opzioni": [{"testo": "🔴 NO, FATTURATO È FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, HO LICENZIATO CLIENTI", "punti": 0}], "lezione": "I soldi di un cliente tossico costano il triplo in stress. 'Licenziare' i peggiori aumenta gli utili."},
    {"area": "STRATEGIA", "testo": "CONOSCI IL TUO BEST SELLER PER MARGINE?", "sotto": "(Quello che ti fa guadagnare di più, non vendere di più)", "opzioni": [{"testo": "🔴 NON SONO SICURO", "punti": 1}, {"testo": "🟢 SÌ, LO CONOSCO", "punti": 0}], "lezione": "Spesso vendiamo tanto ciò che lascia briciole. Se non sai cosa ti arricchisce, lavorerai tanto per poco."},
    {"area": "STRATEGIA", "testo": "SAI QUANTO COSTA ACQUISIRE UN CLIENTE?", "sotto": "(Marketing, tempo commerciale...)", "opzioni": [{"testo": "🔴 BO, IMPOSSIBILE SAPERLO", "punti": 1}, {"testo": "🟢 SÌ, IL MIO CAC È CHIARO", "punti": 0}], "lezione": "Se spendi 100€ per acquisire chi te ne porta 50€, stai pagando per lavorare. La matematica deve tornare."},
    {"area": "STRATEGIA", "testo": "HAI UN PIANO SCRITTO PER I 12 MESI?", "sotto": "(Non un sogno, un piano)", "opzioni": [{"testo": "🔴 È NELLA MIA TESTA", "punti": 1}, {"testo": "🟢 SÌ, SCRITTO E CONDIVISO", "punti": 0}], "lezione": "Se è nella testa, è un'allucinazione. Le aziende si costruiscono sui progetti scritti."}
]

# --- STATO SESSIONE ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'area_scores' not in st.session_state: st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
if 'show_lesson' not in st.session_state: st.session_state.show_lesson = False

# --- HEADER ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=180)
st.title("🐹 ANSIA S.P.A.")

# --- LOGICA TEST ---
if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    st.markdown(f"<div class='area-header'>AREA: {item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(item['sotto'])
    st.divider()

    if not st.session_state.show_lesson:
        cols = st.columns(len(item['opzioni']))
        for i, opt in enumerate(item['opzioni']):
            if cols[i].button(opt['testo']):
                st.session_state.total_score += opt['punti']
                st.session_state.area_scores[item['area']] += opt['punti']
                st.session_state.show_lesson = True
                st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        btn_label = "VEDI LA TUA DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        if st.button(btn_label, type="primary"):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- RISULTATI FINALI ---
    with st.spinner("L'Esorcista sta elaborando..."): time.sleep(1.5)
    
    score = st.session_state.total_score
    st.header("📊 LA TUA DIAGNOSI FINALE")
    
    if score <= 4:
        st.success("PROFILO A: L'OROLOGIO SVIZZERO")
        st.write("Complimenti. Sei nell'1% degli imprenditori. Tutto gira liscio, ma non smettere di innovare.")
    elif score <= 12:
        st.markdown(f"<div class='profile-box' style='background-color: #fff3cd;'><h3>PROFILO B: IL CRICETO STANCO</h3><p>Sei nella media italiana. L'azienda sta in piedi, ma il motore sta fondendo. Lavori troppo per compensare la mancanza di processi.</p></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='profile-box' style='background-color: #f8d7da;'><h3>PROFILO C: L'AZIENDA POSSEDUTA</h3><p>Allarme Rosso. Sei passeggero di un treno in fiamme. Bruci ricchezza e salute.</p></div>", unsafe_allow_html=True)

    # --- IL KIT DI SOPRAVVIVENZA DINAMICO ---
    if score > 4:
        st.write("")
        st.markdown("### 🚑 KIT DI SOPRAVVIVENZA DELL'ESORCISTA")
        
        advice = []
        sorted_areas = sorted(st.session_state.area_scores.items(), key=lambda x: x[1], reverse=True)
        
        for area, s in sorted_areas[:3]:
            if area == "SOLDI" and s > 0: advice.append("💰 **SOLDI:** Domani chiedi al commercialista il tuo margine reale invece di guardare solo il fatturato.")
            if area == "TEMPO" and s > 0: advice.append("⏰ **TEMPO:** Blocca due slot da 30 min per le email e ignora le notifiche per il resto del giorno.")
            if area == "SQUADRA" and s > 0: advice.append("👥 **SQUADRA:** Scegli un compito che spieghi sempre a voce e registra un video mentre lo fai. Ecco la tua prima procedura.")
            if area == "STRATEGIA" and s > 0: advice.append("🎯 **STRATEGIA:** Guarda quale cliente ti fa perdere più tempo e preparati a dirgli di 'No'.")
        
        for a in advice: st.info(a)

    st.divider()
    st.subheader("LA PROGNOSI NON È IL DESTINO")
    st.write("Il Caos guarisce solo con l'azione. Non restare solo con il tuo punteggio.")
    
    c1, c2 = st.columns(2)
    c1.link_button("📘 SCARICA L'EBOOK COMPLETO", "https://yourlink.com", type="primary")
    c2.link_button("📅 PRENOTA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI CON NUMERO CLICCABILE E PROTEZIONE DARK MODE
    st.markdown("""
        <div class="contact-box">
            <b style="font-size: 1.1em;">Daniele Salvatori</b><br>
            <span style="color:#666;">Consulenza Organizzativa</span><br><br>
            📧 <a href="mailto:daniele@comunicattivamente.it" style="color: #ff4b4b !important;">daniele@comunicattivamente.it</a><br>
            📞 <a href="tel:+393929334563" class="phone-link">+39 392 933 4563</a>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("---")
    if st.button("🔄 RICOMINCIA IL TEST"):
        st.session_state.step = 0
        st.session_state.total_score = 0
        st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
        st.rerun()
