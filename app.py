import streamlit as st
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Comunicattivamente Hub", page_icon="🛡️", layout="centered")

# --- STILE CSS (Blindato, Anti-Dark Mode, Rosso #dc061e) ---
st.markdown("""
    <style>
    /* FORZA SFONDO BIANCO E TESTO NERO */
    .stApp { background-color: #ffffff !important; }
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, li {
        color: #1a1a1a !important;
    }

    /* TITOLI IN ROSSO ISTITUZIONALE */
    h1, h2, h3 { color: #dc061e !important; }

    /* MENU A DISCESA (Selectbox) */
    div[data-baseweb="select"] > div {
        background-color: #f1f3f6 !important;
        border: 2px solid #dc061e !important;
        border-radius: 10px !important;
    }

    /* BOTTONI ROSSI */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #dc061e !important; color: #ffffff !important; 
        border: none !important; width: 100%; height: 3.5em; font-weight: bold;
        text-transform: uppercase;
    }
    
    /* BOTTONI SECONDARI (Opzioni) */
    .stButton>button {
        width: 100%; border-radius: 8px !important; background-color: #f1f3f6 !important;
        color: #1a1a1a !important; border: 1px solid #d1d5db !important;
    }

    /* BOX INFO / NOTA DELL'ARCHITETTO */
    .info-box {
        background-color: #f8f9fa !important; border-left: 8px solid #dc061e !important;
        padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    header {visibility: hidden !important;} footer {visibility: hidden !important;} #MainMenu {visibility: hidden !important;}
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE DOMANDE ANSIA SPA (Strategia) ---
domande_ansia = [
    {"testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "Non l'incasso. Il margine pulito rimasto in tasca.", "feedback": "Il fatturato è vanità. Se non conosci il margine, stai pilotando un aereo bendato."},
    {"testo": "VAI A 'SENTIMENTO' QUANDO FAI UN PREZZO?", "sotto": "O hai un calcolo matematico basato sui tuoi costi fissi?", "feedback": "Il prezzo 'di mercato' è un'illusione pericolosa. La matematica non ha sentimenti."},
    {"testo": "LE TUE RIUNIONI HANNO SEMPRE UN ORDINE SCRITTO?", "sotto": "Tutti sanno cosa si decide o lo scoprite lì per lì?", "feedback": "Una riunione senza agenda è un furto di stipendi autorizzato."},
    {"testo": "SE SPARISCI PER 30 GIORNI, L'AZIENDA CONTINUA?", "sotto": "L'azienda produce utile o si ferma tutto?", "feedback": "Se l'azienda dipende da te, non hai un business. Hai un lavoro molto faticoso."},
    {"testo": "TI FIDATI PIÙ DEI DATI O DEL TUO INTUITO?", "sotto": "Guardi i report o segui la sensazione del mattino?", "feedback": "L'intuito è un pregiudizio. I dati sono l'unica via per la sanità mentale."},
    {"testo": "LICENZI MAI I CLIENTI TOSSICI?", "sotto": "O accetti chiunque pur di far girare il fatturato?", "feedback": "I clienti vampiri ti rubano tempo e salute. Toglierli è un atto di igiene finanziaria."},
    {"testo": "USI LE MAIL PER CHIEDERE DISPONIBILITÀ?", "sotto": "O hai un calendario condiviso e link di prenotazione?", "feedback": "Il ping-pong di mail per un appuntamento è uno spreco di vita."},
    {"testo": "OGNI PROCESSO È SCRITTO O REGISTRATO IN VIDEO?", "sotto": "O spieghi le cose a voce ogni volta da zero?", "feedback": "Se non è scritto, non esiste. Le procedure sono la tua unica via per la libertà."},
    {"testo": "CONOSCI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "La cifra esatta per coprire ogni singolo costo?", "feedback": "Sapere quando inizi a guadagnare davvero ti dà la calma del leader."},
    {"testo": "SAI QUANTO TI COSTA ACQUISIRE UN CLIENTE?", "sotto": "Tempo, marketing, telefonate... sai la cifra esatta?", "feedback": "Se non sai quanto costa vendere, rischi di pagare per lavorare."}
]

# --- STATO SESSIONE (Per non resettare i test) ---
if 'step_ansia' not in st.session_state: st.session_state.step_ansia = 0
if 'score_ansia' not in st.session_state: st.session_state.score_ansia = 0
if 'ansia_complete' not in st.session_state: st.session_state.ansia_complete = False

# --- UI APPLICAZIONE ---
st.write("# 🛡️")
st.title("HUB DELL'EFFICIENZA")
st.write("Smetti di essere un criceto. Inizia a essere un Architetto.")

# --- NAVIGAZIONE CENTRALE ---
st.markdown("---")
menu = st.selectbox("COSA VUOI FARE OGGI?", 
                    ["🏠 Home Page", 
                     "📊 Diagnosi Strategica (Ansia SPA)", 
                     "🛠️ Pronto Intervento (Toolkit)", 
                     "📖 Pillole di Efficienza (Bignami)"])
st.markdown("---")

# --- 1. HOME PAGE ---
if menu == "🏠 Home Page":
    st.subheader("Benvenuto nel Centro di Comando.")
    st.markdown("""
    <div class='info-box'>
    Questa app è l'estensione digitale dei tuoi manuali di esorcismo aziendale.<br><br>
    Scegli la <b>Diagnosi</b> per capire quanto è grave la situazione strategica, 
    o entra nel <b>Toolkit</b> per applicare i protocolli operativi immediati.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### I pilastri del sistema:")
    st.write("✅ **Strategia:** Basata sul libro *Ansia SPA*.")
    st.write("✅ **Operatività:** Basata sul libro *La riunione poteva essere una mail*.")

# --- 2. DIAGNOSI STRATEGICA ---
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
        st.subheader("LA TUA DIAGNOSI STRATEGICA")
        score = st.session_state.score_ansia
        if score <= 2:
            st.success("PROFILO: GAZZELLA. La tua azienda è sana e snella.")
        elif score <= 6:
            st.warning("PROFILO: CRICETO. Sei in affanno, la ruota cigola.")
        else:
            st.error("PROFILO: POSSEDUTO. Serve un esorcismo immediato.")
        
        if st.button("RICOMINCIA TEST", type="primary"):
            st.session_state.step_ansia = 0
            st.session_state.score_ansia = 0
            st.session_state.ansia_complete = False
            st.rerun()

# --- 3. PRONTO INTERVENTO ---
elif menu == "🛠️ Pronto Intervento (Toolkit)":
    st.subheader("Protocolli Operativi Digitali")
    tool = st.radio("Seleziona lo strumento:", ["💸 Calcola lo Spreco", "📅 Invito Intelligente", "📧 Script di Risposta"])
    st.divider()

    if tool == "💸 Calcola lo Spreco":
        st.markdown("<div class='info-box'>Scopri quanto costa davvero quella riunione inutile.</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            n = st.number_input("Partecipanti", min_value=1, value=4)
            h = st.slider("Durata (ore)", 0.5, 4.0, 1.0, 0.5)
        with col2:
            c = st.number_input("Costo orario medio (€)", min_value=1, value=45)
        tot = n * c * h
        st.error(f"VALORE BRUCIATO: {tot} €")
        st.write("💡 *Potevi scrivere una mail e salvare questo margine.*")

    elif tool == "📅 Invito Intelligente":
        st.write("Genera il testo per far scegliere l'orario agli altri:")
        tipo = st.selectbox("Tipo di incontro:", ["Chiamata (15 min)", "Meeting (30 min)", "Strategia (1 ora)"])
        link = st.text_input("Il tuo link Calendly/TidyCal:", "https://calendly.com/tuonome")
        if st.button("GENERA INVITO", type="primary"):
            msg = f"Ciao [Nome], per fissare la nostra {tipo.lower()} ed evitare mille mail, ti lascio il link alla mia agenda: {link}. Scegli pure lo slot più comodo!"
            st.code(msg, language="text")

    elif tool == "📧 Script di Risposta":
        motivo = st.selectbox("Perché vuoi rifiutare?", ["Manca agenda", "Siamo in troppi", "Posso risolvere via mail"])
        if st.button("GENERA RISPOSTA", type="primary"):
            if motivo == "Manca agenda":
                script = "Ciao [Nome], non vedo un'agenda allegata. Propongo di rimandare finché non avremo punti chiari su cui decidere."
            else:
                script = "Ciao [Nome], credo di non essere fondamentale in questa fase. Attendo il verbale per agire sui miei punti."
            st.code(script, language="text")

# --- 4. BIGNAMI ---
elif menu == "📖 Pillole di Efficienza (Bignami)":
    st.subheader("Il succo dell'esorcismo")
    with st.expander("📖 ANSIA SPA (Strategia)"):
        st.write("• **Il Fatturato è vanità.** Conta solo il margine.")
        st.write("• **Sei il collo di bottiglia?** Se tutto passa da te, l'azienda è ferma.")
    with st.expander("📧 LA RIUNIONE... (Operatività)"):
        st.write("• **La Fonte della Verità:** Mai più allegati, solo link al cloud.")
        st.write("• **Comunicazione Asincrona:** La mail è lenta, la chat è per l'incendio.")

# --- FOOTER ---
st.markdown("---")
st.write("Daniele Salvatori | daniele@comunicattivamente.it")
