update_env:
	@echo "Updating the 'car_payments' Conda environment from environment.yml..."
	conda env update --name car_payments --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate car_payments"
