import streamlit as st

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🐹")

# --- STILE AZIENDALE ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; font-weight: bold; }
    .lesson-box { background-color: #000000; color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; }
    .area-header { background-color: #000000; color: white; padding: 10px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DOMANDE (Puoi aggiungerne quante ne vuoi) ---
domande = [
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "domanda": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?",
        "sotto_testo": "(O guardi cosa fanno i concorenti e ti metti un po' sotto?)",
        "lezione": "**LA LEZIONE DELL'ESORCISTA:** Il 'prezzo di mercato' è una bugia. Se il tuo concorrente sta fallendo e tu copi i suoi prezzi, fallirai con lui. La matematica non ha sentimenti.",
        "punti_si": 1
    },
    {
        "area": "AREA 2: IL TEMPO (LA RUOTA)",
        "domanda": "SE TI ASSENTI 3 GIORNI, L'AZIENDA SI FERMA?",
        "sotto_testo": "(O ricevi 50 telefonate all'ora dai collaboratori?)",
        "lezione": "**LA LEZIONE DELL'ESORCISTA:** Se l'azienda non gira senza di te, non hai un'azienda, hai un lavoro faticoso. Sei il collo di bottiglia del tuo successo.",
        "punti_si": 1
    }
]

# --- LOGICA DI NAVIGAZIONE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_lesson' not in st.session_state:
    st.session_state.show_lesson = False

# --- INTERFACCIA ---
st.title("🐹 ANSIA S.P.A.")
st.subheader("Diagnosi per Titolari Criceti")

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    # Header Area
    st.markdown(f"<div class='area-header'>{item['area']}</div>", unsafe_allow_html=True)
    st.write("")
    
    # Domanda
    st.info(f"DOMANDA #{st.session_state.step + 1}")
    st.header(item['domanda'])
    st.write(item['sotto_testo'])
    
    st.divider()

    # Bottoni Risposta
    col1, col2 = st.columns(2)
    
    if not st.session_state.show_lesson:
        if col1.button("SÌ, VADO A OCCHIO"):
            st.session_state.score += item['punti_si']
            st.session_state.show_lesson = True
            st.rerun()
        
        if col2.button("NO, HO UN CALCOLO MATEMATICO"):
            st.session_state.show_lesson = True
            st.rerun()
    else:
        # Mostra la Lezione
        st.markdown(f"<div class='lesson-box'>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("PROSSIMA DOMANDA ➡️"):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- RISULTATO FINALE ---
    st.balloons()
    st.header("📊 DIAGNOSI FINALE")
    
    livello_ansia = (st.session_state.score / len(domande)) * 100
    
    if livello_ansia > 70:
        st.error(f"LIVELLO ANSIA: {livello_ansia:.0f}% - CODICE ROSSO")
        st.write("Sei un criceto dopato. La tua ruota sta per esplodere. Dobbiamo fermarci subito.")
    elif livello_ansia > 30:
        st.warning(f"LIVELLO ANSIA: {livello_ansia:.0f}% - CODICE GIALLO")
        st.write("Corri tanto, ma rimani fermo. Qualche ingranaggio è bloccato.")
    else:
        st.success(f"LIVELLO ANSIA: {livello_ansia:.0f}% - CODICE VERDE")
        st.write("L'azienda gira bene, ma non abbassare la guardia.")

    if st.button("RICOMINCIA TEST"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
