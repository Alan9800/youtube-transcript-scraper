thonimport requests
from bs4 import BeautifulSoup

class YouTubeTranscriptParser:
    @staticmethod
    def extract_transcript(video_url):
        try:
            # Fetch YouTube video page
            response = requests.get(video_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Locate the transcript (this is just an example; real implementation would need YouTube API or another method)
            transcript_data = soup.find_all('div', {'class': 'caption-text'})
            if not transcript_data:
                return None

            transcript = []
            for caption in transcript_data:
                transcript.append(caption.get_text())
            return transcript
        except Exception as e:
            print(f"Failed to extract transcript: {e}")
            return None