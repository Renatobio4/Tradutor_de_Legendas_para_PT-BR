import os
import time
import torch
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor

def translate_line(line, translator):
    try:
        return translator.translate(line)
    except Exception as e:
        print(f"Error translating line: {line}. Error: {e}")
        return line

def translate_srt(file_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    translator = GoogleTranslator(source='en', target='pt')
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(translate_line, line, translator) for line in lines if not line.strip().isdigit() and '-->' not in line]
        for line, future in zip(lines, futures):
            if not line.strip().isdigit() and '-->' not in line:
                translated_lines.append(future.result() + '\n')
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
