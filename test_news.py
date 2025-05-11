import pytest
from unittest import mock
from news_digest import generate_news_digest, send_email
import news_parser 
import openai
import smtplib
import os

# Mock RSS feed data
mock_rss_data = [
    {
        'title': 'Tech News Today',
        'description': 'New breakthroughs in AI.',
        'link': 'http://example.com/tech'
    }, 
    {
        'title': 'Global Economy Update',
        'description': 'Inflation rates are on the rise.',
        'link': 'http://example.com/economy'
    }

]

# Test case 1: Test  function
@mock.patch("feedparser.parse")
def test_fetch_rss_feeds(mock_parse):
    # Mocking feedparser.parse to return controlled RSS data
    mock_parse.return_value.entries = mock_rss_data

    
    # Temporarily override RSS_FEEDS in the module where it's defined
    original_feeds = news_parser.RSS_FEEDS
    
     # Limit feeds to test only 1 iteration
    news_parser.RSS_FEEDS = ["http://mocked.url"]

    result = news_parser.fetch_rss_feeds()

    # Restore original RSS_FEEDS after test
    news_parser.RSS_FEEDS = original_feeds
    
    assert len(result) == 2, "Expected 2 articles in the fetched RSS data"
    assert result[0]["title"] == "Tech News Today", "Title mismatch in first article"
    assert result[1]["description"] == "Inflation rates are on the rise.", "Summary mismatch in second article"
    assert result[0]["link"] == "http://example.com/tech", "Link mismatch in first article"

# Test case 2: Test generate_news_digest function
@mock.patch("news_digest.OpenAI")
@mock.patch.dict(os.environ, {"OPENAI_API_KEY": "your-api-key-here"})  # Mock the API key
def test_generate_news_digest(mock_client):

    
    # Properly mock the OpenAI response structure
    mock_response = mock.MagicMock()
    mock_choice = mock.MagicMock()
    mock_choice.message.content = "Global Headlines:\n- Tech breakthrough... (source: example.com)"
    mock_response.choices = [mock_choice]
    
    mock_client.return_value.chat.completions.create.return_value = mock_response
    
    # Mock RSS summary to feed into the digest function
    rss_summary = mock_rss_data

    result = generate_news_digest(rss_summary)
    assert "Global Headlines:" in result, "Expected 'Global Headlines' in the digest"
    assert "Tech breakthrough" in result, "Expected a tech news headline in the digest"
    assert "(source: example.com)" in result, "Expected a source link in the digest"

# Test case 3: Test send_email function
@mock.patch("smtplib.SMTP")
@mock.patch.dict(os.environ, {
    "EMAIL_FROM": "your-email@example.com",
    "SMTP_PASSWORD": "your-password",
    "EMAIL_TO": "recipient@example.com",
    "SMTP_SERVER": "smtp.example.com",
    "SMTP_PORT": "587",
})
def test_send_email(mock_smtp):
    # Mocking the SMTP connection and send_message
    mock_server = mock.MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    subject = "Test Email"
    body = "This is a test email body."

    # Print the environment variables to ensure they're set correctly
    print(f"EMAIL_FROM: {os.environ['EMAIL_FROM']}")
    print(f"SMTP_PASSWORD: {os.environ['SMTP_PASSWORD']}")
    
    send_email(subject, body)

    mock_server.starttls.assert_called_once(), "starttls was not called"
    mock_server.login.assert_called_once_with(os.environ["EMAIL_FROM"],
        os.environ["SMTP_PASSWORD"]), "Login was not called with correct credentials"
    mock_server.send_message.assert_called_once(), "send_message was not called"
    assert mock_server.send_message.call_args[0][0]["Subject"] == subject, "Email subject does not match"
    assert mock_server.send_message.call_args[0][0].get_content().strip() == body.strip(), "Email body does not match"

# Test case 4: Test the full process from fetching to sending email
@mock.patch("feedparser.parse")
@mock.patch("news_digest.OpenAI")
@mock.patch("smtplib.SMTP")
def test_main_process(mock_smtp, mock_openai, mock_parse):
    # Mocking all components
    mock_parse.return_value.entries = mock_rss_data

    mock_client = mock.MagicMock()
    mock_openai.return_value = mock_client

    # Create a mock response object that supports dot notation
    mock_response = mock.MagicMock()
    mock_response.choices = [
        mock.MagicMock(message=mock.MagicMock(content="Global Headlines:\n- Tech breakthrough... (source: example.com)"))
    ]
    
    # Set the mock to return this mock response
    mock_client.return_value.chat.completions.create.return_value = mock_response
      
    # Mock SMTP server
    mock_server = mock.MagicMock()
    mock_smtp.return_value.__enter__.return_value = mock_server

    # Execute the main function
    from news_digest import main
    main()

    # Check if all parts were called correctly
    assert mock_parse.call_count>0, "Expected feedparser.parse to be called at least once"
    mock_openai.assert_called_once()
    mock_server.send_message.assert_called_once()

