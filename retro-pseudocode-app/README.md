# Pseudo-Gen 3000 🕹️

**Your Nostalgic Python-to-Pseudocode Converter**

A retro-styled web application that converts Python code into clear, structured pseudocode using Google's Gemini AI. Built with Flask and styled with an 80s arcade aesthetic.

![Retro Terminal](https://img.shields.io/badge/style-retro-f923d2?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.8+-00ff41?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/flask-2.0+-f923d2?style=for-the-badge&logo=flask)

## ✨ Features

- **AI-Powered Conversion**: Uses Google Gemini 1.5 Flash to generate accurate pseudocode
- **Retro Aesthetic**: Neon-soaked 80s terminal design with CRT effects and pixel fonts
- **Simple Interface**: Clean, intuitive UI for pasting code and viewing results
- **Responsive Design**: Works on desktop and mobile devices
- **Error Handling**: Graceful error messages when API calls fail

## 🖥️ Demo

The application features a nostalgic terminal-style interface with:
- Bright green text on dark purple background
- Hot pink neon borders and glowing effects
- Pixel-perfect retro fonts (VT323 and Press Start 2P)
- Flickering title animation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Google API Key for the Gemini API
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   cd retro-pseudocode-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY='your-google-api-key-here'
   ```
   
   > 💡 Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   
   Navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
retro-pseudocode-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # HTML template
├── static/
│   └── style.css         # Retro styling
└── .env                  # Environment variables (API keys)
```

## 🎮 Usage

1. Paste your Python code into the input box
2. Click the **GENERATE** button
3. View the generated pseudocode in the result box below

### Example Input

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))
```

### Example Output

```
FOR each number from 0 to 9:
    CALCULATE fibonacci of that number
    PRINT the result

FUNCTION fibonacci WITH parameter n:
    IF n is less than or equal to 1:
        RETURN n
    ELSE:
        RETURN fibonacci(n-1) + fibonacci(n-2)
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

### Dependencies

- **Flask** - Web framework
- **google-generativeai** - Google's AI SDK
- **python-dotenv** - Environment variable management

## 🎨 Customization

Want to tweak the retro vibes? Edit `static/style.css`:

- Change colors by modifying CSS variables
- Adjust font sizes for different screen sizes
- Modify the flicker animation timing
- Add more retro effects (scanlines, chromatic aberration, etc.)

## 🐛 Troubleshooting

### "GOOGLE_API_KEY not found"
Make sure you've created a `.env` file with your API key in the project root.

### "Failed to configure GenerativeAI"
- Check that your API key is valid
- Ensure you have an internet connection
- Verify your Google Cloud project has the Gemini API enabled

### Empty response from model
This might occur if:
- The input code is empty or malformed
- The API quota is exceeded
- There are network issues

## Tutorial 
https://softwarejournal.blog/blog/retro-pseudocode-generator-flask-gemini-explained/

## 📝 License

See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🙏 Acknowledgments

- Google Gemini for the AI capabilities
- Flask community for the awesome web framework
- All the retro gaming enthusiasts who inspired the design

---

**Made with 💖 and ☕ by the Pseudo-Gen Team**

*Keep it retro, keep it coding!* 🕹️
