import pytest
from unittest import mock
from news_digest import fetch_rss_feeds, generate_news_digest, send_email
import openai
import smtplib

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

# Test case 1: Test fetch_rss_feeds function
@mock.patch("feedparser.parse")
def test_fetch_rss_feeds(mock_parse):
    # Mocking feedparser.parse to return controlled RSS data
    mock_parse.return_value.entries = mock_rss_data

    result = fetch_rss_feeds()
    assert len(result) == 2, "Expected 2 articles in the fetched RSS data"
    assert result[0]["title"] == "Tech News Today", "Title mismatch in first article"
    assert result[1]["description"] == "Inflation rates are on the rise.", "Summary mismatch in second article"
    assert result[0]["link"] == "http://example.com/tech", "Link mismatch in first article"

# Test case 2: Test generate_news_digest function
@mock.patch("openai.ChatCompletion.create")
def test_generate_news_digest(mock_openai):
    # Mocking OpenAI's API response
    mock_openai.return_value.choices = [{'message': {'content': "Global Headlines:\n- Tech breakthrough... (source: example.com)"}
}]
    # Mock RSS summary to feed into the digest function
    rss_summary = mock_rss_data

    result = generate_news_digest(rss_summary)
    assert "Global Headlines:" in result, "Expected 'Global Headlines' in the digest"
    assert "Tech breakthrough" in result, "Expected a tech news headline in the digest"
    assert "(source: example.com)" in result, "Expected a source link in the digest"

# Test case 3: Test send_email function
@mock.patch("smtplib.SMTP")
def test_send_email(mock_smtp):
    # Mocking the SMTP connection and send_message
    mock_server = mock.MagicMock()
    mock_smtp.return_value = mock_server

    subject = "Test Email"
    body = "This is a test email body."
    send_email(subject, body)

    mock_server.starttls.assert_called_once(), "starttls was not called"
    mock_server.login.assert_called_once_with("your-email@example.com", "your-password"), "Login was not called with correct credentials"
    mock_server.send_message.assert_called_once(), "send_message was not called"
    assert mock_server.send_message.call_args[0][0]["Subject"] == subject, "Email subject does not match"
    assert mock_server.send_message.call_args[0][0].get_payload() == body, "Email body does not match"

# Test case 4: Test the full process from fetching to sending email
@mock.patch("feedparser.parse")
@mock.patch("openai.ChatCompletion.create")
@mock.patch("smtplib.SMTP")
def test_main_process(mock_smtp, mock_openai, mock_parse):
    # Mocking all components
    mock_parse.return_value.entries = mock_rss_data
    mock_openai.return_value.choices = [{"message": {"content": "Global Headlines:\n- Tech breakthrough... (source: example.com)"}}]
    
    # Mock SMTP server
    mock_server = mock.MagicMock()
    mock_smtp.return_value = mock_server

    # Execute the main function
    from news_digest import main
    main()

    # Check if all parts were called correctly
    mock_parse.assert_called_once()
    mock_openai.assert_called_once()
    mock_server.send_message.assert_called_once()

