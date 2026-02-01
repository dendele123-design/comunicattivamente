import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🐹", layout="centered")

# --- DESIGN "DEGNO" (CSS AVANZATO) ---
st.markdown("""
    <style>
    /* Import font elegante da Google */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Pulizia menu Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}

    /* Card per le domande */
    .question-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        margin-bottom: 20px;
    }

    /* Area Header */
    .area-header {
        background-color: #000000;
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        display: inline-block;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }

    /* Bottoni */
    .stButton>button {
        border-radius: 10px;
        height: 3.5em;
        transition: all 0.3s;
    }
    
    /* Testo contatti cliccabile e protetto dal "vada a capo" */
    .contact-box {
        text-align: center;
        padding: 25px;
        background-color: #f9f9f9;
        border-radius: 15px;
        margin-top: 40px;
        font-size: 14px;
    }
    .phone-link {
        white-space: nowrap; /* Impedisce al numero di andare a capo */
        color: #ff4b4b;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DOMANDE ---
domande = [
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "(Non quanto hai incassato. Quanto ti è rimasto pulito).", "opzioni": [{"testo": "🔴 NO / GUARDO IL FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, CONOSCO IL MARGINE", "punti": 0}], "lezione": "Il fatturato è vanità. Se incassi 1.000€ ma ne spendi 950€, sei un volontario, non un imprenditore."},
    {"area": "TEMPO", "testo": "SE TI ASSENTI 3 GIORNI, L'AZIENDA SI FERMA?", "sotto": "(O ricevi 50 telefonate all'ora dai collaboratori?)", "opzioni": [{"testo": "🔴 SI FERMA TUTTO", "punti": 1}, {"testo": "🟢 VA AVANTI", "punti": 0}], "lezione": "Se l'azienda non gira senza di te, hai un lavoro faticoso, non un'azienda. Sei il collo di bottiglia del tuo successo."},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "(Manuali su come si fanno le cose)", "opzioni": [{"testo": "🔴 NO, È NELLA TESTA", "punti": 1}, {"testo": "🟢 SÌ, ABBIAMO I MANUALI", "punti": 0}], "lezione": "L'oralità è il medioevo. Se devi spiegare una cosa due volte, hai fallito. Scrivila o fai un video."}
]

# --- INIZIALIZZAZIONE ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'area_scores' not in st.session_state: st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0}
if 'show_lesson' not in st.session_state: st.session_state.show_lesson = False

# --- HEADER ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=180)
st.write("")

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    # Card Domanda
    st.markdown(f"<div class='area-header'>{item['area']}</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="question-card">
        <small style="color:#888">DOMANDA {st.session_state.step + 1} di {len(domande)}</small>
        <h2 style="margin-top:10px;">{item['testo']}</h2>
        <p style="color:#666;">{item['sotto']}</p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.show_lesson:
        col1, col2 = st.columns(2)
        if col1.button(item['opzioni'][0]['testo']):
            st.session_state.score += item['opzioni'][0]['punti']
            st.session_state.area_scores[item['area']] += item['opzioni'][0]['punti']
            st.session_state.show_lesson = True
            st.rerun()
        if col2.button(item['opzioni'][1]['testo']):
            st.session_state.show_lesson = True
            st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        testo_tasto = "VEDI DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        if st.button(testo_tasto):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- RISULTATI ---
    with st.spinner("L'Esorcista sta elaborando..."): time.sleep(1.5)
    
    st.header("📊 DIAGNOSI FINALE")
    score = st.session_state.score
    
    # Definiamo il profilo
    if score <= 4:
        titolo, colore, desc = "L'OROLOGIO SVIZZERO", "#d4edda", "Ottimo lavoro. Sei nell'1% degli imprenditori. Continua così."
    elif score <= 12:
        titolo, colore, desc = "IL CRICETO STANCO", "#fff3cd", "Sei nella media. L'azienda sta in piedi ma tu sei esausto. Serve metodo."
    else:
        titolo, colore, desc = "L'AZIENDA POSSEDUTA", "#f8d7da", "Allarme Rosso. Sei prigioniero di un sistema che brucia tempo e salute."

    st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p>{desc}</p></div>", unsafe_allow_html=True)

    st.write("")
    st.subheader("🚑 KIT DI SOPRAVVIVENZA")
    st.info("💡 Domani chiedi al commercialista il tuo margine reale invece del fatturato.")
    
    st.divider()
    
    # CALL TO ACTION
    c1, c2 = st.columns(2)
    c1.link_button("📘 SCARICA EBOOK", "https://tuolink.com")
    c2.link_button("📅 PRENOTA ORA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI CON NUMERO CLICCABILE E PROTEZIONE "A CAPO"
    st.markdown("""
        <div class="contact-box">
            <b>Daniele Salvatori | comunicAttivamente</b><br>
            <a href="mailto:daniele@comunicattivamente.it" style="color:#444; text-decoration:none;">daniele@comunicattivamente.it</a><br>
            <span style="color:#888;">Chiama ora:</span> 
            <a href="tel:+393929334563" class="phone-link">+39 392 933 4563</a>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("---")
    if st.button("🔄 RICOMINCIA"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
