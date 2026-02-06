import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🎯", layout="centered")

# --- STILE CSS (HARDCODED - ROSSO #dc061e) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {
        color: #1a1a1a !important;
    }
    
    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #f1f3f6 !important;
        border-right: 2px solid #dc061e !important;
    }

    /* BOTTONI ROSSI */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #dc061e !important; color: #ffffff !important; border: none !important;
        width: 100%; height: 3.5em; font-weight: bold; text-transform: uppercase;
    }
    
    /* BOX INFO */
    .info-box {
        background-color: #f8f9fa !important; border-left: 8px solid #dc061e !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px;
    }

    /* TITOLI */
    h1, h2 { color: #dc061e !important; }
    
    header {visibility: hidden !important;} footer {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGAZIONE SIDEBAR ---
with st.sidebar:
    st.title("🛡️ HUB ESORCISMO")
    st.write("Seleziona lo strumento:")
    menu = st.radio("", ["🏠 Home", "📊 Diagnosi (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Bignami Interattivo"])
    st.divider()
    st.write("Daniele Salvatori")
    st.write("daniele@comunicattivamente.it")

# --- HOME PAGE ---
if menu == "🏠 Home":
    st.title("BENVENUTO NELL'HUB DELL'EFFICIENZA")
    st.markdown("""
    <div class='info-box'>
    <b>Hai in mano gli strumenti per smettere di essere un criceto.</b><br><br>
    Qui non si chiacchiera, si agisce. Seleziona uno strumento dal menu a sinistra per iniziare il tuo percorso di liberazione dal caos.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("L'Esorcismo Strategico")
        st.write("Analizza i 7 Peccati Capitali della tua azienda con il test completo di **Ansia SPA**.")
    with col2:
        st.subheader("L'Esorcismo Operativo")
        st.write("Smetti di sprecare tempo ora. Usa il calcolatore di costi e i protocolli di **La riunione poteva essere una mail**.")

# --- DIAGNOSI (ANSIA SPA) ---
elif menu == "📊 Diagnosi (Ansia SPA)":
    st.title("📊 DIAGNOSI ANSIA SPA")
    st.write("Questa è l'area dedicata all'analisi profonda della tua azienda (Libro 1).")
    st.info("Qui caricheremo le tue 20 domande originali di Ansia SPA.")
    if st.button("INIZIA TEST STRATEGICO", type="primary"):
        st.write("Sviluppo in corso... (Qui inseriremo la logica del tuo test precedente)")

# --- PRONTO INTERVENTO ---
elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.title("🛠️ PRONTO INTERVENTO")
    st.write("Strumenti rapidi per smettere di farsi del male (Libro 2).")
    
    tab1, tab2 = st.tabs(["💸 Calcola Spreco", "📧 Generatore 'No'"])
    
    with tab1:
        st.subheader("Quanto ti costa questa riunione?")
        num = st.number_input("Partecipanti", min_value=1, value=3)
        costo = st.number_input("Costo orario medio (€)", min_value=1, value=40)
        ore = st.slider("Durata (ore)", 0.5, 4.0, 1.0, 0.5)
        
        totale = num * costo * ore
        st.error(f"VALORE BRUCIATO: {totale} €")
        st.write("Potevi scrivere una mail e salvare questo margine.")

    with tab2:
        st.subheader("Generatore di Risposte 'Efficaci'")
        motivo = st.selectbox("Perché non vuoi partecipare?", ["Manca l'agenda", "Siamo in troppi", "Posso risolvere via mail", "Ho un focus importante"])
        if st.button("GENERA MAIL DI RISPOSTA", type="primary"):
            st.code(f"Gentile [Nome],\nIn merito alla riunione proposta, credo che {motivo.lower()}.\nPropongo di procedere via mail o aggiornarci appena ci saranno dati certi.\nBuon lavoro.")

# --- BIGNAMI ---
elif menu == "📖 Bignami Interattivo":
    st.title("📖 PILLOLE DI ESORCISMO")
    st.write("I concetti chiave dei due libri, senza giri di parole.")
    with st.expander("ANSIA SPA: I 3 pilastri del Margine"):
        st.write("1. Il fatturato è vanità.\n2. Il margine è sanità.\n3. La cassa è realtà.")
    with st.expander("LA RIUNIONE...: I 3 pilastri del Tempo"):
        st.write("1. Se non è scritto, non esiste.\n2. Gli allegati sono il demonio.\n3. L'agenda di Schrödinger uccide l'azienda.")
