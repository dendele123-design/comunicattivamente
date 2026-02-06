import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS (Blindato contro Dark Mode e Ottimizzato Mobile) ---
st.markdown("""
    <style>
    /* FORZA SFONDO BIANCO E TESTO NERO OVUNQUE */
    .stApp { background-color: #ffffff !important; }
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li {
        color: #1a1a1a !important;
    }

    /* TITOLI IN ROSSO ISTITUZIONALE */
    h1, h2, h3 { color: #dc061e !important; }

    /* SELECTBOX (IL NUOVO MENU) */
    div[data-baseweb="select"] > div {
        background-color: #f1f3f6 !important;
        border: 2px solid #dc061e !important;
        border-radius: 10px !important;
    }

    /* BOTTONE ROSSO */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #dc061e !important; color: #ffffff !important; 
        border: none !important; width: 100%; height: 3.5em; font-weight: bold;
    }
    
    /* BOX INFO / LEZIONE */
    .info-box {
        background-color: #f8f9fa !important; border-left: 8px solid #dc061e !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* EXPANDER (Bignami) */
    .stAttendance { background-color: #f1f3f6 !important; }

    header {visibility: hidden !important;} footer {visibility: hidden !important;} #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER FISSO ---
st.write("# 🛡️")
st.title("HUB DELL'EFFICIENZA")
st.write("Daniele Salvatori | Comunicattivamente")

# --- NAVIGAZIONE CENTRALE (Sostituisce la Sidebar) ---
st.markdown("---")
menu = st.selectbox("COSA VUOI FARE OGGI?", 
                    ["🏠 Home Page", 
                     "📊 Diagnosi Strategica (Ansia SPA)", 
                     "🛠️ Pronto Intervento (Toolkit)", 
                     "📖 Pillole di Efficienza (Bignami)"])
st.markdown("---")

# --- CONTENUTO DINAMICO ---

if menu == "🏠 Home Page":
    st.subheader("Smetti di essere un criceto.")
    st.markdown("""
    <div class='info-box'>
    Benvenuto nel tuo centro di comando. Questa app è il compagno digitale dei libri <b>Ansia SPA</b> e <b>La riunione poteva essere una mail</b>.<br><br>
    Usa il menù qui sopra per navigare tra gli strumenti di esorcismo aziendale.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### I tuoi strumenti:")
    st.write("✅ **Diagnosi Strategica:** Scopri quanto è grave la 'possessione' della tua azienda.")
    st.write("✅ **Pronto Intervento:** Calcola lo spreco delle riunioni e scarica i protocolli.")
    st.write("✅ **Bignami:** I concetti chiave pronti all'uso.")

elif menu == "📊 Diagnosi Strategica (Ansia SPA)":
    st.subheader("Analisi Profonda (Libro 1)")
    st.write("Rispondi onestamente. Qui non ci sono capi, solo dati.")
    
    # ESEMPIO DI LOGICA TEST (Andrà integrata con le tue 20 domande)
    st.info("Caricamento del test di Ansia SPA in corso...")
    if st.button("AVVIA IL TEST COMPLETO", type="primary"):
        st.write("Test in fase di configurazione...")

elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.subheader("Strumenti Digitali (Libro 2)")
    
    scelta_tool = st.radio("Scegli lo strumento:", ["💸 Calcolatore dello Spreco", "📧 Protocollo 'No Riunione'"])
    
    if scelta_tool == "💸 Calcolatore dello Spreco":
        st.markdown("<div class='info-box'>Inserisci i dati reali e guarda quanto stai bruciando.</div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            num = st.number_input("Partecipanti", min_value=1, value=4)
            ore = st.slider("Durata (ore)", 0.5, 4.0, 1.0, 0.5)
        with c2:
            costo = st.number_input("Costo orario medio (€)", min_value=1, value=45)
        
        totale = num * costo * ore
        st.error(f"VALORE BRUCIATO: {totale} €")
        st.write("💡 *Con questa cifra potevi pagare una campagna marketing o un pranzo stellato al team. Invece avete parlato del nulla.*")

    elif scelta_tool == "📧 Protocollo 'No Riunione'":
        st.write("Scegli la situazione e copia lo script:")
        motivo = st.selectbox("Situazione:", ["Manca l'agenda", "Riunione troppo lunga", "Non sono necessario"])
        
        if motivo == "Manca l'agenda":
            script = "Ciao [Nome], ho ricevuto l'invito. Dato che non è allegata un'agenda con gli obiettivi, propongo di rimandare finché non avremo punti chiari su cui decidere. Procediamo via mail?"
        elif motivo == "Riunione troppo lunga":
            script = "Ciao [Nome], credo che 2 ore siano troppe per questo tema. Propongo uno stand-up meeting di 15 minuti alle ore [X] o di risolvere i punti critici via chat."
        else:
            script = "Ciao [Nome], grazie per l'invito. Leggendo l'agenda, credo che il mio contributo non sia fondamentale in questa fase. Resto in attesa del verbale per agire sui punti di mia competenza."
            
        st.code(script, language="text")
        st.write("*(Copia e incolla. Sii gentile, ma fermo come un Architetto).*")

elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("La Conoscenza in 60 secondi")
    
    with st.expander("📖 ANSIA SPA (Strategia)"):
        st.write("- **Il test dell'autobus:** Se sparisci un mese, l'azienda crolla?")
        st.write("- **Fatturato vs Margine:** Non confondere il giro d'affari con i soldi in tasca.")
        st.write("- **Licenziare i clienti:** I vampiri ti rubano l'anima, non solo il tempo.")
        
    with st.expander("📧 LA RIUNIONE... (Operatività)"):
        st.write("- **La Fonte della Verità:** Una sola cartella cloud, zero allegati via mail.")
        st.write("- **Mail vs Chat:** Se non scade tra 10 minuti, scrivi una mail.")
        st.write("- **Verbali istantanei:** Chi fa cosa, entro quando. O la riunione non è esistita.")

# --- FOOTER CONTATTI ---
st.markdown("---")
st.write("📧 daniele@comunicattivamente.it | 📞 +39 392 933 4563")
