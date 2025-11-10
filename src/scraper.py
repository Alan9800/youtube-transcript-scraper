thonimport requests
from bs4 import BeautifulSoup
import json

class YouTubeTranscriptScraper:
    def __init__(self, video_url):
        self.video_url = video_url
        self.transcript_url = f"https://www.youtube.com/api/timedtext?lang=en&v={self.extract_video_id(video_url)}"

    def extract_video_id(self, url):
        """
        Extract the video ID from the YouTube URL.
        """
        return url.split('v=')[1].split('&')[0]

    def fetch_transcript(self):
        """
        Fetch the transcript for the given YouTube video.
        """
        response = requests.get(self.transcript_url)
        if response.status_code != 200:
            raise Exception("Failed to fetch transcript.")
        
        return self.parse_transcript(response.text)

    def parse_transcript(self, xml_data):
        """
        Parse the transcript XML response and return structured JSON data.
        """
        soup = BeautifulSoup(xml_data, 'xml')
        transcript = []

        for body in soup.find_all('body'):
            for p in body.find_all('p'):
                start_time = p.get('t')
                duration = p.get('d', '0')
                text = p.get_text()
                transcript.append({
                    "start": float(start_time) / 1000,  # Convert ms to seconds
                    "dur": float(duration) / 1000,  # Convert ms to seconds
                    "text": text
                })
        return transcript

    def save_transcript(self, filename="transcript.json"):
        """
        Save the fetched transcript to a JSON file.
        """
        transcript = self.fetch_transcript()
        with open(filename, 'w') as f:
            json.dump(transcript, f, indent=4)

if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ")
    scraper = YouTubeTranscriptScraper(video_url)
    scraper.save_transcript()
    print("Transcript saved to transcript.json.")