# TrioQuad-Encryption

userInput = input('Would you like to encrypt or decrypt? ').lower()

if userInput not in ['encrypt', 'decrypt']:
    print('Please spell encrypt or decrypt right.')
    exit()

binary_inputs = input('Please enter your binary ASCII input(s), separated by spaces: ').split()

for binary_input in binary_inputs:
  # Encrypt
  if userInput == 'encrypt':
    split_input = [binary_input[i:i+4] for i in range(0, len(binary_input), 4)]
    first_half = split_input[0]
    second_half = split_input[1]
    first_half_flipped = first_half[::-1]
    second_half_flipped = second_half[::-1]
    combined_flipped = first_half_flipped + second_half_flipped
    pair_input = [combined_flipped[i:i+2] for i in range(0, len(combined_flipped), 2)]
    pair_flipped = [pair[::-1] for pair in pair_input]
    encrypted = ''.join(pair_flipped)
    print(f'{encrypted} ')

  # Decrypt
  elif userInput == 'decrypt':
    pair_input = [binary_input[i:i+2] for i in range(0, len(binary_input), 2)]
    pair_flipped = [pair[::-1] for pair in pair_input]
    combined_flipped = ''.join(pair_flipped)
    split_input = [combined_flipped[i:i+4] for i in range(0, len(combined_flipped), 4)]
    first_half = split_input[0]
    second_half = split_input[1]
    first_half_flipped = first_half[::-1]
    second_half_flipped = second_half[::-1]
    decrypted = first_half_flipped + second_half_flipped
    print(f'{decrypted} ')