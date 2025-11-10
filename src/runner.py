thonimport json
import os
from extractors.youtube_transcript_parser import YouTubeTranscriptParser
from outputs.transcript_exporter import TranscriptExporter

def run_scraper(video_url):
    try:
        # Extract transcript
        transcript = YouTubeTranscriptParser.extract_transcript(video_url)
        
        if transcript:
            # Export the transcript
            output_file = os.path.join('data', 'sample_output.json')
            TranscriptExporter.export_to_json(transcript, output_file)
            print(f"Transcript saved to {output_file}")
        else:
            print("No transcript available.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    run_scraper(video_url)