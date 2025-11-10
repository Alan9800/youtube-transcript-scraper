thonimport json

class TranscriptExporter:
    @staticmethod
    def export_to_json(transcript, file_path):
        try:
            with open(file_path, 'w') as json_file:
                json.dump(transcript, json_file, indent=4)
        except Exception as e:
            print(f"Error exporting transcript: {e}")