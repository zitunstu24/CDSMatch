import subprocess
import yaml
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SearchIO
import pandas as pd
import ace_tools_open as tools
import os

def load_config(config_path="config/config.yaml"):
    """Load the config file."""

    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def create_blast_db(input_fasta, db_name):
    """Create blast database with the  desired fasta file."""

    subprocess.run(["makeblastdb", "-in", input_fasta, "-dbtype", "nucl", "-out", db_name], check=True)

def run_blast(query_fasta, db_name, output_file, evalue=0.001):
    """Run blast algorithm to find the match among CDS sequences."""

    blastn_cline = NcbiblastnCommandline(
        query=query_fasta,
        db=db_name,
        evalue=evalue,
        outfmt=5,  # XML output
        out=output_file
    )
    blastn_cline()

def parse_blast_results(output_file):
    """Make the blast output results into a dataframe."""

    matches = []
    for result in SearchIO.parse(output_file, "blast-xml"):
        if result.hits:
            best_hit = result.hits[0]
            developer_gene = result.id
            ncbi_gene = best_hit.id
            matches.append([developer_gene, ncbi_gene])
    return pd.DataFrame(matches, columns=["Gene_ID_Y", "Gene_ID_X"])

def save_results(df, output_dir, output_csv):
    """Save the output to desired dir as csv."""

    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, output_csv)
    df.to_csv(csv_path, index=False)
    print(f"Results saved to {csv_path}")

def main():
    config = load_config()
    cds_file_X = config["cds_file_X"]
    cds_file_Y = config["cds_file_Y"]
    blast_db = config["blast_db"]
    XML_output = config["XML_output"]
    output_dir = config.get("output_dir")
    output_csv = config.get("output_csv")
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating BLAST database...")
    create_blast_db(cds_file_X, blast_db)
    
    print("Running BLAST...")
    run_blast(cds_file_Y, blast_db, XML_output, evalue=config.get("evalue", 0.001))
    
    print("Parsing results...")
    df_matches = parse_blast_results(XML_output)

    print("Saving results...")
    save_results(df_matches, output_dir, output_csv)
    
    print("Displaying results...")
    tools.display_dataframe_to_user(name="BLAST Matched Gene IDs", dataframe=df_matches)

if __name__ == "__main__":
    main()