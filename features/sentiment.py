import streamlit as st


POSITIVE_WORDS = [
    'good', 'great', 'excellent', 'happy', 'satisfied',
    'perfect', 'amazing', 'wonderful', 'thanks', 'thank you',
    'helpful', 'love', 'best', 'fantastic', 'superb'
]

NEGATIVE_WORDS = [
    'bad', 'worst', 'terrible', 'angry', 'disappointed',
    'horrible', 'pathetic', 'useless', 'fraud', 'cheat',
    'no reply', 'waste', 'poor', 'awful'
]


def analyse_sentiment(message: str):
    msg = message.lower()
    pos = sum(1 for w in POSITIVE_WORDS if w in msg)
    neg = sum(1 for w in NEGATIVE_WORDS if w in msg)

    if neg > pos:
        return 'Negative', 0.85
    elif pos > neg:
        return 'Positive', 0.88
    return 'Neutral', 0.65


def show_sentiment():
    st.header('😊 Sentiment Analysis')
    st.write('Detect if an incoming WhatsApp message is Positive, Negative, or Neutral.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Input')
        lead_id = st.number_input('Lead ID', min_value=1, value=1)
        message = st.text_area(
            'Message',
            value='Excellent service, very happy with everything thank you',
            height=120
        )

        st.markdown('**Quick Examples:**')
        ex1, ex2, ex3 = st.columns(3)
        if ex1.button('😊 Positive'):
            st.session_state['sent_msg'] = 'Excellent service, very happy, thank you so much'
        if ex2.button('😠 Negative'):
            st.session_state['sent_msg'] = 'Very disappointed, pathetic service, no reply at all'
        if ex3.button('😐 Neutral'):
            st.session_state['sent_msg'] = 'Okay, I will think about it'

        if 'sent_msg' in st.session_state:
            message = st.session_state['sent_msg']

        sent_btn = st.button('🔍 Analyse Sentiment', type='primary')

    with col2:
        st.subheader('Result')
        if sent_btn and message:
            with st.spinner('Analysing...'):
                sentiment, confidence = analyse_sentiment(message)

            if sentiment == 'Positive':
                st.success(f'😊 Sentiment: **{sentiment}**')
            elif sentiment == 'Negative':
                st.error(f'😠 Sentiment: **{sentiment}**')
            else:
                st.warning(f'😐 Sentiment: **{sentiment}**')

            st.metric('Confidence', f'{int(confidence * 100)}%')

            if sentiment == 'Negative':
                st.error('⚠️ Action Required: Escalate to senior agent immediately')
            elif sentiment == 'Positive':
                st.success('✅ Happy customer — good time to upsell')
            else:
                st.info('ℹ️ Neutral — continue normal follow up')

            st.markdown('**API Response:**')
            st.json({
                'lead_id': lead_id,
                'sentiment': sentiment,
                'confidence': confidence
            })
        else:
            st.info('Enter a message and click Analyse Sentiment')