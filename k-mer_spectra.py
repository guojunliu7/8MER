input1 = "sequence1.fasta"
output1 = "results.txt"
count_dict = {}
pai_chu=['\n','H' , 'N' ,'K' , 'Y' , 'W' , 'M' , 'R' , 'S' ,'V' , 'D' ,'B']
row1=""

 


def read_file():
    global row1
    shu_ju=""
    try:
        with open(input1, "r") as f:
            #  
            #row1 = f.readline()
            #row1 = (f.readline()[:-1]).upper()
            #next(f)
            while True:
                #char = f.read(1)
                char=(f.readline()[:-1]).upper()
                if char[0:1] == ">":
                   char = ""
        # print Sq[0:1]
                   continue
                if char:
                    
                     shu_ju += char
                else:
                    break
    except Exception as e:
        print(e)
    return shu_ju
'
def process_data():
    shu_ju = read_file()
    for i in range(len(shu_ju) - 7):
        sequence = shu_ju[i:i + 8]
        if 'H' in sequence or 'N' in sequence or 'K' in sequence or 'Y' in sequence or 'W' in sequence or 'M' in sequence or 'R' in sequence or 'S' in sequence or 'V' in sequence or 'D' in sequence or 'B' in sequence:
            continue
        count_dict[sequence] = count_dict.get(sequence, 0) + 1

def main():
    sequences = generate_sequences()
    for sequence in sequences:
        count_dict[sequence] = 0
    process_data()
    sorted_dict = sorted(count_dict.items(), key=lambda x: x[0], reverse=False)
    #print(sorted_dict)
    try:
        with open(output1, "w") as f:
            if row1:
                f.write(row1)
            for idx, (key, value) in enumerate(sorted_dict, start=1):
                f.write(f"\t{key}\t{value}\n")
            print("good")
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()