/** Import October **/
LOAD DATA INFILE "/local/UKSA_Oct_18_-_Transparency_Data.csv"
INTO TABLE transactions
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
	department,
	entity,
	@date_of_payment,
	expense_type,
	expense_area,
	supplier,
	transaction_number,
	amount,
	description,
	supplier_post_code,
	supplier_type
)
SET date_of_payment = STR_TO_DATE(@date_of_payment, '%d/%m/%Y')
