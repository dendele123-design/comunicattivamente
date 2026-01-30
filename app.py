import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi Aziendale", page_icon="🐹", layout="centered")

# --- STILE CSS PERSONALIZZATO (Look Professionale & Aggressivo) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3.5em; font-weight: bold; text-transform: uppercase; }
    .area-header { background-color: #000000; color: white; padding: 15px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 20px; letter-spacing: 2px; }
    .lesson-box { background-color: #f8f9fa; color: #1a1a1a; padding: 25px; border-radius: 10px; border-left: 8px solid #ff4b4b; margin-top: 20px; font-style: italic; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    .profile-box { padding: 30px; border-radius: 15px; border: 2px solid #000; margin-top: 20px; }
    .contact-link { color: #ff4b4b; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DELLE 20 DOMANDE ---
# Per aggiungere le altre 17 domande, segui lo schema qui sotto: 
# Copia da { a }, e incolla sotto l'ultima virgola.
domande = [
    {
        "area": "AREA 1: IL SANGUE (I SOLDI)",
        "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?",
        "sotto": "(O guardi cosa fanno i concorrenti e ti metti un po' sotto?)",
        "lezione": "Il 'prezzo di mercato' è una bugia. Se il tuo concorrente sta fallendo (e non lo sai) e tu copi i suoi prezzi, fallirai con lui. Il prezzo deve coprire i TUOI costi e garantirti il TUO margine. La matematica non ha sentimenti.",
        "punti": 1
    },
    {
        "area": "AREA 2: IL TEMPO (LA RUOTA)",
        "testo": "SE TI ASSENTI 3 GIORNI, L'AZIENDA SI FERMA?",
        "sotto": "(O ricevi 50 telefonate all'ora dai collaboratori?)",
        "lezione": "Se l'azienda non gira senza di te, non hai un'azienda, hai un lavoro faticoso. Sei il collo di bottiglia del tuo successo. Il sistema deve essere indipendente dal titolare.",
        "punti": 1
    },
    {
        "area": "AREA 3: IL CAOS (L'ORGANIZZAZIONE)",
        "testo": "LE PROCEDURE SONO SCRITTE O SOLO NELLA TUA TESTA?",
        "sotto": "(Se un dipendente nuovo arriva oggi, sa cosa fare senza chiederti nulla?)",
        "lezione": "Le parole volano, i processi restano. Senza procedure scritte, ogni errore dei tuoi dipendenti è in realtà un TUO errore di gestione.",
        "punti": 1
    }
    # AGGIUNGI QUI LE ALTRE 17 DOMANDE SEGUENDO LO STESSO SCHEMA
]

# --- INIZIALIZZAZIONE STATO ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_lesson' not in st.session_state:
    st.session_state.show_lesson = False

# --- INTERFACCIA TEST ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=200) # Se hai un logo online mettilo qui
st.title("🐹 ANSIA S.P.A.")
st.subheader("Trasformiamo il Caos in Efficienza")

if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    # Area e Domanda
    st.markdown(f"<div class='area-header'>{item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(item['sotto'])
    st.divider()

    if not st.session_state.show_lesson:
        col1, col2 = st.columns(2)
        if col1.button("🔴 SÌ (1 PUNTO)"):
            st.session_state.score += item['punti']
            st.session_state.show_lesson = True
            st.rerun()
        if col2.button("🟢 NO (0 PUNTI)"):
            st.session_state.show_lesson = True
            st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("PROSSIMA DOMANDA ➡️"):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # --- RISULTATO FINALE ---
    st.balloons()
    score = st.session_state.score
    st.header("📊 LA TUA DIAGNOSI")
    st.metric("PUNTEGGIO TOTALE", f"{score} Punti")

    # LOGICA PROFILI
    if score <= 4:
        titolo = "PROFILO A: L'OROLOGIO SVIZZERO (O IL BUGIARDO)"
        colore = "#d4edda"
        testo = """Complimenti. Se i tuoi dati sono veri, sei nell'1% degli imprenditori che ha capito come si gioca. 
        Hai costruito un sistema che funziona, hai liquidità e probabilmente riesci anche ad andare in vacanza. 
        <b>Prognosi:</b> Ottima, ma attenzione alla 'Zona di Comfort'. Il tuo prossimo obiettivo è l'Espansione."""
    elif score <= 12:
        titolo = "PROFILO B: IL CRICETO STANCO"
        colore = "#fff3cd"
        testo = """Sei nella media italiana. L'azienda sta in piedi, i soldi girano, ma il motore sta fondendo. 
        Lavori troppo per compensare la mancanza di processi. Riesci a gestire le emergenze, ma non riesci a pianificare il futuro.
        <b>Prognosi:</b> Sei a rischio. Se il mercato tossisce, l'azienda prende la polmonite. Devi smettere di correre e iniziare a organizzare."""
    else:
        titolo = "PROFILO C: L'AZIENDA POSSEDUTA"
        colore = "#f8d7da"
        testo = """Allarme Rosso. Non indoriamo la pillola: sei nei guai. Non stai guidando l'azienda; sei passeggero di un treno in fiamme senza freni.
        I soldi escono senza controllo, il tempo evapora e tu sei l'unico che tiene insieme i pezzi con lo scotch.
        <b>Prognosi:</b> Riservata. Se non intervieni drasticamente con un 'Esorcismo Aziendale', il fallimento è una questione di quando, non di se."""

    st.markdown(f"""
        <div class='profile-box' style='background-color: {colore};'>
            <h3>{titolo}</h3>
            <p style='font-size: 18px;'>{testo}</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()
    
    # LA PROGNOSI NON È IL DESTINO
    st.subheader("LA PROGNOSI NON È IL DESTINO")
    st.write("""Il Caos ha una caratteristica fisica: l'Entropia. Se lasciato a se stesso, peggiora sempre. 
    Guarisce solo con l'azione. Il Kit che hai scaricato è il primo passo, ma se vuoi ricostruire le fondamenta, serve un Architetto.""")
    
    # CALL TO ACTION
    st.write("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.link_button("📘 SCARICA L'EBOOK COMPLETO", "https://www.tuosito.it/ebook-download", type="primary")
    with col_b:
        st.link_button("📅 PRENOTA UNA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI
    st.markdown("""
        <div style='text-align: center; margin-top: 50px; padding: 20px; background-color: #f1f1f1; border-radius: 10px;'>
            <b>Daniele Salvatori | comunicAttivamente</b><br>
            Trasformiamo il Caos in efficienza<br>
            📧 <a href='mailto:daniele@comunicattivamente.it'>daniele@comunicattivamente.it</a> | 📞 +39 392 933 4563<br>
            🌐 <a href='http://www.comunicattivamente.it'>www.comunicAttivamente.it</a>
        </div>
    """, unsafe_allow_html=True)

    if st.button("RIFAI IL TEST"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.rerun()
