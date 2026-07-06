import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


def generate_campaign(business: str, offer: str, tone: str) -> str:
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        prompt = f"""
Write a WhatsApp marketing message for a {business} business in India.
Offer: {offer}
Tone: {tone}
Rules:
- Maximum 160 characters
- End with a clear call to action like Reply YES or Call now
- No ALL CAPS
- Sound human not like a robot
"""
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return (
            f"Special offer from {business}! {offer}. "
            f"Reply YES to know more. Limited time only!"
        )


def show_campaign():
    st.header('📣 Campaign Message Generator')
    st.write('Generate WhatsApp marketing messages for any business type.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Input')
        business_type = st.selectbox(
            'Business Type',
            ['AC Service', 'Coaching Center', 'Tyre Shop',
             'Real Estate', 'Hospital', 'Restaurant', 'Gym']
        )
        offer = st.text_input(
            'Offer / Promotion',
            value='20% off on all services this summer'
        )
        tone = st.selectbox('Tone', ['casual', 'formal', 'festive', 'urgent'])
        variants = st.slider('Number of Variants', 1, 3, 2)

        campaign_btn = st.button('✨ Generate Campaign', type='primary')

    with col2:
        st.subheader('Result')
        if campaign_btn and offer:
            for i in range(variants):
                with st.spinner(f'Generating variant {i + 1}...'):
                    message = generate_campaign(business_type, offer, tone)

                st.markdown(f'**Variant {i + 1}:**')
                st.info(f'"{message}"')
                char_count = len(message)
                if char_count <= 160:
                    st.caption(f'✅ {char_count}/160 characters')
                else:
                    st.caption(f'⚠️ {char_count}/160 characters — too long')
                st.markdown('---')
        else:
            st.info('Fill in the details and click Generate Campaign')