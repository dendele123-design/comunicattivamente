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

# --- STATO SESSIONE ---
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False

# --- DATABASE DOMANDE ANSIA SPA (Strategia) ---
domande_ansia = [
    {"testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Margine pulito, non incasso.", "feedback": "Voli alla cieca senza margine."},
    {"testo": "PREZZI A 'SENTIMENTO'?", "sotto": "O con calcolo matematico dei costi?", "feedback": "La matematica non ha sentimenti."},
    {"testo": "RIUNIONI SENZA AGENDA?", "sotto": "Tutti sanno cosa si decide?", "feedback": "Furto di tempo autorizzato."},
    {"testo": "SE SPARISCI 30 GG, L'AZIENDA VA?", "sotto": "Produce utile senza di te?", "feedback": "Sei uno schiavo, non un boss."},
    {"testo": "DATI O INTUITO?", "sotto": "Report o sensazioni?", "feedback": "I dati sono sanità mentale."},
    {"testo": "LICENZI I CLIENTI VAMPIRI?", "sotto": "O accetti chiunque?", "feedback": "I vampiri rubano la vita."},
    {"testo": "MAIL PER LA DISPONIBILITÀ?", "sotto": "O calendario condiviso?", "feedback": "Spreco di vita in mail."},
    {"testo": "VIDEO-PROCEDURE?", "sotto": "O spieghi tutto a voce?", "feedback": "Se non è registrato, non esiste."},
    {"testo": "PUNTO DI PAREGGIO?", "sotto": "Sai quando inizi a guadagnare?", "feedback": "Essenziale per la calma."},
    {"testo": "COSTO ACQUISIZIONE CLIENTE?", "sotto": "Quanto spendi per vendere?", "feedback": "Evita di pagare per lavorare."}
]

# --- UI APPLICAZIONE ---
st.write("# 🛡️")
st.title("HUB DELL'EFFICIENZA")
menu = st.selectbox("COSA VUOI FARE OGGI?", ["🏠 Home Page", "📊 Diagnosi Strategica (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Pillole di Efficienza (Bignami)"])
st.divider()

if menu == "🏠 Home Page":
    st.subheader("A rapporto, Ammiraglio.")
    st.markdown("<div class='info-box'>Questa è la tua centrale di comando. Smetti di spalare letame nella stalla e sali sul ponte.</div>", unsafe_allow_html=True)
    st.write("📈 **Strategia:** Ansia SPA.")
    st.write("⚙️ **Operatività:** La Riunione poteva essere una Mail.")

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
            if c1.button("🔴 NO", key=f"no_{step}"):
                st.session_state.score_ansia += 1
                st.session_state.step_ansia += 1
                st.rerun()
            if c2.button("🟢 SÌ", key=f"si_{step}"):
                st.session_state.step_ansia += 1
                st.rerun()
        else:
            st.session_state.ansia_complete = True
            st.rerun()
    else:
        st.subheader("DIAGNOSI")
        score = st.session_state.score_ansia
        if score <= 2: st.success("GAZZELLE: Strategia solida.")
        elif score <= 6: st.warning("CRICETO: La ruota cigola.")
        else: st.error("POSSEDUTO: Esorcismo urgente.")
        if st.button("REIMPOSTA TEST", type="primary"):
            st.session_state.step_ansia = 0
            st.session_state.score_ansia = 0
            st.session_state.ansia_complete = False
            st.rerun()

elif menu == "🛠️ Pronto Intervento (Toolkit)":
    tool = st.radio("Seleziona strumento:", ["💸 Calcola Spreco", "📅 Invito Intelligente", "📡 Filtro Urgenza", "📑 Generatore SOP", "🧭 Cruscotto Ammiraglio"])
    st.divider()

    if tool == "💸 Calcola Spreco":
        n = st.number_input("Partecipanti", 1, 20, 4)
        h = st.slider("Durata", 0.5, 4.0, 1.0)
        c = st.number_input("Costo orario medio", 1, 200, 45)
        st.error(f"VALORE BRUCIATO: {n * c * h} €")

    elif tool == "📅 Invito Intelligente":
        link = st.text_input("Link Agenda:", "https://calendly.com/tuonome")
        if st.button("GENERA INVITO", type="primary"):
            st.code(f"Scegli qui lo slot per il nostro incontro: {link}", language="text")

    elif tool == "🧭 Cruscotto Ammiraglio":
        st.write("Proiezione a 30 giorni:")
        saldo = st.number_input("Saldo attuale banca (€)", value=10000)
        incassi = st.number_input("Incassi certi entro 30gg (€)", value=5000)
        spese = st.number_input("Spese/F24/Stipendi entro 30gg (€)", value=7000)
        proiezione = saldo + incassi - spese
        if proiezione > 0: st.success(f"PROIEZIONE: {proiezione} € (Rotta sicura)")
        else: st.error(f"PROIEZIONE: {proiezione} € (Rischio secca!)")

elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("Protocolli Finali")
    with st.expander("🧭 PROTOCOLLO 5: IL CRUSCOTTO"):
        st.write("Guarda i flussi di cassa, non le tasse. Il saldo proiettato a 30 giorni è la tua bussola.")
    with st.expander("📑 PROTOCOLLO 4: CLONAZIONE"):
        st.write("Registra video mentre lavori. Crea procedure per renderti inutile operativamente.")

st.markdown("---")
st.write("Daniele Salvatori | daniele@comunicattivamente.it")
