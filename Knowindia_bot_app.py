import streamlit as st
from transformers import pipeline

# Load the Question Answering pipeline
qa = pipeline("question-answering")

# Static context about India
context = """
India is a vast country in South Asia known for its diversity in culture, religion, language, and geography.
It has 28 states and 8 union territories. The national language is Hindi, and English is widely used in education and business.
The capital city is New Delhi.

CULTURE: India is known for classical dance forms like Bharatanatyam, Kathak, and Odissi. Festivals like Diwali, Holi, Eid, Christmas, and Navratri
are celebrated across the country. Indian cuisine is famous for spices and variety — dishes like biryani, dosa, samosa, and sweets like gulab jamun are popular.

TECHNOLOGY: India has developed rapidly in IT, mobile technology, and digital services. ISRO (Indian Space Research Organisation) has successfully launched
Chandrayaan-3 to the moon and Mangalyaan to Mars. Digital India and UPI have made India a global leader in fintech.

ECONOMY: India is the 5th largest economy in the world. Major industries include IT, agriculture, manufacturing, and services.
Mumbai is the financial capital. The Sensex and Nifty are the main stock markets.

PLACES: Popular tourist places include the Taj Mahal in Agra, Qutub Minar in Delhi, Red Fort, Gateway of India in Mumbai,
backwaters of Kerala, Himalayas in the north, and beaches of Goa. The Ganga, Yamuna, and Brahmaputra are major rivers.

HISTORY: India got independence from British rule on 15 August 1947. Mahatma Gandhi led the freedom movement through non-violence.
The Indian Constitution came into effect on 26 January 1950.

TRADITIONS: Yoga and Ayurveda originated in India and are now popular worldwide. India is also known for meditation, Vedas, and ancient sciences.

SPORTS: Cricket is the most popular sport. India has also made progress in hockey, badminton, wrestling, and athletics.
Neeraj Chopra won Olympic gold in javelin in 2021.

India is known as "Incredible India" because of its unity in diversity.
"""

# ---- Streamlit UI ----
st.title("🇮🇳 Incredible India - Q&A Bot")
st.markdown("Ask any general knowledge question about **India** – culture, history, places, tech, and more!")

# Input field
user_question = st.text_input("🔍 Your Question:")

# Button to get answer
if st.button("Get Answer"):
    if user_question.strip() != "":
        result = qa(question=user_question, context=context)
        st.success(f"**Answer:** {result['answer']}")
    else:
        st.warning("Please enter a question.")
