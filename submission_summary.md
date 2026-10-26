# Online Retail Analysis — Submission Summary
This project analyzes historical online retail transactions to identify sales patterns, product demand, and potential business opportunities. Python and pandas were used to clean the dataset, while Matplotlib and Seaborn were used to create visualizations and explore trends. One of the main challenges was handling missing customer identifiers, duplicate records, and negative quantities while preserving useful transaction data. These issues were addressed by documenting cleaning decisions, removing duplicate records, retaining rows with missing customer IDs and negative quantities, and removing rows with negative unit prices. The analysis provides historical insights into retail activity while recognizing limitations such as the short observation period and incomplete December 2011 data.

## Biggest Challenge
Handling missing customer identifiers, duplicate records, and negative quantities while preserving useful transaction information.

## How I Addressed It
I documented the cleaning decisions, checked the dataset after processing, and retained negative quantities because they may represent returns or credit notes rather than automatically treating them as invalid records.
