import streamlit as st
import time
from datetime import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS (Refined Design, Rosso #DC0612, Mobile Friendly) ---
st.markdown("""
    <style>
    /* FORZA SFONDO BIANCO */
    .stApp { background-color: #ffffff !important; }
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li {
        color: #1a1a1a !important;
    }

    /* NUOVO HEADER RAFFINATO (BORDO INVECE DI SFONDO) */
    .main-header {
        border: 2px solid #DC0612;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        background-color: #fdfdfd;
    }
    .main-header h1 { 
        color: #DC0612 !important; 
        margin: 0; 
        font-size: 1.6em !important; /* Rimpicciolito per mobile */
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* TITOLI INTERNI */
    h2, h3 { color: #DC0612 !important; }

    /* MENU SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #f1f3f6 !important;
        border: 2px solid #DC0612 !important;
        border-radius: 10px !important;
    }

    /* BOTTONI ROSSI */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #DC0612 !important; color: #ffffff !important; 
        border: none !important; width: 100%; height: 3.5em; font-weight: bold;
    }
    
    /* BOX NOTA ARCHITETTO */
    .info-box {
        background-color: #f8f9fa !important; border-left: 8px solid #DC0612 !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* TIMER SPRECO */
    .timer-box {
        font-size: 2.2em; font-weight: bold; color: #DC0612; text-align: center;
        padding: 15px; border: 3px dashed #DC0612; border-radius: 15px; margin: 10px 0;
    }

    /* FOOTER */
    .footer {
        text-align: center; padding: 25px; background-color: #f1f1f1;
        border-radius: 15px; margin-top: 50px; border-top: 5px solid #DC0612;
    }
    .footer a { color: #DC0612 !important; text-decoration: none; font-weight: bold; }

    header {visibility: hidden !important;} footer {visibility: hidden !important;} #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- STATO SESSIONE ---
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False
if 'timer_running' not in st.session_state: st.session_state.timer_running = False
if 'start_time' not in st.session_state: st.session_state.start_time = None

# --- DATABASE ANSIA SPA ---
domande_ansia = [
    {"testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Margine pulito, non incasso.", "feedback": "Il fatturato è vanità."},
    {"testo": "VAI A 'SENTIMENTO' CON I PREZZI?", "sotto": "O hai un calcolo matematico dei costi?", "feedback": "La matematica non ha sentimenti."},
    {"testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "Tutti sanno cosa si decide o lo scoprite lì?", "feedback": "Furto di tempo autorizzato."},
    {"testo": "SE SPARISCI 30 GG, L'AZIENDA VA?", "sotto": "Produce utile senza di te?", "feedback": "Sei uno schiavo, non un boss."},
    {"testo": "TI FIDI PIÙ DEI DATI O DELL'INTUITO?", "sotto": "Report o sensazioni del mattino?", "feedback": "I dati sono sanità mentale."},
    {"testo": "LICENZI I CLIENTI VAMPIRI?", "sotto": "O accetti chiunque pur di fatturare?", "feedback": "I vampiri rubano la vita."},
    {"testo": "USI MAIL PER LA DISPONIBILITÀ?", "sotto": "O hai un calendario condiviso?", "feedback": "Spreco di vita in mail."},
    {"testo": "OGNI PROCESSO È IN VIDEO?", "sotto": "O spieghi tutto a voce ogni volta?", "feedback": "Se non è registrato, non esiste."},
    {"testo": "SAI IL TUO PUNTO DI PAREGGIO?", "sotto": "La cifra esatta per coprire ogni costo?", "feedback": "Essenziale per la calma."},
    {"testo": "SAI QUANTO COSTA ACQUISIRE UN CLIENTE?", "sotto": "Marketing, tempo, chiamate...", "feedback": "Evita di pagare per lavorare."}
]

# --- UI ---
st.markdown("<div class='main-header'><h1>🛡️ HUB DELL'EFFICIENZA</h1></div>", unsafe_allow_html=True)
menu = st.selectbox("COSA VUOI FARE OGGI?", ["🏠 Home Page", "📊 Diagnosi Strategica (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Pillole di Efficienza (Bignami)"])

# --- 🏠 HOME PAGE ---
if menu == "🏠 Home Page":
    st.subheader("Basta correre sulla ruota.")
    st.markdown("<div class='info-box'>Benvenuto, Ammiraglio. Questa è la tua centrale di comando digitale. Usa gli strumenti per eliminare il rumore e navigare verso il margine.</div>", unsafe_allow_html=True)
    st.write("📈 **Strategia:** Test Ansia SPA.")
    st.write("⚙️ **Operatività:** Toolkit La Riunione poteva essere una Mail.")

# --- 📊 DIAGNOSI (ANSIA SPA) ---
elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.write(f"**QUESITO {step + 1} di {len(domande_ansia)}**")
            st.header(item['testo'])
            st.write(f"*{item['sotto']}*")
            st.divider()
            c1, c2 = st.columns(2)
            if c1.button("🔴 NO / NON SEMPRE", key=f"no_{step}"):
                st.session_state.score_ansia += 1
                st.session_state.step_ansia += 1
                st.rerun()
            if c2.button("🟢 SÌ, ASSOLUTAMENTE", key=f"si_{step}"):
                st.session_state.step_ansia += 1
                st.rerun()
        else: st.session_state.ansia_complete = True; st.rerun()
    else:
        st.subheader("DIAGNOSI")
        score = st.session_state.score_ansia
        if score <= 2: st.success("PROFILO: GAZZELLA. Strategia solida.")
        elif score <= 6: st.warning("PROFILO: CRICETO. La ruota cigola.")
        else: st.error("PROFILO: POSSEDUTO. Esorcismo urgente.")
        if st.button("REIMPOSTA TEST", type="primary"):
            st.session_state.step_ansia = 0; st.session_state.score_ansia = 0; st.session_state.ansia_complete = False; st.rerun()

# --- 🛠️ PRONTO INTERVENTO (TOOLKIT) ---
elif menu == "🛠️ Pronto Intervento (Toolkit)":
    tool = st.radio("Seleziona strumento:", ["💸 Timer dello Spreco", "📅 Invito Intelligente", "📡 Filtro Urgenza", "📑 Generatore SOP", "🧭 Cruscotto Ammiraglio"])
    st.divider()

    if tool == "💸 Timer dello Spreco":
        st.write("### Se non hai un obiettivo e un tempo limite, stai bruciando questi soldi:")
        c1, c2 = st.columns(2)
        n_p = c1.number_input("Partecipanti", 1, 50, 4)
        costo_h = c2.number_input("Costo orario medio (€)", 1, 500, 45)
        costo_al_secondo = (n_p * costo_h) / 3600

        if not st.session_state.timer_running:
            if st.button("▶️ AVVIA RIUNIONE", type="primary"):
                st.session_state.timer_running = True
                st.session_state.start_time = time.time()
                st.rerun()
        else:
            placeholder = st.empty()
            if st.button("🛑 FERMA RIUNIONE"):
                st.session_state.timer_running = False
                st.rerun()
            while st.session_state.timer_running:
                trascorso = time.time() - st.session_state.start_time
                bruciato = trascorso * costo_al_secondo
                placeholder.markdown(f"<div class='timer-box'>{bruciato:.2f} €</div>", unsafe_allow_html=True)
                time.sleep(1)

    elif tool == "📅 Invito Intelligente":
        st.markdown("<div class='info-box'>Dare accesso al tuo calendario è 'seguire', dare un link di prenotazione è 'dirigere'. Diventa l'autorità.</div>", unsafe_allow_html=True)
        link = st.text_input("Inserisci il tuo link Calendly/TidyCal:", "https://calendly.com/tuonome")
        if st.button("GENERA INVITO", type="primary"):
            st.code(f"Ciao, per fissare il nostro incontro ed evitare mille mail, ti lascio il link alla mia agenda: {link}. Scegli lo slot più comodo!", language="text")

    elif tool == "📡 Filtro Urgenza":
        st.markdown("<div class='info-box'>Smetti di essere schiavo del 'Ding'. Scegli il canale giusto per proteggere il tuo tempo.</div>", unsafe_allow_html=True)
        msg = st.selectbox("Cosa devi comunicare?", ["Report/Documento", "Domanda Sì/No", "Urgenza reale (Scade ora)", "Pianificazione futura"])
        if st.button("STRUMENTO DA USARE", type="primary"):
            if "Report" in msg or "Pianificazione" in msg: st.success("USA LA MAIL (4-8 ore di risposta)")
            elif "Sì/No" in msg: st.warning("USA LA CHAT (Sii breve e diretto)")
            else: st.error("ALZA IL TELEFONO (Risoluzione immediata)")

    elif tool == "📑 Generatore SOP":
        st.markdown("<div class='info-box'>Se non è scritto, non esiste. Crea qui la bozza della tua procedura digitale.</div>", unsafe_allow_html=True)
        titolo = st.text_input("Cosa stiamo clonando?", "Esempio: Inserimento Fattura")
        ingr = st.text_area("Cosa serve? (Accessi, PDF...)")
        passaggi = st.text_area("Passaggi (1, 2, 3...)")
        if st.button("GENERA SCHEMA", type="primary"):
            st.code(f"PROCEDURA: {titolo}\n\nREQUISITI:\n{ingr}\n\nSTEP:\n{passaggi}", language="text")

    elif tool == "🧭 Cruscotto Ammiraglio":
        st.markdown("<div class='info-box'>Guarda avanti. Se il saldo a 30 giorni è rosso, devi agire oggi, non tra un mese.</div>", unsafe_allow_html=True)
        s = st.number_input("Saldo attuale (€)", value=10000)
        i = st.number_input("Incassi certi (€)", value=5000)
        p = st.number_input("Spese/F24 (€)", value=7000)
        res = s + i - p
        if res > 0: st.success(f"PROIEZIONE: {res} € (Navigazione serena)")
        else: st.error(f"PROIEZIONE: {res} € (Rischio secca!)")

# --- 📖 BIGNAMI ---
elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("L'Esorcismo in sintesi")
    with st.expander("🛡️ PROTOCOLLO 1: LA FONTE DELLA VERITÀ"):
        st.write("Addio allegati. Una sola cartella Cloud AZIENDA. Se mandi un file via mail, crei un universo parallelo di caos.")
    with st.expander("📅 PROTOCOLLO 2: AGENDA DI SCHRÖDINGER"):
        st.write("Se non è sul calendario, non esiste. Usa link di prenotazione per blindare il tuo tempo.")
    with st.expander("📡 PROTOCOLLO 3: MAIL VS CHAT"):
        st.write("La mail è asincrona (riflessione). La chat è l'estintore (azione rapida). Spegni le notifiche.")
    with st.expander("📑 PROTOCOLLO 4: CLONAZIONE UMANA"):
        st.write("Registra video (Loom) mentre lavori. Non spiegare mai due volte la stessa cosa a voce.")
    with st.expander("🧭 PROTOCOLLO 5: IL CRUSCOTTO"):
        st.write("Controlla il saldo proiettato ogni lunedì. L'Ammiraglio guarda la rotta, non le viti della stiva.")

# --- FOOTER ---
st.markdown(f"""
    <div class="footer">
        <b>Daniele Salvatori</b><br>
        <i>Esorcista Aziendale | Partner SuPeR^</i><br><br>
        🌐 <a href="https://www.comunicattivamente.it">www.comunicattivamente.it</a><br><br>
        📧 <a href="mailto:daniele@comunicattivamente.it">daniele@comunicattivamente.it</a><br>
        📞 <a href="tel:+393929334563">+39 392 933 4563</a><br>
        💬 <a href="https://wa.me/393929334563">Chatta su WhatsApp</a>
    </div>
""", unsafe_allow_html=True)
