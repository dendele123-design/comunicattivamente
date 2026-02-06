import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS (Blindato, Rosso #dc061e, Anti-Dark Mode) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li { color: #1a1a1a !important; }
    h1, h2, h3 { color: #dc061e !important; }
    div[data-baseweb="select"] > div { background-color: #f1f3f6 !important; border: 2px solid #dc061e !important; border-radius: 10px !important; }
    div.stButton > button:first-child[kind="primary"] { background-color: #dc061e !important; color: #ffffff !important; border: none !important; width: 100%; height: 3.5em; font-weight: bold; text-transform: uppercase; }
    .stButton>button { width: 100%; border-radius: 8px !important; background-color: #f1f3f6 !important; color: #1a1a1a !important; border: 1px solid #d1d5db !important; }
    .info-box { background-color: #f8f9fa !important; border-left: 8px solid #dc061e !important; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    header {visibility: hidden !important;} footer {visibility: hidden !important;} #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DOMANDE ANSIA SPA (Prime 10) ---
domande_ansia = [
    {"testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Non l'incasso. Il margine pulito.", "feedback": "Il fatturato è vanità. Se non conosci il margine, voli alla cieca."},
    {"testo": "VAI A 'SENTIMENTO' QUANDO FAI UN PREZZO?", "sotto": "O hai un calcolo matematico basato sui costi?", "feedback": "Il prezzo di mercato è un'illusione. La matematica non ha sentimenti."},
    {"testo": "LE TUE RIUNIONI HANNO SEMPRE UN ORDINE SCRITTO?", "sotto": "Tutti sanno cosa si decide o lo scoprite lì?", "feedback": "Senza agenda, la riunione è un furto di tempo autorizzato."},
    {"testo": "SE SPARISCI PER 30 GIORNI, L'AZIENDA CONTINUA?", "sotto": "L'azienda produce utile o si ferma tutto?", "feedback": "Se dipendono da te, hai un lavoro, non un business."},
    {"testo": "TI FIDI PIÙ DEI DATI O DEL TUO INTUITO?", "sotto": "Guardi i report o segui la sensazione?", "feedback": "L'intuito è un pregiudizio. I dati sono la sanità mentale."},
    {"testo": "LICENZI MAI I CLIENTI TOSSICI?", "sotto": "O accetti chiunque pur di fatturare?", "feedback": "I vampiri rubano anima e tempo. Toglierli è igiene."},
    {"testo": "USI LE MAIL PER CHIEDERE DISPONIBILITÀ?", "sotto": "O hai un calendario condiviso?", "feedback": "Il ping-pong di mail è uno spreco di vita."},
    {"testo": "OGNI PROCESSO È REGISTRATO IN VIDEO?", "sotto": "O spieghi le cose a voce ogni volta?", "feedback": "Se non è scritto, non esiste. La procedura è libertà."},
    {"testo": "CONOSCI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "La cifra esatta per coprire ogni costo?", "feedback": "Sapere quando inizi a guadagnare dà calma."},
    {"testo": "SAI QUANTO TI COSTA ACQUISIRE UN CLIENTE?", "sotto": "Marketing, tempo, chiamate... sai la cifra?", "feedback": "Se non sai quanto costa vendere, paghi per lavorare."}
]

# --- STATO SESSIONE ---
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False

# --- UI APPLICAZIONE ---
st.write("# 🛡️")
st.title("HUB DELL'EFFICIENZA")
menu = st.selectbox("COSA VUOI FARE OGGI?", ["🏠 Home Page", "📊 Diagnosi Strategica (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Pillole di Efficienza (Bignami)"])
st.divider()

if menu == "🏠 Home Page":
    st.subheader("Benvenuto a bordo, Ammiraglio.")
    st.markdown("<div class='info-box'>Hai in mano il timone della tua azienda. Usa gli strumenti per eliminare il rumore e iniziare a navigare verso il margine.</div>", unsafe_allow_html=True)
    st.write("📈 **Strategia:** Ansia SPA.")
    st.write("⚙️ **Operatività:** La Riunione poteva essere una Mail.")

elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.markdown(f"<div class='area-header'>QUESITO {step + 1} di {len(domande_ansia)}</div>", unsafe_allow_html=True)
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
        else:
            st.session_state.ansia_complete = True
            st.rerun()
    else:
        st.subheader("LA TUA DIAGNOSI")
        score = st.session_state.score_ansia
        if score <= 2: st.success("PROFILO: GAZZELLA. Ottimo!")
        elif score <= 6: st.warning("PROFILO: CRICETO. Attenzione.")
        else: st.error("PROFILO: POSSEDUTO. Esorcismo urgente.")
        if st.button("REIMPOSTA TEST", type="primary"):
            st.session_state.step_ansia = 0
            st.session_state.score_ansia = 0
            st.session_state.ansia_complete = False
            st.rerun()

elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.subheader("Kit di Sopravvivenza Digitale")
    tool = st.radio("Seleziona:", ["💸 Calcola lo Spreco", "📅 Invito Intelligente", "📡 Filtro Urgenza", "📑 Generatore di Procedure (SOP)"])
    st.divider()

    if tool == "💸 Calcola lo Spreco":
        n = st.number_input("Partecipanti", min_value=1, value=4)
        h = st.slider("Durata (ore)", 0.5, 4.0, 1.0, 0.5)
        c = st.number_input("Costo orario medio (€)", min_value=1, value=45)
        st.error(f"VALORE BRUCIATO: {n * c * h} €")

    elif tool == "📅 Invito Intelligente":
        tipo = st.selectbox("Tipo:", ["Chiamata", "Meeting", "Strategia"])
        link = st.text_input("Link Agenda:", "https://calendly.com/tuonome")
        if st.button("GENERA INVITO", type="primary"):
            st.code(f"Ciao, per fissare la nostra {tipo.lower()} ti lascio il link alla mia agenda: {link}. Scegli lo slot!", language="text")

    elif tool == "📡 Filtro Urgenza":
        msg = st.selectbox("Situazione:", ["Report/Doc", "Domanda Sì/No", "Urgenza reale", "Pianificazione"])
        if st.button("STRUMENTO DA USARE", type="primary"):
            if "Report" in msg or "Pianificazione" in msg: st.success("MAIL (Asincrona)")
            elif "Sì/No" in msg: st.warning("CHAT (Sincrona rapida)")
            else: st.error("VOCE (Risoluzione immediata)")

    elif tool == "📑 Generatore di Procedure (SOP)":
        st.write("Crea la struttura per la tua prossima procedura:")
        titolo = st.text_input("Cosa stiamo clonando?", "Esempio: Inserimento Fattura")
        ingr = st.text_area("Ingredienti (Cosa serve?)", "Password gestionale, PDF fattura...")
        passaggi = st.text_area("Preparazione (Passaggi numerati)", "1. Apri sito...\n2. Inserisci...")
        if st.button("GENERA SCHEMA PROCEDURA", type="primary"):
            sop = f"--- PROCEDURA: {titolo.upper()} ---\n\nINGREDIENTI:\n{ingr}\n\nPASSAGGI:\n{passaggi}\n\n[Nota: Se puoi, registra un video di 2 min mentre lo fai!]"
            st.code(sop, language="text")

elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("I Comandamenti dell'Efficienza")
    with st.expander("🛡️ PROTOCOLLO 4: CLONAZIONE UMANA"):
        st.write("Smetti di spiegare a voce. Registra un video mentre lavori (Loom) e salvalo nella cartella PROCEDURE. Se non è registrato, non esiste.")
    with st.expander("📡 PROTOCOLLO 3: RUMORE VS SEGNALE"):
        st.write("La mail è la tua fortezza. La chat è l'estintore. Spegni le notifiche o sarai schiavo del Ding.")

st.markdown("---")
st.write("Daniele Salvatori | daniele@comunicattivamente.it")
