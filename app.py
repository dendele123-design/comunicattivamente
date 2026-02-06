import streamlit as st
import time
import pandas as pd
import random
from datetime import datetime

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (#DC0612)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. Hub", page_icon="🛡️", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li {{
        color: #1a1a1a !important;
    }}
    .main-header {{
        border: 3px solid {ROSSO_BRAND};
        padding: 20px; border-radius: 15px; text-align: center;
        margin-bottom: 25px; background-color: #fdfdfd;
    }}
    .main-header h1 {{ color: {ROSSO_BRAND} !important; margin: 0; text-transform: uppercase; letter-spacing: 2px; }}
    .info-box {{
        background-color: #f8f9fa !important; border-left: 8px solid {ROSSO_BRAND} !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px;
    }}
    .lesson-box {{ 
        background-color: #000000 !important; color: #ffffff !important; 
        padding: 25px; border-radius: 10px; border-left: 10px solid {ROSSO_BRAND} !important; 
        margin-top: 20px; font-style: italic; 
    }}
    .lesson-box b, .lesson-box p {{ color: #ffffff !important; }}
    .profile-box {{ padding: 30px; border-radius: 15px; border: 3px solid #000 !important; margin-top: 20px; }}
    div.stButton > button {{ border-radius: 10px !important; height: 3.5em; font-weight: bold; text-transform: uppercase; }}
    div.stButton > button[kind="primary"] {{ background-color: {ROSSO_BRAND} !important; color: #ffffff !important; border: none !important; }}
    .timer-box {{
        font-size: 3em !important; font-weight: bold; color: {ROSSO_BRAND} !important; text-align: center;
        padding: 20px; border: 4px dashed {ROSSO_BRAND}; border-radius: 20px; margin: 20px 0; background-color: #fff5f5;
    }}
    .tool-desc {{ color: #666 !important; font-style: italic; margin-bottom: 15px; font-size: 0.95em; }}
    .footer {{ text-align: center; padding: 30px; background-color: #f1f1f1; border-radius: 15px; margin-top: 50px; border-top: 6px solid {ROSSO_BRAND}; }}
    .footer a {{ color: {ROSSO_BRAND} !important; text-decoration: none; font-weight: bold; }}
    header {{visibility: hidden !important;}} footer {{visibility: hidden !important;}} #MainMenu {{visibility: hidden !important;}}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. DATABASE DOMANDE (20 QUESITI COMPLETI)
# =================================================================
domande_ansia = [
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Margine pulito, non incasso.", "lezione": "Il fatturato è vanità. Senza margine sei un volontario, non un imprenditore.", "opzioni": [{"t": "🔴 NO / SOLO FATTURATO", "p": 1}, {"t": "🟢 SÌ, CONOSCO IL MARGINE", "p": 0}]},
    {"area": "SOLDI", "testo": "VAI A 'SENTIMENTO' CON I PREZZI?", "sotto": "O hai un calcolo matematico dei costi?", "lezione": "Il prezzo deve coprire i TUOI costi e il TUO margine. La matematica non ha sentimenti.", "opzioni": [{"t": "🔴 SÌ, VADO A OCCHIO", "p": 1}, {"t": "🟢 NO, HO IL CALCOLO DEI COSTI", "p": 0}]},
    {"area": "SOLDI", "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?", "sotto": "Cedi per non perdere il cliente?", "lezione": "Lo sconto è la droga dei poveri. Spesso togli il 50% dal tuo utile netto.", "opzioni": [{"t": "🔴 SÌ, SPESSO", "p": 1}, {"t": "🟢 MAI / SOLO IN CAMBIO DI ALTRO", "p": 0}]},
    {"area": "SOLDI", "testo": "SAI IL TUO PUNTO DI PAREGGIO MENSILE?", "sotto": "La cifra esatta per coprire ogni spesa.", "lezione": "Se non sai quanto ti costa la serranda alzata, vivi nell'ansia.", "opzioni": [{"t": "🔴 NON ESATTAMENTE", "p": 1}, {"t": "🟢 LO SO AL CENTESIMO", "p": 0}]},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "Quanti mesi di ossigeno (cassa) hai?", "lezione": "Le aziende falliscono perché finiscono la cassa. Costruisci la riserva di guerra.", "opzioni": [{"t": "🔴 MENO DI UN MESE", "p": 1}, {"t": "🟢 ALMENO 3 MESI", "p": 0}]},
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "Tutti sanno cosa si decide prima di entrare?", "lezione": "Una riunione senza agenda è beneficenza oraria ai dipendenti.", "opzioni": [{"t": "🔴 NO, PARLIAMO E BASTA", "p": 1}, {"t": "🟢 SÌ, SEMPRE", "p": 0}]},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "O è il 'Ding' del telefono a decidere per te?", "lezione": "La reattività non è efficienza. Se rispondi a tutto subito, sei un citofono.", "opzioni": [{"t": "🔴 APPENA ARRIVANO", "p": 1}, {"t": "🟢 A BLOCCHI ORARI FISSI", "p": 0}]},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "Preventivi, loghi, fatture...", "lezione": "Il caos digitale mangia settimane di stipendio all'anno a ogni dipendente.", "opzioni": [{"t": "🔴 TANTO / DIPENDE", "p": 1}, {"t": "🟢 ZERO, SO DOVE SONO", "p": 0}]},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "O hai un filtro/segretaria?", "lezione": "Essere sempre disponibili ti fa sembrare servile, non professionale.", "opzioni": [{"t": "🔴 RISPONDO SEMPRE", "p": 1}, {"t": "🟢 HO FILTRI E ORARI", "p": 0}]},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "O ti chiedono 'Sei libero martedì'?", "lezione": "Chiedere la disponibilità a voce genera un ping-pong inutile.", "opzioni": [{"t": "🔴 NO / WHATSAPP", "p": 1}, {"t": "🟢 SÌ, GOOGLE CALENDAR", "p": 0}]},
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE?", "sotto": "L'azienda produce utile senza di te?", "lezione": "Se l'azienda sei tu, hai un lavoro a vita da cui non puoi dimetterti.", "opzioni": [{"t": "🔴 SI FERMA / CROLLA", "p": 1}, {"t": "🟢 VA AVANTI", "p": 0}]},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "Manuali operativi su come si fanno le cose.", "lezione": "L'oralità è il medioevo. Se spieghi due volte la stessa cosa, hai fallito.", "opzioni": [{"t": "🔴 NO, È NELLA TESTA", "p": 1}, {"t": "🟢 SÌ, ABBIAMO I MANUALI", "p": 0}]},
    {"area": "SQUADRA", "testo": "TI SENTI DIRE 'FACCIO PRIMA A FARLO IO'?", "sotto": "E alla fine lo fai tu.", "lezione": "Questa frase è la lapide della tua crescita aziendale.", "opzioni": [{"t": "🔴 QUASI OGNI GIORNO", "p": 1}, {"t": "🟢 RARAMENTE", "p": 0}]},
    {"area": "SQUADRA", "testo": "I DIPENDENTI SANNO L'OBIETTIVO DEL MESE?", "sotto": "O vengono solo a timbrare il cartellino?", "lezione": "Non puoi vincere se la squadra non sa il punteggio. Crea alleati, non mercenari.", "opzioni": [{"t": "🔴 NON CREDO", "p": 1}, {"t": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "p": 0}]},
    {"area": "SQUADRA", "testo": "ERRORE: CERCHI IL COLPEVOLE O LA CAUSA?", "sotto": "Onestamente: chi ha sbagliato o dov'è il buco nel processo?", "lezione": "Le persone sbagliano se il processo è confuso. Aggiustare la procedura è definitivo.", "opzioni": [{"t": "🔴 CHI HA SBAGLIATO?", "p": 1}, {"t": "🟢 DOVE È FALLITO IL PROCESSO?", "p": 0}]},
    {"area": "STRATEGIA", "testo": "PRENDI DECISIONI SUI DATI O SULL'INTUITO?", "sotto": "Report freddi o sensazioni della pancia?", "lezione": "L'intuito è spesso un pregiudizio mascherato. Fidati di Excel.", "opzioni": [{"t": "🔴 INTUITO / PANCIA", "p": 1}, {"t": "🟢 DATI / REPORT", "p": 0}]},
    {"area": "STRATEGIA", "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE?", "sotto": "Se è tossico o fuori target, lo licenzi?", "lezione": "I soldi di un cliente tossico costano il triplo in stress e tempo.", "opzioni": [{"t": "🔴 NO, FATTURATO È TUTTO", "p": 1}, {"t": "🟢 SÌ, HO LICENZIATO CLIENTI", "p": 0}]},
    {"area": "STRATEGIA", "testo": "CONOSCI IL TUO BEST SELLER PER MARGINE?", "sotto": "Cosa ti arricchisce davvero?", "lezione": "Spesso vendiamo tanto ciò che ci lascia briciole. Fermati e analizza.", "opzioni": [{"t": "🔴 NON SONO SICURO", "p": 1}, {"t": "🟢 SÌ, LO CONOSCO", "p": 0}]},
    {"area": "STRATEGIA", "testo": "SAI QUANTO COSTA ACQUISIRE UN CLIENTE?", "sotto": "Marketing, tempo, campagne...", "lezione": "Se spendi 100 per incassare 50 di margine, stai pagando per lavorare.", "opzioni": [{"t": "🔴 IMPOSSIBILE SAPERLO", "p": 1}, {"t": "🟢 SÌ, IL CAC È CHIARO", "p": 0}]},
    {"area": "STRATEGIA", "testo": "HAI UN PIANO SCRITTO PER I 12 MESI?", "sotto": "Non un sogno, un piano con date e nomi.", "lezione": "Se è nella testa, è un'allucinazione. Le aziende si basano sui progetti.", "opzioni": [{"t": "🔴 È NELLA MIA TESTA", "p": 1}, {"t": "🟢 SÌ, SCRITTO E CONDIVISO", "p": 0}]}
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

menu = st.selectbox("COSA DEVI FARE OGGI?", ["🏠 Home Page", "📊 Diagnosi Strategica (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Pillole di Efficienza"])

# --- 🏠 HOME PAGE ---
if menu == "🏠 Home Page":
    st.subheader("Basta correre sulla ruota.")
    st.markdown("<div class='info-box'>Benvenuto, Ammiraglio. Questa è la tua centrale di comando. Identifica i blocchi e riprenditi la tua libertà imprenditoriale.</div>", unsafe_allow_html=True)
    st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=150)

# --- 📊 DIAGNOSI (ANSIA SPA) ---
elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.write(f"**AREA: {item['area']}** | Quesito {step + 1} di {len(domande_ansia)}")
            st.header(item['testo'])
            if not st.session_state.show_feedback:
                c1, c2 = st.columns(2)
                if c1.button(item['opzioni'][0]['t'], key=f"n_{step}"):
                    st.session_state.score_ansia += item['opzioni'][0]['p']
                    st.session_state.area_scores[item['area']] += item['opzioni'][0]['p']
                    st.session_state.show_feedback = True; st.rerun()
                if c2.button(item['opzioni'][1]['t'], key=f"s_{step}"):
                    st.session_state.show_feedback = True; st.rerun()
            else:
                st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br>{item['lezione']}</div>", unsafe_allow_html=True)
                if st.button("PROSSIMA DOMANDA ➡️", type="primary"):
                    st.session_state.step_ansia += 1; st.session_state.show_feedback = False; st.rerun()
        else: st.session_state.ansia_complete = True; st.rerun()
    else:
        st.subheader("📊 LA TUA PROGNOSI")
        score = st.session_state.score_ansia
        if score <= 4:
            titolo, colore, desc = "PROFILO A: L'OROLOGIO SVIZZERO", "#d4edda", "Ottimo lavoro. Sei nell'1% degli imprenditori sani."
        elif score <= 12:
            titolo, colore, desc = "PROFILO B: IL CRICETO STANCO", "#fff3cd", "Sei nella media. L'azienda regge ma tu stai esaurendo l'energia."
        else:
            titolo, colore, desc = "PROFILO C: L'AZIENDA POSSEDUTA", "#f8d7da", "Allarme Rosso. Sei prigioniero di un sistema inefficiente."
        st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("### 🚑 KIT DI SOPRAVVIVENZA")
        critiche = sorted(st.session_state.area_scores.items(), key=lambda x: x[1], reverse=True)
        for area, punti in critiche[:3]:
            if punti > 0:
                if area == "SOLDI": st.info("💰 **SOLDI:** Smetti di guardare l'incasso. Chiedi il MARGINE reale domani.")
                if area == "TEMPO": st.info("⏰ **TEMPO:** Disattiva le notifiche. Blocca due slot da 30 min per le mail.")
                if area == "SQUADRA": st.info("👥 **SQUADRA:** Registra un video mentre lavori. Ecco la tua prima procedura.")
                if area == "STRATEGIA": st.info("🎯 **STRATEGIA:** Analizza i clienti. Trova il più tossico e lascialo andare.")
        if st.button("🔄 RICOMINCIA"): st.session_state.step_ansia = 0; st.session_state.ansia_complete = False; st.session_state.score_ansia = 0; st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}; st.rerun()

# --- 🛠️ PRONTO INTERVENTO (TOOLKIT) ---
elif menu == "🛠️ Pronto Intervento (Toolkit)":
    tool = st.radio("Seleziona strumento:", ["💸 Timer dello Spreco", "🔄 Calcolatore Delega", "🔔 Tassa sulle Notifiche", "🧗 Stipendio Reale"], horizontal=True)
    st.divider()

    if tool == "💸 Timer dello Spreco":
        st.write("### 💸 Timer dello Spreco")
        st.markdown("<p class='tool-desc'>Avvia il timer e guarda quanto ti costa una riunione senza un obiettivo stabilito.</p>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        n_p = c1.number_input("Partecipanti", 1, 50, 4)
        costo_h = c2.number_input("Costo orario medio (€)", 1, 500, 45)
        costo_al_sec = (n_p * costo_h) / 3600
        if not st.session_state.timer_running:
            if st.button("▶️ AVVIA RIUNIONE", type="primary"):
                st.session_state.timer_running = True; st.session_state.start_time = time.time(); st.rerun()
        else:
            if st.button("🛑 STOP / RESET"): st.session_state.timer_running = False; st.rerun()
            ph = st.empty()
            while st.session_state.timer_running:
                ph.markdown(f"<div class='timer-box'>{(time.time() - st.session_state.start_time) * costo_al_sec:.2f} €</div>", unsafe_allow_html=True)
                time.sleep(1)

    elif tool == "🔄 Calcolatore Delega":
        st.write("### 🔄 Calcolatore di Libertà")
        st.markdown("<p class='tool-desc'>Quanto tempo ti restituisce scrivere una procedura oggi invece di rispiegarla per sempre?</p>", unsafe_allow_html=True)
        min_c = st.number_input("Minuti per spiegare/fare ogni volta", 5, 300, 30)
        freq = st.slider("Volte al mese", 1, 30, 4)
        risparmio_h = (min_c * freq * 12) / 60
        st.write(f"### Risparmio Annuo: **{risparmio_h:.1f} Ore**")
        if st.button("VEDI VALORE DELEGA", type="primary"):
            st.success(f"Scrivere una procedura ti regala circa {int(risparmio_h/8)} giorni di ferie all'anno.")

    elif tool == "🔔 Tassa sulle Notifiche":
        st.write("### 🔔 Tassa sulle Notifiche (Money Edition)")
        st.markdown("<p class='tool-desc'>Ogni interruzione costa 15 min di focus. Quanto ti costa economicamente essere reattivo?</p>", unsafe_allow_html=True)
        ding = st.number_input("Volte al giorno che guardi il telefono per notifiche", 5, 200, 30)
        valore_h = st.number_input("Quanto vale un'ora del tuo tempo strategico? (€)", 20, 1000, 100)
        ore_perse = (ding * 15) / 60
        costo_die = ore_perse * valore_h
        st.error(f"Oggi stai buttando: € {costo_die:.2f}")
        if st.button("CALCOLA TASSA ANNUALE", type="primary"):
            st.subheader(f"Spreco Annuo: € {costo_die * 220:,.0f}")
            st.info("Spegnere le notifiche è l'investimento più redditizio che puoi fare.")

    elif tool == "🧗 Stipendio Reale":
        st.write("### 🧗 Il Paradosso del Titolare")
        st.markdown("<p class='tool-desc'>Calcola quanto guadagni davvero all'ora, considerando tutto il tempo passato a spegnere incendi.</p>", unsafe_allow_html=True)
        guadagno = st.number_input("Tuo guadagno mensile netto (prelievi titolare) €", 1000, 20000, 3000)
        ore_lavoro = st.number_input("Ore passate al lavoro (o a pensarci) a settimana", 20, 100, 50)
        paga_h = guadagno / (ore_lavoro * 4.3)
        st.write(f"## Paga Oraria Reale: € {paga_h:.2f}")
        if paga_h < 15: st.error("🚨 Guadagni come un dipendente junior, ma con tutti i rischi. Qualcosa non va.")
        else: st.success("✅ La tua paga oraria è dignitosa, ma possiamo migliorarla organizzando.")

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        <b>Daniele Salvatori</b><br><i>Esorcista Aziendale | Partner SuPeR</i><br><br>
        📞 <a href="tel:+393929334563">+39 392 933 4563</a> | 💬 <a href="https://wa.me/393929334563">WhatsApp</a><br>
        🌐 <a href="https://www.comunicattivamente.it">www.comunicattivamente.it</a>
    </div>
""", unsafe_allow_html=True)
