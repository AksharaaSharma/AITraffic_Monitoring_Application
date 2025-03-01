import streamlit as st
import base64
from PIL import Image
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="RouteVision AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to add background image with overlay
def add_bg_from_local(image_file, overlay_color="rgba(0, 0, 0, 0.5)"):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient({overlay_color}, {overlay_color}), 
                              url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stButton > button {{
            background-color: rgba(0, 120, 212, 0.8);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
            width: 100%;
            height: 80px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }}
        .stButton > button:hover {{
            background-color: rgba(0, 90, 180, 0.9);
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.3);
            transform: translateY(-2px);
        }}
        .title-container {{
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            animation: fadeIn 1.5s;
        }}
        .button-container {{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 25px;
            margin-top: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: all 0.3s ease;
            animation: slideUp 0.5s;
        }}
        .button-container:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.3);
        }}
        .button-title {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #333;
            text-align: center;
        }}
        .button-description {{
            font-size: 14px;
            color: #555;
            margin-bottom: 15px;
            text-align: center;
        }}
        .button-icon {{
            font-size: 36px;
            margin-bottom: 10px;
            text-align: center;
        }}
        h1, h2, h3 {{
            font-family: 'Helvetica Neue', sans-serif;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .home-button {{
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 999;
        }}
        .home-button button {{
            background-color: rgba(255, 255, 255, 0.9);
            color: #333;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Dictionary to hold background images and their properties
background_images = {
    'home': {
        'path': r"1.jpg",
        'overlay': "rgba(0, 0, 0, 0.4)"
    },
    'traffic_video': {
        'path': r"1.jpg",
        'overlay': "rgba(0, 0, 0, 0.6)"
    },
    'route_optimize_predictor': {
        'path': r"images.png",
        'overlay': "rgba(0, 0, 0, 0.5)"
    },
    'smart_signal': {
        'path': r"photo-1520594923568-1b5d82587f86.jpeg",
        'overlay': "rgba(0, 0, 0, 0.5)"
    }
}

# Set session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Add home button when not on home page
if st.session_state.page != 'home':
    home_button_placeholder = st.empty()
    with home_button_placeholder:
        st.markdown(
            """
            <div class="home-button">
                <button onclick="document.getElementById('home-button-hidden').click()">🏠</button>
            </div>
            """,
            unsafe_allow_html=True
        )
    # Hidden button to trigger the action
    if st.button("Home", key="home-button-hidden", help="Return to homepage"):
        st.session_state.page = 'home'
        
# Add the background image based on the current page
current_page = st.session_state.page
if current_page in background_images:
    page_bg = background_images[current_page]
    add_bg_from_local(page_bg['path'], page_bg['overlay'])

# Logic to navigate to different Python files
if st.session_state.page == 'home':
    # Title and subtitle displayed on the home page with animation
    st.markdown(
        """
        <div class="title-container">
            <h1 style='color: #333; text-align: center; margin-bottom: 10px;'>RouteVision AI</h1>
            <h3 style='color: #555; text-align: center; font-weight: normal;'>Advanced Traffic Monitoring & Optimization Platform</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Add space above buttons
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create horizontal layout with enhanced buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="button-container">
                <div class="button-icon">🎥</div>
                <div class="button-title">Traffic Feed</div>
                <div class="button-description">View real-time traffic cameras and AI-powered analytics</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("EXPLORE TRAFFIC FEED", key="traffic_btn"):
            st.session_state.page = 'traffic_video'
    
    with col2:
        st.markdown(
            """
            <div class="button-container">
                <div class="button-icon">🗺️</div>
                <div class="button-title">Route Optimizer</div>
                <div class="button-description">Find the fastest routes with AI predictive analysis</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("OPTIMIZE ROUTES", key="route_btn"):
            st.session_state.page = 'route_optimize_predictor'
    
    with col3:
        st.markdown(
            """
            <div class="button-container">
                <div class="button-icon">🚦</div>
                <div class="button-title">Signal Simulation</div>
                <div class="button-description">Smart traffic signal control and simulation</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("RUN SIMULATION", key="signal_btn"):
            st.session_state.page = 'smart_signal'
    
    # Footer section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='background-color: rgba(255, 255, 255, 0.7); padding: 15px; border-radius: 10px; position: fixed; bottom: 20px; width: calc(100% - 40px); text-align: center;'>
            <p style='margin: 0; color: #666; font-size: 12px;'>© 2025 RouteVision AI - Transforming Urban Mobility Through Artificial Intelligence</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
else:
    # Simulate the redirection by running the corresponding Python file
    try:
        if st.session_state.page == 'traffic_video':
            exec(open(r"Traffic_Video.py", encoding="utf-8").read())
        elif st.session_state.page == 'route_optimize_predictor':
            exec(open(r"predictive_analysis_route_analysis.py", encoding="utf-8").read())
        elif st.session_state.page == 'smart_signal':
            exec(open(r"SignalSimulation.py", encoding="utf-8").read())
    except Exception as e:
        st.error(f"Error loading page: {e}")
        st.button("Return to Home", on_click=lambda: setattr(st.session_state, 'page', 'home'))
