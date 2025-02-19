"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import numpy as np
from scipy import signal as sg
import sounddevice as sd
import time

# st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

def get_y(plot_type="Sine", index=0):
  """
  Get y point position based on plot type
  """
  x = np.arange(0, 100*np.pi, 0.1)
  if plot_type == "Sine":
    y = np.sin(x[index])
  elif plot_type == "Square":
    y = sg.square(x[index])
  elif plot_type == "Sawtooth":
    y = sg.sawtooth(x[index], width=1)
  elif plot_type == "Triangle":
    y = sg.sawtooth(x[index], width=0.5)
  else:
    y = np.sin(x[index])
  return y


# st.title("🦜🔗 Dynamic Tone Generator App")
st.title("🦜 Dynamic Tone Generator App 🦜")
st.divider()  # 👈 Draws a horizontal rule

#Select frequency
initial_frequency = 19
st.sidebar.subheader("Select Frequency between 20Hz & 20,000Hz")
frequency = st.sidebar.number_input("Select Frequency between 20Hz & 20,000Hz", min_value=19, max_value=20000, step=10, value=initial_frequency, disabled=False, label_visibility="hidden")

#Select duration
initial_duration = 3
st.sidebar.subheader("Select  duration between 3s & 10s")
duration = st.sidebar.number_input("Select  duration between 3s & 10s", min_value=3, max_value=10, value="min", disabled=False, label_visibility="hidden")
st.sidebar.divider()  # 👈 Draws a horizontal rule<

#Select Frequency Type
freq_type_header = st.sidebar.markdown("## %s..." % "Select a Frequency Type")
frequency_type_options = ["Sine", "Square", "Sawtooth", "Triangle"]
frequency_type = st.sidebar.radio("Select a Frequency Type", ["Sine", "Square", "Sawtooth", "Triangle"], index=0 , label_visibility="hidden")
st.sidebar.divider()  # 👈 Draws a horizontal rule<

if frequency > initial_frequency:

  # Parameters
  sampling_rate = 44100  # Samples per second

  # Generate time   
  t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
  
  #Generate frequencies based on selection using if else statements
  
  if frequency_type == "Sine":
    # Generate sine wave
    selected_wave = np.sin(2 * np.pi * frequency * t)
  elif frequency_type == "Square":
    ## square wave
    selected_wave = sg.square(2 * np.pi * frequency * t)
  elif frequency_type == "Sawtooth":
    ## Sawtooth wave
    selected_wave = sg.sawtooth(2 * np.pi * frequency * t, width=1)
  elif frequency_type == "Triangle":
    ## Triangle wave
    selected_wave = sg.sawtooth(2 * np.pi * frequency * t, width=0.5)
  else:
    # Generate sine wave
    selected_wave = np.sin(2 * np.pi * frequency * t)

  

  # Play the sine wave
  d = st.sidebar.empty()
  d.markdown("## %s..." % "Playing ...")
  sd.play(selected_wave, sampling_rate)
  # sd.wait()


  chart = st.line_chart(np.zeros(shape=(1,1)))
  # x = np.arange(0, 100*np.pi, 0.1)
 
  for idx,i in enumerate(np.linspace(0, duration * 10 , num=100).tolist()):
    y = get_y(plot_type=frequency_type, index=idx)
    chart.add_rows([y])
    time.sleep(0.02)
  
  # sd.wait()

  d.markdown("## %s..." % "Done ...")
  
 