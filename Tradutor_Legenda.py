import os
import time
from deep_translator import GoogleTranslator

def translate_srt(file_path):
    translator = GoogleTranslator(source='en', target='pt')
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    translated_lines = []
    for line in lines:
        if not line.strip().isdigit() and '-->' not in line:
            try:
                translated = translator.translate(line)
                if translated:
                    translated_lines.append(translated + '\n')
                else:
                    translated_lines.append(line)
            except Exception as e:
                print(f"Error translating line: {line}. Error: {e}")
                translated_lines.append(line)
        else:
            translated_lines.append(line)
    
    return translated_lines

def main():
    print("Iniciando o processo de tradução...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    for file_name in os.listdir(current_dir):
        if file_name.endswith('_en.srt'):
            file_path = os.path.join(current_dir, file_name)
            print(f"Translating file: {file_path}")
            start_time = time.time()
            try:
                translated_lines = translate_srt(file_path)
                new_file_name = file_name.replace('_en.srt', '_pt-br.srt')
                new_file_path = os.path.join(current_dir, new_file_name)
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.writelines(translated_lines)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"File saved as: {new_file_path}")
                print(f"Translation completed in {elapsed_time:.2f} seconds")
            except Exception as e:
                print(f"Error translating file {file_path}: {e}")

if __name__ == "__main__":
    main()
