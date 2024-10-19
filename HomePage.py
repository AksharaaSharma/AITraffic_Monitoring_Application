import streamlit as st
import base64

# Function to add background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Dictionary to hold background images for each page
background_images = {
    'home': r"1.jpg",  # Homepage image
    'traffic_video': r"1.jpg",  # Traffic video image
    'route_optimize_pridictor': r"images.png",  # Route optimizer image
    'smart_signal': r"photo-1520594923568-1b5d82587f86.jpeg",  # Smart signal image
}

# Set session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Add the background image based on the current page
current_page = st.session_state.page
if current_page in background_images:
    add_bg_from_local(background_images[current_page])

# Logic to navigate to different Python files
if st.session_state.page == 'home':
    # Title and subtitle only displayed on the home page
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='color: black;'>RouteVision AI: Traffic Monitoring Application</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add space above buttons
    st.markdown("<br><br><br>", unsafe_allow_html=True)  # Adjust the number of <br> tags for more or less space

    # Custom CSS to center the columns
    st.markdown("""
        <style>
        div[class^="stColumn"] {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """, unsafe_allow_html=True)

    # Create horizontal layout with buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("See Traffic Feed"):
            st.session_state.page = 'traffic_video'

    with col2:
        if st.button("Route Optimizer & Predictor"):
            st.session_state.page = 'route_optimize_predictor'

    with col3:
        if st.button("Traffic Signal Simulation"):
            st.session_state.page = 'smart_signal' 

else:
    # Simulate the redirection by running the corresponding Python file here
    if st.session_state.page == 'traffic_video':
        exec(open(r"Traffic_Video.py", encoding="utf-8").read())
    elif st.session_state.page == 'route_optimize_predictor':
        exec(open(r"predictive_analysis_route_analysis.py", encoding="utf-8").read())  # Update with your route map file path
    elif  st.session_state.page == 'smart_signal':
        exec(open(r"SignalSimulation.py", encoding="utf-8").read())  # Update with your RoadBot AI file path  
