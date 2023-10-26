import csv
import pandas as pd


def clean_genome_browser_data(fasta_file, csv_file):
    """
    Convert a FASTA file to CSV format UCSC Genome Browser Dataset

    Parameters:
    - fasta_file (str): Path to the input FASTA file.
    - csv_file (str): Path to the output CSV file.

    Returns:
    None
    """
    with open(fasta_file, "r") as f_in, open(csv_file, "w", newline="") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(["Header", "Sequence"])  # Writing headers
        
        header = None
        sequence = []
        for line in f_in:
            if line.startswith(">"):
                if header:
                    writer.writerow([header, "".join(sequence)])
                header = line.strip().lstrip(">")
                sequence = []
            else:
                sequence.append(line.strip())
        writer.writerow([header, "".join(sequence)])  # Writing the last entry

# Example usage:
# clean_genome_browser_data("hg38.fa", "hg38.csv")


def clean_ClinVar_data(input_file="clinvar.vcf", output_file="clinvar.csv"):
    """
    Convert a VCF file to CSV format ClinVar Dataset

    Parameters:
    - input_file (str): Path to the input VCF file.
    - output_file (str): Path to the output CSV file.

    Returns:
    None
    """
    with open(input_file, 'r') as vcf, open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in vcf:
            if line.startswith('##'):
                continue
            if line.startswith('#CHROM'):
                header = line.strip().split('\t')
                writer.writerow(header)
                continue
            row = line.strip().split('\t')
            writer.writerow(row)

# Example usage:
# clean_ClinVar_data("clinvar.vcf", "clinvar.csv")



def clean_protein_atlas_data(input_file="protein_atlas_data.tsv", output_file="cleaned_protein_atlas_data.csv"):
    """
    Clean and transform the Human Protein Atlas data.

    Parameters:
    - input_file (str): Path to the input TSV file.
    - output_file (str): Path to the output CSV file.

    Returns:
    None
    """
    data = pd.read_csv(input_file, sep="\t")

    # Convert columns to appropriate data types (example: converting a column to datetime format)
    # data['date_column'] = pd.to_datetime(data['date_column'])

    # Handle missing values (example: filling NaN values with the mean of the column)
    # data['numeric_column'].fillna(data['numeric_column'].mean(), inplace=True)

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    # Remove any rows with missing values
    data.dropna(inplace=True)

    # Save the cleaned data
    data.to_csv(output_file, index=False)

# Example usage:
# clean_protein_atlas_data("protein_atlas_data.tsv", "cleaned_protein_atlas_data.csv")



def clean_pharmgkb_data(input_file="pharmgkb_data.txt", output_file="cleaned_pharmgkb_data.csv"):
    """
    Clean and transform the PharmGKB data.

    Parameters:
    - input_file (str): Path to the input TXT file.
    - output_file (str): Path to the output CSV file.

    Returns:
    None
    """
    data = pd.read_csv(input_file, sep="\t")

    # Convert columns to appropriate data types (example: converting a column to datetime format)
    # data['date_column'] = pd.to_datetime(data['date_column'])

    # Handle missing values (example: filling NaN values with the mean of the column)
    # data['numeric_column'].fillna(data['numeric_column'].mean(), inplace=True)

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    # Remove any rows with missing values
    data.dropna(inplace=True)

    # Save the cleaned data
    data.to_csv(output_file, index=False)

# Example usage:
# clean_pharmgkb_data("pharmgkb_data.txt", "cleaned_pharmgkb_data.csv")



def clean_gene_ontology_data(input_file="geo_data.soft", output_file="geo_data.csv"):
    """
    Convert a GEO SOFT file to CSV format Gene Ontology dataset

    Parameters:
    - input_file (str): Path to the input SOFT file.
    - output_file (str): Path to the output CSV file.

    Returns:
    None
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Extract data lines (assuming they start after the "!series_matrix_table_begin" line)
    data_lines = lines[lines.index("!series_matrix_table_begin\n")+1:lines.index("!series_matrix_table_end\n")]

    # Split lines into lists and create a DataFrame
    data = [line.strip().split("\t") for line in data_lines]
    df = pd.DataFrame(data[1:], columns=data[0])

    # Save the cleaned data
    df.to_csv(output_file, index=False)

# Example usage:
# clean_gene_ontology_data("geo_data.soft", "geo_data.csv")



def clean_protein_atlas_data(input_file="protein_atlas_data.tsv", output_file="cleaned_protein_atlas_data.csv"):
    """
    Clean and transform the Human Protein Atlas data.

    Parameters:
    - input_file (str): Path to the input TSV file.
    - output_file (str): Path to the output CSV file.

    Returns:
    None
    """
    data = pd.read_csv(input_file, sep="\t")

    # Convert columns to appropriate data types (example: converting a column to datetime format)
    # data['date_column'] = pd.to_datetime(data['date_column'])

    # Handle missing values (example: filling NaN values with the mean of the column)
    # data['numeric_column'].fillna(data['numeric_column'].mean(), inplace=True)

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    # Remove any rows with missing values
    data.dropna(inplace=True)

    # Additional cleaning and transformation steps can be added as needed

    # Save the cleaned data
    data.to_csv(output_file, index=False)

# Example usage:
# clean_protein_atlas_data("protein_atlas_data.tsv", "cleaned_protein_atlas_data.csv")
