package caesar


func EncryptCaesar(plaintext string, shift int) string {
	var ciphertext string

	shift = shift % 26
	for i := range plaintext {
		if (i>='A' && i<='Z') || (i>='a' && i<='z') {
			ciphertext+=string(rune(i)+rune(shift))
		} else if (i >= 'X' && i <= 'Z') || (i >= 'x' && i <= 'z') {
			ciphertext+=string(rune(i)+rune(shift)-26)
		} else if i>='!' && i<= '@' {
			ciphertext += string(i)
		}

	}

	return ciphertext
}

func DecryptCaesar(ciphertext string, shift int) string {
	var plaintext string

	shift = shift % 26
	for i := range plaintext {
		if (i>='A' && i<='Z') || (i>='a' && i<='z') {
			ciphertext+=string(rune(i)-rune(shift))
		} else if (i >= 'X' && i <= 'Z') || (i >= 'x' && i <= 'z') {
			ciphertext+=string(rune(i)-rune(shift)+26)
		} else if i>='!' && i<= '@' {
			ciphertext += string(i)
		}

	}

	return plaintext
}
