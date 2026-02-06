import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li { color: #1a1a1a !important; }
    h1, h2, h3 { color: #dc061e !important; }
    div[data-baseweb="select"] > div { background-color: #f1f3f6 !important; border: 2px solid #dc061e !important; border-radius: 10px !important; }
    div.stButton > button:first-child[kind="primary"] { background-color: #dc061e !important; color: #ffffff !important; border: none !important; width: 100%; height: 3.5em; font-weight: bold; }
    .info-box { background-color: #f8f9fa !important; border-left: 8px solid #dc061e !important; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    header {visibility: hidden !important;} footer {visibility: hidden !important;} #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DOMANDE ANSIA SPA ---
domande_ansia = [
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Non quanto hai incassato. Quanto ti è rimasto pulito.", "lezione": "Il fatturato è vanità. Guidare senza conoscere il margine è come volare alla cieca."},
    {"area": "SOLDI", "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?", "sotto": "O ti basi su un calcolo matematico dei tuoi costi reali?", "lezione": "Il prezzo di mercato è una bugia. Se il tuo concorrente fallisce e tu lo copi, fallirai con lui."},
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "Tutti sanno di cosa si parla o lo scoprite al tavolo?", "lezione": "Una riunione senza agenda è una chiacchierata al bar molto costosa."},
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE...", "sotto": "L'azienda continua a produrre o si ferma tutto?", "lezione": "Se l'azienda sei tu, non hai un business, hai un lavoro a vita senza ferie."},
    {"area": "STRATEGIA", "testo": "DECISIONI: DATI O INTUITO?", "sotto": "Ti fidi di Excel o della sensazione che hai al mattino?", "lezione": "L'intuito è un pregiudizio mascherato. I dati sono freddi, ma dicono la verità."}
    # Qui aggiungeremo le altre 15 man mano, per ora testiamo la logica con queste 5.
]

# --- STATO SESSIONE ---
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False

# --- UI APPLICAZIONE ---
st.write("# 🛡️")
st.title("HUB DELL'EFFICIENZA")
menu = st.selectbox("MENU PRINCIPALE", ["🏠 Home Page", "📊 Diagnosi Strategica (Ansia SPA)", "🛠️ Pronto Intervento (Toolkit)", "📖 Pillole di Efficienza (Bignami)"])
st.divider()

if menu == "🏠 Home Page":
    st.subheader("Smetti di essere un criceto.")
    st.markdown("<div class='info-box'>Benvenuto nel tuo centro di comando. Seleziona uno strumento qui sopra.</div>", unsafe_allow_html=True)

elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    if not st.session_state.ansia_complete:
        step = st.session_state.step_ansia
        if step < len(domande_ansia):
            item = domande_ansia[step]
            st.write(f"**DOMANDA {step + 1} di {len(domande_ansia)}**")
            st.header(item['testo'])
            st.write(f"*{item['sotto']}*")
            
            c1, c2 = st.columns(2)
            if c1.button("🔴 NO / NON SEMPRE", key=f"ans_no_{step}"):
                st.session_state.score_ansia += 1
                st.session_state.step_ansia += 1
                st.rerun()
            if c2.button("🟢 SÌ, ASSOLUTAMENTE", key=f"ans_si_{step}"):
                st.session_state.step_ansia += 1
                st.rerun()
        else:
            st.session_state.ansia_complete = True
            st.rerun()
    else:
        st.subheader("RISULTATO DIAGNOSI")
        score = st.session_state.score_ansia
        if score <= 1: st.success("PROFILO: LA GAZZELLA. La tua strategia è solida.")
        else: st.error(f"PROFILO: IL CRICETO. Hai {score} punti di inefficienza strategica.")
        
        if st.button("RICOMINCIA TEST", type="primary"):
            st.session_state.step_ansia = 0
            st.session_state.score_ansia = 0
            st.session_state.ansia_complete = False
            st.rerun()

elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.subheader("Strumenti Operativi")
    # Qui manteniamo il calcolatore e il generatore di mail che abbiamo fatto prima
    st.write("Seleziona uno strumento dal sottomenu:")
    tool = st.radio("", ["Calcolatore Spreco", "Script Risposte"])
    if tool == "Calcolatore Spreco":
        st.info("Tool per il calcolo dei costi riunione...")

elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("Bignami Interattivo")
    with st.expander("Il paradosso del 'Faccio prima io'"):
        st.write("Spiegazione rapida del concetto...")

st.divider()
st.write("📧 daniele@comunicattivamente.it | 📞 +39 392 933 4563")
