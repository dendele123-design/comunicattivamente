import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS (Blindato, Anti-Dark Mode, Rosso #dc061e) ---
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
    st.subheader("Basta correre sulla ruota.")
    st.markdown("<div class='info-box'>Benvenuto, Ammiraglio. Questa app è il tuo centro di comando digitale. Scegli uno strumento per iniziare l'esorcismo.</div>", unsafe_allow_html=True)
    st.write("📖 **Ansia SPA:** Per la strategia e i numeri.")
    st.write("📧 **La Riunione...:** Per i protocolli operativi quotidiani.")

elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.write(f"**DOMANDA {step + 1} di {len(domande_ansia)}**")
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
        st.subheader("RISULTATO DIAGNOSI")
        score = st.session_state.score_ansia
        if score <= 2: st.success("PROFILO: GAZZELLA. Ottimo lavoro.")
        elif score <= 6: st.warning("PROFILO: CRICETO. La ruota sta cigolando.")
        else: st.error("PROFILO: POSSEDUTO. Serve un esorcismo immediato.")
        if st.button("RICOMINCIA TEST", type="primary"):
            st.session_state.step_ansia = 0
            st.session_state.score_ansia = 0
            st.session_state.ansia_complete = False
            st.rerun()

elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.subheader("Protocolli Operativi")
    tool = st.radio("Scegli lo strumento:", ["💸 Calcola lo Spreco", "📅 Invito Intelligente", "📡 Filtro dell'Urgenza"])
    st.divider()

    if tool == "💸 Calcola lo Spreco":
        n = st.number_input("Partecipanti", min_value=1, value=4)
        h = st.slider("Durata (ore)", 0.5, 4.0, 1.0, 0.5)
        c = st.number_input("Costo orario medio (€)", min_value=1, value=45)
        st.error(f"VALORE BRUCIATO: {n * c * h} €")

    elif tool == "📅 Invito Intelligente":
        tipo = st.selectbox("Tipo di incontro:", ["Chiamata (15 min)", "Meeting (30 min)", "Strategia (1 ora)"])
        link = st.text_input("Il tuo link agenda:", "https://calendly.com/tuonome")
        if st.button("GENERA INVITO", type="primary"):
            st.code(f"Ciao, per fissare la nostra {tipo.lower()} ti lascio il link alla mia agenda: {link}. Scegli lo slot più comodo!", language="text")

    elif tool == "📡 Filtro dell'Urgenza":
        st.write("Cosa devi comunicare?")
        msg_type = st.selectbox("Seleziona:", ["Devo mandare un report/documento", "Ho una domanda da sì/no", "C'è un problema urgente (scade ora)", "Devo pianificare una attività futura"])
        if st.button("QUALE STRUMENTO USO?", type="primary"):
            if "report" in msg_type or "futura" in msg_type:
                st.success("USA LA MAIL. Non interrompere il flusso degli altri per qualcosa che può aspettare.")
            elif "sì/no" in msg_type:
                st.warning("USA LA CHAT. Sii breve e diretto. Non aspettare il 'Ciao come va'.")
            else:
                st.error("ALZA IL TELEFONO. Le urgenze vere si risolvono a voce in 2 minuti.")

elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("Bignami dell'Esorcista")
    with st.expander("📖 PROTOCOLLO 1: LA FONTE DELLA VERITÀ"):
        st.write("Mai più allegati. Solo link al Cloud. Una sola cartella AZIENDA.")
    with st.expander("📅 PROTOCOLLO 2: AGENDA DI SCHRÖDINGER"):
        st.write("Se non è sul calendario, non esiste. Usa link di prenotazione automatica.")
    with st.expander("📡 PROTOCOLLO 3: MAIL VS CHAT"):
        st.write("La mail è asincrona (4-8h). La chat è estintore (30 sec). Spegni le notifiche.")

st.markdown("---")
st.write("Daniele Salvatori | daniele@comunicattivamente.it")
