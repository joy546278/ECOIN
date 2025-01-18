import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import  load_model
import streamlit as st
import numpy as np 

st.header('E-Components Resuability')
model = load_model('C:/Users\OMEN\OneDrive\Desktop\Capstone Project(CDV11)\Reusability Of Electronic Components\ECOIN.keras')
data_cat = ['Ceiling Fan',
 'Central Processing Unit(CPU)',
 'Circuit Board',
 'Computer Keyboard',
 'Computer Mouse',
 'Cracked Screen Smartphone',
 'Hard Disk',
 'Headphones',
 'Laptop',
 'Monitor',
 'Smart Watch',
 'Smartphone',
 'Speakers',
 'Washing Machine']
img_height = 180
img_width = 180
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
#image =st.text_input('Enter Image name','img.jpg')

image_load = tf.keras.utils.load_img(image, target_size=(img_height,img_width))
img_arr = tf.keras.utils.array_to_img(image_load)
img_bat=tf.expand_dims(img_arr,0)

predict = model.predict(img_bat)

score = tf.nn.softmax(predict)
st.image(image, width=200)
st.markdown('Electronic Component in image is ' + data_cat[np.argmax(score)])
st.markdown('With accuracy of ' + str(np.max(score)*100))
predicted_category = data_cat[np.argmax(score)]

st.markdown('**Know Your ' +  predicted_category + "'s" + ' Reusability:**')
if predicted_category=="Laptop":
    st.markdown("""
        <p>By reusing and recycling laptops in these ways, we can significantly reduce electronic waste while extending the lifespan of tech components.</p>
        <p>Reusing laptops in different conditions can help extend their lifespan and reduce e-waste. Here's a guide on how to approach reusing laptops based on their functionality</p>
                """, unsafe_allow_html=True)
elif predicted_category == 'Smartphone':
    st.markdown("""
        <p>By reusing smartphones in these various ways, you can help reduce electronic waste, extend the life of useful components, and contribute to sustainability efforts.</p>
        <p>Reusing smartphones in different conditions can also help reduce e-waste and make the most of their usable parts. Here’s how you can approach reusing smartphones based on their functionality</p>
             """, unsafe_allow_html=True)
elif predicted_category == 'Computer Keyboard':
    st.markdown("""
        <p>Reusing a "Computer Keyboard" in different conditions requires creative approaches, tailored to whether the keyboard is partially functioning, fully functioning, or non-functioning (disposable).</p>
             """, unsafe_allow_html=True)
elif predicted_category == 'Computer Mouse':
    st.markdown("""
    <p>By reusing or recycling computer mouce in these ways, you can reduce e-waste and make sure that even the smallest components are put to good use, extending their value and functionality.</p>
    <p>Reusing computer mouce, like other electronic devices, depends on their functionality. Below are strategies for reusing or recycling computer mice in different conditions</p>
    <h2>General Tips for All Mouse Conditions:</h2>
    <ul>
        <li><strong>Proper Cleaning:</strong> Before reusing or donating, clean the mouse thoroughly. Use a microfiber cloth to remove dust and grime, and clean the optical sensor and scroll wheel to ensure better functionality.</li>
        <li><strong>Donating to Schools or Charities:</strong> Even older or partially working mice can be donated to schools, charities, or organizations that accept tech donations. They can still be useful for basic computing tasks</li>
        <li><strong>Look for E-Waste Programs:</strong> Many electronics stores and recycling centers offer programs to recycle old or broken computer accessories. These programs ensure safe disposal and may help recover valuable materials.</li>
    </ul>       
                """, unsafe_allow_html=True)
elif predicted_category == 'Cracked Screen Smartphone':
    st.markdown("""
        <p>By reusing smartphones in these various ways, you can help reduce electronic waste, extend the life of useful components, and contribute to sustainability efforts.</p>
        <p>Reusing smartphones in different conditions can also help reduce e-waste and make the most of their usable parts. Here’s how you can approach reusing smartphones based on their functionality</p>
             """, unsafe_allow_html=True)
elif predicted_category == 'Speakers':
    st.markdown("""
        <p>Reusing speakers in different conditions (partial functioning, fully functioning, and no functioning/disposable) opens up various possibilities. Whether you are looking to repair, repurpose, or recycle,</p>
    """, unsafe_allow_html=True)
elif predicted_category == 'Monitor':
    st.markdown("""
        <p>Reusing a computer monitor in the three conditions (partial functioning, fully functioning, and no functioning/disposable) can involve a range of creative, practical, and environmental approaches.</p>
    """, unsafe_allow_html=True)
elif predicted_category == 'Smart Watch':
    st.markdown("""
            <p>Reusing a smartwatch in different conditions (partial functioning, fully functioning, and no functioning/disposable) presents a variety of creative, practical, and sustainable options.</p>
        """, unsafe_allow_html=True)
elif predicted_category == 'Washing Machine':
    st.markdown("""
    <p>Reusing or repurposing a washing machine in different conditions (partial functioning, fully functioning, or no functioning/disposable) offers a variety of creative, practical, and eco-friendly options.</p>
    <p>By reusing, recycling, or repurposing a washing machine, whether it's partially functional or completely non-functional, you can reduce waste, conserve resources, and give the appliance a second life in a new form.</p>
    """, unsafe_allow_html=True)
elif predicted_category == 'Ceiling Fan':
    st.markdown("""
        <p>Reusing ceiling fans in different conditions (partial functioning, fully functioning, or non-functioning) also presents a variety of practical, creative, and environmentally responsible options.</p>
        <p>By repurposing the fan's motor, blades, or other components, you can reduce waste and make creative use of what would otherwise be a discarded item. Even a non-functioning ceiling fan can have a second life in many forms!</p>
    """, unsafe_allow_html=True)
elif predicted_category == 'Circuit Board':
    st.markdown("""
    <p>Reusing circuit boards (PCBs), whether they are partially functional, fully functional, or no longer functioning, offers numerous opportunities for recycling, repurposing, or upcycling.</p>
    <p>By reusing, recycling, or repurposing circuit boards (PCBs), you can contribute to reducing electronic waste while getting creative with DIY projects, education, and innovation. Even if the board is no longer working as intended, there are many ways to give it a second life.</p>
    """, unsafe_allow_html=True)
elif predicted_category == 'Headphones':
    st.markdown("""
        <p>Reusing headphones in different conditions (partial functioning, fully functioning, or no functioning/disposable) presents several practical, creative, and environmentally friendly options.</p>
    """)
elif predicted_category == 'Central Processing Unit(CPU)':
    st.markdown('Message for Smartphone with Option B: Example B')
elif predicted_category == 'Feature Phone(Keypad)':
    st.markdown("""
        <p>Reusing a feature phone (keypad phone) in different conditions (partial functioning, fully functioning, or no functioning/disposable) can be done in several creative, practical, and eco-friendly ways.</p>
    """, unsafe_allow_html=True)

option = st.radio(
        "Select the condition of the " + predicted_category,
        ("Partially Functioning", "Fully Functioning", "No Functioning (Disposable)"), 
    )

    
if option=="Partially Functioning":
    if predicted_category == 'Laptop':
        st.markdown("""
        <h2>Partially Functioning Laptops</h2>
            <p>These laptops may have some issues, such as a malfunctioning hard drive, broken screen, or faulty keyboard, but they still have functional components that can be repurposed.</p>
    
        <h3>Reuse Strategies:</h3>
    
        <h4>1. Repair and Restore:</h4>
        <ul>
            <li><strong>Hardware:</strong> Replace faulty components like the hard drive, battery, or screen.</li>
            <li><strong>Software:</strong> Install a lightweight operating system (e.g., Linux) if the original OS has performance issues.</li>
            <li><strong>Upgrade:</strong> Add more RAM or install an SSD to improve speed and functionality.</li>
        </ul>
    
        <h4>2. Repurpose for Specific Tasks:</h4>
        <ul>
            <li><strong>Media Center:</strong> Use it as a media server or streaming device.</li>
            <li><strong>Learning Tool:</strong> Give it to students or beginners who need a laptop for basic tasks (web browsing, word processing, etc.).</li>
            <li><strong>Secondary Device:<   /strong> Use it as a second laptop for specific tasks like coding, design, or office work.</li>
        </ul>
    
        <h4>3. Donate or Sell:</h4>
        <p>If you can repair it at a reasonable cost, consider donating or selling it to those who need it but can't afford a new laptop.</p>
        """, unsafe_allow_html=True)
    elif predicted_category == 'Smartphone':
        st.markdown("""
        <h3>Partially Functioning Smartphones</h3>
            <p>These phones may have minor issues like cracked screens, low battery life, or software problems but are still mostly usable.</p>
        
        <h4>Reuse Strategies:</h4>
        
        <h5>Repair and Restore:</h5>
            <ul>
                <li><strong>Screen Replacement:</strong> Replace a cracked screen if the rest of the phone is working fine.</li>
                <li><strong>Battery Replacement:</strong> If the battery is draining quickly, consider replacing it with a new one to extend the phone's life.</li>
                <li><strong>Software Optimization:</strong> Install a lightweight operating system or reset the phone to factory settings to fix software issues.</li>
            </ul>
        
        <h5>Repurpose for Specific Uses:</h5>
            <ul>
                <li><strong>Media Player or Streaming Device:</strong> Use it as a music player, podcast device, or a media streamer for watching videos.</li>
                <li><strong>Security Camera:</strong> Turn the phone into a security camera or baby monitor with apps designed for surveillance.</li>
                <li><strong>Remote Control Hub:</strong> Use it as a universal remote for smart home devices.</li>
                <li><strong>Backup Phone:</strong> Keep it as a backup phone in case your main phone is lost or damaged.</li>
            </ul>
        
        <h5>Donate or Sell:</h5>
        <p>After repairing it, donate it to people who need a basic phone, or sell it as a low-cost option to someone who needs it for basic use.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Computer Keyboard':
        st.markdown("""
    <h3>Partial Functioning Keyboard</h3>
    <p>If only some keys or features are working, you can still repurpose the keyboard in various ways:</p>

    <h4>Reassign Functioning Keys:</h4>
    <p>Use software to remap functioning keys to specific tasks, making the keyboard functional for a particular need. For example, use a remapping tool to reassign unused keys for shortcuts or custom functions.</p>

    <h4>Create a Custom Control Interface:</h4>
    <p>If only a few keys are working, repurpose the working ones to create a control interface for specific tasks (e.g., for gaming or video editing shortcuts).</p>

    <h4>Use as a Special Input Device:</h4>
    <p>Repurpose the functioning keys as triggers for automation, where each key could trigger a specific action, e.g., controlling a smart home device or triggering certain software functions.</p>

    <h4>DIY Projects (Arduino/ESP32 Integration):</h4>
    <p>If you have a partial working keyboard, you could use it in a DIY project with Arduino or similar microcontrollers. Some parts of the keyboard can be stripped and connected to external circuits for custom control purposes.</p>

    <h4>Parts for Other Projects:</h4>
    <p>Even if only parts of the keyboard are functional, the individual components like the keys, key switches, and even the wiring can be reused in other DIY electronics projects, like custom keypads or sensors.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Computer Mouse':
        st.markdown("""
        <h3>Partially Functioning Computer Mice</h3>
        <p>These mice may have issues such as a broken scroll wheel, faulty buttons, or intermittent connectivity, but they still work to some extent.</p>
        
        <h4>Reuse Strategies:</h4>
        
        <h5>Repair and Restore:</h5>
        <ul>
            <li><strong>Fix the Scroll Wheel:</strong> If the scroll wheel is stuck or malfunctioning, you can try cleaning or repairing it by disassembling the mouse and fixing the wheel mechanism.</li>
            <li><strong>Button Repair:</strong> If the buttons are not responsive, check if the contacts are dirty or broken, and clean or replace them. Sometimes re-soldering or adjusting the internal switches can help.</li>
            <li><strong>Replace Cable:</strong> If the cable is frayed or damaged, you can replace it if you're comfortable with basic wiring, or use a wireless adapter if it’s a wired mouse.</li>
        </ul>
        
        <h5>Repurpose for Specific Uses:</h5>
        <ul>
            <li><strong>Backup or Secondary Mouse:</strong> Use it as a secondary or backup mouse for when your main mouse is unavailable or during travel.</li>
            <li><strong>Use for Other Devices:</strong> Repurpose the mouse for use with different devices, like a Raspberry Pi, smart TV, or gaming console (if compatible).</li>
            <li><strong>Test Mouse for Repairs:</strong> Use the partially working mouse to test computer or software repairs if you're a technician or hobbyist.</li>
        </ul>
        
        <h5>Donate or Sell:</h5>
        <p>After fixing it, you can donate it to a school, office, or community center, or sell it as a budget-friendly option for someone who needs it but doesn't mind a slight issue.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Cracked Screen Smartphone':
        st.markdown("""
        <h3>Partially Functioning Smartphones</h3>
            <p>These phones may have minor issues like cracked screens, low battery life, or software problems but are still mostly usable.</p>
        
        <h4>Reuse Strategies:</h4>
        
        <h5>Repair and Restore:</h5>
            <ul>
                <li><strong>Screen Replacement:</strong> Replace a cracked screen if the rest of the phone is working fine.</li>
                <li><strong>Battery Replacement:</strong> If the battery is draining quickly, consider replacing it with a new one to extend the phone's life.</li>
                <li><strong>Software Optimization:</strong> Install a lightweight operating system or reset the phone to factory settings to fix software issues.</li>
            </ul>
        
        <h5>Repurpose for Specific Uses:</h5>
            <ul>
                <li><strong>Media Player or Streaming Device:</strong> Use it as a music player, podcast device, or a media streamer for watching videos.</li>
                <li><strong>Security Camera:</strong> Turn the phone into a security camera or baby monitor with apps designed for surveillance.</li>
                <li><strong>Remote Control Hub:</strong> Use it as a universal remote for smart home devices.</li>
                <li><strong>Backup Phone:</strong> Keep it as a backup phone in case your main phone is lost or damaged.</li>
            </ul>
        
        <h5>Donate or Sell:</h5>
        <p>After repairing it, donate it to people who need a basic phone, or sell it as a low-cost option to someone who needs it for basic use.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Speakers':
        st.markdown("""
    <h3>Partial Functioning Speakers</h3>
    <p>If the speakers are partially working (e.g., distorted sound, low volume, one speaker works but not the other, etc.), there are still ways to repurpose them creatively or fix them:</p>

    <h4>Use for Smaller, Specific Tasks:</h4>
    <p>Even if the speakers are not functioning at full capacity, you can repurpose them for less critical tasks such as background music or sound notifications. For instance, they can be used in home automation or smart home projects for alerts or simple sound effects.</p>

    <h4>Create a Multi-Speaker Setup:</h4>
    <p>If one speaker works while the other doesn't, you can combine the functioning speaker with another speaker (from a different set or new) to create a basic stereo or multi-speaker system, though the audio quality may be compromised.</p>

    <h4>DIY Audio Projects:</h4>
    <p>Use the partially working speakers in DIY projects such as a simple Bluetooth speaker, a low-budget sound system for a workshop, or as part of an audio-based project for a Raspberry Pi or Arduino.</p>

    <h4>Sound Alerts for Automation:</h4>
    <p>Repurpose the speakers as part of an alert system in an automation setup. For instance, it can beep or play sound effects when specific conditions are met (temperature changes, motion detection, etc.).</p>

    <h4>Repurpose Parts:</h4>
    <p>The individual components of the speakers (driver, casing, wiring) can be used for other projects. For example, you can extract the speakers’ magnets or use the casing to house other small electronic components.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Monitor':
        st.markdown("""
    <h3>Partial Functioning Monitor</h3>
    
    <p>If the monitor is partially functioning (e.g., some pixels are dead, it has screen flickering, or the display is dimming), it can still be repurposed in various ways:</p>
    
    <h4>Repurpose as Secondary Monitor:</h4>
    
    <p>A partially functioning monitor can still serve as a secondary or auxiliary display for less critical tasks. Even if there are dead pixels or areas with issues, you can use it for displaying notifications, email, or chat windows.</p>
    
    <h4>Repurpose as a Digital Picture Frame:</h4>
    
    <p>A partially functioning monitor can be used as a digital photo frame, playing a slideshow of pictures or artwork. The damaged areas may be less noticeable when the screen displays images with less detail.</p>
    
    <h4>Use for Specific Tasks:</h4>
    
    <p>You can repurpose the monitor for specific tasks that don't require perfect display quality, such as using it for a dedicated server console, monitoring system logs, or displaying non-critical information like weather updates, stock tickers, or a calendar.</p>
    
    <h4>DIY Projects (Smart Mirror, Dashboard, etc.):</h4>
    
    <p>A partially working screen can be incorporated into a smart mirror project, where the display is behind a reflective surface, or as a part of a custom information dashboard, providing real-time data (e.g., home automation controls, IoT sensor data, etc.).</p>
    
    <h4>External Display for Embedded Systems:</h4>
    
    <p>Use the monitor for projects involving Raspberry Pi, Arduino, or other embedded systems, where visual quality isn't critical for the application. This could include things like surveillance displays or simple data dashboards.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Smart Watch':
        st.markdown("""
    <h3>Partial Functioning Smartwatch</h3>
    <p>If your smartwatch is partially working (e.g., certain functions like heart rate tracking or notifications work, but the display is dim, the battery is weak, or there’s a software issue), it can still be repurposed in several ways:</p>

    <h4>Use for Limited Functionality:</h4>
    <p>Even if some features are malfunctioning, the smartwatch can still be used for basic functions such as checking the time, setting alarms, or simple fitness tracking (step counting, distance tracking, etc.).</p>

    <h4>DIY Projects:</h4>
    <p><strong>Sensors for Other Devices:</strong> If the health tracking functions are still working (e.g., heart rate, step counter), you can repurpose the sensors into DIY projects. For instance, integrating the heart rate monitor into another wearable or using it for a custom fitness device.</p>
    <p><strong>Smart Home Control:</strong> You could repurpose the smartwatch to control other smart devices, such as using it to adjust lighting or the thermostat, or to trigger home automation tasks via Bluetooth or Wi-Fi.</p>

    <h4>Create a Custom Fitness Device:</h4>
    <p>A smartwatch with limited functioning can still track basic metrics like steps, distance, and calories. Repurpose it into a dedicated fitness or health tracker for basic exercise or daily activity monitoring.</p>

    <h4>Use as a Standalone Timer or Stopwatch:</h4>
    <p>Even if other features are faulty, you could use the smartwatch simply as a timer or stopwatch for various tasks like cooking, working out, or time tracking in projects.</p>

    <h4>Use as a Fashionable Accessory:</h4>
    <p>If the display or some features are broken, you could remove the smartwatch's main components (screen, case, etc.) and use the casing as a unique fashion accessory, or even as a decorative pendant or keychain.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Washing Machine':
        st.markdown("""
    <h3>Partial Functioning Washing Machine</h3>
    <p>If your washing machine is partially working (e.g., it washes clothes but doesn’t spin properly, the water drainage is slow, or it has a broken setting), there are still several ways to repurpose or continue using it:</p>

    <h4>Use for Specific Laundry Functions:</h4>
    <p>If the washing machine still works for certain cycles, you can use it for specific laundry tasks. For example, use it to wash clothes on basic settings or for laundry that doesn't require spinning or high-level washing.</p>
    <p><strong>Manual Drying:</strong> If the spin cycle is broken, you can manually wring out the clothes or use a clothesline to dry them.</p>

    <h4>Repurpose for Non-Laundry Tasks:</h4>
    <p><strong>Storage:</strong> A partially functioning washing machine can serve as a large storage unit. The drum of the washing machine can be used to store tools, sports equipment, or other bulky items.</p>
    <p><strong>Composting:</strong> You could repurpose the washing machine drum as a composting bin. The mesh-like drum is perfect for creating airflow in compost piles, helping to speed up the decomposition process.</p>

    <h4>DIY Projects:</h4>
    <p><strong>Garden Planter:</strong> The metal drum of the washing machine can be turned into a garden planter. Its cylindrical shape is perfect for planting flowers, herbs, or even small shrubs.</p>
    <p><strong>Creative Furniture or Art:</strong> You can use the washing machine drum or other parts of the machine to create unique furniture or art pieces. For instance, it can be turned into a modern, industrial-style coffee table or a decorative light fixture.</p>

    <h4>Upcycle for Farm or Garden Use:</h4>
    <p><strong>Animal Feeder or Waterer:</strong> The drum or parts of the washing machine can be repurposed as a feeder or watering station for small animals (e.g., chickens, rabbits).</p>
    <p><strong>Rainwater Collection:</strong> You can modify the washing machine to be part of a rainwater harvesting system by using its drum as a large collection vessel.</p>

    <h4>Use for Heavy Duty Cleaning:</h4>
    <p>If the washing machine's cycle functions but is not ideal for delicate clothes, you can use it for heavy-duty cleaning of non-clothing items, such as cleaning mats, rags, and other fabric-based items.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Ceiling Fan':
        st.markdown("""
    <h3>Partial Functioning Ceiling Fans</h3>
    <p>If the ceiling fan is partially working (e.g., it wobbles, doesn't spin at full speed, or has issues with the light feature), you can still make use of the components or repurpose the fan for different purposes:</p>

    <h4>Repurpose for DIY Projects:</h4>
    <p><strong>Fan Motor:</strong> If the motor still works, it can be used in DIY projects like small wind turbines, custom ventilation systems, or even homemade air circulators.</p>
    <p><strong>Fan Blades:</strong> The fan blades can be removed and used for arts and crafts. For example, you could turn them into a wall decoration, a garden trellis, or even as part of a larger sculpture.</p>

    <h4>Use in Smaller Spaces:</h4>
    <p>If the fan doesn’t work well in large spaces, it can be used in smaller areas like a kitchen, bathroom, or garage where full performance isn’t necessary. Even a partially functioning fan can still provide some air circulation.</p>

    <h4>Install a New Motor:</h4>
    <p>If the motor is partially broken, you can potentially replace it to restore the fan's functionality. This is an option if you have basic electrical knowledge or are willing to hire a professional.</p>

    <h4>Create a Custom Ventilation System:</h4>
    <p>Use the motor and blades to create a small ventilation system, especially for areas like attics, crawl spaces, or workshops where airflow is important but full functionality isn’t required.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Circuit Board':
        st.markdown("""
    <h2>Partial Functioning</h2>
    <p><strong>Repurpose Components:</strong> If the circuit board is partially functioning, it may still have valuable components that can be salvaged and reused. For example:</p>
    <ul>
        <li><strong>Capacitors, Resistors, Transistors:</strong> Components that are still working can be extracted and used in other projects or repairs.</li>
        <li><strong>Integrated Circuits (ICs):</strong> These can be desoldered and reused in new designs, provided they are intact and not damaged.</li>
        <li><strong>Connectors and Switches:</strong> These parts are often reusable if they are still functioning correctly.</li>
    </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Headphones':
        st.markdown("""
    <h3>Partial Functioning Headphones</h3>
    <p>If your headphones are partially working (e.g., one earbud or side isn't functioning, audio quality is poor, or there is intermittent connectivity), you can still repurpose them in various ways:</p>

    <h4>Use for Specific Tasks:</h4>
    <p>Even if only one earbud works, you can still use the functional earbud for tasks like listening to podcasts, audiobooks, or audio notifications. Alternatively, you could use the one working side for a basic hands-free experience when making calls.</p>

    <h4>DIY Projects:</h4>
    <p><strong>Custom Bluetooth Headset:</strong> If the wired headphones are partially functional, you can repurpose them into a custom Bluetooth headset by adding a Bluetooth transmitter/receiver module.</p>
    <p><strong>Modified Headphones:</strong> If one side of the headphones still works, you can strip the functional components and integrate them into a new housing, potentially creating a custom audio device.</p>

    <h4>Repurpose as a Backup:</h4>
    <p>Use the partially functioning headphones as a backup pair for low-priority tasks like quick calls, casual listening, or as an emergency set when your main headphones are unavailable.</p>

    <h4>Use for Audio Alerts or Notifications:</h4>
    <p>You can repurpose the headphones for specific audio alerts in projects. For example, they can serve as a notification system for a smart home setup or a DIY alarm system.</p>

    <h4>Repurpose the Cables:</h4>
    <p>Even if the audio isn't working, the cables can be repurposed for other DIY projects. They are useful for crafting, electrical projects, or as spare wiring for other devices.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Central Processing Unit(CPU)':
        st.markdown('Message for Smartphone with Option B: Example B')
    elif predicted_category == 'Feature Phone(Keypad)':
        st.markdown("""
    <h3>Partial Functioning Feature Phone</h3>
    <p>If your feature phone is partially working (e.g., the screen flickers, the keypad is malfunctioning, or there’s poor signal reception), there are still several ways to repurpose it:</p>

    <h4>Use as a Backup Phone:</h4>
    <p>Even with partial functionality, a feature phone can be kept as a backup in case your main phone is lost, damaged, or out of battery. It’s useful for basic tasks like making calls or sending SMS.</p>

    <h4>Emergency Phone:</h4>
    <p>You can dedicate the feature phone as an emergency phone. Keep it charged and stored in your car, emergency kit, or at home for use during power outages, travel, or in situations where you only need basic communication.</p>

    <h4>Dedicated SMS or Voice-only Phone:</h4>
    <p>If the phone’s display is not functioning fully, but the keypad works, you can repurpose it for making and receiving voice calls or text messages only. It can serve as a simpler device for minimal distractions.</p>

    <h4>Repurpose for Specific Tasks:</h4>
    <p>Use the phone for tasks like monitoring your home (if it has basic camera functionality), as a remote control for other devices, or a dedicated GPS device for specific tasks.</p>

    <h4>DIY Projects:</h4>
    <p><strong>Keypad for Custom Devices:</strong> The keypad and buttons of the phone could be repurposed for DIY electronics or interactive projects. You can integrate it into custom alarm systems, control panels, or even build a simple calculator using the keypad.</p>
    <p><strong>Phone Speaker:</strong> The phone's built-in speaker can be repurposed for small sound projects or audio setups.</p>

    <h4>Personalized Communication Device:</h4>
    <p>Turn the partially working phone into a personal device for specific family members or elderly relatives who only need basic functions like calling and texting.</p>
    """, unsafe_allow_html=True)
    else:
        st.markdown('Message for selected category with Option A')

if option=="Fully Functioning":
    if predicted_category == 'Laptop':
        st.markdown("""
        <h2>Fully Functioning Laptops</h2>
            <p>These laptops are in good condition and can be reused easily for a variety of tasks.</p>
    
        <h3>Reuse Strategies:</h3>
    
        <h4>1. Repurpose for New Uses:</h4>
        <ul>
            <li><strong>Workstation:</strong> Set up the laptop as a dedicated work machine for specific tasks such as remote work, programming, or data analysis.</li>
            <li><strong>Media Hub or Server:</strong> Use it as a personal media server to stream content to other devices.</li>
            <li><strong>Portable Learning Center:</strong> Reinstall the operating system and distribute it to students or local community centers for educational purposes.</li>
        </ul>
    
        <h4>2. Upgrade and Resell:</h4>
        <ul>
            <li><strong>Upgrade Hardware:</strong> If needed, you could upgrade the RAM, storage, or battery to improve performance.</li>
            <li><strong>Sell or Donate:</strong> Resell it or donate it to charities, schools, or non-profit organizations that accept tech donations.</li>
        </ul>
        """, unsafe_allow_html=True)
    elif predicted_category == 'Smartphone':
        st.markdown("""
            <h3>Fully Functioning Smartphones</h3>
                <p>These phones are in good condition and can easily be reused or repurposed for various tasks.</p>
        
            <h4>Reuse Strategies:</h4>
        
            <h5>Repurpose for New Uses:</h5>
            <ul>
                <li><strong>Dedicated Work Device:</strong> Use it for specific tasks such as a personal assistant, GPS navigation system, or business communications.</li>
                <li><strong>Smart Home Controller:</strong> Use it as a hub for controlling IoT (Internet of Things) devices in your home (e.g., smart lights, security systems).</li>
                <li><strong>Learning Tool for Kids:</strong> If it’s still in good working order, give it to children as an educational device or for entertainment purposes.</li>
            </ul>
        
            <h5>Upgrade and Resell:</h5>
            <ul>
                <li><strong>Upgrade Storage or Accessories:</strong> In some cases, upgrading accessories like a new case or a power bank can enhance the phone's functionality.</li>
                <li><strong>Sell or Donate:</strong> If the phone is relatively new and still working well, you can resell it or donate it to organizations that accept used devices, such as schools or charity groups.</li>
            </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Computer Keyboard':
        st.markdown('Message for Smartphone with Option B: Example B')
    elif predicted_category == 'Computer Mouse':
        st.markdown("""
        <h3>Fully Functioning Computer Mice</h3>
        <p>These mice are in good condition and can be reused for a variety of tasks without requiring repairs.</p>
        
        <h4>Reuse Strategies:</h4>
        
        <h5>Repurpose for New Uses:</h5>
        <ul>
            <li><strong>Multiple Workstations:</strong> Use the mouse at different workstations or with multiple computers or laptops.</li>
            <li><strong>Set Up as a Dedicated Mouse for Specific Tasks:</strong> You can use it with a specific device like a home theater PC, a secondary computer, or a remote server.</li>
            <li><strong>Gaming Mouse:</strong> If it’s a high-performance mouse, consider repurposing it for gaming, or use it for specialized tasks like 3D modeling or video editing.</li>
            <li><strong>Use for Special Needs:</strong> Some people with disabilities may benefit from a specific type of mouse (e.g., ergonomic or larger buttons). Donate your functioning mouse to them if appropriate.</li>
        </ul>
        
        <h5>Upgrade and Resell:</h5>
        <ul>
            <li><strong>Keep It as a Backup:</strong> Even if you have a newer or fancier mouse, keep the functioning one as a backup, or for travel purposes.</li>
            <li><strong>Sell or Donate:</strong> If it’s still in good condition, sell it or donate it to those in need (e.g., schools, libraries, or non-profit organizations).</li>
        </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Cracked Screen Smartphone':
        st.markdown("""
            <h3>Fully Functioning Smartphones</h3>
                <p>These phones are in good condition and can easily be reused or repurposed for various tasks.</p>
        
            <h4>Reuse Strategies:</h4>
        
            <h5>Repurpose for New Uses:</h5>
            <ul>
                <li><strong>Dedicated Work Device:</strong> Use it for specific tasks such as a personal assistant, GPS navigation system, or business communications.</li>
                <li><strong>Smart Home Controller:</strong> Use it as a hub for controlling IoT (Internet of Things) devices in your home (e.g., smart lights, security systems).</li>
                <li><strong>Learning Tool for Kids:</strong> If it’s still in good working order, give it to children as an educational device or for entertainment purposes.</li>
            </ul>
        
            <h5>Upgrade and Resell:</h5>
            <ul>
                <li><strong>Upgrade Storage or Accessories:</strong> In some cases, upgrading accessories like a new case or a power bank can enhance the phone's functionality.</li>
                <li><strong>Sell or Donate:</strong> If the phone is relatively new and still working well, you can resell it or donate it to organizations that accept used devices, such as schools or charity groups.</li>
            </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Speakers':
        st.markdown("""
    <h3>Fully Functioning Speakers</h3>
    <p>Fully functioning speakers are ideal for a variety of reuse options and are most versatile. Here are ways to repurpose or utilize them:</p>

    <h4>Home Audio System:</h4>
    <p>Use them as part of your home audio setup for music, TV sound, or theater system. You can add them to an existing setup for enhanced sound quality or expand a multi-room audio system.</p>

    <h4>Portable Bluetooth Speaker:</h4>
    <p>Turn the speakers into a portable Bluetooth speaker by integrating a Bluetooth receiver. This allows the speakers to work wirelessly with your phone, tablet, or other Bluetooth-enabled devices, offering flexibility and mobility.</p>

    <h4>Upgrade Your Computer or TV Sound System:</h4>
    <p>If you're not satisfied with your computer or TV sound, use the fully functioning speakers to upgrade your audio experience. They can provide higher quality audio for media consumption, gaming, or video conferencing.</p>

    <h4>Donate or Resell:</h4>
    <p>If you have no use for the speakers, you can donate them to schools, libraries, or local charities. Alternatively, you can sell them online or to second-hand stores to benefit someone else who needs quality audio equipment.</p>

    <h4>Sound System for Outdoor or Workshop Use:</h4>
    <p>Fully functioning speakers can be used in a workshop, garage, or patio setup to play music, podcasts, or instructions while you work or relax. They can be easily connected to a smartphone or computer for easy access to your favorite media.</p>

    <h4>Audio Systems for Events or Parties:</h4>
    <p>Fully functioning speakers can be used at events, parties, or gatherings, offering amplified sound for music, speeches, or presentations. They can be paired with a microphone or other audio equipment for live events.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Monitor':
        st.markdown("""
    <h3>Fully Functioning Monitor</h3>
    
    <p>If the monitor is fully operational, there are a number of ways to reuse it effectively:</p>
    
    <h4>Multi-Monitor Setup:</h4>
    
    <p>If you don’t need a second monitor but have a spare, you can use it to set up a multi-monitor workstation. This can be particularly useful for productivity tasks (e.g., video editing, coding, or managing multiple applications at once).</p>
    
    <h4>Gaming or Entertainment Station:</h4>
    
    <p>Use it for gaming, video streaming, or as an entertainment display. It could serve as a dedicated screen for watching movies, playing games, or browsing multimedia content in a living room or entertainment setup.</p>
    
    <h4>Donate or Sell:</h4>
    
    <p>If the monitor is still in good working condition but no longer needed, you can donate it to educational institutions, non-profits, or individuals who may benefit from it. Alternatively, you can sell it online or at a second-hand store.</p>
    
    <h4>Repurpose for Smart Home Displays:</h4>
    
    <p>Transform it into a smart home hub for displaying information like security camera feeds, weather updates, home automation controls, or notifications. It could serve as a central control unit for a smart home system.</p>
    
    <h4>Create a Home Office Setup:</h4>
    
    <p>Set up the monitor as part of a home office for work or study. It can be connected to a laptop or desktop to provide extra screen real estate, improving productivity.</p>
    
    <h4>Use for Educational Purposes:</h4>
    
    <p>It can be used in classrooms or workshops for educational displays, project presentations, or interactive learning environments, such as digital whiteboards or student computer terminals.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Smart Watch':
        st.markdown("""
    <h3>Fully Functioning Smartwatch</h3>
    <p>If the smartwatch is fully functional, you have many options for reuse and repurposing that take advantage of its full capabilities:</p>

    <h4>Wear it for Fitness Tracking:</h4>
    <p>Continue using the smartwatch as intended, for fitness monitoring, step counting, sleep tracking, heart rate monitoring, and GPS tracking for outdoor activities. Many people use smartwatches to track daily activity, workouts, and health metrics.</p>

    <h4>Smart Notifications and Productivity:</h4>
    <p>Use it to receive notifications for emails, texts, social media, calendar alerts, and other apps directly on your wrist. You can keep it connected to your phone for enhanced productivity, such as quick replies, voice commands, or managing tasks.</p>

    <h4>Use as a Health Monitoring Device:</h4>
    <p>A fully functioning smartwatch can be used for monitoring health parameters, especially if it offers features like ECG, blood oxygen saturation, or stress monitoring. It can be useful for people who are looking to track their health or use it for medical purposes under certain conditions.</p>

    <h4>Control Smart Home Devices:</h4>
    <p>Use the smartwatch to control smart home gadgets like lights, thermostats, and security cameras. Many modern smartwatches can integrate with home automation systems, allowing you to control devices from your wrist.</p>

    <h4>Use for GPS and Navigation:</h4>
    <p>Utilize the GPS functionality for navigation, especially while walking or cycling. Smartwatches can provide turn-by-turn directions, making it easier to navigate without having to pull out a phone.</p>

    <h4>Donate or Sell:</h4>
    <p>If you have a fully functioning smartwatch that you no longer need, you can donate it to someone who could benefit from it (like a family member or friend), or you could sell it online through platforms like eBay or trade-in services.</p>

    <h4>Smartwatch as a Remote for Other Devices:</h4>
    <p>Many smartwatches can be used as remotes for controlling other devices, such as cameras, TVs, music players, and even drones. This can provide a convenient and hands-free way to manage entertainment or gadgets.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Washing Machine':
        st.markdown("""
    <h3>Fully Functioning Washing Machine</h3>
    <p>If the washing machine is fully functional, you can continue to use it for its intended purpose or find additional ways to maximize its potential:</p>

    <h4>Regular Laundry Use:</h4>
    <p>The primary use for a fully functioning washing machine is, of course, for laundry. You can wash clothes, linens, blankets, and other fabric items efficiently.</p>

    <h4>Energy-Efficient Laundry System:</h4>
    <p>If your washing machine is energy-efficient, it can be integrated into a broader system of sustainable practices. You can pair it with energy-saving settings, such as using cold water washes to save on electricity.</p>

    <h4>DIY Projects:</h4>
    <p><strong>Upcycle Parts for Art and Crafts:</strong> You can repurpose certain parts of the washing machine, such as the drum, motor, and other components, into creative art projects or functional tools.</p>
    <p><strong>Drum as Furniture:</strong> A fully functioning or disassembled washing machine drum can be repurposed into a chair, stool, or even a fire pit.</p>

    <h4>Community Sharing or Donation:</h4>
    <p>If you no longer need the washing machine, consider donating it to someone in need, or to a charity, school, or community center. A fully functional washing machine can be a valuable asset to families or organizations that are lacking this basic appliance.</p>

    <h4>Mobile Laundry Services:</h4>
    <p>A fully functioning washing machine can be repurposed into a mobile laundry unit for those who offer laundry services on the go, such as in places with limited access to laundry facilities (e.g., campers, RV parks, or rural areas).</p>

    <h4>Laundry for Small Business:</h4>
    <p>If you run a small business (e.g., Airbnb rentals, bed and breakfasts, or a daycare), a fully functioning washing machine can be part of your operational setup for washing linens, towels, and other items in bulk.</p>

    <h4>Sell or Trade-In:</h4>
    <p>If you're upgrading or no longer need your fully functioning washing machine, you can sell it online, trade it in for a newer model, or take advantage of recycling programs offered by some manufacturers.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Ceiling Fan':
        st.markdown("""
    <h3>Fully Functioning Ceiling Fans</h3>
    <p>Fully functioning ceiling fans are in their best condition for practical reuse and even creative repurposing. Here are ways you can make the most of them:</p>

    <h4>Upgrade Home Comfort:</h4>
    <p><strong>Install in New Rooms:</strong> If you’re upgrading or changing rooms, you can easily install the fully functioning fan in another room to improve airflow and comfort. Ceiling fans are especially useful in living rooms, bedrooms, and offices.</p>

    <h4>Outdoor Use:</h4>
    <p>If the fan is designed for indoor use, consider installing it on a covered porch or patio. Many ceiling fans are suitable for outdoor areas, enhancing ventilation and comfort during warm weather.</p>

    <h4>Energy-Efficient Cooling:</h4>
    <p>Ceiling fans help reduce the need for air conditioning by circulating air effectively. You can install a fully functioning fan to reduce energy consumption in your home, saving on electricity bills.</p>

    <h4>Modernization with Smart Features:</h4>
    <p>Upgrade a fully functioning fan with smart technology. You can add a smart switch or smart fan controller to control the fan speed and light through an app or voice commands (e.g., with Alexa or Google Assistant).</p>

    <h4>Donate or Sell:</h4>
    <p>If you have a fully functioning ceiling fan but no longer need it, donate it to a local charity, community center, or thrift store. Alternatively, you can sell it online, providing someone else with a good quality fan.</p>

    <h4>Install as Part of a Home Renovation:</h4>
    <p>If you’re renovating your home, a ceiling fan can be a stylish addition to a living room, dining area, or bedroom. Modern ceiling fans can fit seamlessly into both traditional and contemporary home designs.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Circuit Board':
        st.markdown("""
    <h2>Fully Functioning</h2>
    <p><strong>Direct Reuse in the Same Application:</strong> If the board is fully functioning, the simplest approach is to continue using it in its original context. For example:</p>
    <ul>
        <li><strong>Spare or Replacement Part:</strong> A fully functional board can be kept as a spare or used to replace a damaged unit in the same system.</li>
        <li><strong>Upgrade or Enhance Existing System:</strong> If there are newer versions or models of the system that the PCB is part of, the functioning board can be reused as an upgrade for an existing device.</li>
        <li><strong>Sell or Donate:</strong> A fully functioning circuit board can be sold or donated for reuse in other applications. Some businesses or individuals specialize in refurbishing electronics, and they may be interested in taking the board off your hands.</li>
        <li><strong>Open-Source and DIY Projects:</strong> Many hobbyists and engineers would appreciate a fully functioning circuit board as part of open-source or DIY projects. For instance, an old motherboard or controller board could be used to create a custom piece of hardware for a maker project.</li>
    </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Headphones':
        st.markdown("""
    <h3>Fully Functioning Headphones</h3>
    <p>If your headphones are fully functioning, you can continue using them for their intended purpose, but also explore creative or additional ways to maximize their potential:</p>

    <h4>Regular Use for Music, Calls, and Media:</h4>
    <p>Use them for daily listening to music, podcasts, or audiobooks. You can also use fully functioning headphones for high-quality calls, video conferencing, or gaming.</p>

    <h4>Upgrade to a Premium Setup:</h4>
    <p>If you're passionate about audio quality, you can continue using them as part of an upgraded audio setup, pairing them with high-quality audio sources (such as DACs, amplifiers, or better smartphones).</p>

    <h4>Gaming Headphones:</h4>
    <p>Fully functioning headphones with a good microphone can be repurposed for gaming. They can provide immersive sound and clear communication during multiplayer games.</p>

    <h4>Use for Travel or Commute:</h4>
    <p>Keep them as your go-to headphones for travel. Their portability and ease of use make them ideal for commuting, flight entertainment, or long road trips.</p>

    <h4>Donate or Gift:</h4>
    <p>If you no longer need the headphones, you can donate them to someone who could benefit, such as a friend, family member, school, or charity. You can also sell them online or trade them in for discounts on new products.</p>

    <h4>Smart Home Integration:</h4>
    <p>Use fully functioning wireless headphones as part of a smart home system. For example, you could connect them to a smart speaker or your phone to receive notifications or control smart devices with voice commands while enjoying audio.</p>

    <h4>Fitness Companion:</h4>
    <p>Use them for fitness tracking, whether you're running, cycling, or exercising in the gym. Many headphones are designed for sports use and can be sweat-resistant and comfortable for active use.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Central Processing Unit(CPU)':
        st.markdown('Message for Smartphone with Option B: Example B')
    elif predicted_category == 'Feature Phone(Keypad)':
        st.markdown("""
    <h3>Fully Functioning Feature Phone</h3>
    <p>A fully functioning feature phone can still be a reliable, low-maintenance alternative to a smartphone. It can also be repurposed for specific tasks:</p>

    <h4>Basic Communication Device:</h4>
    <p>Use it as a primary phone for calls and text messages. Feature phones are popular among those who prefer a simple, distraction-free device without the complex functionalities of smartphones.</p>

    <h4>Travel Phone:</h4>
    <p>Use it as a travel phone for international trips. You can buy a local SIM card in the country you're visiting, avoiding high roaming charges on a smartphone. This phone can serve as a simple communication tool while traveling.</p>

    <h4>Dedicated Work or Business Phone:</h4>
    <p>If you work in an environment where distractions from social media or apps are a concern, use the feature phone as your work phone. It's excellent for focusing on essential communication like calls and emails.</p>

    <h4>Fitness or Outdoor Companion:</h4>
    <p>Use it during outdoor activities or fitness workouts, where you might not want to risk damaging a smartphone. It’s rugged, simple to use, and has a long battery life, making it ideal for hiking, biking, or outdoor adventures.</p>

    <h4>Child’s First Phone:</h4>
    <p>A fully functioning feature phone can be a good choice for a child's first phone. It allows them to make calls and send texts without the distractions of a smartphone, providing safety and communication in case of emergencies.</p>

    <h4>Sell or Donate:</h4>
    <p>If you no longer need the fully functioning feature phone, consider selling it online or donating it to a family member, school, or charity that can benefit from a low-cost communication device.</p>

    <h4>Use as a Smartwatch Companion:</h4>
    <p>Some feature phones can be paired with smartwatches via Bluetooth. This allows you to receive notifications, calls, and texts on a larger device while keeping the phone in your pocket.</p>

    <h4>Use as a Music or Audio Player:</h4>
    <p>Many feature phones support basic music playback. Use it as a simple music player for workouts, road trips, or in environments where you don’t want to risk damaging a smartphone.</p>
    """, unsafe_allow_html=True)
    else:
        st.markdown('Message for selected category with Option B')

if option=="No Functioning (Disposable)":
    if predicted_category == 'Laptop':
        st.markdown("""
            <h2>Non-Functioning (Disposable) Laptops</h2>
                <p>These laptops are not working properly (e.g., motherboard failure, severely damaged components) and cannot be easily repaired or upgraded.</p>
    
            <h3>Reuse Strategies:</h3>
    
            <h4>1. Recycle for Parts:</h4>
            <ul>
                <li><strong>Harvest Functional Components:</strong> Salvage reusable parts such as RAM, storage drives (HDD/SSD), Wi-Fi cards, and screens if they are still functional.</li>
                <li><strong>Battery Recycling:</strong> Laptop batteries can often be recycled or used in DIY projects (e.g., for building battery banks).</li>
                <li><strong>Metal and Plastic Recycling:</strong> The aluminum or plastic casing can be recycled through e-waste programs.</li>
            </ul>
    
            <h4>2. Sell for Parts:</h4>
            <p>If the components are still valuable, consider selling them online as spare parts.</p>
    
            <h4>3. E-Waste Disposal:</h4>
            <p>If the laptop is beyond repair and parts are unusable, it should be disposed of at an authorized e-waste recycling center to ensure proper environmental disposal.</p>
    
            <p>By reusing and recycling laptops in these ways, we can significantly reduce electronic waste while extending the lifespan of tech components.</p>
        """, unsafe_allow_html=True)
    elif predicted_category == 'Smartphone':
        st.markdown("""
            <h3>Non-Functioning (Disposable) Smartphones</h3>
                <p>These phones are no longer working properly (e.g., motherboard failure, screen completely damaged) and are no longer useful for everyday tasks.</p>
        
            <h4>Reuse Strategies:</h4>
        
            <h5>Recycle for Parts:</h5>
            <ul>
                <li><strong>Salvage Reusable Components:</strong> Remove components like the camera, screen (if undamaged), battery, speaker, microphone, or charging port, as they may still have value or can be reused in other devices.</li>
                <li><strong>Battery Recycling:</strong> Recycle the battery, as it can be hazardous if not disposed of properly. It can also be used in DIY projects like creating portable chargers or battery banks.</li>
                <li><strong>Materials Recycling:</strong> Smartphones contain valuable materials like gold, copper, and other metals that can be recovered and recycled. This should be done by a certified e-waste recycler.</li>
            </ul>
        
            <h5>Repurpose for DIY Projects:</h5>
            <ul>
                <li><strong>DIY Electronics Projects:</strong> Use components like the screen, camera, or sensors for DIY electronics or creative projects (e.g., building a custom smart mirror or digital photo frame).</li>
            </ul>
        
            <h5>E-Waste Disposal:</h5>
            <p>If none of the components are salvageable or reusable, dispose of the phone through an authorized e-waste recycling center to ensure it is recycled in an environmentally safe way.</p>
        """, unsafe_allow_html=True)
    elif predicted_category == 'Computer Keyboard':
        st.markdown('Message for Smartphone with Option B: Example B')
    elif predicted_category == 'Computer Mouse':
        st.markdown("""
        <h3>Non-Functioning (Disposable) Computer Mice</h3>
        <p>These mice are no longer working properly (e.g., completely broken sensors, faulty wiring, unresponsive buttons), and repairing them might not be practical.</p>
        
        <h4>Reuse Strategies:</h4>
        
        <h5>Recycle for Parts:</h5>
        <ul>
            <li><strong>Salvage Usable Components:</strong> Mice often contain useful components such as buttons, scroll wheels, and wiring. These can be repurposed for DIY electronics projects or used in other devices.</li>
            <li><strong>USB Connector or PCB Board:</strong> In some cases, you may be able to salvage the USB connector or circuit board for use in other projects.</li>
        </ul>
        
        <h5>DIY Projects:</h5>
        <ul>
            <li><strong>Art and Upcycling:</strong> Some people use old mice in creative upcycling projects like art installations, sculptures, or even DIY gadgets.</li>
            <li><strong>Robotics or Electronics Projects:</strong> If you're into DIY electronics or robotics, you can use the sensors, switches, and wiring in small machines or interactive projects.</li>
        </ul>
        
        <h5>E-Waste Recycling:</h5>
        <p>If the mouse cannot be reused in any way, dispose of it responsibly by taking it to an authorized e-waste recycling center. These centers can properly recycle components like plastic, metal, and circuit boards.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Cracked Screen Smartphone':
        st.markdown("""
            <h3>Non-Functioning (Disposable) Smartphones</h3>
                <p>These phones are no longer working properly (e.g., motherboard failure, screen completely damaged) and are no longer useful for everyday tasks.</p>
        
            <h4>Reuse Strategies:</h4>
        
            <h5>Recycle for Parts:</h5>
            <ul>
                <li><strong>Salvage Reusable Components:</strong> Remove components like the camera, screen (if undamaged), battery, speaker, microphone, or charging port, as they may still have value or can be reused in other devices.</li>
                <li><strong>Battery Recycling:</strong> Recycle the battery, as it can be hazardous if not disposed of properly. It can also be used in DIY projects like creating portable chargers or battery banks.</li>
                <li><strong>Materials Recycling:</strong> Smartphones contain valuable materials like gold, copper, and other metals that can be recovered and recycled. This should be done by a certified e-waste recycler.</li>
            </ul>
        
            <h5>Repurpose for DIY Projects:</h5>
            <ul>
                <li><strong>DIY Electronics Projects:</strong> Use components like the screen, camera, or sensors for DIY electronics or creative projects (e.g., building a custom smart mirror or digital photo frame).</li>
            </ul>
        
            <h5>E-Waste Disposal:</h5>
            <p>If none of the components are salvageable or reusable, dispose of the phone through an authorized e-waste recycling center to ensure it is recycled in an environmentally safe way.</p>
        """, unsafe_allow_html=True)
    elif predicted_category == 'Speakers':
        st.markdown("""
    <h3>No Functioning (Disposable Speakers)</h3>
    <p>If the speakers are no longer working (completely dead or broken), they can still be repurposed or recycled in various ways:</p>

    <h4>Recycle the Materials:</h4>
    <p>Speakers contain valuable materials such as metals, plastics, and magnets. Proper recycling through an e-waste program ensures that these materials are processed in an environmentally responsible manner.</p>

    <h4>Repurpose Parts for Other DIY Projects:</h4>
    <p><strong>Magnets:</strong> The powerful magnets in speakers (especially in larger ones) can be repurposed for DIY projects, such as building motors, custom tools, or other electronics projects.</p>
    <p><strong>Casing:</strong> The speaker's casing or housing can be reused for storing other objects or as an enclosure for a custom project. For example, you can transform the casing into a small storage container or even a custom power supply box for DIY electronics.</p>

    <h4>DIY Art Projects:</h4>
    <p>Old, non-functioning speakers can be used as part of artistic projects. For example, they can be turned into sculptures, industrial-style décor, or creative installations, combining the mechanical look with artistic themes.</p>

    <h4>Create a Sound Installation (No Power Needed):</h4>
    <p>The physical structure of the speaker, even without its internal functionality, can be used to create a static sound installation. For instance, you could create a unique art piece that "repurposes" speakers as part of the visual theme, without requiring them to produce sound.</p>

    <h4>Convert into a Non-Electronic Object:</h4>
    <p>Non-working speakers could be converted into non-electronic objects, such as a lamp (with the speaker casing housing the light fixture) or a decorative element for a home or office space.</p>

    <h4>Use for Educational or Training Purposes:</h4>
    <p>Even if the speakers don't work, you can use them in educational contexts to teach about audio equipment, speaker construction, or as a hands-on tool for understanding electronics, especially in classes focused on repair or electronics.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Monitor':
        st.markdown("""
    <h3>No Functioning (Disposable Monitor)</h3>
    <p>If the monitor is completely non-functional (e.g., the screen is entirely dead, or it no longer powers on), it can still be recycled or creatively reused in different ways:</p>

    <h4>Recycle the Components:</h4>
    <p>The monitor contains valuable materials (plastic, glass, metals) that can be recycled. You can recycle it through an e-waste program to ensure that harmful substances are disposed of safely and that reusable components (such as metals and plastic) are recovered.</p>

    <h4>Repurpose for DIY Projects:</h4>
    <p>Even if the display no longer works, the monitor’s frame, stand, and casing can be repurposed into a custom enclosure for DIY projects like creating an external enclosure for a Raspberry Pi, a smart home hub, or a custom control panel.</p>

    <h4>Turn It into an Art Project:</h4>
    <p>The screen and components can be used in art or creative design projects. Broken monitors have been transformed into sculptures, wall art, and other creative works, integrating the parts into a mixed-media project.</p>

    <h4>Make a Custom Lightbox or Backlight:</h4>
    <p>The backlight of the monitor can be used as part of a custom lightbox or backlight for other projects. It can serve as lighting for photography or as ambient lighting in a room, using the LED strips or light panels from the monitor.</p>

    <h4>Repurpose for a Smart Mirror (If Only Screen is Broken):</h4>
    <p>If the display itself is dead but the casing and backlight still function, you can transform the monitor into a smart mirror project. This involves placing a reflective surface (like a one-way mirror) over the screen, which displays useful information (calendar, time, weather, etc.) when powered on.</p>

    <h4>Extract and Repurpose the Circuit Board:</h4>
    <p>If the monitor’s PCB (Printed Circuit Board) is still intact, it can be used in educational projects to teach about electronics or repurposed for other DIY electronics projects.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Smart Watch':
        st.markdown("""
    <h3>No Functioning (Disposable Smartwatch)</h3>
    <p>If the smartwatch is no longer working (e.g., dead screen, unresponsive touch, broken components), it might seem disposable, but it can still be creatively reused or recycled in several ways:</p>

    <h4>Recycling:</h4>
    <p><strong>Electronic Waste Recycling:</strong> Even a non-functional smartwatch contains valuable materials (metals, plastics, battery) that can be recycled properly through e-waste recycling programs. This helps prevent environmental pollution and recovers useful materials for future electronics.</p>
    <p><strong>Battery Recycling:</strong> The battery inside the smartwatch can be repurposed or recycled, as batteries from electronic devices can be hazardous if disposed of improperly.</p>

    <h4>Repurpose for Components:</h4>
    <p><strong>Display and Screen:</strong> If the screen or display is intact but the rest of the smartwatch is malfunctioning, the screen can be salvaged for use in DIY projects or be recycled as part of a larger device.</p>
    <p><strong>Sensors:</strong> If the sensors (heart rate monitor, gyroscope, accelerometer) are still functioning, these can be repurposed for other projects. For example, you could extract the sensors to create your own fitness tracking system or integrate them into other wearable devices.</p>

    <h4>Upcycle the Casing for DIY Projects:</h4>
    <p>The casing and watchband can be reused in various creative DIY projects. The casing might be repurposed into a small storage compartment, custom jewelry, or even as a unique case for a different electronic project.</p>

    <h4>Convert into a Decorative Piece or Art:</h4>
    <p>Old smartwatches, especially if they have a stylish or unique design, can be repurposed into a decorative art piece, like a steampunk-style sculpture or as part of a larger electronic art installation.</p>

    <h4>Repurpose for Educational Purposes:</h4>
    <p>Non-functioning smartwatches are great for educational purposes, especially for teaching about electronics, repair, or component reuse. Students or hobbyists can practice disassembling and analyzing the components inside the smartwatch, learning about the technology and structure.</p>

    <h4>Use for Parts in Repair or Customization:</h4>
    <p>If you’re into watchmaking or tech repair, you could disassemble the non-functioning smartwatch for its components (circuit board, screws, internal wiring, etc.) to repair other devices or customize other watches.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Washing Machine':
        st.markdown("""
    <h3>No Functioning (Disposable) Washing Machine</h3>
    <p>If the washing machine is completely non-functional (e.g., motor failure, leaking, broken drum), there are still several ways to repurpose, recycle, or reuse it:</p>

    <h4>Recycle for Parts:</h4>
    <p><strong>Scrap Metal:</strong> If the washing machine has significant damage, it can be taken to a scrap metal facility. The metal components (including the drum, frame, and other parts) can be recycled for reuse in manufacturing new products.</p>
    <p><strong>Motors and Electronics:</strong> The motor, wiring, and electronic components inside the machine can be salvaged and repurposed in DIY projects or recycled for parts.</p>

    <h4>Repurpose the Drum:</h4>
    <p><strong>Garden Planter:</strong> The metal drum can easily be converted into a large planter for flowers or vegetables. Its perforated design makes it great for drainage, and it provides ample space for plants to grow.</p>
    <p><strong>Fire Pit:</strong> The drum from a non-functioning washing machine can be used to create an outdoor fire pit. Simply add some rocks or gravel at the bottom for safety, and you’ve got a rustic, functional fire pit.</p>
    <p><strong>Composting Bin:</strong> The washing machine drum can also be used for composting. Its cylindrical design allows for airflow, which is perfect for helping organic matter break down more quickly.</p>

    <h4>Use as a Large Storage Container:</h4>
    <p>The outer casing of the washing machine can be used as a large storage container for tools, gardening supplies, or outdoor equipment.</p>

    <h4>Create Artistic Pieces:</h4>
    <p><strong>Sculptures and Art Installations:</strong> Broken washing machines can be used in sculpture and art installations. For instance, you could use the inner drum to create industrial-style art pieces or garden sculptures.</p>
    <p><strong>Upcycled Furniture:</strong> Broken washing machine parts can be transformed into upcycled furniture. The drum can be turned into a base for a side table or lamp stand.</p>

    <h4>Turn into a Workshop or DIY Tool:</h4>
    <p><strong>Workshop Storage or Shelves:</strong> Parts of the washing machine, such as the metal frame or drum, can be used to create a durable workbench or shelves for your garage or workshop.</p>
    <p><strong>DIY Washing Station:</strong> For small items or tools, you could convert the drum or frame into a washing station for cleaning parts or materials in your workshop or garage.</p>

    <h4>Repurpose as an Outdoor Feature:</h4>
    <p><strong>Garden Water Feature:</strong> Use the drum or casing as a base for a DIY water feature or fountain in your garden. This gives it a new life as part of a decorative landscaping project.</p>

    <h4>Recycling Programs:</h4>
    <p>If you are unable to repurpose the washing machine for any of these purposes, consider sending it to an appliance recycling program. Many municipalities and stores offer recycling for large appliances, ensuring that all components are properly disposed of and reused.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Ceiling Fan':
        st.markdown("""
    <h3>No Functioning (Disposable Ceiling Fans)</h3>
    <p>When the ceiling fan is no longer working (i.e., the motor is completely dead, or it's beyond repair), it still has value for parts and can be creatively reused:</p>

    <h4>Recycling the Materials:</h4>
    <p><strong>Metal and Plastic:</strong> The fan’s metal components (like the blades, motor housing, and other parts) and plastic casing can be recycled. These materials are valuable in e-waste recycling programs and can be repurposed for new products.</p>
    <p><strong>Electric Motor:</strong> If the motor is still in good condition, it may be repurposed in other DIY projects. For example, it can be used to power small mechanical devices, model cars, or custom fans in other setups.</p>

    <h4>Repurpose the Fan Blades for DIY Projects:</h4>
    <p>Fan blades can be creatively reused in a variety of DIY craft projects:</p>
    <ul>
        <li><strong>Wall Art:</strong> You can paint and decorate the blades to create unique wall art, or arrange them in a pattern to form a decorative piece.</li>
        <li><strong>Garden Decoration:</strong> Fan blades can be used as part of garden sculptures or to make wind chimes.</li>
        <li><strong>Furniture Elements:</strong> The blades can be repurposed into a custom chair or table, with the blades forming the base or legs of a new piece of furniture.</li>
    </ul>

    <h4>Transform into a Table Fan:</h4>
    <p>You can take the motor and fan blades and create a small table fan. This could be used in smaller spaces or be mounted on a custom stand. This process might involve rewiring and reconfiguring the motor to run at a smaller scale.</p>

    <h4>Create Wind-Powered Projects:</h4>
    <p>The fan blades and motor can be used for wind-powered projects like small DIY wind turbines. While it won’t generate a lot of energy, it’s a fun project for learning about wind power or generating small amounts of electricity.</p>

    <h4>Art and Sculptures:</h4>
    <p>Old ceiling fans are popular in upcycling and industrial art. The motor and blades can be used to create sculptures or large installations, often as part of modern or steampunk designs.</p>

    <h4>Use as a Decoration or Prop:</h4>
    <p>If you don’t need the fan for any functional purpose, you can use its components as part of a décor theme, such as a vintage or retro look in your home or office. Fan parts can also be used as props for theater productions, film sets, or themed parties.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Circuit Board':
        st.markdown("""
    <h2>No Functioning (Disposable)</h2>
    <p><strong>E-Waste Recycling:</strong> If the circuit board is completely non-functional and cannot be repaired or repurposed, it’s best to recycle it through appropriate e-waste recycling channels. This ensures that the materials (e.g., metals, plastics, and other valuable elements) are recovered and reused, minimizing environmental impact.</p>
    <ul>
        <li><strong>Extract Valuable Materials:</strong> Even if the board itself is not functioning, many circuit boards contain valuable metals like gold, silver, and copper. These can be extracted and repurposed, either manually or through specialized processes in recycling plants.</li>
        <li><strong>Creative Upcycling:</strong> In some cases, even non-functional boards can be used for creative or artistic purposes. For example, old circuit boards have been used in sculptures, jewelry, and other art projects. The intricate designs and components can make interesting decorative elements.</li>
        <li><strong>Parts for Educational Purposes:</strong> Non-functional circuit boards can be used in educational settings for students learning about electronics. They can practice soldering, component identification, and circuit analysis on these boards without the risk of damaging something valuable.</li>
    </ul>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Headphones':
        st.markdown("""
    <h3>No Functioning (Disposable Headphones)</h3>
    <p>Even if your headphones are completely non-functional, there are still ways to reuse, repurpose, or recycle them in an environmentally friendly manner:</p>

    <h4>Recycling:</h4>
    <p><strong>Electronic Waste Recycling:</strong> Headphones contain several recyclable materials, including plastics, wires, and sometimes precious metals in the components. You can properly recycle them through an e-waste collection program to ensure the materials are repurposed.</p>

    <h4>Repurpose Parts:</h4>
    <p><strong>Speakers:</strong> The individual speakers from the headphones can be reused in various DIY audio projects. For example, you could use them in custom speakers, small Bluetooth audio systems, or even as part of a home-made hearing aid system (if working properly).</p>
    <p><strong>Headphone Cables:</strong> Even non-functioning headphones typically have good-quality cables that can be repurposed for other electronics projects. The cables can be used in DIY electronics, as charging cables, or for small wiring tasks.</p>

    <h4>Use for Art Projects:</h4>
    <p><strong>Sculptures or Art Installations:</strong> Old headphones can be used in art and sculpture projects. The headband, ear cups, and components can form part of a larger piece, or you can incorporate them into a retro or industrial-themed sculpture.</p>
    <p><strong>Decorative Elements:</strong> The non-functional parts can also be used for decoration, such as in creating wall art, repurposed accessories, or customized furniture.</p>

    <h4>Custom Audio Projects:</h4>
    <p>Even broken headphones can be salvaged for their speaker components. These can be integrated into DIY sound systems, mini speaker boxes, or custom-designed audio gadgets. For example, you could use the speakers in a homemade radio or sound amplifier project.</p>

    <h4>Turn into a "Tech" Fashion Accessory:</h4>
    <p>Non-functioning headphones, especially if they have a unique design, can be turned into an accessory like a necklace or bracelet, or even a unique decorative headband.</p>

    <h4>Use for Educational Purposes:</h4>
    <p>If you’re a student, hobbyist, or educator, non-functioning headphones can be a great tool for teaching about electronics and repairs. You can use them to demonstrate how headphones work, show how to fix broken components, or practice disassembling and reassembling devices.</p>

    <h4>Create a Toy or Prop:</h4>
    <p>Old headphones can be repurposed as a prop for role-playing, theatrical performances, or movie/TV set design. If you're creating a futuristic or retro theme, headphones can be used as a prop or costume element.</p>
    """, unsafe_allow_html=True)
    elif predicted_category == 'Central Processing Unit(CPU)':
        st.markdown('Message for Smartphone with Option B: Example B')
    elif predicted_category == 'Feature Phone(Keypad)':
        st.markdown("""
    <h3>No Functioning (Disposable) Feature Phone</h3>
    <p>Even if the feature phone is no longer functioning (e.g., screen is completely dead, battery doesn't charge, or internal components are beyond repair), there are still ways to repurpose, recycle, or reuse it:</p>

    <h4>Recycle for E-Waste:</h4>
    <p>Feature phones contain valuable metals, plastics, and other materials that can be recycled. Send it to an electronic waste recycling facility where the materials can be recovered and reused for manufacturing new devices.</p>

    <h4>Extract Useful Parts:</h4>
    <p><strong>Battery Reuse:</strong> If the battery is still functional, it can be repurposed for other devices or DIY projects. For example, you could use it in custom electronics projects, like powering a small device, flashlight, or homemade power bank.</p>
    <p><strong>Circuit Boards:</strong> The internal circuit boards and components can be used for educational purposes or incorporated into other DIY electronics projects.</p>
    <p><strong>Screen:</strong> If the screen is still intact and functional, it could be repurposed in another project, like a small display for a custom device, clock, or digital sign.</p>
    <p><strong>Camera Module:</strong> Some feature phones come with cameras that can be repurposed in DIY projects or for use in robotics, smart home setups, or other tech hobbies.</p>

    <h4>Repurpose the Housing or Casing:</h4>
    <p>The phone’s outer casing can be used as a container for small objects or repurposed into a decorative piece, such as a coin holder or a quirky desk organizer.</p>

    <h4>Create Art or Sculptures:</h4>
    <p>Broken or non-functioning phones can be used in art and sculpture projects. For example, you could use the phone casing, buttons, and circuit boards to create a retro or industrial-themed art piece.</p>

    <h4>Turn It into a Decorative or Unique Accessory:</h4>
    <p>If you're into crafting, you can upcycle the phone’s parts for creating unique jewelry pieces like bracelets, necklaces, or even keychains. The buttons or casing can be reimagined as part of a wearable design.</p>

    <h4>Use as a Decorative Piece in Vintage Style:</h4>
    <p>Non-functioning phones with a unique design or retro appearance can be displayed as vintage decor in a home or office. It can also be part of a nostalgic tech collection.</p>

    <h4>Use for Educational Purposes:</h4>
    <p>If you’re learning about electronics or technology, non-functioning phones are great tools for educational purposes. You can disassemble them to explore their components and learn how mobile devices are built.</p>
    """, unsafe_allow_html=True)
    else:
        st.markdown('Not E-Components')
