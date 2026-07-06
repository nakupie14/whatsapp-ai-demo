import streamlit as st
from datetime import datetime, timedelta


def get_followup(score: str):
    if score == 'Hot':
        return 1, 'Hot lead — follow up within 1 hour'
    elif score == 'Warm':
        return 24, 'Warm lead — follow up within 24 hours'
    return 72, 'Cold lead — follow up within 3 days'


def show_followup():
    st.header('⏰ Smart Follow-up Timing')
    st.write('Get the best time recommendation to follow up with a lead.')
    st.markdown('---')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Input')
        lead_id = st.number_input('Lead ID', min_value=1, value=1)
        score = st.selectbox('Lead Score', ['Hot', 'Warm', 'Cold'])
        created_at = st.text_input('Created At', value='2025-05-01 10:00:00')
        last_contacted = st.text_input('Last Contacted', value='2025-05-01 10:00:00')

        followup_btn = st.button('⏰ Get Follow-up Time', type='primary')

    with col2:
        st.subheader('Result')
        if followup_btn:
            with st.spinner('Calculating...'):
                hours, recommendation = get_followup(score)

            now = datetime.now()
            followup_time = now + timedelta(hours=hours)

            if score == 'Hot':
                st.error(f'🔥 {recommendation}')
            elif score == 'Warm':
                st.warning(f'☀️ {recommendation}')
            else:
                st.info(f'❄️ {recommendation}')

            st.metric(
                'Follow Up By',
                followup_time.strftime('%d %b %Y, %I:%M %p')
            )

            st.markdown('**API Response:**')
            st.json({
                'lead_id': lead_id,
                'follow_up_in_hours': hours,
                'recommendation': recommendation
            })
        else:
            st.info('Select a score and click Get Follow-up Time')