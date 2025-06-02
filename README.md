# OpenAI Chatbot

A simple Python application that demonstrates how to interact with OpenAI's GPT-4 API to create a basic chatbot.

## Features

- Simple chat completion using OpenAI's GPT-4 model
- Environment variable configuration for secure API key management
- Configurable temperature settings for controlling response creativity
- Clean output extraction from API responses

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install required dependencies:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
API_KEY=your_openai_api_key_here
```

## Usage

Run the script:
```bash
python main.py
```

The application will send a predefined question to GPT-4 and display the response.

## Configuration

### Temperature Settings

The `temperature` parameter controls the randomness/creativity of the AI responses:

- **0.0**: Deterministic responses (same input → same output)
  - Best for: factual questions, math problems, answers requiring consistency
- **0.1-0.9**: Balanced randomness
  - Best for: marketing copy, creative writing, storytelling
- **1.0+**: Highly creative/random responses

### Model Selection

Currently configured to use `gpt-4.1-2025-04-14`. You can modify this in the code to use other available models.

## Code Structure

```python
# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("API_KEY"))

# Create chat completion
response = client.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=[{"role": "user", "content": "Your question here"}],
    temperature=0.0
)

# Extract and display response
print(response.choices[0].message.content)
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | Your OpenAI API key | Yes |

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key secure and don't share it publicly
- Consider using API key rotation for production applications

## Dependencies

- `openai`: Official OpenAI Python client library
- `python-dotenv`: Load environment variables from .env file

## Example Output

The current example asks "왜 강남은 강남이라고 할까요?" (Why is Gangnam called Gangnam?) and displays the AI's response in Korean.

## Customization

To modify the chatbot:

1. Change the question in the `messages` array
2. Adjust the `temperature` value for different response styles
3. Switch to a different OpenAI model if needed
4. Add conversation history by expanding the `messages` array

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues related to:
- OpenAI API: Check the [OpenAI documentation](https://platform.openai.com/docs)
- This code: Open an issue in this repository
