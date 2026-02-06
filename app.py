import streamlit as st
import time

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (#DC0612)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🎯", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
<style>
    /* FORZA TEMA CHIARO */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {{
        color: #1a1a1a !important;
    }}
    .stApp {{ background-color: #ffffff !important; }}
    
    header {{visibility: hidden !important;}}
    footer {{visibility: hidden !important;}}
    .stAppDeployButton {{display:none !important;}}
    [data-testid="stHeader"] {{display:none !important;}}

    /* LOGO TESTUALE */
    .brand-logo {{
        text-align: center;
        color: {ROSSO_BRAND} !important;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 0px;
    }}
    .brand-sub {{
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        color: #666 !important;
        margin-top: -10px;
        margin-bottom: 30px;
    }}

    /* AREA HEADER DOMANDA */
    .area-header {{ 
        background-color: #000000 !important; 
        color: white !important; 
        padding: 15px; 
        text-align: center; 
        font-weight: bold; 
        border-radius: 5px; 
        margin-bottom: 20px; 
    }}

    /* LEZIONE ESORCISTA */
    .lesson-box {{ 
        background-color: #f8f9fa !important; 
        color: #1a1a1a !important; 
        padding: 25px; 
        border-radius: 10px; 
        border-left: 8px solid {ROSSO_BRAND} !important; 
        margin-top: 20px; 
        font-style: italic; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
    }}

    /* PROFILI FINALI */
    .profile-box {{ padding: 30px; border-radius: 15px; border: 2px solid #000 !important; margin-top: 20px; }}

    /* BOTTONI */
    .stButton>button {{ width: 100%; border-radius: 5px; height: 3.5em; font-weight: bold; text-transform: uppercase; }}
    div.stButton > button:first-child[kind="primary"] {{
        background-color: {ROSSO_BRAND} !important;
        color: white !important;
        border: none;
    }}

    .phone-link {{ color: {ROSSO_BRAND} !important; text-decoration: none; font-weight: bold; white-space: nowrap; }}
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. DATABASE DELLE 20 DOMANDE
# =================================================================
domande = [
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Margine pulito, non incasso.", "opzioni": [{"testo": "🔴 NO / SOLO FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, CONOSCO IL MARGINE", "punti": 0}], "lezione": "Il fatturato è vanità. Guidare senza conoscere il margine è come correre senza guardare la benzina."},
    {"area": "SOLDI", "testo": "VAI A 'SENTIMENTO' CON I PREZZI?", "sotto": "O hai un calcolo matematico dei costi?", "opzioni": [{"testo": "🔴 SÌ, VADO A OCCHIO", "punti": 1}, {"testo": "🟢 NO, HO IL CALCOLO DEI COSTI", "punti": 0}], "lezione": "Il 'prezzo di mercato' è una bugia. La matematica non ha sentimenti."},
    {"area": "SOLDI", "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?", "sotto": "Cedi per non perdere il cliente?", "opzioni": [{"testo": "🔴 SÌ, SPESSO", "punti": 1}, {"testo": "🟢 MAI / SOLO IN CAMBIO DI ALTRO", "punti": 0}], "lezione": "Lo sconto è la droga dei poveri. Togli il 10% dal prezzo e spesso togli il 50% dal tuo utile."},
    {"area": "SOLDI", "testo": "SAI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "La cifra esatta per coprire ogni spesa.", "opzioni": [{"testo": "🔴 NON ESATTAMENTE", "punti": 1}, {"testo": "🟢 LO SO AL CENTESIMO", "punti": 0}], "lezione": "Se non sai quanto ti costa tenere la serranda alzata, vivi nell'ansia."},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "Quanti mesi di ossigeno hai in cassa?", "opzioni": [{"testo": "🔴 MENO DI UN MESE", "punti": 1}, {"testo": "🟢 ALMENO 3 MESI", "punti": 0}], "lezione": "Le aziende falliscono perché finiscono la cassa. Costruisci la riserva di guerra."},
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "Tutti sanno di cosa si parla o lo scoprite lì?", "opzioni": [{"testo": "🔴 NO, PARLIAMO E BASTA", "punti": 1}, {"testo": "🟢 SÌ, SEMPRE", "punti": 0}], "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa."},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "O è il 'Ding' del telefono a deciderlo?", "opzioni": [{"testo": "🔴 APPENA ARRIVANO", "punti": 1}, {"testo": "🟢 A BLOCCHI ORARI FISSI", "punti": 0}], "lezione": "La reattività immediata è nevrosi. Se rispondi a tutto subito, sei un citofono."},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "Fatture, loghi, preventivi...", "opzioni": [{"testo": "🔴 TANTO / DIPENDE", "punti": 1}, {"testo": "🟢 ZERO, SO DOVE SONO", "punti": 0}], "lezione": "Il caos digitale mangia settimane di stipendio all'anno a ogni dipendente."},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "O hai un filtro/segretaria?", "opzioni": [{"testo": "🔴 RISPONDO SEMPRE", "punti": 1}, {"testo": "🟢 HO FILTRI E ORARI", "punti": 0}], "lezione": "Essere sempre disponibili ti fa sembrare servile. Il chirurgo non risponde al cellulare mentre opera."},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "O ti chiedono ancora 'Sei libero martedì'?", "opzioni": [{"testo": "🔴 NO / WHATSAPP", "punti": 1}, {"testo": "🟢 SÌ, GOOGLE CALENDAR", "punti": 0}], "lezione": "Chiedere la disponibilità a voce genera un ping-pong inutile."},
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE...?", "sotto": "L'azienda produce utile senza di te?", "opzioni": [{"testo": "🔴 SI FERMA / CROLLA", "punti": 1}, {"testo": "🟢 VA AVANTI", "punti": 0}], "lezione": "Se l'azienda sei tu, hai un lavoro a vita da cui non puoi dimetterti."},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "Manuali operativi su come si fanno le cose.", "opzioni": [{"testo": "🔴 NO, È NELLA TESTA", "punti": 1}, {"testo": "🟢 SÌ, ABBIAMO I MANUALI", "punti": 0}], "lezione": "L'oralità è il medioevo. Se spieghi una cosa due volte, hai fallito. Scrivila."},
    {"area": "SQUADRA", "testo": "TI SENTI DIRE 'FACCIO PRIMA A FARLO IO'?", "sotto": "E alla fine il lavoro operativo lo fai tu.", "opzioni": [{"testo": "🔴 QUASI OGNI GIORNO", "punti": 1}, {"testo": "🟢 RARAMENTE", "punti": 0}], "lezione": "Questa frase è la lapide della tua crescita aziendale."},
    {"area": "SQUADRA", "testo": "I DIPENDENTI SANNO L'OBIETTIVO DEL MESE?", "sotto": "O vengono solo a timbrare il cartellino?", "opzioni": [{"testo": "🔴 NON CREDO", "punti": 1}, {"testo": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "punti": 0}], "lezione": "Non puoi vincere se la squadra non sa il punteggio."},
    {"area": "SQUADRA", "testo": "ERRORE: CERCHI IL COLPEVOLE O LA CAUSA?", "sotto": "Chi ha sbagliato o dove è fallito il processo?", "opzioni": [{"testo": "🔴 CHI HA SBAGLIATO?", "punti": 1}, {"testo": "🟢 DOVE È FALLITO IL PROCESSO?", "punti": 0}], "lezione": "Aggiustare la procedura è l'unico modo per non far ripetere l'errore."},
    {"area": "STRATEGIA", "testo": "DECISIONI SUI DATI O SULL'INTUITO?", "sotto": "Report freddi o sensazioni della pancia?", "opzioni": [{"testo": "🔴 INTUITO / PANCIA", "punti": 1}, {"testo": "🟢 DATI / REPORT", "punti": 0}], "lezione": "L'intuito è spesso un pregiudizio mascherato. Fidati di Excel."},
    {"area": "STRATEGIA", "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE?", "sotto": "Se è tossico o fuori target, lo licenzi?", "opzioni": [{"testo": "🔴 NO, FATTURATO È TUTTO", "punti": 1}, {"testo": "🟢 SÌ, HO LICENZIATO CLIENTI", "punti": 0}], "lezione": "I soldi di un cliente tossico costano il triplo in stress."},
    {"area": "STRATEGIA", "testo": "CONOSCI IL TUO BEST SELLER PER MARGINE?", "sotto": "Cosa ti arricchisce davvero?", "opzioni": [{"testo": "🔴 NON SONO SICURO", "punti": 1}, {"testo": "🟢 SÌ, LO CONOSCO", "punti": 0}], "lezione": "Spesso vendiamo tanto ciò che ci lascia briciole."},
    {"area": "STRATEGIA", "testo": "SAI QUANTO COSTA ACQUISIRE UN CLIENTE?", "sotto": "Marketing, tempo commerciale, adv...", "opzioni": [{"testo": "🔴 IMPOSSIBILE SAPERLO", "punti": 1}, {"testo": "🟢 SÌ, IL CAC È CHIARO", "punti": 0}], "lezione": "Se spendi 100 per incassare 50 di margine, stai pagando per lavorare."},
    {"area": "STRATEGIA", "testo": "HAI UN PIANO SCRITTO PER I 12 MESI?", "sotto": "Non un sogno, un piano concreto.", "opzioni": [{"testo": "🔴 È NELLA MIA TESTA", "punti": 1}, {"testo": "🟢 SÌ, SCRITTO E CONDIVISO", "punti": 0}], "lezione": "Se è nella testa, è un'allucinazione. Se è scritto, è un progetto."}
]

# =================================================================
# 3. STATO E LOGICA
# =================================================================
if 'step' not in st.session_state: st.session_state.step = 0
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'area_scores' not in st.session_state: st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
if 'show_feedback' not in st.session_state: st.session_state.show_feedback = False

st.markdown(f'<div class="brand-logo">comunicAttivamente</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">Esorcismo del Caos Aziendale</div>', unsafe_allow_html=True)

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    st.markdown(f"<div class='area-header'>AREA: {item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(f"*{item.get('sotto', '')}*")
    st.divider()

    if not st.session_state.show_feedback:
        c1, c2 = st.columns(2)
        if c1.button(item['opzioni'][0]['testo'], key=f"btn0_{st.session_state.step}"):
            st.session_state.total_score += item['opzioni'][0]['punti']
            st.session_state.area_scores[item['area']] += item['opzioni'][0]['punti']
            st.session_state.show_feedback = True
            st.rerun()
        if c2.button(item['opzioni'][1]['testo'], key=f"btn1_{st.session_state.step}"):
            st.session_state.show_feedback = True
            st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        btn_txt = "VEDI DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        if st.button(btn_txt, type="primary"):
            st.session_state.step += 1
            st.session_state.show_feedback = False
            st.rerun()

else:
    score = st.session_state.total_score
    st.header("📊 RISULTATO DIAGNOSI")
    if score <= 4:
        st.markdown(f"<div class='profile-box' style='background-color:#d4edda'><h3>PROFILO A: L'OROLOGIO SVIZZERO</h3><p>Sei nell'1% degli imprenditori. Prognosi: Ottima.</p></div>", unsafe_allow_html=True)
    elif score <= 12:
        st.markdown(f"<div class='profile-box' style='background-color:#fff3cd'><h3>PROFILO B: IL CRICETO STANCO</h3><p>Sei nella media. L'azienda regge ma tu sei esausto.</p></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='profile-box' style='background-color:#f8d7da'><h3>PROFILO C: L'AZIENDA POSSEDUTA</h3><p>Allarme Rosso. Sei passeggero di un treno in fiamme.</p></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 🚑 KIT DI SOPRAVVIVENZA")
    aree = sorted(st.session_state.area_scores.items(), key=lambda x: x[1], reverse=True)
    for area, p in aree[:3]:
        if p > 0:
            if area == "SOLDI": st.info("💰 **SOLDI:** Domani mattina chiedi il tuo MARGINE reale.")
            if area == "TEMPO": st.info("⏰ **TEMPO:** Disattiva le notifiche e usa blocchi orari.")
            if area == "SQUADRA": st.info("👥 **SQUADRA:** Registra un video-manuale di un compito.")

    st.divider()
    col_a, col_b = st.columns(2)
    col_a.link_button("📘 SCARICA EBOOK", "https://www.comunicattivamente.it/ebook-ansia-spa", type="primary")
    col_b.link_button("📅 PRENOTA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    st.markdown(f"""
        <div style='text-align: center; padding: 20px; background-color: #f1f1f1; border-radius: 10px; margin-top:20px;'>
            <b>Daniele Salvatori | <a href="https://www.comunicattivamente.it" target="_blank" style="color:{ROSSO_BRAND}">comunicAttivamente</a></b><br>
            Partner <a href="https://www.superstart.it" target="_blank" style="color:#888;">SuPeR</a><br>
            📞 <a href='tel:+393929334563' class='phone-link'>+39 392 933 4563</a><br>
            <a href='https://wa.me/393929334563' style='background-color:#25D366; color:white; padding:8px 15px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px;'>💬 WHATSAPP</a>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.link_button("🌐 VEDI TUTTE LE NOSTRE WEB APP", "https://hub-comunicattivamente.streamlit.app")
    if st.button("🔄 RICOMINCIA"):
        st.session_state.step = 0; st.session_state.total_score = 0; st.rerun()
