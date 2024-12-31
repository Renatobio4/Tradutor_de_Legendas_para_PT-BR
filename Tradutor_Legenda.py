import os
import time
from deep_translator import GoogleTranslator

def translate_line(line, translator):
    try:
        return translator.translate(line)
    except Exception as e:
        print(f"Error translating line: {line}. Error: {e}")
        return line

def translate_srt(file_path):
    translator = GoogleTranslator(source='en', target='pt')
    translated_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().isdigit() or '-->' in line:
                translated_lines.append(line)
            else:
                translated_lines.append(translate_line(line, translator) + '\n')

    return translated_lines

def main():
    print("Iniciando o processo de tradução...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    for root, dirs, files in os.walk(current_dir):
        for file_name in files:
            if file_name.endswith('_en.srt'):
                file_path = os.path.join(root, file_name)
                new_file_name = file_name.replace('_en.srt', '_pt-br.srt')
                new_file_path = os.path.join(root, new_file_name)
                
                if os.path.exists(new_file_path):
                    print(f"Translation already exists for: {new_file_path}")
                    continue
                
                print(f"Translating file: {file_path}")
                start_time = time.time()
                try:
                    translated_lines = translate_srt(file_path)
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
