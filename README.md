# Text-to-Speech Converter App

A **Streamlit** and **gTTS (Google Text-to-Speech)** powered web application that converts text into high-quality speech. It supports multiple input methods (plain text and SSML), voice customization, different output formats, and more. The app allows users to easily convert text into speech in multiple languages with the option to adjust voice pitch, speed, and volume.


https://github.com/user-attachments/assets/d6bd4741-2ce4-40de-9b3a-f455fd4d8530



## Features

- **Plain Text and SSML Input**: 
  - Convert **plain text** directly into speech.
  - Use **SSML (Speech Synthesis Markup Language)** for more advanced speech customization (e.g., adjusting pitch, speed, pauses, voice type).
  
- **Multiple Language Support**: 
  - Select from a variety of languages, including **English**, **Hindi**, and more (depending on the available voices from gTTS).
  
- **Voice Customization**:
  - **Voice Selection**: Choose from available voice types, including different accents and tones.
  - **Pitch Adjustment**: Control the pitch of the speech to make it higher or lower.
  - **Speed Control**: Adjust the speaking rate to slow down or speed up the speech.
  - **Volume Control**: Modify the volume level to suit your preferences.

- **Output Format Options**:
  - Choose between **WAV (lossless)** and **MP3 (lossy)** formats based on your requirements.
  - **WAV (lossless)** preserves the highest quality audio, ideal for professional work.
  - **MP3 (lossy)** reduces file size while maintaining good sound quality, perfect for general use.

- **Downloadable Audio**:
  - **Play**: Listen to the speech directly in the browser using the built-in audio player.
  - **Download**: Get the speech file in MP3 format with the click of a button.
  
- **Audio Device Profile** (Optional):
  - **Handset**: Optimized for small devices like phones.
  - **Headphones**: Tailored for better sound quality through headphones.
  - **Smartphone**: Optimized for smartphones and mobile speakers.
  - **Wearable**: Designed for smartwatches or Bluetooth earbuds, focusing on speech clarity.

- **Responsive UI**:
  - The app's interface is designed to be simple and intuitive, with sliders for customization and a clean layout for easy navigation.

- **Support for Special Characters**:
  - The app supports special characters like punctuation, emojis, and non-English alphabets in text and SSML input.

## Installation

Follow these steps to run the app locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/text-to-speech-converter.git
cd text-to-speech-converter
```

### 2. Install Dependencies

Make sure you have **Python 3.x** installed. Install the required packages using:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```


## Usage

1. **Choose Input Method**: 
   - Select between **Plain Text** and **SSML** for text input.
   - For **Plain Text**, simply enter the text you want to convert.
   - For **SSML**, you can input advanced markup to control voice features such as pitch, speed, and pauses.
  
2. **Enter Text or SSML**: 
   - Enter the desired text or SSML markup.
   - Example SSML for Hindi:
     ```xml
     <speak>
         <voice name="hi-IN-Wavenet-A">
             <prosody rate="fast" pitch="high">
                 नमस्ते! यह एक हिंदी वाक्य है जिसे आवाज में बदला जाएगा।
             </prosody>
         </voice>
     </speak>
     ```

3. **Select Language**: Choose from the available languages in the dropdown (e.g., English, Hindi).

4. **Customize Voice**: 
   - Use the **Pitch** slider to adjust the pitch of the voice.
   - Use the **Speed** slider to adjust the rate of speech (slow or fast).
   - Use the **Volume** slider to control the output volume.

5. **Select Audio Format**: Choose between **WAV** (lossless) or **MP3** (lossy) as the output file format.

6. **Convert to Speech**: Click the **Convert** button to generate the speech.

7. **Playback and Download**:
   - Once the conversion is complete, use the **audio player** to play the speech directly in your browser.
   - **Download** the audio file in MP3 format by clicking the download link.

## Screenshots

![App Screenshot](screenshot.png)

## Contributing

We welcome contributions! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Implement your feature and commit changes (`git commit -am 'Add new feature'`).
4. Push your branch (`git push origin feature-name`).
5. Create a pull request.
