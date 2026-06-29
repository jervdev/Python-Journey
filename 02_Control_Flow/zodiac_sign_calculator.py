try:
	month = int(input("Enter your birth month (1-12): "))
	day = int(input("Enter your birth day (1-31): "))
	
	match month:
		case 1:
			if day <= 19:
				zodiac = "Capricornus"
			elif day >= 20 and day <= 31:
				zodiac = "Aquarius"
			else: 
				zodiac = "Invalid day"
		case 2:
			if day <= 18:
				zodiac = "Aquarius"
			elif day >= 19 and day <= 29:
				zodiac = "Pisces"
			else: 
				zodiac = "Invalid day"
		case 3:
			if day <= 20:
				zodiac = "Pisces"
			elif day >= 21 and day <= 31:
				zodiac = "Aries"
			else: 
				zodiac = "Invalid day"
		case 4:
			if day <= 19:
				zodiac = "Aries"
			elif day >= 20 and day <= 30:
				zodiac = "Taurus"
			else: 
				zodiac = "Invalid day"
		case 5:
			if day <= 20:
				zodiac = "Taurus"
			elif day >= 21 and day <= 31:
				zodiac = "Gemini"
			else: 
				zodiac = "Invalid day"
		case 6:
			if day <= 20:
				zodiac = "Gemini"
			elif day >= 21 and day <= 30:
				zodiac = "Cancer"
			else: 
				zodiac = "Invalid day"
		case 7:
			if day <= 22:
				zodiac = "Cancer"
			elif day >= 23 and day <= 31:
				zodiac = "Leo"
			else: 
				zodiac = "Invalid day"
		case 8:
			if day <= 22:
				zodiac = "Leo"
			elif day >= 23 and day <= 31:
				zodiac = "Virgo"
			else: 
				zodiac = "Invalid day"
		case 9:
			if day <= 22:
				zodiac = "Virgo"
			elif day >= 23 and day <= 30:
				zodiac = "Libra"
			else: 
				zodiac = "Invalid day"
		case 10:
			if day <= 22:
				zodiac = "Libra"
			elif day >= 23 and day <= 31:
				zodiac = "Scorpius"
			else: 
				zodiac = "Invalid day"
		case 11:
			if day <= 21:
				zodiac = "Scorpius"
			elif day >= 22 and day <= 30:
				zodiac = "Sagittarius"
			else: 
				zodiac = "Invalid day"
		case 12:
			if day <= 21:
				zodiac = "Sagittarius"
			elif day >= 22 and day <= 31:
				zodiac = "Capricornus"
			else: 
				zodiac = "Invalid day"
	print(f"Your zodiac sign is: {zodiac}")

except ValueError:
	print("Error: Please input number only for month and day.")

