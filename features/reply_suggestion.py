import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


def get_ai_reply(name: str, business: str, message: str) -> str:
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        prompt = f"""
You are a helpful assistant for a {business} business in India.
A customer named {name} sent this WhatsApp message: '{message}'
Write a short, polite, professional reply in 2-3 sentences.
Keep it friendly. Do not use complex English.
"""
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return (
            f"Hi {name}, thank you for reaching out to us! "
            f"We received your message about {business} and will get back to you shortly."
        )


def show_reply_suggestion():
    st.header('💬 AI Reply Suggestion')
    st.write('Generate smart WhatsApp replies for incoming lead messages.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Input')
        lead_name = st.text_input('Lead Name', value='Rahul')
        business_type = st.selectbox(
            'Business Type',
            ['AC Service', 'Coaching Center', 'Tyre Shop',
             'Real Estate', 'Hospital', 'Restaurant', 'Other']
        )
        customer_message = st.text_area(
            'Customer Message',
            value='I need AC installation for my office urgently',
            height=120
        )

        reply_btn = st.button('✨ Generate Reply', type='primary')

    with col2:
        st.subheader('Result')
        if reply_btn and customer_message:
            with st.spinner('Generating AI reply...'):
                reply = get_ai_reply(lead_name, business_type, customer_message)

            st.success('Reply Generated!')
            st.markdown(f'**Suggested Reply:**')
            st.info(f'"{reply}"')

            st.markdown('**API Response:**')
            st.json({'suggested_reply': reply})

            # Copy hint
            st.caption('Copy this reply and send it on WhatsApp')
        else:
            st.info('Fill in the details and click Generate Reply')