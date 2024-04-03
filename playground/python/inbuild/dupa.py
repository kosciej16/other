# import csv

# with open("som.csv", newline="") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=" ")
#     for row in reader:
#         print(row["SAMPLE_ID"])

DIR_NAME = "/home/kosciej/"

with open("som.csv", "r") as f:
    next(f)
    for line in f.readlines():
        line = line.strip()
        sample_list = {line.split()[0]}
        chrom = "chr" + line.split()[1]
        pos = line.split()[2]
        ref = line.split()[3]
        alt = line.split()[4]
        for sample_name in sample_list:
            out_vcf = open(DIR_NAME + str(sample_name) + ".vcf", "a")
            out_vcf.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t" + sample_name + "\n")
            ID = "."
            QUAL = "."
            FILTER = "."
            INFO = "."
            FORMAT = "."
            out = [chrom, pos, ID, ref, alt, QUAL, FILTER, INFO, FORMAT]
            print(out)
            out_vcf.write("\t".join(out) + "\n")
