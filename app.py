import streamlit as st
import time

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Ansia S.p.A. Identity)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🐹", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
    <style>
    /* FORZA TEMA CHIARO PER EVITARE PROBLEMI CON DARK MODE */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {{
        color: #1a1a1a !important;
    }}
    .stApp {{ background-color: #ffffff !important; }}
    
    /* NASCONDE HEADER E PULSANTI TECNICI */
    header {{visibility: hidden !important;}}
    footer {{visibility: hidden !important;}}
    .stAppDeployButton {{display:none !important;}}
    [data-testid="stHeader"] {{display:none !important;}}

    /* AREA HEADER */
    .area-header {{ 
        background-color: #000000 !important; 
        color: white !important; 
        padding: 15px; 
        text-align: center; 
        font-weight: bold; 
        border-radius: 5px; 
        margin-bottom: 20px; 
        letter-spacing: 2px; 
    }}

    /* LEZIONE ESORCISTA */
    .lesson-box {{ 
        background-color: #f8f9fa !important; 
        color: #1a1a1a !important; 
        padding: 25px; 
        border-radius: 10px; 
        border-left: 8px solid {ROSSO_BRAND} !important; 
        margin-top: 20px; 
        font-style: italic; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
    }}

    /* PROFILI FINALI */
    .profile-box {{ 
        padding: 30px; 
        border-radius: 15px; 
        border: 2px solid #000 !important; 
        margin-top: 20px; 
    }}

    /* BOTTONI */
    .stButton>button {{ 
        width: 100%; 
        border-radius: 5px; 
        height: 3.5em; 
        font-weight: bold; 
        text-transform: uppercase;
    }}

    .phone-link {{
        white-space: nowrap !important;
        color: {ROSSO_BRAND} !important;
        text-decoration: none !important;
        font-weight: bold !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. IL DATABASE DELLE 20 DOMANDE
# =================================================================
domande = [
    # AREA 1: SOLDI
    {"area": "SOLDI", "testo": "SAI ESATTAMENTE QUANTO HAI GUADAGNATO IERI?", "sotto": "(Non quanto hai incassato. Quanto ti è rimasto pulito).", "opzioni": [{"testo": "🔴 NO / SOLO FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, CONOSCO IL MARGINE", "punti": 0}], "lezione": "Il fatturato è vanità. Guidare senza conoscere il margine è come correre senza guardare la benzina: ti fermerai all'improvviso."},
    {"area": "SOLDI", "testo": "QUANDO FAI UN PREZZO, VAI A 'SENTIMENTO'?", "sotto": "(O guardi i concorrenti e ti metti un po' sotto?)", "opzioni": [{"testo": "🔴 SÌ, VADO A OCCHIO", "punti": 1}, {"testo": "🟢 NO, HO IL CALCOLO DEI COSTI", "punti": 0}], "lezione": "Il 'prezzo di mercato' è una bugia. Il prezzo deve coprire i TUOI costi e garantirti il TUO margine. La matematica non ha sentimenti."},
    {"area": "SOLDI", "testo": "FAI SCONTI PER CHIUDERE LA VENDITA?", "sotto": "(Il cliente tira sul prezzo e tu cedi per non perderlo).", "opzioni": [{"testo": "🔴 SÌ, SPESSO", "punti": 1}, {"testo": "🟢 MAI / SOLO IN CAMBIO DI ALTRO", "punti": 0}], "lezione": "Lo sconto è la droga dei poveri. Se togli il 10% dal prezzo, spesso togli il 50% dal tuo utile netto."},
    {"area": "SOLDI", "testo": "SAI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "(La cifra esatta per coprire tutte le spese fisse e variabili).", "opzioni": [{"testo": "🔴 NON ESATTAMENTE", "punti": 1}, {"testo": "🟢 LO SO AL CENTESIMO", "punti": 0}], "lezione": "Se non sai quanto ti costa tenere la serranda alzata, vivi nell'ansia. Il Break-Even ti dà la calma di chi sa quando inizia a guadagnare."},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "(Il test della cassa: quanti mesi di ossigeno hai?)", "opzioni": [{"testo": "🔴 MENO DI UN MESE", "punti": 1}, {"testo": "🟢 ALMENO 3 MESI", "punti": 0}], "lezione": "Le aziende falliscono perché finiscono la cassa. Se vivi bonifico su bonifico, sei ostaggio dei tuoi clienti. Costruisci la riserva di guerra."},
    
    # AREA 2: TEMPO
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "(Tutti sanno di cosa si parla e per quanto tempo?)", "opzioni": [{"testo": "🔴 NO, PARLIAMO E BASTA", "punti": 1}, {"testo": "🟢 SÌ, SEMPRE", "punti": 0}], "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa. Se non c'è un obiettivo, avete appena bruciato stipendi per nulla."},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "(O è il 'Ding' del telefono a deciderlo per te?)", "opzioni": [{"testo": "🔴 APPENA ARRIVANO", "punti": 1}, {"testo": "🟢 A BLOCCHI ORARI FISSI", "punti": 0}], "lezione": "La reattività immediata è nevrosi. Il cervello impiega 15 min per ritrovare il focus dopo un'interruzione. Se rispondi subito, non lavori: reagisci."},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "(Fatture, loghi, preventivi...)", "opzioni": [{"testo": "🔴 TANTO / DIPENDE", "punti": 1}, {"testo": "🟢 ZERO, SO DOVE SONO", "punti": 0}], "lezione": "Il caos digitale mangia 40 min al giorno a ogni dipendente. Sono settimane di stipendio pagate per giocare a nascondino col server."},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "(O hai un filtro/segretaria o orari dedicati?)", "opzioni": [{"testo": "🔴 RISPONDO SEMPRE", "punti": 1}, {"testo": "🟢 HO FILTRI E ORARI", "punti": 0}], "lezione": "Essere sempre disponibili ti fa sembrare servile, non professionale. Il chirurgo non risponde al cellulare mentre opera. Tu sì?"},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "(O ti chiedono ancora 'Sei libero martedì' a voce?)", "opzioni": [{"testo": "🔴 NO / WHATSAPP", "punti": 1}, {"testo": "🟢 SÌ, GOOGLE CALENDAR", "punti": 0}], "lezione": "Chiedere la disponibilità a voce genera un ping-pong inutile. Il calendario occupato zittisce tutti e ottimizza gli incastri."},

    # AREA 3: SQUADRA
    {"area": "SQUADRA", "testo": "TEST AUTOBUS: SE SPARISCI UN MESE...", "sotto": "(L'azienda continua a produrre o si ferma tutto?)", "opzioni": [{"testo": "🔴 SI FERMA / CROLLA", "punti": 1}, {"testo": "🟢 VA AVANTI", "punti": 0}], "lezione": "Se l'azienda sei tu, non hai un'azienda. Hai un lavoro a vita da cui non puoi dimetterti. L'obiettivo è rendersi inutili operativamente."},
    {"area": "SQUADRA", "testo": "HAI PROCEDURE SCRITTE PER I COMPITI?", "sotto": "(Manuali operativi su come si fanno le cose)", "opzioni": [{"testo": "🔴 NO, È NELLA TESTA", "punti": 1}, {"testo": "🟢 SÌ, ABBIAMO I MANUALI", "punti": 0}], "lezione": "L'oralità è il medioevo. Se devi spiegare una cosa due volte, hai fallito. Scrivila o fai un video. Solo così puoi delegare senza ansia."},
    {"area": "SQUADRA", "testo": "TI SENTI DIRE 'FACCIO PRIMA A FARLO IO'?", "sotto": "(E alla fine lo fai tu...)", "opzioni": [{"testo": "🔴 QUASI OGNI GIORNO", "punti": 1}, {"testo": "🟢 RARAMENTE", "punti": 0}], "lezione": "Questa frase è la lapide della tua crescita. Facendo tu il lavoro operativo, rubi tempo alla strategia e impedisci ai tuoi di imparare."},
    {"area": "SQUADRA", "testo": "I DIPENDENTI SANNO L'OBIETTIVO DEL MESE?", "sotto": "(O vengono solo a timbrare il cartellino?)", "opzioni": [{"testo": "🔴 NON CREDO", "punti": 1}, {"testo": "🟢 SÌ, CONDIVIDIAMO I NUMERI", "punti": 0}], "lezione": "Non puoi vincere la partita se non dici alla squadra qual è il punteggio. Condividere gli obiettivi crea alleati, nasconderli crea mercenari."},
    {"area": "SQUADRA", "testo": "ERRORE: CERCHI IL COLPEVOLE O LA CAUSA?", "sotto": "(Onestamente: chi ha sbagliato o dove è fallito il processo?)", "opzioni": [{"testo": "🔴 CHI HA SBAGLIATO?", "punti": 1}, {"testo": "🟢 DOVE È FALLITO IL PROCESSO?", "punti": 0}], "lezione": "Sgridare le persone è inutile se il processo è confuso. Aggiustare la procedura è l'unico modo per non far ripetere l'errore."},

    # AREA 4: STRATEGIA
    {"area": "STRATEGIA", "testo": "PRENDI DECISIONI SUI DATI O SULL'INTUITO?", "sotto": "(Cosa spingere, chi tagliare, dove investire?)", "opzioni": [{"testo": "🔴 INTUITO / PANCIA", "punti": 1}, {"testo": "🟢 DATI / REPORT", "punti": 0}], "lezione": "L'intuito è spesso un pregiudizio mascherato. I dati sono freddi e veritieri. Fidati di Excel, non delle sensazioni del mattino."},
    {"area": "STRATEGIA", "testo": "HAI IL CORAGGIO DI DIRE 'NO' A UN CLIENTE?", "sotto": "(Se è tossico, rompiscatole o fuori target)", "opzioni": [{"testo": "🔴 NO, FATTURATO È FATTURATO", "punti": 1}, {"testo": "🟢 SÌ, HO LICENZIATO CLIENTI", "punti": 0}], "lezione": "Non tutti i soldi sono uguali. I soldi di un cliente tossico costano il triplo in stress e tempo. Licenziarli è il modo più veloce per aumentare gli utili."},
    {"area": "STRATEGIA", "testo": "CONOSCI IL TUO BEST SELLER PER MARGINE?", "sotto": "(Quello che ti arricchisce davvero, non quello che vendi di più)", "opzioni": [{"testo": "🔴 NON SONO SICURO", "punti": 1}, {"testo": "🟢 SÌ, LO CONOSCO", "punti": 0}], "lezione": "Spesso vendiamo tantissimo prodotti che lasciano briciole e trascuriamo quelli d'oro. Se non sai cosa ti arricchisce, lavorerai tanto per poco."},
    {"area": "STRATEGIA", "testo": "SAI QUANTO TI COSTA ACQUISIRE UN CLIENTE?", "sotto": "(Marketing, tempo commerciale, adv...)", "opzioni": [{"testo": "🔴 IMPOSSIBILE SAPERLO", "punti": 1}, {"testo": "🟢 SÌ, IL CAC È CHIARO", "punti": 0}], "lezione": "Se spendi 100€ per acquisire un cliente che te ne porta 50€ di margine, stai pagando per lavorare. La matematica del marketing deve tornare."},
    {"area": "STRATEGIA", "testo": "HAI UN PIANO SCRITTO PER I PROSSIMI 12 MESI?", "sotto": "(Non un sogno, un piano concreto con date e nomi)", "opzioni": [{"testo": "🔴 È NELLA MIA TESTA", "punti": 1}, {"testo": "🟢 SÌ, SCRITTO E CONDIVISO", "punti": 0}], "lezione": "Se è nella testa, è un'allucinazione. Se è scritto, è un progetto. Le aziende si costruiscono sui progetti, non sulle speranze."}
]

# =================================================================
# 3. LOGICA DI NAVIGAZIONE E STATO
# =================================================================
if 'step' not in st.session_state: st.session_state.step = 0
if 'total_score' not in st.session_state: st.session_state.total_score = 0
if 'area_scores' not in st.session_state: st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
if 'show_lesson' not in st.session_state: st.session_state.show_lesson = False

# --- HEADER FISSO ---
st.image("https://www.comunicattivamente.it/wp-content/uploads/2023/logo-comunicattivamente.png", width=180)
st.title("🐹 ANSIA S.P.A.")
st.subheader("Diagnosi per Titolari Criceti")

# =================================================================
# 4. IL TEST INTERATTIVO
# =================================================================
if st.session_state.step < len(domande):
    item = domande[st.session_state.step]
    
    st.markdown(f"<div class='area-header'>AREA: {item['area']}</div>", unsafe_allow_html=True)
    st.write(f"**DOMANDA {st.session_state.step + 1} di {len(domande)}**")
    st.header(item['testo'])
    st.write(item['sotto'])
    st.divider()

    if not st.session_state.show_lesson:
        col1, col2 = st.columns(2)
        if col1.button(item['opzioni'][0]['testo']):
            st.session_state.total_score += item['opzioni'][0]['punti']
            st.session_state.area_scores[item['area']] += item['opzioni'][0]['punti']
            st.session_state.show_lesson = True
            st.rerun()
        if col2.button(item['opzioni'][1]['testo']):
            st.session_state.show_lesson = True
            st.rerun()
    else:
        st.markdown(f"<div class='lesson-box'><b>LA LEZIONE DELL'ESORCISTA:</b><br><br>{item['lezione']}</div>", unsafe_allow_html=True)
        st.write("")
        # Tasto dinamico all'ultima domanda
        testo_btn = "VEDI LA TUA DIAGNOSI 📊" if st.session_state.step == len(domande)-1 else "PROSSIMA DOMANDA ➡️"
        if st.button(testo_btn, type="primary"):
            st.session_state.step += 1
            st.session_state.show_lesson = False
            st.rerun()

else:
    # =================================================================
    # 5. RISULTATI FINALI E KIT DI SOPRAVVIVENZA
    # =================================================================
    with st.spinner("L'Esorcista sta calcolando il tuo livello di ansia..."): 
        time.sleep(1.5)
    
    score = st.session_state.total_score
    st.header("📊 RISULTATO DELLA DIAGNOSI")
    
    # LOGICA PROFILI
    if score <= 4:
        titolo, colore, desc = "PROFILO A: L'OROLOGIO SVIZZERO", "#d4edda", "Complimenti. Sei nell'1% degli imprenditori. Hai un sistema, non un lavoro. Prognosi: Ottima."
    elif score <= 12:
        titolo, colore, desc = "PROFILO B: IL CRICETO STANCO", "#fff3cd", "Sei nella media italiana. L'azienda sta in piedi ma tu sei esausto. Prognosi: Sei a rischio di burnout."
    else:
        titolo, colore, desc = "PROFILO C: L'AZIENDA POSSEDUTA", "#f8d7da", "Allarme Rosso. Sei passeggero di un treno in fiamme senza freni. Prognosi: Serve un intervento drastico."

    st.markdown(f"<div class='profile-box' style='background-color: {colore};'><h3>{titolo}</h3><p>{desc}</p></div>", unsafe_allow_html=True)

    # --- IL KIT DI SOPRAVVIVENZA DINAMICO ---
    if score > 4:
        st.write("")
        st.markdown(f"### 🚑 KIT DI SOPRAVVIVENZA DELL'ESORCISTA")
        st.write("In base alle tue risposte, ecco le 3 priorità su cui lavorare domani mattina:")
        
        # Ordiniamo le aree dove l'utente ha fatto più errori
        aree_critiche = sorted(st.session_state.area_scores.items(), key=lambda x: x[1], reverse=True)
        
        for area, punti in aree_critiche[:3]:
            if area == "SOLDI": st.info("💰 **SOLDI:** Smetti di guardare l'incasso. Domani mattina chiedi al tuo commercialista il MARGINE reale su ogni prodotto.")
            if area == "TEMPO": st.info("⏰ **TEMPO:** Disattiva le notifiche. Blocca due slot da 30 min per le mail e il resto del tempo lavora sulla strategia.")
            if area == "SQUADRA": st.info("👥 **SQUADRA:** Scegli un compito ripetitivo e registra un video mentre lo fai. Ecco la tua prima video-procedura.")
            if area == "STRATEGIA": st.info("🎯 **STRATEGIA:** Analizza il tuo database. Trova il cliente più tossico e preparati a dirgli di 'No'.")

    st.divider()
    st.subheader("LA PROGNOSI NON È IL DESTINO")
    st.write("Il Caos guarisce solo con l'azione. Non restare solo con il tuo punteggio.")
    
    col_a, col_b = st.columns(2)
    col_a.link_button("📘 SCARICA L'EBOOK COMPLETO", "https://www.comunicattivamente.it/ebook-ansia-spa", type="primary")
    col_b.link_button("📅 PRENOTA CONSULENZA", "mailto:daniele@comunicattivamente.it")

    # CONTATTI CON TELEFONO CLICCABILE
    st.write("")
    st.markdown(f"""
        <div style='text-align: center; padding: 25px; background-color: #f1f1f1; border-radius: 10px;'>
            <b>Daniele Salvatori | comunicAttivamente</b><br>
            Esorcismo del Caos Aziendale<br><br>
            📧 <a href='mailto:daniele@comunicattivamente.it' style='color: {ROSSO_BRAND};'>daniele@comunicattivamente.it</a><br>
            📞 <a href='tel:+393929334563' class='phone-link'>+39 392 933 4563</a><br><br>
            <a href='https://wa.me/393929334563' style='background-color:#25D366; color:white; padding:10px 20px; border-radius:50px; text-decoration:none; font-weight:bold;'>💬 WHATSAPP</a>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 RICOMINCIA IL TEST"):
        st.session_state.step = 0
        st.session_state.total_score = 0
        st.session_state.area_scores = {"SOLDI": 0, "TEMPO": 0, "SQUADRA": 0, "STRATEGIA": 0}
        st.rerun()
