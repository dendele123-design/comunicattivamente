import streamlit as st
import time
import pandas as pd
import random
from datetime import datetime

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (#DC0612)
# =================================================================
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
    <style>
    /* ANTI DARK-MODE E COLORI BASE */
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li {{
        color: #1a1a1a !important;
    }}

    /* HEADER RAFFINATO */
    .main-header {{
        border: 3px solid {ROSSO_BRAND};
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        background-color: #fdfdfd;
    }}
    .main-header h1 {{ 
        color: {ROSSO_BRAND} !important; 
        margin: 0; 
        font-size: 1.8em !important; 
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    /* TITOLI E BOX INFO */
    h2, h3 {{ color: {ROSSO_BRAND} !important; }}
    .info-box {{
        background-color: #f8f9fa !important; border-left: 8px solid {ROSSO_BRAND} !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }}

    /* BOX LEZIONE ESORCISTA (Durante il test) */
    .lesson-box {{ 
        background-color: #000000 !important; color: #ffffff !important; 
        padding: 25px; border-radius: 10px; border-left: 10px solid {ROSSO_BRAND} !important; 
        margin-top: 20px; font-style: italic; 
    }}
    .lesson-box b, .lesson-box p {{ color: #ffffff !important; }}

    /* PROFILO FINALE */
    .profile-box {{ padding: 30px; border-radius: 15px; border: 3px solid #000 !important; margin-top: 20px; }}

    /* BOTTONI */
    div.stButton > button {{
        border-radius: 10px !important; height: 3.5em; font-weight: bold; text-transform: uppercase;
    }}
    div.stButton > button[kind="primary"] {{
        background-color: {ROSSO_BRAND} !important; color: #ffffff !important; border: none !important;
    }}

    /* FOOTER */
    .footer {{
        text-align: center; padding: 30px; background-color: #f1f1f1;
        border-radius: 15px; margin-top: 50px; border-top: 6px solid {ROSSO_BRAND};
    }}
    .footer a {{ color: {ROSSO_BRAND} !important; text-decoration: none; font-weight: bold; }}
    
    header {{visibility: hidden !important;}} footer {{visibility: hidden !important;}} #MainMenu {{visibility: hidden !important;}}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. DATABASE DOMANDE ANSIA S.P.A. (20 QUESITI)
# =================================================================
domande_ansia = [
    # AREA 1: SOLDI
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Margine pulito, non incasso.", "lezione": "Il fatturato è vanità. Guidare senza conoscere il margine è come correre senza guardare la benzina: ti fermerai all'improvviso.", "opzioni": [{"t": "🔴 NO / SOLO FATTURATO", "p": 1}, {"t": "🟢 SÌ, CONOSCO IL MARGINE", "p": 0}]},
    {"area": "SOLDI", "testo": "VAI A 'SENTIMENTO' CON I PREZZI?", "sotto": "O hai un calcolo matematico dei costi?", "lezione": "Il 'prezzo di mercato' è una bugia. Il prezzo deve coprire i TUOI costi e garantirti il TUO margine. La matematica non ha sentimenti.", "opzioni": [{"t": "🔴 SÌ, VADO A OCCHIO", "p": 1}, {"t": "🟢 NO, HO IL CALCOLO DEI COSTI", "p": 0}]},
    {"area": "SOLDI", "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?", "sotto": "Cedi pur di non perdere il cliente?", "lezione": "Lo sconto è la droga dei poveri. Se togli il 10% dal prezzo, spesso togli il 50% dal tuo utile netto.", "opzioni": [{"t": "🔴 SÌ, SPESSO", "p": 1}, {"t": "🟢 MAI / SOLO IN CAMBIO DI ALTRO", "p": 0}]},
    {"area": "SOLDI", "testo": "SAI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "La cifra esatta per coprire tutte le spese.", "lezione": "Se non sai quanto ti costa tenere la serranda alzata, vivi nell'ansia. Il Break-Even ti dà la calma strategica.", "opzioni": [{"t": "🔴 NON ESATTAMENTE", "p": 1}, {"t": "🟢 LO SO AL CENTESIMO", "p": 0}]},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "Quanti mesi di ossigeno hai in cassa?", "lezione": "Le aziende falliscono perché finiscono la cassa. Se vivi bonifico su bonifico, sei ostaggio dei tuoi clienti.", "opzioni": [{"t": "🔴 MENO DI UN MESE", "p": 1}, {"t": "🟢 ALMENO 3 MESI", "p": 0}]},
    
    # AREA 2: TEMPO
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "Tutti sanno di cosa si parla e per quanto tempo?", "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa. Senza obiettivo, avete solo bruciato stipendi.", "opzioni": [{"t": "🔴 NO, PARLIAMO E BASTA", "p": 1}, {"t": "🟢 SÌ, SEMPRE", "p": 0}]},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "O è il 'Ding' del telefono a deciderlo per te?", "lezione": "La reattività immediata è nevrosi. Il cervello impiega 15 min per ritrovare il focus. Se rispondi subito, reagisci, non lavori.", "opzioni": [{"t": "🔴 APPENA ARRIVANO", "p": 1}, {"t": "🟢 A BLOCCHI ORARI FISSI", "p": 0}]},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "Fatture, loghi, preventivi spariti...", "lezione": "Il caos digitale mangia 40 min al giorno a ogni dipendente. Sono settimane di stipendio pagate per giocare a nascondino.", "opzioni": [{"t": "🔴 TANTO / DIPENDE", "p": 1}, {"t": "🟢 ZERO, SO DOVE SONO", "p": 0}]},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "O hai un filtro o orari dedicati?", "lezione": "Essere sempre disponibili ti fa sembrare servile. Il chirurgo non risponde al cellulare mentre opera. Tu sì?", "opzioni": [{"t": "🔴 RISPONDO SEMPRE", "p": 1}, {"t": "🟢 HO FILTRI E ORARI", "p": 0}]},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "O ti chiedono ancora 'Sei libero martedì'?", "lezione": "Chiedere la disponibilità a voce genera un ping-pong inutile. Il calendario occupato zittisce il caos.", "opzioni": [{"t": "🔴 NO / WHATSAPP", "p": 1}, {"t": "🟢 SÌ, GOOGLE CALENDAR", "p": 0}]},

    # AREA 3: SQUADRA
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE...?", "sotto": "L'azienda produce utile senza di te?", "lezione": "Se l'azienda sei tu, hai un lavoro a vita da cui non puoi dimetterti. L'obiettivo è rendersi inutili operativamente.", "opzioni": [{"t": "🔴 SI FERMA / CROLLA", "p": 1}, {"t": "🟢 VA AVANTI", "p": 0}]},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "Manuali operativi su come si fanno le cose.", "lezione": "L'oralità è il medioevo. Se devi spiegare una cosa due volte, hai fallito. Scrivila o fai un video.", "opzioni": [{"t": "🔴 NO, È NELLA TESTA", "p": 1}, {"t": "🟢 SÌ, ABBIAMO I MANUALI", "p": 0}]},
    {"area": "SQUADRA", "testo": "TI SENTI DIRE 'FACCIO PRIMA A FARLO IO'?", "sotto": "E alla fine il lavoro operativo lo fai tu.", "lezione": "Questa frase è la lapide della tua crescita. Facendo l'operativo, uccidi il tempo per la strategia.", "opzioni": [{"t": "🔴 QUASI OGNI GIORNO", "p": 1}, {"t": "🟢 RARAMENTE", "p": 0}]},
    {"area": "SQUADRA", "testo": "I DIPENDENTI SANNO L'OBIETTIVO DEL MESE?", "sotto": "O vengono solo a timbrare il cartellino?", "lezione": "Non puoi vincere se la squadra non sa il punteggio. Condividere gli obiettivi crea alleati, nasconderli crea mercenari.", "opzioni": [{"t": "🔴 NON CREDO", "p": 1}, {"t": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "p": 0}]},
    {"area": "SQUADRA", "testo": "ERRORE: CERCHI IL COLPEVOLE O LA CAUSA?", "sotto": "Chi ha sbagliato o dove è fallito il processo?", "lezione": "Sgridare le persone è inutile se il processo è confuso. Aggiustare la procedura è l'unico modo definitivo.", "opzioni": [{"t": "🔴 CHI HA SBAGLIATO?", "p": 1}, {"t": "🟢 DOVE È FALLITO IL PROCESSO?", "p": 0}]},

    # AREA 4: STRATEGIA
    {"area": "STRATEGIA", "testo": "DECISIONI SUI DATI O SULL'INTUITO?", "sotto": "Cosa spingere o chi tagliare si decide con i report?", "lezione": "L'intuito è spesso un pregiudizio mascherato. I dati sono freddi e veritieri. Fidati di Excel, non della pancia.", "opzioni": [{"t": "🔴 INTUITO / PANCIA", "p": 1}, {"t": "🟢 DATI / REPORT", "p": 0}]},
    {"area": "STRATEGIA", "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE?", "sotto": "Se è tossico o fuori target, lo licenzi?", "lezione": "Non tutti i soldi sono uguali. I soldi di un cliente tossico costano il triplo in stress. Licenziarli aumenta gli utili.", "opzioni": [{"t": "🔴 NO, FATTURATO È TUTTO", "p": 1}, {"t": "🟢 SÌ, HO LICENZIATO CLIENTI", "p": 0}]},
    {"area": "STRATEGIA", "testo": "CONOSCI IL TUO BEST SELLER PER MARGINE?", "sotto": "Quello che ti arricchisce, non quello che vendi di più.", "lezione": "Spesso vendiamo tantissimo prodotti che lasciano briciole. Se non sai cosa ti arricchisce, lavorerai tanto per poco.", "opzioni": [{"t": "🔴 NON SONO SICURO", "p": 1}, {"t": "🟢 SÌ, LO CONOSCO", "p": 0}]},
    {"area": "STRATEGIA", "testo": "SAI QUANTO COSTA ACQUISIRE UN CLIENTE?", "sotto": "Marketing, tempo commerciale, chiamate...", "lezione": "Se spendi 100€ per acquisire chi te ne porta 50€ di margine, stai pagando per lavorare.", "opzioni": [{"t": "🔴 IMPOSSIBILE SAPERLO", "p": 1}, {"t": "🟢 SÌ, IL CAC È CHIARO", "p": 0}]},
    {"area": "STRATEGIA", "testo": "HAI UN PIANO SCRITTO PER I 12 MESI?", "sotto": "Non un sogno, un piano con date e nomi.", "lezione": "Se è nella testa, è un'allucinazione. Se è scritto, è un progetto. Le aziende si costruiscono sui progetti.", "opzioni": [{"t": "🔴 È NELLA MIA TESTA", "p": 1}, {"t": "🟢 SÌ, SCRITTO E CONDIVISO", "p": 0}]}
]

# =================================================================
# 3. STATO SESSIONE
# =================================================================
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'area_scores' not in st.session_state: st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False
if 'show_feedback' not in st.session_state: st.session_state.show_feedback = False
if 'timer_running' not in st.session_state: st.session_state.timer_running = False

# =================================================================
# 4. INTERFACCIA E MENU
# =================================================================
st.markdown("<div class='main-header'><h1>🛡️ HUB DELL'EFFICIENZA</h1></div>", unsafe_allow_html=True)

menu = st.selectbox("COSA DEVI FARE OGGI?", [
    "🏠 Home Page", 
    "📊 Diagnosi Strategica (Ansia SPA)", 
    "🛠️ Pronto Intervento (Toolkit)", 
    "📖 Pillole di Efficienza (Bignami)"
])

# --- 🏠 HOME PAGE ---
if menu == "🏠 Home Page":
    st.subheader("Basta correre sulla ruota.")
    st.markdown("<div class='info-box'>Benvenuto, Ammiraglio. Questa è la tua centrale di comando digitale. Usa gli strumenti per eliminare il rumore e navigare verso il margine reale.</div>", unsafe_allow_html=True)
    st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=150)
    st.write("📈 **Strategia:** Test Ansia SPA completo.")
    st.write("⚙️ **Operatività:** Toolkit 'La Riunione poteva essere una Mail'.")

# --- 📊 DIAGNOSI (ANSIA SPA - VERSIONE 20 DOMANDE) ---
elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.markdown(f"<div class='info-box'><b>AREA: {item['area']}</b></div>", unsafe_allow_html=True)
            st.write(f"**QUESITO {step + 1} di {len(domande_ansia)}**")
            st.header(item['testo'])
            st.write(f"*{item['sotto']}*")
            st.divider()
            
            if not st.session_state.show_feedback:
                c1, c2 = st.columns(2)
                if c1.button(item['opzioni'][0]['t'], key=f"btn0_{step}"):
                    st.session_state.score_ansia += item['opzioni'][0]['p']
                    st.session_state.area_scores[item['area']] += item['opzioni'][0]['p']
                    st.session_state.show_feedback = True
                    st.rerun()
                if c2.button(item['opzioni'][1]['t'], key=f"btn1_{step}"):
                    st.session_state.show_feedback = True
                    st.rerun()
            else:
                st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
                st.write("")
                label_next = "VEDI LA TUA DIAGNOSI 📊" if step == len(domande_ansia)-1 else "PROSSIMA DOMANDA ➡️"
                if st.button(label_next, type="primary"):
                    st.session_state.step_ansia += 1
                    st.session_state.show_feedback = False
                    st.rerun()
        else:
            st.session_state.ansia_complete = True
            st.rerun()
    else:
        # RISULTATI FINALI
        with st.spinner("L'Esorcista sta calcolando il tuo livello di ansia..."): time.sleep(1.5)
        score = st.session_state.score_ansia
        st.subheader("📊 IL RISULTATO DELLA TUA DIAGNOSI")
        
        if score <= 4:
            titolo, colore, desc = "PROFILO A: L'OROLOGIO SVIZZERO", "#d4edda", "Complimenti. Sei nell'1% degli imprenditori. Hai un sistema, non un lavoro."
        elif score <= 12:
            titolo, colore, desc = "PROFILO B: IL CRICETO STANCO", "#fff3cd", "Sei nella media. L'azienda sta in piedi ma tu sei esausto. Serve metodo subito."
        else:
            titolo, colore, desc = "PROFILO C: L'AZIENDA POSSEDUTA", "#f8d7da", "Allarme Rosso. Sei passeggero di un treno in fiamme. Serve intervento drastico."

        st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p>{desc}</p></div>", unsafe_allow_html=True)

        # KIT DI SOPRAVVIVENZA DINAMICO
        st.write("")
        st.markdown("### 🚑 KIT DI SOPRAVVIVENZA")
        aree_critiche = sorted(st.session_state.area_scores.items(), key=lambda x: x[1], reverse=True)
        for area, punti in aree_critiche[:3]:
            if punti > 0:
                if area == "SOLDI": st.info("💰 **SOLDI:** Smetti di guardare l'incasso. Domani chiedi il MARGINE reale su ogni prodotto.")
                if area == "TEMPO": st.info("⏰ **TEMPO:** Disattiva le notifiche. Blocca due slot da 30 min per le mail e basta.")
                if area == "SQUADRA": st.info("👥 **SQUADRA:** Registra un video (Loom) di un compito ripetitivo. Ecco la tua prima procedura.")
                if area == "STRATEGIA": st.info("🎯 **STRATEGIA:** Analizza i clienti. Trova il più tossico e preparati a dirgli di 'No'.")

        if st.button("🔄 RICOMINCIA TEST", type="primary"):
            st.session_state.step_ansia = 0; st.session_state.score_ansia = 0; st.session_state.ansia_complete = False; st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}; st.rerun()

# --- 🛠️ PRONTO INTERVENTO (TOOLKIT) ---
elif menu == "🛠️ Pronto Intervento (Toolkit)":
    tool = st.radio("Seleziona strumento:", ["💸 Timer dello Spreco", "📅 Invito Intelligente", "📡 Filtro Urgenza", "📑 Generatore SOP", "🧭 Cruscotto Ammiraglio"], horizontal=True)
    st.divider()

    if tool == "💸 Timer dello Spreco":
        st.write("### Se la riunione non ha un obiettivo, stai bruciando soldi:")
        c1, c2 = st.columns(2)
        n_p = c1.number_input("Partecipanti", 1, 50, 4)
        costo_h = c2.number_input("Costo orario medio (€)", 1, 500, 45)
        costo_al_sec = (n_p * costo_h) / 3600
        if not st.session_state.timer_running:
            if st.button("▶️ AVVIA RIUNIONE", type="primary"):
                st.session_state.timer_running = True; st.session_state.start_time = time.time(); st.rerun()
        else:
            ph = st.empty()
            if st.button("🛑 FERMA RIUNIONE"): st.session_state.timer_running = False; st.rerun()
            while st.session_state.timer_running:
                bruciato = (time.time() - st.session_state.start_time) * costo_al_sec
                ph.markdown(f"<div class='timer-box'>{bruciato:.2f} €</div>", unsafe_allow_html=True)
                time.sleep(1)

    elif tool == "📑 Generatore SOP":
        st.markdown("<div class='info-box'>Crea qui la bozza della tua procedura digitale.</div>", unsafe_allow_html=True)
        titolo = st.text_input("Nome Procedura", "Esempio: Gestione Nuova Fattura")
        passaggi = st.text_area("Passaggi (1, 2, 3...)")
        if st.button("GENERA SCHEMA", type="primary"):
            st.code(f"PROCEDURA: {titolo}\n\nSTEP:\n{passaggi}", language="text")
    
    # ... Gli altri tool restano simili (Codice abbreviato per brevità)
    else:
        st.info("Strumento in fase di ottimizzazione. Usa gli altri nel frattempo!")

# --- 📖 BIGNAMI ---
elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("Protocolli Anti-Ansia")
    with st.expander("🛡️ PROTOCOLLO 1: LA FONTE DELLA VERITÀ"): st.write("Una sola cartella Cloud AZIENDA. Se mandi un file via mail, crei caos.")
    with st.expander("📑 PROTOCOLLO 4: CLONAZIONE UMANA"): st.write("Registra video mentre lavori. Non spiegare due volte la stessa cosa a voce.")

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        <b>Daniele Salvatori</b><br>
        <i>Esorcista Aziendale | Partner SuPeR</i><br><br>
        📧 <a href="mailto:daniele@comunicattivamente.it">daniele@comunicattivamente.it</a> | 
        📞 <a href="tel:+393929334563">+39 392 933 4563</a><br><br>
        <a href="https://wa.me/393929334563" style="background-color:#25D366; color:white !important; padding:10px 20px; border-radius:50px; text-decoration:none;">💬 CHATTA SU WHATSAPP</a><br><br>
        🌐 <a href="https://www.comunicattivamente.it">www.comunicattivamente.it</a>
    </div>
""", unsafe_allow_html=True)
