---

# JeyMeetings.ai

JeyMeetings.ai is an AI-powered meeting preparation tool that leverages multiple AI models to analyze meeting contexts, provide industry insights, develop strategies, and create executive briefs. This application is designed to assist users in organizing and optimizing their meetings effectively.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Keys](#api-keys)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Context Analysis**: Analyze the context of meetings based on company information, objectives, attendees, and specific focus areas.
- **Industry Insights**: Generate in-depth industry analysis and identify key trends.
- **Strategy Development**: Create tailored meeting strategies and detailed agendas.
- **Executive Briefs**: Synthesize information into concise and impactful briefs.
- **User-Friendly Interface**: Intuitive Streamlit interface for easy interaction.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **LangChain**: For integrating various AI models.
  - `langchain-anthropic`: For using Anthropic's Claude model.
  - `langchain-google-genai`: For leveraging Google's Gemini model.
  - `langchain-ollama`: For utilizing Ollama's LLM.
- **CrewAI**: To manage agents and tasks efficiently.
- **SerperDevTool**: For conducting web searches to gather relevant information.

## Installation

To get started with JeyMeetings.ai, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jeymeetings.ai.git
   cd jeymeetings.ai
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run jeyMeetingsai.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter your API keys in the sidebar:
   - **Anthropic API Key**
   - **Gemini API Key**
   - **Serper API Key**

4. Fill out the meeting details:
   - Company Name
   - Meeting Objective
   - Attendees and their roles
   - Meeting Duration
   - Specific Areas of Concern

5. Click the "Prepare Meeting" button to generate a comprehensive meeting preparation package.

## API Keys

To use JeyMeetings.ai, you need valid API keys for the following services:

- **Anthropic**: For accessing Claude models.
- **Google Gemini**: For leveraging Google's generative AI capabilities.
- **Serper**: For conducting web searches.

Make sure to keep your API keys secure and do not share them publicly.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or feedback, feel free to reach out:

- Dharren Pius Makoha - [dharrenpius@icloud.com](mailto:dharrenpius@icloud.com)
- GitHub: [Dharren09](https://github.com/Dharren09)

---
