'''Importo le librerie necessarie'''
import sys, argparse, os, csv, shutil

#riporto la funzione che mi serve per identificare il tipo di file
def tipo_file(filename):
    #Verifico se il file non è una cartella
    if os.path.isdir(filename) == False:

        #per ogni tipo di file indico le sue possibili estensioni
        doc = ['.doc', '.txt', '.odt', '.docx', '.pdf']
        image = ['.jpg','.jpeg','.png','.gif']
        audio = ['.mp3','.wav']
        #utilizzo split per individuare l'estensione
        if os.path.splitext(filename)[1] in image:
            return 'image'
        elif os.path.splitext(filename)[1] in doc:
            return 'doc'
        elif os.path.splitext(filename)[1] in audio:
            return 'audio'
        else: #se il file non è in un formato leggibile o non elencato allora restituisce un errore
            return 'Non leggibile'


def main():
    parser = argparse.ArgumentParser()  # creiamo un argument che ha un argomento filename di tipo stringa
    parser.add_argument('filename', type=str,
                        help='Insert file name or insert --file')

    args = parser.parse_args()

    file = args.filename #recupero il nome del file inserito nella CLI

    # se il file è leggibile e non si trova già in una cartella, sposta e scrive nel recap
    if tipo_file(file) != 'Non leggibile' and tipo_file(file) not in os.listdir('C:\\Users\\anton\\Desktop\\FileOrganizer\\files\\' + tipo_file(file)):
        with open('C:\\Users\\anton\\Desktop\\FileOrganizer\\files\\recap.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
            filewriter.writerow([os.path.splitext(file)[0], tipo_file(file), str(os.path.getsize('C:\\Users\\anton\\Desktop\\FileOrganizer\\files\\' + file)) + 'B']) #scrivo le info file su recap
            shutil.move('C:\\Users\\anton\\Desktop\\FileOrganizer\\files\\' + file, 'C:\\Users\\anton\\Desktop\\FileOrganizer\\files\\' + tipo_file(file)) #sposto il file nella relativa cartella
            sys.stdout.write(f'Il file {file} è stato spostato')
    else:
        sys.stdout.write(f'Non esiste nessun file nominato {file}') #se il file non rispetta una delle precendenti condizioni allora viene stampato questo avviso


if __name__ == "__main__":
    main()