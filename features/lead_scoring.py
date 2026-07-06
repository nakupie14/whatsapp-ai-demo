import streamlit as st


HOT_WORDS = [
    'urgent', 'urgently', 'immediately', 'asap',
    'bulk', 'wholesale', 'units', 'price', 'pricing',
    'cost', 'how much', 'quote', 'purchase', 'order',
    'demo', 'today', 'buy', 'invoice', 'payment'
]

WARM_WORDS = [
    'interested', 'looking for', 'need', 'want',
    'tell me more', 'more details', 'features',
    'recommend', 'suggest', 'explain', 'catalogue',
    'warranty', 'service', 'offer', 'discount'
]

COLD_WORDS = [
    'just browsing', 'just checking', 'not sure',
    'maybe', 'later', 'someday', 'no budget',
    'expensive', 'next year', 'just curious'
]


def score_lead(message: str):
    msg = message.lower()
    hot_hits = [w for w in HOT_WORDS if w in msg]
    warm_hits = [w for w in WARM_WORDS if w in msg]
    cold_hits = [w for w in COLD_WORDS if w in msg]

    hot_count = len(hot_hits)
    cold_count = len(cold_hits)

    if cold_count >= 1 and hot_count == 0:
        return 'Cold', 'Low intent signals detected', cold_hits, 0.75
    elif hot_count >= 2:
        return 'Hot', 'Multiple urgency or buying signals detected', hot_hits, 0.92
    elif hot_count == 1:
        return 'Warm', 'Some buying interest detected', hot_hits + warm_hits, 0.70
    return 'Warm', 'No strong signals — needs follow up', warm_hits, 0.60


def show_lead_scoring():
    st.header('🔥 Lead Scoring')
    st.write('Classify incoming leads as Hot, Warm, or Cold based on their message.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Input')
        lead_id = st.number_input('Lead ID', min_value=1, value=1)
        name = st.text_input('Lead Name', value='Rahul Sharma')
        source = st.selectbox('Source', ['website', 'manual', 'csv', 'google_ad'])
        message = st.text_area(
            'Lead Message',
            value='I need 10 AC units urgently for my office building',
            height=120
        )

        # Example buttons
        st.markdown('**Quick Examples:**')
        ex1, ex2, ex3 = st.columns(3)
        if ex1.button('Hot Example'):
            st.session_state['ls_msg'] = 'I need bulk order with pricing urgently asap'
        if ex2.button('Warm Example'):
            st.session_state['ls_msg'] = 'I am interested, can you tell me more details'
        if ex3.button('Cold Example'):
            st.session_state['ls_msg'] = 'Just browsing, not sure if I need this'

        if 'ls_msg' in st.session_state:
            message = st.session_state['ls_msg']

        score_btn = st.button('🔍 Score This Lead', type='primary')

    with col2:
        st.subheader('Result')
        if score_btn and message:
            with st.spinner('Scoring lead...'):
                score, reason, signals, confidence = score_lead(message)

            # Score badge
            if score == 'Hot':
                st.success(f'🔥 Score: **{score}**')
            elif score == 'Warm':
                st.warning(f'☀️ Score: **{score}**')
            else:
                st.info(f'❄️ Score: **{score}**')

            st.metric('Confidence', f'{int(confidence * 100)}%')
            st.write(f'**Reason:** {reason}')

            if signals:
                st.write('**Signals Detected:**')
                for s in signals:
                    st.markdown(f'- `{s}`')

            # JSON view
            st.markdown('**API Response:**')
            st.json({
                'lead_id': lead_id,
                'score': score,
                'reason': reason,
                'confidence': confidence
            })
        else:
            st.info('Fill in the details and click Score This Lead')