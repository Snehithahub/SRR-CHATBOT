import streamlit as st

# Set page title and icon
st.set_page_config(page_title="SRR CloudExpertsGuru", page_icon="☁️", layout="wide")

# Header
st.title("Welcome to SRR CloudExpertsGuru")
st.subheader("Empowering Businesses with Scalable Cloud Solutions")

# Introduction Section
st.write("""
CloudExpertsGuru specializes in modernizing business-critical applications and infrastructure.  
We offer cloud solutions for companies of all sizes, providing seamless integration with **Google Cloud, AWS, and Microsoft Azure**.
""")

# Navigation Bar
st.markdown("""
    <style>
        .nav-bar {
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .nav-bar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-size: 18px;
        }
    </style>
    <div class="nav-bar">
        <a href="#solutions">Solutions</a>
        <a href="#industries">Industries</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# Solutions Section
st.header("🌟 Our Solutions")
st.write("""
✅ **Cloud Optimization**: Data Analytics, Governance, Security  
✅ **Cloud Migrations**: Storage, Data Center, Cloud-to-Cloud  
✅ **DevOps & Automation**: CI/CD Pipelines, Kubernetes, Docker  
✅ **Cloud Security**: IAM, Compliance, Disaster Recovery  
""")

# Industries Section
st.header("🏢 Industries We Serve")
st.write("""
We work with **Retail, Healthcare, E-commerce, Education, Utilities, and Travel & Hospitality**  
to accelerate digital transformation and improve operational efficiency.
""")

# Chatbot Section
st.header("💬 Ask SRR CloudExpertsGuru AI")
st.write("""
Our AI assistant can answer your questions about our services.  
**You can ask questions using the following keywords**: 
- solutions, cloud offerings, platforms, consulting, industries, about us, media, contact

Please ask anything related to these topics!
""")

# Chatbot Logic
faq_data = {
    "solutions": "We offer a wide range of cloud solutions like cloud optimization, migrations, DevOps automation, and security.",
    "cloud offerings": "Our cloud offerings include native development services, cloud managed services, application assessment, legacy modernization, and more.",
    "platforms": "We work with Google Cloud, AWS, and Microsoft Azure to deliver world-class cloud solutions.",
    "consulting": "We provide cloud advisory, cloud strategy, cloud adoption, and cloud delivery models like IaaS, PaaS, and SaaS.",
    "industries": "We serve industries like Retail, Travel & Hospitality, Utilities, E-commerce, Healthcare, and Education.",
    "about us": "SRR CloudExpertsGuru helps streamline your cloud journey, specializing in cloud solutions for businesses worldwide. Our experts focus on business outcomes with the best cloud practices.",
    "media": "Check out our media section for the latest news, press releases, and blogs about CloudExpertsGuru.",
    "contact us": "You can contact us at +91 7842111055 or email info@cloudexpertsguru.com for further inquiries."
}

# Helper function for handling flexible query responses
def get_response(query):
    query = query.lower()

    # Keywords to check for
    keywords = {
        "solutions": ["solutions", "offer", "different solutions", "cloud solutions", "what solutions"],
        "cloud offerings": ["cloud offerings", "offerings", "cloud services", "what services do you offer"],
        "platforms": ["platforms", "cloud platforms", "which platforms do you use", "what platforms"],
        "consulting": ["consulting", "cloud advisory", "cloud strategy", "consulting services"],
        "industries": ["industries", "which industries", "sectors we serve", "what industries do you serve"],
        "about us": ["about us", "who we are", "our company", "who are we"],
        "media": ["media", "latest news", "press releases", "blog", "news"],
        "contact": ["contact", "contact us", "get in touch", "how to contact"]
    }

    # Match query with keywords
    for key, values in keywords.items():
        for value in values:
            if value in query:
                return faq_data.get(key, "I’m not sure about that. Please contact us at +91 7842111055 or email info@cloudexpertsguru.com.")

    # Default response if no keywords match
    return "I didn’t quite catch that. Could you clarify? Or contact us at +91 7842111055 or email info@cloudexpertsguru.com for more details."

# Chatbot Input
user_query = st.text_input("Ask me anything about our cloud solutions:")

if st.button("Ask"):
    # Get a flexible response based on the query
    response = get_response(user_query)
    st.success(response)

# Contact Section
st.header("📞 Contact Us")
st.write("Reach out to our cloud specialists for a free consultation.")

contact_form = """
<form action="mailto:info@cloudexpertsguru.com" method="post" enctype="text/plain">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email"><br>
    <label for="message">Message:</label><br>
    <textarea id="message" name="message"></textarea><br>
    <input type="submit" value="Send">
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Contact: +91 7842111055 | Email: <a href="mailto:info@cloudexpertsguru.com" style="color: #4CAF50;">info@cloudexpertsguru.com</a>
    </div>
""", unsafe_allow_html=True)
