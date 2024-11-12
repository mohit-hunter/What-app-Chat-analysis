# WhatsApp Chat Analysis Tool 🚀

A powerful Streamlit-based web application that provides comprehensive analysis of WhatsApp chat data, including message statistics, timeline activities, user engagement metrics, and sentiment analysis.

## 🌟 Features

- **Message Statistics**
  - Total message count
  - Word count analysis
  - Media messages tracking
  - Links shared counter

- **Timeline Analysis**
  - Monthly activity trends
  - Date-wise message distribution
  - Day-of-week activity patterns
  - Month-wise message analysis

- **User Analytics**
  - Most active users identification
  - User participation percentages
  - Common words analysis
  - Group vs individual chat analysis

- **Sentiment Analysis**
  - Day-wise sentiment trends
  - Message polarity detection
  - Emotional context understanding

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd whatsapp-chat-analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Required packages:
- streamlit
- pandas
- numpy
- matplotlib
- regex
- urlextract
- textblob

## 📊 Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Export your WhatsApp chat:
   - Open WhatsApp
   - Go to the desired chat
   - Click on three dots (menu)
   - Select 'More'
   - Choose 'Export chat'
   - Select 'Without media'

3. Upload the exported chat file to the application
4. Select user for specific analysis or choose 'overall' for complete chat analysis
5. Click 'Show analysis' to generate insights

## 📁 Project Structure

```
whatsapp-chat-analysis/
├── app.py              # Main Streamlit application
├── preprocess.py       # Data preprocessing functions
├── helper.py           # Analysis helper functions
├── stop_hinglish.txt   # Stop words for text analysis
└── requirements.txt    # Project dependencies
```

## 🔍 Analysis Components

### Preprocessing
- Date-time parsing
- User message separation
- Message type classification
- Temporal feature extraction

### Data Analysis
- Message frequency analysis
- User participation metrics
- Content type distribution
- Temporal pattern recognition
- Sentiment classification

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Requirements

- Python 3.6+
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Regex
- URLExtract
- TextBlob

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to Streamlit for the amazing web app framework
- TextBlob for sentiment analysis capabilities
- URLExtract for link detection

## 📫 Contact

For any queries or suggestions, please open an issue in the repository.

---
Made with ❤️ for WhatsApp chat analysis
