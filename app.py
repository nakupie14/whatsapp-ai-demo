import streamlit as st

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title='WhatsApp AI Service — Demo',
    page_icon='🤖',
    layout='wide'
)

# ── Header ────────────────────────────────────────────────────
st.title('🤖 WhatsApp AI Service')
st.caption('One Step Marketing — Jaipur | Built by Nakul Soni')
st.markdown('---')

# ── Sidebar ───────────────────────────────────────────────────
st.sidebar.title('📋 Navigation')
feature = st.sidebar.radio(
    'Select Feature',
    [
        '🔥 Lead Scoring',
        '💬 AI Reply Suggestion',
        '😊 Sentiment Analysis',
        '⏰ Follow-up Timing',
        '📣 Campaign Generator'
    ]
)

st.sidebar.markdown('---')
st.sidebar.markdown('**All 5 AI Features:**')
st.sidebar.markdown('✅ Lead Scoring (ML Model)')
st.sidebar.markdown('✅ AI Reply Suggestion')
st.sidebar.markdown('✅ Sentiment Analysis')
st.sidebar.markdown('✅ Follow-up Timing')
st.sidebar.markdown('✅ Campaign Generator')

# ── Feature 1: Lead Scoring ───────────────────────────────────
if feature == '🔥 Lead Scoring':
    from features.lead_scoring import show_lead_scoring
    show_lead_scoring()

# ── Feature 2: AI Reply Suggestion ───────────────────────────
elif feature == '💬 AI Reply Suggestion':
    from features.reply_suggestion import show_reply_suggestion
    show_reply_suggestion()

# ── Feature 3: Sentiment Analysis ────────────────────────────
elif feature == '😊 Sentiment Analysis':
    from features.sentiment import show_sentiment
    show_sentiment()

# ── Feature 4: Follow-up Timing ──────────────────────────────
elif feature == '⏰ Follow-up Timing':
    from features.followup import show_followup
    show_followup()

# ── Feature 5: Campaign Generator ────────────────────────────
elif feature == '📣 Campaign Generator':
    from features.campaign import show_campaign
    show_campaign()
    