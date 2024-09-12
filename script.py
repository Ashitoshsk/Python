import pandas as pd
import qrcode
import os

# Define the folder where the CSV file is located and where QR codes will be saved
input_folder = './'
output_folder = './Data'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load the CSV file
csv_file = os.path.join(input_folder, 'Data.csv')  # Update 'your_file.csv' to your actual file name
df = pd.read_csv(csv_file)

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Generate a QR code for each row
    data = row.to_string(index=False)  # Convert row to a string
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the QR code image
    qr_image_filename = os.path.join(output_folder, f'qrcode_row_{index}.png')
    img.save(qr_image_filename)

    print(f'Saved QR code for row {index} to {qr_image_filename}')

print('QR code generation complete.')
