CREATE TABLE transactions (
	department VARCHAR(255),
	entity VARCHAR(255),
	date_of_payment DATE,
	expense_type VARCHAR(255),
	expense_area VARCHAR(255),
	supplier VARCHAR(255),
	transaction_number INTEGER,
	amount DECIMAL(15,2),
	description VARCHAR(255),
	supplier_post_code VARCHAR(10),
	supplier_type VARCHAR(255)
)
