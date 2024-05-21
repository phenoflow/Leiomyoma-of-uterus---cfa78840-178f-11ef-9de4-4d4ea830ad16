# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"93437","system":"readv2"},{"code":"61105","system":"readv2"},{"code":"32719","system":"readv2"},{"code":"28324","system":"readv2"},{"code":"3402","system":"readv2"},{"code":"55349","system":"readv2"},{"code":"759","system":"readv2"},{"code":"72251","system":"readv2"},{"code":"98291","system":"readv2"},{"code":"33691","system":"readv2"},{"code":"4117","system":"readv2"},{"code":"61404","system":"readv2"},{"code":"432","system":"readv2"},{"code":"41134","system":"readv2"},{"code":"67322","system":"readv2"},{"code":"12512","system":"readv2"},{"code":"8655","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leiomyoma-of-uterus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["leiomyoma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["leiomyoma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["leiomyoma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
