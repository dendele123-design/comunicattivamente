import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi Aziendale", page_icon="🐹", layout="centered")

# --- STILE CSS PERSONALIZZATO ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; font-weight: bold; text-transform: uppercase; }
    .area-header { background-color: #000000; color: white; padding: 15px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 20px; letter-spacing: 2px; }
    .lesson-box { background-color: #f8f9fa; color: #1a1a1a; padding: 25px; border-radius: 10px; border-left: 8px solid #ff4b4b; margin-top: 20px; font-style: italic; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    .profile-box { padding: 30px; border-radius: 15px; border: 2px solid #000; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DELLE DOMANDE ---
domande = [
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?",
        "sotto": "(O guardi cosa fanno i concorrenti e ti metti un po' sotto?)",
        "lezione": "Il 'prezzo di mercato' è una bugia. Se il tuo concorrente sta fallendo e tu copi i suoi prezzi, fallirai con lui. Il prezzo deve coprire i TUOI costi e garantirti il TUO margine.",
        "punti": 1
    },
    {
        "area": "AREA 2: IL TEMPO (LA RUOTA)",
        "testo": "SE TI ASSENTI 3 GIORNI, L'AZIENDA SI FERMA?",
        "sotto": "(O ricevi 50 telefonate all'ora dai collaboratori?)",
        "lezione": "Se l'azienda non gira senza di te, non hai un'azienda, hai un lavoro faticoso. Sei il collo di bottiglia del tuo successo. Il sistema deve essere indipendente dal titolare.",
        "punti": 1
    }
    # AGGIUNGI QUI LE ALTRE DOMANDE...
]

# --- INIZIALIZZAZIONE STATO ---
if 'step' not in st.session_state: st.session_state.step = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'show_lesson' not in st.session_state: st.session_state.show_lesson = False

# --- HEADER FISSO ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=200) 
st.title("🐹 ANSIA S.P.A.")
st.subheader("Diagnosi per Titolari Criceti")

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    st.markdown(f"<div class='area-header'>{item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(item['sotto'])
    st.divider()

    if not st.session_state.show_lesson:
        col1, col2 = st.columns(2)
        if col1.button("🔴 SÌ"):
            st.session_state.score += item['punti']
            st.session_state.show_lesson = True
            st.rerun()
        if col2.button("🟢 NO"):
            st.session_state.show_lesson = True
            st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        
        # LOGICA TASTO DINAMICO
        testo_tasto = "VEDI LA TUA DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        
        if st.button(testo_tasto):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- SCHERMATA FINALE ---
    with st.spinner("Generando la prognosi..."):
        time.sleep(1.5)
        
    score = st.session_state.score
    st.header("📊 RISULTATO DELLA DIAGNOSI")
    
    # LOGICA PROFILI
    if score <= 4:
        titolo, colore, testo = "PROFILO A: L'OROLOGIO SVIZZERO", "#d4edda", "Complimenti. Sei nell'1% degli imprenditori che ha capito come si gioca. Prognosi: Ottima, punta all'espansione."
    elif score <= 12:
        titolo, colore, testo = "PROFILO B: IL CRICETO STANCO", "#fff3cd", "Sei nella media. L'azienda sta in piedi ma il motore sta fondendo. Prognosi: Sei a rischio, serve metodo subito."
    else:
        titolo, colore, testo = "PROFILO C: L'AZIENDA POSSEDUTA", "#f8d7da", "Allarme Rosso. Sei passeggero di un treno in fiamme. Prognosi: Riservata, serve un intervento drastico."

    st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p style='font-size: 18px;'>{testo}</p></div>", unsafe_allow_html=True)
    st.divider()
    
    st.subheader("LA PROGNOSI NON È IL DESTINO")
    st.write("Il Caos non guarisce col tempo. Guarisce solo con l'azione. Se vuoi ricostruire le fondamenta, serve un Architetto.")
    
    st.write("")
    col_a, col_b = st.columns(2)
    with col_a: st.link_button("📘 SCARICA L'EBOOK", "https://yourlink.com", type="primary")
    with col_b: st.link_button("📅 PRENOTA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI CON SPAZIATURA
    st.write("")
    st.write("")
    st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f1f1f1; border-radius: 10px;'>
            <b>Daniele Salvatori | comunicAttivamente</b><br>
            📧 <a href='mailto:daniele@comunicattivamente.it'>daniele@comunicattivamente.it</a> | 📞 +39 392 933 4563
        </div>
    """, unsafe_allow_html=True)

    # TASTO RESET BEN DISTANZIATO
    st.write("")
    st.write("")
    st.write("---")
    if st.button("🔄 RICOMINCIA IL TEST"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
