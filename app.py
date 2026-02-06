import streamlit as st
import time

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (Ansia S.p.A. Identity)
# =================================================================
st.set_page_config(page_title="Ansia S.p.A. - Diagnosi", page_icon="🎯", layout="centered")

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

    /* LOGO TESTUALE PERSONALIZZATO */
    .brand-logo {{
        text-align: center;
        color: {ROSSO_BRAND} !important;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 1px;
        margin-bottom: 0px;
    }}
    .brand-sub {{
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        color: #666 !important;
        margin-top: -10px;
        margin-bottom: 30px;
    }}

    /* AREA HEADER DOMANDA */
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
    
    /* BOTTONE PRIMARIO ROSSO */
    div.stButton > button:first-child[kind="primary"] {{
        background-color: {ROSSO_BRAND} !important;
        color: white !important;
        border: none;
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
    {"area": "SOLDI", "testo": "SAI IL TUO 'PUNTO DI PAREGGIO' MENSILE?", "sotto": "(La cifra esatta per coprire tutte le spese fisse e variabili).", "opzioni": [{"testo": "🔴 NON ESATTAMENTE", "punti": 1}, {"testo": "🟢 LO SO AL CENTESIMO", "punti": 0}], "lezione": "Se non sai quanto ti costa tenere la serranda alzata, vivi nell'ansia. Il Break-Even ti dà la calma strategica."},
    {"area": "SOLDI", "testo": "SE I CLIENTI NON PAGANO OGGI, QUANTO SOPRAVVIVI?", "sotto": "(Il test della cassa: quanti mesi di ossigeno hai?)", "opzioni": [{"testo": "🔴 MENO DI UN MESE", "punti": 1}, {"testo": "🟢 ALMENO 3 MESI", "punti": 0}], "lezione": "Le aziende falliscono perché finiscono la cassa. Se vivi bonifico su bonifico, sei ostaggio dei tuoi clienti. Costruisci la riserva di guerra."},
    
    # AREA 2: TEMPO
    {"area": "TEMPO", "testo": "LE TUE RIUNIONI HANNO UN ORDINE SCRITTO?", "sotto": "(Tutti sanno di cosa si parla e per quanto tempo?)", "opzioni": [{"testo": "🔴 NO, PARLIAMO E BASTA", "punti": 1}, {"testo": "🟢 SÌ, SEMPRE", "punti": 0}], "lezione": "Una riunione senza agenda è una chiacchierata al bar costosa. Se non c'è un obiettivo, avete bruciato stipendi per nulla."},
    {"area": "TEMPO", "testo": "SEI TU A DECIDERE QUANDO LEGGERE LE MAIL?", "sotto": "(O è il 'Ding' del telefono a deciderlo per te?)", "opzioni": [{"testo": "🔴 APPENA ARRIVANO", "punti": 1}, {"testo": "🟢 A BLOCCHI ORARI FISSI", "punti": 0}], "lezione": "La reattività immediata è nevrosi. Il cervello impiega 15 min per ritrovare il focus dopo un'interruzione. Se rispondi subito, reagisci, non lavori."},
    {"area": "TEMPO", "testo": "QUANTO TEMPO PERDI A CERCARE I FILE?", "sotto": "(Fatture, loghi, preventivi...)", "opzioni": [{"testo": "🔴 TANTO / DIPENDE", "punti": 1}, {"testo": "🟢 ZERO, SO DOVE SONO", "punti": 0}], "lezione": "Il caos digitale mangia 40 min al giorno a ogni dipendente. Sono settimane di stipendio pagate per giocare a nascondino."},
    {"area": "TEMPO", "testo": "QUANDO UN CLIENTE CHIAMA, INTERROMPI TUTTO?", "sotto": "(O hai un filtro/segretaria o orari dedicati?)", "opzioni": [{"testo": "🔴 RISPONDO SEMPRE", "punti": 1}, {"testo": "🟢 HO FILTRI E ORARI", "punti": 0}], "lezione": "Essere sempre disponibili ti fa sembrare servile, non professionale. Il chirurgo non risponde al cellulare mentre opera."},
    {"area": "TEMPO", "testo": "USI UN CALENDARIO CONDIVISO CON IL TEAM?", "sotto": "(O ti chiedono ancora 'Sei libero martedì'?)", "opzioni": [
